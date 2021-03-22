import pytube
import logging

# This hard-coded default itag represents 720p videostreams. You ca
DEFAULT_ITAG = 22
AUDIO_ITAG = 251


def dev_show_streams(current_video_object):
    """
    Log all available video streams to the console. This enables the user to inspect logs to choose a different itag.

    :param current_video_object: pytube.YouTube()
    :return: None
    """
    for stream in current_video_object.streams:
        if "video" in str(stream) and "mp4" in str(stream):
            logging.debug(stream)
        if "audio" in str(stream):
            logging.debug(stream)


def download_video(target_video: pytube.YouTube, target_path: str, audio_only: bool):
    """
    Takes in the link to the target video and where to download it to.
    Downloads video based on ITag value of 22 (720p stream). Can change itag value to change resolution.
    If audio_only, downloads highest quality audio stream

    :param target_video: pytube.Youtube()
    :param target_path: str
    :param audio_only: bool
    :return: None
    """
    try:
        itag = DEFAULT_ITAG if not audio_only else AUDIO_ITAG
        stream = target_video.streams.get_by_itag(itag)
        while not stream:
            itag -= 1
            stream = target_video.streams.get_by_itag(itag)

    except Exception as e:
        logging.warning(f'Error getting the default stream.\n\nError code {e}')
    else:
        logging.info(f'Downloading video to {target_path}...')
        stream.download(target_path)
        logging.info(f'Done downloading to {target_path}.')


def create_video_object(url):
    """
    Takes in a URL and creates a PyTube YT object.
    In debug mode, it can also show all available video streams.

    :param url: str
    :return: video_object: pytube.YouTube()
    """

    try:
        video_object = pytube.YouTube(url=url)
    except Exception as e:
        logging.warning(f'Could not create youtube video object. \n\nError {e}')
    else:
        logging.info(f'Video Object Created for {url}...')
        dev_show_streams(video_object)
        return video_object
