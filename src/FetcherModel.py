import concurrent.futures
import logging
import os
import time

import pafy

import tqdm


class Fetcher:
    def __init__(self, video_list, output_dir, audio_only):
        self.video_list = video_list
        self.output_dir = output_dir
        self.audio_only = audio_only
        os.makedirs(self.output_dir, exist_ok=True)
        self.threads_list = []

        self.prev_received = 0

    def get_videos_using_threads(self):
        """
        Command-line based threading for video downloads.

        Create up to 5 threads at a time to get all videos. Number can be modified in max_workers parameter.

        :return: None
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            for video in self.video_list:
                self.make_and_append_thread(executor, video)
            self.thread_print_when_done()

    def make_and_append_thread(self, executor, video):
        """
        Make thread, and add to list if successful

        :param executor: concurrent.futures.ThreadPoolExecutor()
        :param video: str
        :return:
        """
        try:
            thread = executor.submit(self.download_file, video)
        except Exception as e:
            logging.warning(f'Error making thread for {video};\n\n error code {e}')
        else:
            self.threads_list.append(thread)
            time.sleep(.3)

    def download_file(self, item):
        """
        Function that runs on the thread; download item parameter to output directory.

        :param item: str
        :return: None
        """
        try:
            print(f'\nStarting downloading {item}')
            logging.info(f'Working on {item}')

            self.pafy_download_video(item)

            print(f'\nCompleted {item}')
        except Exception as e:
            logging.warning(f'Error downloading {item};\n\nerror {e}')

    def thread_print_when_done(self):
        """
        When a thread in the threads list finishes, output the return value to the log.

        :return: None
        """
        for thread in concurrent.futures.as_completed(self.threads_list):
            logging.debug(thread.result())

    def pafy_download_video(self, url):
        """
        Determine if audio only or not, then download accordingly.

        :param url:
        :param output_dir_name:
        :param audio_only:
        :return:
        """
        video_obj = pafy.new(url)
        if self.audio_only:
            video_stream = video_obj.getbestaudio('m4a', False)
        else:
            video_stream = video_obj.getbest('mp4', False)
            """
            video_stream.download(filepath=self.output_dir)
            """
            with tqdm.tqdm(desc=f"{video_obj.title}", total=video_stream.get_filesize(), unit_scale=True, unit='B', initial=0, maxinterval=100) as pbar:
                video_stream.download(quiet=True, filepath=self.output_dir, callback=lambda _, received, *args: self.update(pbar, received))


    def update(self, pbar, current_received):
        diff = current_received - self.prev_received
        pbar.update(diff)
        self.prev_received = current_received


