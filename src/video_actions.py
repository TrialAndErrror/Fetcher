import logging
import pafy


def make_pafy_object(url, verbose=False):
    try:
        video_obj = pafy.new(url)
    except Exception as e:
        message = f'Error creating video object: {e}'
        if verbose:
            print(message)
        logging.error(message)
        return None
    else:
        return video_obj


def get_pafy_stream(video_obj, audio=False, verbose=False):
    try:
        if audio:
            video_stream = video_obj.getbestaudio('m4a', False)
        else:
            video_stream = video_obj.getbest('mp4', False)
    except Exception as e:
        message = f'Error creating stream from pafy object: {e}'
        if verbose:
            print(message)
        logging.error(message)
        return None
    else:
        return video_stream
