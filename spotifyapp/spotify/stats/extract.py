import json
import zipfile
import os
from datetime import datetime
import re
from unidecode import unidecode

# Função para formatar duração em minutos e segundos
def format_duration(ms):
    minutes = ms // 60000
    seconds = (ms % 60000) // 1000
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
        timestamp = datetime.strptime(entry["ts"], "%Y-%m-%dT%H:%M:%SZ")
        
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
def process_zip_and_generate_summary(zip_path, output_file=f'media/extracted/summary.json'):
    # Passo 1: Verificar se o arquivo ZIP existe
    if not os.path.exists(zip_path):
        print("Arquivo ZIP não encontrado.")
        return
    
    # Passo 2: Extrair o ZIP
    extracted_dir = extract_zip(zip_path)
    
    # Passo 3: Inicializar a tabela de resumo
    summary_data = {}
    
    # Passo 4: Processar cada arquivo JSON dentro da pasta extraída
    for root, dirs, files in os.walk(extracted_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                process_json_file(file_path, summary_data)
    
    # Passo 5: Formatar as durações para minutos e segundos
    for artist, artist_data in summary_data.items():
        # Formatar o total_play_time do artista
        artist_data['total_play_time'] = format_duration(artist_data['total_play_time'])
        
        for album, album_duration in artist_data['albums'].items():
            # Formatar a duração de cada álbum
            artist_data['albums'][album] = format_duration(album_duration)
        
        for track, track_duration in artist_data['tracks'].items():
            # Formatar a duração de cada música
            artist_data['tracks'][track] = format_duration(track_duration)
    
    # Passo 6: Salvar o resumo no arquivo JSON de saída
    with open(output_file, 'w') as out_file:
        json.dump(summary_data, out_file, indent=4)
    
    # Passo 7: Limpar os arquivos extraídos
    for root, dirs, files in os.walk(extracted_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    
    os.rmdir(extracted_dir)
    print(f"Resumo gerado com sucesso em {output_file}")

# Rodar o script de forma independente
if __name__ == "__main__":
    # Caminho do arquivo ZIP (atualize conforme necessário)
    zip_path = "media/uploads/user_1/Spotify_Extended_Streaming_History.zip"
    
    # Gerar o resumo
    process_zip_and_generate_summary(zip_path, output_file='summary.json')
