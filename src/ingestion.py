from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUT_DIR = Path("data/parquet")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def process_file(path: Path):
    print("Processing", path)
    try:
        if path.suffix.lower() == '.csv':
            df = pd.read_csv(path)
        elif path.suffix.lower() in {'.xls', '.xlsx'}:
            df = pd.read_excel(path, sheet_name=0)
        else:
            print("Unsupported format", path)
            return
        out = OUT_DIR / (path.stem + '.parquet')
        df.to_parquet(out, index=False)
        print(f"Saved -> {out}")
    except Exception as e:
        print('Error processing', path, e)

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            process_file(Path(event.src_path))

if __name__ == '__main__':
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    observer = Observer()
    observer.schedule(NewFileHandler(), str(DATA_DIR), recursive=False)
    observer.start()
    print('Watching', DATA_DIR)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
