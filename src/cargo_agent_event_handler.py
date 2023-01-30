from watchdog.events import FileSystemEventHandler
import logging
import json
from src.analyzer.moving_pandas_analyzer import MovingPandasAnalyzer


class CargoAgentEventHandler(FileSystemEventHandler):

    def __init__(self, output_file_name):
        super().__init__()
        logging.info(f'init for {output_file_name}')
        self.output_file_name = output_file_name
        self.moving_pandas_analyzer = MovingPandasAnalyzer()

    def on_any_event(self, event):
        super().on_any_event(event)

        if not event.is_directory:
            if event.src_path == self.output_file_name:
                if event.event_type == "created" or event.event_type == "modified":
                    logging.info(f'output-file change detected! {event}')
                    deserialize = self.moving_pandas_analyzer.read(path=event.src_path)
                    result = self.moving_pandas_analyzer.analyze(data=deserialize)
                    j = json.dumps(result)
                    print(j)
                    return
        logging.debug(f'skipping {event}')
