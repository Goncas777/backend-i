from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from stats.forms import SignupForm, UploadFileForm
from stats.models import UploadedFile
from django.http import JsonResponse, HttpResponseNotFound
import json
import zipfile
import os
from datetime import datetime
from unidecode import unidecode
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.urls import reverse
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
import os
import json



class CustomLoginView(LoginView):
    template_name = 'login.html'

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)  # Faz login automático após o registro
            return redirect("home")  # Redireciona para a página inicial (ou outra que quiseres)
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

def home_view(request):
    return render(request, "home.html")




@login_required
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect("upload_success")  # Redireciona para a página de sucesso
    else:
        form = UploadFileForm()

    return render(request, "upload.html", {"form": form})

def process_music_data(request):
    # Obter o usuário logado
    user = request.user
    
    # Chamar a função que processa os dados
    process_zip_and_generate_summary(user, output_file='summary.json')

    # Retornar uma resposta ou renderizar a página
    return JsonResponse({"message": "Resumo gerado com sucesso!"})



# Função para formatar a duração em minutos e segundos
def format_duration(ms):
    minutes = ms // 60000  # Calcula os minutos
    seconds = (ms % 60000) // 1000  # Calcula os segundos

    if minutes >= 10:
        return f"{minutes}m"  # Exibe apenas os minutos, se for superior a 10 minutos
    else:
        return f"{minutes}m {seconds}s"  

# Função para descompactar o arquivo ZIP
def extract_zip(zip_path, extract_to='temp_dir'):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

def clean_string(text):
    if text is None:
        return ""  # Retorna uma string vazia se o valor for None

    newstr = unidecode(text)  # Aplica unidecode apenas se o texto não for None
    return newstr

def process_json_file(file_path, summary_data):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for entry in data:
        artist = clean_string(entry["master_metadata_album_artist_name"])
        track = clean_string(entry["master_metadata_track_name"])
        album = clean_string(entry["master_metadata_album_album_name"])
        duration = entry["ms_played"]
        
        # Verifica se o artista já está na tabela
        if artist not in summary_data:
            summary_data[artist] = {'total_play_time': 0, 'albums': {}, 'tracks': {}}
        
        # Soma o tempo de reprodução do artista
        summary_data[artist]['total_play_time'] += duration
        
        # Verifica se o álbum já está na tabela
        if album not in summary_data[artist]['albums']:
            summary_data[artist]['albums'][album] = 0
        # Soma o tempo de reprodução do álbum
        summary_data[artist]['albums'][album] += duration
        
        # Verifica se a música já está na tabela
        if track not in summary_data[artist]['tracks']:
            summary_data[artist]['tracks'][track] = 0
        # Soma o tempo de reprodução da música
        summary_data[artist]['tracks'][track] += duration

# Função principal para processar os arquivos JSON no ZIP e gerar o arquivo de resumo

def process_zip_and_generate_summary(zip_path, output_file=None):
    if output_file is None:
        output_file = os.path.join(settings.MEDIA_ROOT, 'extracted', 'summary.json') 

    # Criar a pasta caso não exista
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Passo 2: Extrair o ZIP
    extracted_dir = extract_zip(zip_path)

    # Inicializar a tabela de resumo
    summary_data = {}

    # Passo 3: Processar cada arquivo JSON dentro da pasta extraída
    for root, dirs, files in os.walk(extracted_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                process_json_file(file_path, summary_data)

    # Passo 4: Formatar as durações para minutos e segundos
    for artist, artist_data in summary_data.items():
        artist_data['total_play_time'] = format_duration(artist_data['total_play_time'])

        for album, album_duration in artist_data['albums'].items():
            artist_data['albums'][album] = format_duration(album_duration)

        for track, track_duration in artist_data['tracks'].items():
            artist_data['tracks'][track] = format_duration(track_duration)

    # Passo 5: Salvar o resumo no arquivo JSON de saída
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(summary_data, out_file, indent=4)

    print(f"Resumo gerado com sucesso em {output_file}")

    # Passo 6: Limpar os arquivos extraídos
    for root, dirs, files in os.walk(extracted_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))

    os.rmdir(extracted_dir)

def upload_file(request):
    # A view de upload que salva o arquivo
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redireciona para a página de sucesso após o upload
            return redirect(reverse('upload_success'))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')


def process_file(request):
    # Obter o último arquivo enviado
    last_uploaded_file = UploadedFile.objects.latest('uploaded_at')
    zip_path = last_uploaded_file.file.path  # Caminho do arquivo ZIP enviado

    # Define o caminho correto do JSON
    output_file = os.path.join(settings.MEDIA_ROOT, 'extracted', 'summary.json')

    # Chama a função para processar
    process_zip_and_generate_summary(zip_path, output_file)

    # Redireciona para a página que exibe o resumo
    return redirect('show_summary')
    


def show_summary(request):
    # Caminho correto do ficheiro JSON
    summary_file = os.path.join(settings.MEDIA_ROOT, 'extracted', 'summary.json')

    # Verifica se o ficheiro existe
    if not os.path.exists(summary_file):
        return HttpResponseNotFound("Erro 404: O resumo não foi encontrado.")

    try:
        # Lê os dados do JSON
        with open(summary_file, "r", encoding="utf-8") as file:
            summary_data = json.load(file)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Erro ao processar o JSON."}, status=500)

    return render(request, "summary.html", {"summary": summary_data})



# Create your views here.
