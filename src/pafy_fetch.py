import pafy
import logging


def pafy_download_playlist(url, output_dir_name, audio_only, callback=None):
    playlist = pafy.get_playlist(url)
    output_dir_name += f'/{playlist.get("title", "Playlist")}/'
    for video_link in playlist['items']:
        pafy_get(audio_only, output_dir_name, video_link['pafy'], callback)


def pafy_download(url, output_dir_name, audio_only, callback=None):
    """
    Create video object;
    Determine if audio only or not;
    then download accordingly.
    
    :param url: str
    :param output_dir_name: str
    :param audio_only: bool
    :return: None
    """
    video_obj = make_pafy_video_object(url)
    """
    If error in make_pafy_video, then video_obj will be none and it will skip the following steps.
    output_dir_name is a string that represents the folder to save the video/audio file to.
    """
    if video_obj:
        pafy_get(audio_only, output_dir_name, video_obj, callback)


def pafy_get(audio_only, output_dir_name, video_obj, callback=None):
    if audio_only:
        pafy_get_audio(output_dir_name, video_obj, callback)
    else:
        pafy_get_video(output_dir_name, video_obj, callback)


def make_pafy_video_object(url):
    """
    Make video object from url using Pafy.

    :param url: str
    :return: pafy.Pafy()
    """
    try:
        video_obj = pafy.new(url)
    except Exception as e:
        logging.warning(f'Error creating PAFY video object from url {url}; error {e}')
    else:
        return video_obj
    finally:
        return None


def pafy_get_video(output_dir_name, video_obj, callback=None):
    """
    Get best video stream from video_obj;
    if stream found, download video.

    :param output_dir_name: str
    :param video_obj: pafy.Pafy()
    :return: None
    """
    try:
        video_stream = video_obj.getbest('mp4', False)
    except Exception as e:
        logging.warning(f'Error creating PAFY video stream from video object for {video_obj.title}; error {e}')
    else:
        if callback:
            video_stream.download(output_dir_name, callback=callback)
        else:
            video_stream.download(output_dir_name)


def pafy_get_audio(output_dir_name, video_obj, callback=None):
    """
    Get best audio stream from video_obj;
    if stream found, download audio.

    :param output_dir_name: str
    :param video_obj: pafy.Pafy()
    :return: None
    """
    try:
        video_stream = video_obj.getbestaudio('m4a', False)
    except Exception as e:
        logging.warning(f'Error creating PAFY audio stream from video object for {video_obj.title}; error {e}')
    else:
        if callback:
            video_stream.download(output_dir_name, callback=callback)
        else:
            video_stream.download(output_dir_name)
