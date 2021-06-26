import pafy


def pafy_download_video(file, output_dir_name, audio_only):
    if audio_only:
        download_audio(file, output_dir_name)
    else:
        download_video(file, output_dir_name)


def mycb(total, recvd, ratio, rate, eta):
    print(recvd, ratio, eta)


def download_video(file, output_dir_name):
    video_obj = pafy.new(file)
    video_stream = video_obj.getbest('mp4', False)
    video_stream.download(output_dir_name)


def download_audio(file, output_dir_name):
    video_obj = pafy.new(file)
    video_stream = video_obj.getbestaudio('m4a', False)
    video_stream.download(output_dir_name)
