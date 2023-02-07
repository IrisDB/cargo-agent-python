import os
import shutil
from watchdog.events import FileSystemEventHandler
import logging
import json
from src.analyzer.moving_pandas_trajectory_collection.analyzer import MovingPandasAnalyzer
from src.analyzer.void.analyzer import VoidAnalyzer


class CargoAgentEventHandler(FileSystemEventHandler):

    def __init__(self, output_file_name, result_json_file_name, analyze_file_type, working_copy):
        super().__init__()
        logging.info(f'init for {output_file_name}')
        self.output_file_name = output_file_name
        self.result_file_name = result_json_file_name
        self.my_working_copy = working_copy
        output_type_to_analyze = analyze_file_type
        match output_type_to_analyze:
            case "MovingPandas.TrajectoryCollection":
                self.analyzer = MovingPandasAnalyzer()
            case _:
                self.analyzer = VoidAnalyzer()

    def on_any_event(self, event):
        super().on_any_event(event)

        if not event.is_directory:
            if event.src_path == self.output_file_name:
                if event.event_type == "created" or event.event_type == "modified":
                    logging.info(f'output-file change detected! {event}')
                    shutil.copy2(event.src_path, self.my_working_copy)
                    result = self.analyzer.analyze(path=self.my_working_copy)
                    self.__write_result(result=result)
                    return
        logging.debug(f'skipping {event}')

    def __write_result(self, result: dict) -> None:
        j = json.dumps(result)
        logging.info(f'result: {j}')
        with open(self.result_file_name, "w") as result_json_file:
            result_json_file.write(j)

