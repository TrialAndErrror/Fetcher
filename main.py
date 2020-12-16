from src.video_actions import download_video, create_video_object
from src.file_actions import find_files, read_list_path


def fetch():
    """
    Perform Video Fetch.
    :return: None
    """
    (files_found, files_list) = find_files()
    if files_found:
        download_all_videos(files_list)
        print('All Done')
    else:
        print('No files found; please place CSV files in this directory')


def download_all_videos(files_list):
    """
    Download all videos in all files for a given list of files.
    :param files_list: list(str)
    :return: None
    """
    for file in files_list:
        output_dir_name = file[:-4]
        current_video_files = read_list_path(file)
        for item in current_video_files:
            print(f'Working on {item}')
            current_video = create_video_object(item)
            download_video(current_video, output_dir_name)


if __name__ == '__main__':
    fetch()
