import os
import pandas as pd
from transformers import pipeline


class AudioTranscriber:


    def __init__(self, csv_filename, model_name="facebook/seamless-m4t-v2-large", target_lang="arb", output_csv_dir='./datasets/audio_text_datasets'):
        self.csv_filename = csv_filename
        self.transcription_pipeline = pipeline("automatic-speech-recognition", model=model_name)
        self.target_lang = target_lang
        self.output_csv_dir = output_csv_dir


    def transcribe_audio(self, audio_path):
        transcription = self.transcription_pipeline(audio_path, generate_kwargs={"tgt_lang": self.target_lang})
        return transcription


    def transcribe_audio_folder(self, folder_path):
        transcriptions = {}
        for filename in os.listdir(folder_path):
            if filename.endswith(".wav"):
                audio_path = os.path.join(folder_path, filename)
                transcription = self.transcribe_audio(audio_path)
                transcriptions[filename] = transcription['text']

        keys, values = zip(*transcriptions.items())

        df = pd.DataFrame({
            'filename': keys,
            'text': values
        })

        df.to_csv(os.path.join(self.output_csv_dir, self.csv_filename), encoding='utf-8-sig', index=False)