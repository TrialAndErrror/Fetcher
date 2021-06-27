from src.file_actions import read_spreadsheet
from src.thread_actions import get_all_videos, download_file


def run_fetch(files_list, audio=False):
    """
    Download all videos in all files for a given list of files.

    audio param is optional flag to indicate only audio downloads.
    :param files_list: list(str)
    :param audio: bool
    :return: None
    """
    count_sheets = len(files_list)
    count_videos = 0
    file: str
    # audio = False
    for file in files_list:
        if file.startswith('[AUDIO]') or audio:
            print(f'Working on Audio Spreadsheet {file[7:]}')
            audio = True
        else:
            print(f'\nWorking on {file}')
        output_dir_name, current_video_files = read_spreadsheet(file)
        count_videos += len(current_video_files)
        get_all_videos(current_video_files, output_dir_name, audio)
    return count_sheets, count_videos


def run_single_sheet(args):
    """
    Same as Run Fetch, but providing a list of one sheet as the files parameter.
    Accessible from GUI or using the -f parameter.


    :param args: dict
    :return:
    """
    return run_fetch([args["file"]], audio=args.get("audio", False))


def run_single_url(args):
    """
    Download a single url.
    Accessible from GUI or using the -u parameter.

    :param args: dict
    :return:
    """
    download_file(args["url"], 'Downloads', args.get("audio", False))
    num_sheets = 0
    num_videos = 1
    return num_sheets, num_videos