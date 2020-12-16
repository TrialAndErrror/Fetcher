import pytube

DEBUG = False


def dev_show_streams(current_video_object):
    for stream in current_video_object.streams:
        if "video" in str(stream) and "mp4" in str(stream):
            print(stream)


def download_video(target_video):
    try:
        stream = target_video.streams.get_by_itag(22)
    except Exception as e:
        print(f'Error getting the default stream.\n\nError code {e}')
    else:
        print('Downloading video...')
        stream.download()
        print('Done')


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
