import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
import json
import zipfile
import os
from datetime import datetime
from unidecode import unidecode

from stats.forms import SignupForm, UploadFileForm
from stats.models import UploadedFile

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler() 
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class CustomLoginView(LoginView):
    template_name = 'login.html'


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            logger.info(f"User {user.username} signed up and logged in.")
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})


def home_view(request):
    logger.info("Home page accessed.")
    return render(request, "home.html")


@login_required
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            logger.info(f"File uploaded by user {request.user.username}.")
            return redirect("upload_success")
    else:
        form = UploadFileForm()

    return render(request, "upload.html", {"form": form})


def process_music_data(request):
    user = request.user
    logger.info(f"Processing music data for user {user.username}.")
    process_zip_and_generate_summary(user, output_file='summary.json')
    return JsonResponse({"message": "Summary generated successfully!"})


def format_duration(ms):
    minutes = ms // 60000
    seconds = (ms % 60000) // 1000
    if minutes >= 10:
        return f"{minutes}m"
    else:
        return f"{minutes}m {seconds}s"


def extract_zip(zip_path, extract_to='temp_dir'):
    logger.debug(f"Extracting zip file from {zip_path} to {extract_to}.")
    
    # Garante que o diretório existe
    os.makedirs(extract_to, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    return extract_to



def clean_string(text):
    if text is None:
        return ""
    newstr = unidecode(text)
    return newstr


def process_json_file(file_path, summary_data, global_stats):
    logger.debug(f"Processing JSON file: {file_path}.")
    with open(file_path, 'r') as file:
        data = json.load(file)

    for entry in data:
        artist = clean_string(entry["master_metadata_album_artist_name"])
        track = clean_string(entry["master_metadata_track_name"])
        album = clean_string(entry["master_metadata_album_album_name"])
        duration = entry["ms_played"]

        global_stats['total_minutes'] += duration // 60000
        global_stats['unique_artists'].add(artist)
        global_stats['unique_tracks'].add(track)
        global_stats['unique_albums'].add(album)
        
        if artist not in summary_data:
            summary_data[artist] = {'total_play_time': 0, 'albums': {}, 'tracks': {}}
        summary_data[artist]['total_play_time'] += duration

        if album not in summary_data[artist]['albums']:
            summary_data[artist]['albums'][album] = 0
        summary_data[artist]['albums'][album] += duration
        
        if track not in summary_data[artist]['tracks']:
            summary_data[artist]['tracks'][track] = 0
        summary_data[artist]['tracks'][track] += duration

def process_zip_and_generate_summary(zip_path, output_file=None):
    if output_file is None:
        output_file = os.path.join(settings.MEDIA_ROOT, 'extracted', 'summary.json')

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    logger.debug(f"Extracting and processing zip file: {zip_path}.")
    extracted_dir = extract_zip(zip_path)
    
    summary_data = {}
    global_stats = {'total_minutes': 0, 'unique_artists': set(), 'unique_tracks': set(), 'unique_albums': set()}

    for root, dirs, files in os.walk(extracted_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                process_json_file(file_path, summary_data, global_stats)
    
    for artist, artist_data in summary_data.items():
        artist_data['total_play_time'] = format_duration(artist_data['total_play_time'])
        for album, album_duration in artist_data['albums'].items():
            artist_data['albums'][album] = format_duration(album_duration)
        for track, track_duration in artist_data['tracks'].items():
            artist_data['tracks'][track] = format_duration(track_duration)
    
    final_data = {
        'global': {
            'total_minutes': global_stats['total_minutes'],
            'unique_artists': len(global_stats['unique_artists']),
            'unique_tracks': len(global_stats['unique_tracks']),
            'unique_albums': len(global_stats['unique_albums'])
        },
        'artists': summary_data
    }
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(final_data, out_file, indent=4)
    
    logger.info(f"Summary generated successfully at {output_file}.")
    
    for root, dirs, files in os.walk(extracted_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))



    logger.info(f"Summary generated successfully at {output_file}.")

    for root, dirs, files in os.walk(extracted_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))

    os.rmdir(extracted_dir)


def upload_success(request):
    logger.info("Upload success page accessed.")
    return render(request, 'upload_success.html')


def process_file(request):
    last_uploaded_file = UploadedFile.objects.latest('uploaded_at')
    zip_path = last_uploaded_file.file.path
    output_file = os.path.join(settings.MEDIA_ROOT, 'extracted', 'summary.json')

    logger.debug(f"Processing file {zip_path}.")
    process_zip_and_generate_summary(zip_path, output_file)

    return redirect('show_summary')


def show_summary(request):
    summary_file = os.path.join(settings.MEDIA_ROOT, 'extracted', 'summary.json')

    if not os.path.exists(summary_file):
        logger.error("Summary file not found.")
        return HttpResponseNotFound("Error 404: Summary not found.")

    try:
        with open(summary_file, "r", encoding="utf-8") as file:
            summary_data = json.load(file)
    except json.JSONDecodeError:
        logger.error("Error decoding JSON file.")
        return JsonResponse({"error": "Error processing the JSON."}, status=500)

    logger.info("Summary file loaded successfully.")
    return render(request, "summary.html", {"summary": summary_data})


def download_summary(request):
    summary_file_path = os.path.join(settings.MEDIA_ROOT, 'extracted', 'summary.json')

    if os.path.exists(summary_file_path):
        with open(summary_file_path, 'r') as json_file:
            json_content = json_file.read()

        response = HttpResponse(json_content, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="summary.json"'
        logger.info("Summary file downloaded.")
        return response
    else:
        logger.error("Summary file not found for download.")
        return HttpResponse("The summary.json file was not found.", status=404)
