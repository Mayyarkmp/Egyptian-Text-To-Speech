import os
import pandas as pd
from transformers import pipeline
from transformers import pipeline, AutoTokenizer
import torch
import time 

# Check if MPS is available and set device accordingly
if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")  # Fallback to CPU if MPS is not available

class AudioTranscriber:
    
    
    def __init__(self, csv_filename, model_name="facebook/seamless-m4t-v2-large", target_lang="arb", output_csv_dir='./datasets_csv/audio_text_datasets'):
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
        # Use the determined device
        self.transcription_pipeline = pipeline("automatic-speech-recognition", model=model_name, tokenizer=tokenizer,device=0)
        self.csv_filename = csv_filename
        self.target_lang = target_lang
        self.output_csv_dir = output_csv_dir


    def transcribe_audio(self, audio_path):
        transcription = self.transcription_pipeline(audio_path, generate_kwargs={"tgt_lang": self.target_lang})
        return transcription


    def transcribe_audio_folder(self, folder_path):
        transcriptions = {}
        sorted_filenames = sorted(os.listdir(folder_path))
        start = time.time()
        for filename in sorted_filenames:
            if filename.endswith(".wav"):
                audio_path = os.path.join(folder_path, filename)
                transcription = self.transcribe_audio(audio_path)
                transcriptions[filename] = transcription['text']
                print(f"Finished processing {filename} , {i} out of {len(sorted_filenames)}")
        end = time.time()
        print(f"Time taken: {end - start}")
        keys, values = zip(*transcriptions.items())

        df = pd.DataFrame({
            'filename': keys,
            'text': values
        })

        df.to_csv(os.path.join(self.output_csv_dir, self.csv_filename), encoding='utf-8-sig', index=False)