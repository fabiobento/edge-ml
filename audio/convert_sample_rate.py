

import os
import soundfile as sf

def convert_sample_rate(input_file, target_sample_rate):
    # Lê o áudio original
    audio, sample_rate = sf.read(input_file)
    # Converte a taxa de amostragem, se necessário
    if sample_rate != target_sample_rate:
        sf.write(input_file, audio, target_sample_rate)  # Sobrescreve o arquivo original
        print(f'Converted {input_file} to sample rate {target_sample_rate}')
    else:
        print(f'No conversion needed for {input_file}')

def convert_sample_rate_recursively(directory, target_sample_rate):
    # Percorre todos os arquivos e subdiretórios
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.wav'):  # Verifica a extensão dos arquivos
                input_file = os.path.join(dirpath, filename)
                # Converte a taxa de amostragem
                convert_sample_rate(input_file, target_sample_rate)

# Caminho para o diretório contendo os arquivos de áudio
audio_directory = '/workspace/audio/datasets/Snoring Dataset'
# Define a taxa de amostragem alvo
target_sample_rate = 16000  # Alterar conforme necessário

# Chama a função para converter recursivamente
convert_sample_rate_recursively(audio_directory, target_sample_rate)



