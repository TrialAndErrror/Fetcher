import concurrent.futures
import logging
import time

from src.video_actions import make_pafy_object, get_pafy_stream


class Fetcher:
    def __init__(self, video_list, output_dir, audio_only):
        self.video_list = video_list
        self.output_dir = output_dir
        self.audio_only = audio_only
        self.threads_list = []

        self.verbose = True

    def get_videos_using_threads(self):
        """
        Command-line based threading for video downloads.

        Create up to 5 threads at a time to get all videos. Number can be modified in max_workers parameter.

        :return: None
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

            for video in self.video_list:
                self.make_and_append_thread(executor, video)

            for thread in concurrent.futures.as_completed(self.threads_list):
                logging.debug(thread.result())

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

    def download_file(self, url):
        """
        Function that runs on the thread; download item parameter to output directory.

        :param url: str
        :return: None
        """
        video_obj = make_pafy_object(url)

        if self.verbose:
            print(f'Downloading {video_obj.title}')

        if video_obj:
            video_stream = get_pafy_stream(video_obj, audio=self.audio_only, verbose=self.verbose)
            if video_stream:
                video_stream.download(filepath=self.output_dir, quiet=True)

            if self.verbose:
                print(f'Finished downloading {video_obj.title}\n')
