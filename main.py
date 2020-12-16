import sys
import os
import pytube

from Classes import Fetcher

DEBUG = False


def read_list_path(path):
    try:
        file = open(path)
    except Exception as e:
        print('Could not read file')
        print(f'Error: {e}')
    else:
        video_string = file.read()
        video_files = video_string.split(',')
        file.close()
        return video_files


def dev_show_streams(current_video_object):
    for stream in current_video_object.streams:
        if "video" in str(stream) and "mp4" in str(stream):
            print(stream)


def create_video_object(url):
    try:
        video_object = pytube.YouTube(url)
    except Exception as e:
        print(f'Could not create youtube video object. \n\nError {e}')
    else:
        print('Video Object Created...')
        if DEBUG:
            dev_show_streams(video_object)
        return video_object


def download_video(target_video):
    try:
        stream = target_video.streams.get_by_itag(22)
    except Exception as e:
        print(f'Error getting the default stream.\n\nError code {e}')
    else:
        print('Downloading video...')
        stream.download()
        print('Done')


def download_all_videos(files, path):
    for item in files:
        print(f'Working on {item}')
        current_video = create_video_object(item)
        download_video(current_video, path)


def print_done():
    print('All Done')


def find_files():
    try:
        home_dir = os.listdir()
    except Exception as e:
        print('Error reading files in home directory')
        print(f'Error was {e}')
    else:
        files_list = [file for file in home_dir if file[-4:] == '.csv']
        return files_list


def start_project():
    files_list = find_files()
    for file in files_list:
        video_files = read_list_path(file)
        path = f'/{file}'
        download_all_videos(video_files, path)
    print_done()


def fetch():
    myFetcher = Fetcher()
    myFetcher.fetch()


if __name__ == '__main__':
    fetch()
    # start_project()
