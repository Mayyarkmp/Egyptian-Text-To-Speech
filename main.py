from modules.audio_transcriber import AudioTranscriber

def main():
    name = 'ADD_NAME_HERE'
    target_lang = 'ADD_LANG_HERE'
    transcriber = AudioTranscriber(csv_filename=f'{name}.csv', target_lang=target_lang)

    folder_path = 'PATH/TO/AUDIOS'
    transcriber.transcribe_audio_folder(folder_path)

if __name__ == '__main__':
    main()