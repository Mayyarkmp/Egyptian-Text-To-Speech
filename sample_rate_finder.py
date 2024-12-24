import soundfile as sf
import os


path = "./audios/wavs"
samples = []
for i, audio in enumerate(os.listdir(path)):
    print(f'Processing audio {i}')
    audio_path = os.path.join(path, audio)
    data, sample_rate = sf.read(audio_path)
    samples.append(len(data))


print(f'Max: {max(samples)}')
print(f'Min: {min(samples)}')

