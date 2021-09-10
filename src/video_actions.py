import logging
import pafy


def make_pafy_object(url, audio_only):
    try:
        video_obj = pafy.new(url)
    except Exception as e:
        message = f'Error creating video object: {e}'
        logging.error(message)
        return None
    else:
        return get_pafy_stream(video_obj, audio_only)


def get_pafy_stream(video_obj, audio_only):
    try:
        if audio_only:
            video_stream = video_obj.getbestaudio('m4a', False)
        else:
            video_stream = video_obj.getbest('mp4', False)
    except Exception as e:
        message = f'Error creating stream from pafy object: {e}'
        logging.error(message)
        return None
    else:
        return video_stream
