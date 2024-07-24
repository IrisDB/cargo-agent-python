import time
import logging
from watchdog.observers import Observer
from src.cargo_agent_event_handler import CargoAgentEventHandler
import os

dev_analyze_file: str = os.getcwd() + "/resources/raw/input1_LatLon.pickle"
dev_analyze_file_type_slug: str = "moving_pandas_trajectory_collection"
dev_result_file: str = os.getcwd() + "/resources/result/result.json"
dev_working_copy: str = os.getcwd() + "/resources/result/working_copy"


def main():
    logging.basicConfig(
        level=os.environ.get('LOG_LEVEL_CARGO_AGENT_PYTHON', 'INFO'),
        format=os.environ.get(
            'LOG_PATTERN_CARGO_AGENT_PYTHON',
            '%(asctime)s.%(msecs)03d %(relativeCreated)6d [%(threadName)s] %(name)s %(levelname)s: %(message)s'
        ),
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    listen_on = os.environ.get('OUTPUT_FILE', dev_analyze_file)
    event_handler = CargoAgentEventHandler(
        output_file_name=listen_on,
        result_json_file_name=os.environ.get('OUTPUT_FILE_CARGO_AGENT_PYTHON', dev_result_file),
        analyze_file_type_slug=os.environ.get('OUTPUT_TYPE_SLUG', dev_analyze_file_type_slug),
        working_copy=os.environ.get('OUTPUT_WORKING_COPY_FILE', dev_working_copy)
    )
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(listen_on), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main()
