import time
import logging
from watchdog.observers import Observer
from src.cargo_agent_event_handler import CargoAgentEventHandler
import os

dev_analyze_file: str = os.getcwd() + "/data/raw/sample_2-animals_output.pickle"
dev_analyze_file_type: str = "MovingPandas.TrajectoryCollection"
dev_result_file: str = os.getcwd() + "/data/raw/result.json"


def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    listen_on = os.environ.get('OUTPUT_FILE', dev_analyze_file)
    write_to = os.environ.get('OUTPUT_FILE_CARGO_AGENT_PYTHON', dev_result_file)
    event_handler = CargoAgentEventHandler(
        output_file_name=listen_on,
        result_json_file_name=write_to,
        dev_analyze_file_type=dev_analyze_file_type
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
