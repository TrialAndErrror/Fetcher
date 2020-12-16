from src.video_actions import download_video, create_video_object
from src.file_actions import find_files, read_list_path


class Fetcher:
    def __init__(self):
        self.files_list = []
        self.files_found = False
        self.current_video_files = []
        self.current_path = ''
        self.output_dir_name = ''

    def fetch(self):
        (self.files_found, self.files_list) = find_files()
        if self.files_found:
            for file in self.files_list:
                self.output_dir_name = file[:-4]
                self.current_path, self.current_video_files = read_list_path(file)
                self.download_all_videos()
            print('All Done')
        else:
            print('No files found; please place CSV files in this directory')

    def download_all_videos(self):
        for item in self.current_video_files:
            print(f'Working on {item}')
            current_video = create_video_object(item)
            download_video(current_video, self.output_dir_name)



