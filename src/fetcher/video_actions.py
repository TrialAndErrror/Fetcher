import pytube

# Set this to True to show all streams available for your video
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


def download_video(target_video: pytube.YouTube, target_path: str):
    """
    Takes in the link to the target video and where to download it to.
    Downloads video based on ITag value of 22 (720p stream). Can change itag value to change resolution.

    :param target_video: pytube.Youtube()
    :param target_path: str
    :return: None
    """
    try:
        itag = 22
        stream = target_video.streams.get_by_itag(itag)
    except Exception as e:
        print(f'Error getting the default stream.\n\nError code {e}')
    else:
        print(f'Downloading video to {target_path}...')
        stream.download(target_path)
        print(f'Done downloading to {target_path}.')


def create_video_object(url):
    """
    Takes in a URL and creates a PyTube YT object.
    In debug mode, it can also show all available video streams.

    :param url: str
    :return: video_object: pytube.YouTube()
    """

    try:
        video_object = pytube.YouTube(url)
    except Exception as e:
        print(f'Could not create youtube video object. \n\nError {e}')
    else:
        print(f'Video Object Created for {url}...')
        if DEBUG:
            dev_show_streams(video_object)
        return video_object
