import os
from audio_splitter import AudioSplitter
from youTube_scraper import YouTubeScraper


def akhdar_conditional_function(lst1, lst2, output_audio_dir):
    remove_file1 = lst1[-1]
    remove_file2 = lst1[-2]

    os.remove(os.path.join(output_audio_dir, remove_file1+'.wav'))
    os.remove(os.path.join(output_audio_dir, remove_file2+'.wav'))

    length = len(lst1)
    lst1 = lst1[:length-2]
    lst2 = lst2[:length-2]

    return lst1, lst2


if __name__ == '__main__':
    # scraper = YouTubeScraper('Akhdar', 'https://www.youtube.com/@a5drcom/videos', 'voice 1', './datasets_csv', 'akhdar_data.csv')
    # scraper.collect_data()

    # scraper = YouTubeScraper('ReadTube', 'https://www.youtube.com/@Jeelyaqraa/videos', 'voice 3', './datasets_csv', 'readtube_data.csv')
    # scraper.collect_data()

    scraper = YouTubeScraper('Ali_Muhammad_Ali', 'https://www.youtube.com/@AliMuhammadAli/videos', 'voice 4', './datasets_csv', 'ali_muhammad_ali_data.csv')
    scraper.collect_data()
    
    # downloader = AudioSplitter('./datasets_csv/akhdar_data_modified.csv', 'audio', 'akhdar', 'akhdar_splitted_audio.csv', conditional_function=akhdar_conditional_function)
    # downloader.process_videos()