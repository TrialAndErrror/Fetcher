import pytube

DEBUG = False


def dev_show_streams(current_video_object):
    """
    FOR DEV MODE ONLY!
    Shows all available streams in the console.
    :param current_video_object: pytube.YouTube()
    :return: None
    """
    for stream in current_video_object.streams:
        if "video" in str(stream) and "mp4" in str(stream):
            print(stream)


def download_video(target_video, target_path):
    """
    Takes in the link to the target video and where to download it to.
    Downloads video based on ITag value of 22 (720p stream).
    :param target_video: str
    :param target_path: str
    :return: None
    """
    try:
        stream = target_video.streams.get_by_itag(22)
    except Exception as e:
        print(f'Error getting the default stream.\n\nError code {e}')
    else:
        print('Downloading video...')
        stream.download(target_path)
        print('Done')


def create_video_object(url):
    """
    Takes in a URL and creates a PyTube YT object.
    In debug mode, it can also show all available video streams.
    Currently set to stream 22, 720p video.
    :param url: str
    :return: video_object: pytube.YouTube()
    """

    try:
        video_object = pytube.YouTube(url)
    except Exception as e:
        print(f'Could not create youtube video object. \n\nError {e}')
    else:
        print('Video Object Created...')
        if DEBUG:
            dev_show_streams(video_object)
        return video_object
