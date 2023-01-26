from watchdog.events import FileSystemEventHandler
import logging


class CargoAgentEventHandler(FileSystemEventHandler):

    def __init__(self, output_file_name):
        super().__init__()
        logging.info(f'init for {output_file_name}')
        self.output_file_name = output_file_name

    def on_any_event(self, event):
        super().on_any_event(event)

        if not event.is_directory:
            if event.src_path == self.output_file_name:
                if event.event_type == "created" or event.event_type == "modified":
                    logging.info(f'output-file change detected! {event}')
                    return
        logging.debug(f'skipping {event}')
