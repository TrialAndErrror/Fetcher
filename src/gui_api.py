from src.fetch import fetch, run_single_file, run_single_sheet
from src.debug_tools import timer, report_success_or_failure


def process_gui_command(command):
    if command['type'] == 'url':
        args = {'url': command['url'], 'audio': command.get('audio', False)}
        run_single_file(args)
        print(f'\nSuccess! Downloaded {args["url"]}.')

    elif command['type'] == 'sheet':
        if command.get('file', None):
            args = {'file': command['file'], 'audio': command.get('audio', False)}
            num_sheets, num_videos = run_single_sheet(args)
        else:
            num_sheets, num_videos = fetch(audio=command.get("audio", False))
        report_success_or_failure(num_sheets, num_videos)

    else:
        num_sheets, num_videos = 0, 0
        report_success_or_failure(num_sheets, num_videos)
