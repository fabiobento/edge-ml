import os
import soundfile as sf
import numpy as np

def convert_to_mono(input_file):
    # Lê o áudio original
    audio, sample_rate = sf.read(input_file)
    # Verifica se o áudio já é mono
    if audio.ndim > 1:
        # Converte para mono, tirando a média das duas (ou mais) canais
        audio_mono = np.mean(audio, axis=1)
        # Salva o arquivo original sobrescrevendo
        sf.write(input_file, audio_mono, sample_rate)
        print(f'Converted {input_file} to mono.')
    else:
        print(f'No conversion needed for {input_file}.')

def convert_audio_recursively(directory):
    # Percorre todos os arquivos e subdiretórios
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.wav'):  # Verifica a extensão dos arquivos
                input_file = os.path.join(dirpath, filename)
                convert_to_mono(input_file)

# Caminho para o diretório contendo os arquivos de áudio
input_audio_directory = '/workspace/audio/datasets/Snoring Dataset'

# Chama a função para converter recursivamente
convert_audio_recursively(input_audio_directory)
