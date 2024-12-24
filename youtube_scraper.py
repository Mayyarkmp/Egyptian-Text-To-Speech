import os
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


class YouTubeScraper:
    
    
    def __init__(self, channel_name, channel_url, voice, output_dir, csv_name):
        self.channel_name = channel_name
        self.channel_url = channel_url
        self.voice = voice
        self.output_dir = output_dir
        self.csv_name = csv_name
        self._driver = webdriver.Chrome()
    
    
    def _scroll_to_end(self):
        last_height = self._driver.execute_script("return document.documentElement.scrollHeight")
        
        while True:
            self._driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self._driver.execute_script("return document.documentElement.scrollHeight")
            
            if new_height == last_height:
                break
                
            last_height = new_height


    def _split_time_ago(self, text):
        splitted_text = text.split()
        num = splitted_text[0]
        time_period = splitted_text[1].replace('s', '')
        return num, time_period


    def collect_data(self):
        self._driver.get(self.channel_url)
        time.sleep(2)

        self._scroll_to_end()

        video_title_lst = []
        release_date_lst1 = []
        release_date_lst2 = []
        video_link_lst = []
        video_duration_lst = []
        
        video_details = self._driver.find_elements(By.ID, 'video-title-link')
        video_time_dates = self._driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[2]')
        video_durations = self._driver.find_elements(By.XPATH, '//*[@id="length"]')
        
        for i, video_detail in enumerate(video_details):            
            video_link_lst.append(video_detail.get_attribute('href'))
            video_title_lst.append(video_detail.get_attribute('title'))
            video_duration_lst.append(video_durations[i].get_attribute('aria-label').split()[0])

            num, time_period = self._split_time_ago(video_time_dates[i].text)
            release_date_lst1.append(num)
            release_date_lst2.append(time_period)

        self._driver.quit()

        df = pd.DataFrame({
            'channel_name': [self.channel_name]*len(video_link_lst),
            'video_title': video_title_lst,
            'release_date_1': release_date_lst1,
            'release_date_2': release_date_lst2,
            'video_link': video_link_lst,
            'video_duration (min)': video_duration_lst,
            'voice': [self.voice]*len(video_link_lst),
        })
        
        df.to_csv(os.path.join(self.output_dir, self.csv_name), encoding='utf-8-sig', index=False)