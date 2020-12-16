import os


def find_files():
    '''
    Generates list of CSV files in current working directory.

    :return: (files_found: bool; files_list: list)
    '''

    try:
        home_dir = os.listdir()
    except Exception as e:
        print('Error reading files in home directory')
        print(f'Error was {e}')
    else:
        files_list = [file for file in home_dir if file[-4:] == '.csv']
        files_found = bool(len(files_list) > 0)
        return files_found, files_list


def read_list_path(path):
    '''
    Reads CSV file located at path param and returns all video files contained within

    :param path: str
    :return: (current_path: str, current_video_files: list(str)
    '''
    try:
        file = open(path)
    except Exception as e:
        print('Could not read file')
        print(f'Error: {e}')
    else:
        current_path = f'/{file}'
        video_string = file.read()
        current_video_files = video_string.split(',')
        file.close()
        return current_path, current_video_files
