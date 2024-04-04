import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from downloadMan import download_manager    

DOWNLOAD_FOLDER = "D:/teste/"
DOWNLOAD_SORCE = "C:/Users/games/Downloads"
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        time.sleep(1)
        print(f"Arquivo criado: {event.src_path}")
        # Aqui você pode executar o seu programa
        download_manager(DOWNLOAD_SORCE,DOWNLOAD_FOLDER)  

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DOWNLOAD_SORCE, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

