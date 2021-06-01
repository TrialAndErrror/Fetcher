import pytube
import logging
import os
from pathlib import Path
# from moviepy.editor import AudioFileClip
from moviepy.audio.io import AudioFileClip

# This hard-coded default itag represents 720p videostreams.
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
        """
        Starting from default ITAG,
        use a while loop to get streams by ITAG.
        Decrement by 1 until we get a valid stream.
        """
        itag = DEFAULT_ITAG if not audio_only else AUDIO_ITAG
        stream = target_video.streams.get_by_itag(itag)
        while not stream:
            itag -= 1
            stream = target_video.streams.get_by_itag(itag)

    except Exception as e:
        logging.warning(f'Error getting the default stream.\n\nError code {e}')
    else:
        """
        Cleanup the filename before downloading so that we can avoid changing the filename of videos with
        invalid characters in their titles.
        
        Omitted because of MoviePy error: []
        """
        stream_title = process_title(stream.title)
        file_name = "".join(x for x in stream_title if x.isalnum() or x in "_ ()-")


        """
        Once we have a valid stream and filename, download to target path
        """
        logging.info(f'Downloading {file_name} to {target_path}...')

        stream.download(target_path, filename=file_name)

        """
        Special handling for audio only files; they need to be renamed
        """
        if audio_only:
            """
            Rename file from mp4 to mp3
            """
            clip_path = str(Path(os.getcwd(), target_path, f"{file_name}.webm"))
            my_clip = AudioFileClip.AudioFileClip(clip_path)
            print(f'Converting {file_name} to MP3 file')
            my_clip.write_audiofile(str(Path(os.getcwd(), target_path, f'{file_name}.mp3')))
            os.remove(Path(target_path, f'{file_name}.webm'))

        os.startfile(target_path)
        logging.info(f'Done downloading {file_name}.')


def process_title(title):
    stream_title = title
    stream_title = stream_title.replace("[", '(')
    stream_title = stream_title.replace("]", ")")
    return stream_title


def create_video_object(url):
    """
    Takes in a URL and creates a PyTube YT object.
    In debug mode, it can also show all available video streams.

    :param url: str
    :return: video_object: pytube.YouTube()
    """

    try:
        """
        Attempt to make the video object; if this fails, then PyTube isn't working.
        """
        video_object = pytube.YouTube(url=url)
    except Exception as e:
        logging.warning(f'Could not create youtube video object. \n\nError {e}')
    else:
        logging.info(f'Video Object Created for {url}...')
        dev_show_streams(video_object)
        return video_object
