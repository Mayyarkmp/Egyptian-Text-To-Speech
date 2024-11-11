import os
from audio_splitter import AudioSplitter
from youTube_scraper import YouTubeScraper
from audio_transcriber import AudioTranscriber


def akhdar_conditional_function(lst1, lst2, output_audio_dir):
    remove_file1 = lst1[-1]
    remove_file2 = lst1[-2]

    os.remove(os.path.join(output_audio_dir, remove_file1+'.wav'))
    os.remove(os.path.join(output_audio_dir, remove_file2+'.wav'))

    length = len(lst1)
    lst1 = lst1[:length-2]
    lst2 = lst2[:length-2]

    return lst1, lst2


def main():
    scraper = YouTubeScraper('Akhdar', 'https://www.youtube.com/@a5drcom/videos', 'voice 1', './datasets_csv/main_datasets', 'akhdar_data.csv')
    scraper.collect_data()

    scraper = YouTubeScraper('ReadTube', 'https://www.youtube.com/@Jeelyaqraa/videos', 'voice 3', './datasets_csv/main_datasets', 'readtube_data.csv')
    scraper.collect_data()

    scraper = YouTubeScraper('Ali_Muhammad_Ali', 'https://www.youtube.com/@AliMuhammadAli/videos', 'voice 4', './datasets_csv/main_datasets', 'ali_muhammad_ali_data.csv')
    scraper.collect_data()


def main_akhdar():
    # downloader = AudioSplitter('./datasets_csv/cleaned_datasets/akhdar_data_cleaned.csv', 'audio', 'akhdar', 'akhdar_splitted_audio.csv', conditional_function=akhdar_conditional_function)
    downloader = AudioSplitter('./datasets_csv/cleaned_datasets/akhdar_data_cleaned.csv', 'audio', 'akhdar', 'akhdar_splitted_audio.csv')
    downloader.process_videos()


def main_readtube():
    downloader = AudioSplitter('./datasets_csv/cleaned_datasets/readtube_cleaned.csv', 'audio', 'readtube', 'readtube_splitted_audio.csv')
    downloader.process_videos()


def main_ali_muhammad_ali():
    downloader = AudioSplitter('./datasets_csv/cleaned_datasets/ali_muhammad_ali_cleaned.csv', 'audio', 'ali_muhammad_ali', 'ali_muhammad_ali_splitted_audio.csv')
    downloader.process_videos()

def main_trascribe():
    name = 'ADD_NAME_HERE'
    target_lang = 'ADD_LANG_HERE'
    transcriber = AudioTranscriber(csv_filename=f'{name}.csv', target_lang=target_lang)

    folder_path = './audios/splitted_audios'
    transcriber.transcribe_audio_folder(folder_path)

if __name__ == '__main__':
    # If you are going to scrape youtube run this main
    # main()

    # If you are going to download Akhdar audios run this main
    # main_akhdar()

    # If you are goint to download ReadTube audios run this main
    # main_readtube()

    # If you are goint to download Ali Muhammad Ali audios run this main
    # main_ali_muhammad_ali()

    # If you are going to extract text from audios run this
    # You must rename some variables in this function
    # main_trascribe()