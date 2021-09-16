import os

from src.file_actions import find_youtube_links
from src.gui.models.ProgressWindow import ProgressDisplay


def get_file_names():
    file_names = os.listdir(os.getcwd())

    # return [file for file in file_names
    #         if file.endswith('.xls')
    #         or file.endswith('.csv')
    #         or file.endswith('.xlsx')]

    return [file for file in file_names if file.endswith('.csv')]


def clean_video_urls(video_files):
    video_set = set(video_files)
    cleaned_video_urls = list(video_set)

    return cleaned_video_urls


def process_one_sheet(file, audio):
    output_dir, video_files = find_youtube_links(file)
    cleaned_video_urls = clean_video_urls(video_files)
    return ProgressDisplay(output_dir, urls=cleaned_video_urls, audio=audio), output_dir
