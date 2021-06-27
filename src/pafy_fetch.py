import pafy


def pafy_download_video(url, output_dir_name, audio_only):
    """
    Determine if audio only or not, then download accordingly.
    
    :param url: 
    :param output_dir_name: 
    :param audio_only: 
    :return: 
    """
    video_obj = pafy.new(url)
    if audio_only:
        video_stream = video_obj.getbestaudio('m4a', False)
    else:
        video_stream = video_obj.getbest('mp4', False)
    video_stream.download(output_dir_name)