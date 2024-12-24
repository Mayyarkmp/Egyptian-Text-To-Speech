import os
from pydub import AudioSegment
import pandas as pd

def get_audio_durations(csv_path, folder_path):
    audio_durations = []
    df = pd.read_csv(csv_path)
    for i, file_name in enumerate(df['splitted_audio_name'].tolist()):
        if i > 10:
            break
        file_path = os.path.join(folder_path, file_name)
        try:
            audio = AudioSegment.from_file(file_path)
            duration = audio.duration_seconds
            audio_durations.append(duration)
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
    
    df['duration'] = audio_durations
    csv_path = csv_path.replace('.csv', '_new') + '.csv'
    df.to_csv(csv_path, encoding='utf-8-sig', index=False)


if __name__ == '__main__':
    folder_path = ""
    csv_path = ""
    get_audio_durations(csv_path, folder_path)