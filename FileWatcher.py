import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- PATH CONFIGURATIONS ---
# expanduser ensures it works across different user profiles
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")
DESKTOP_DIR = os.path.expanduser("~/Desktop")

# --- EXTENSION MAPPING ---
# Define your categories and their respective file extensions
EXTENSION_MAP = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh"]
}

class FileOrganizerHandler(FileSystemEventHandler):
    """
    Handles file system events. Whenever a change is detected,
    it triggers the organization logic for both targeted directories.
    """
    def on_modified(self, event):
        self.organize_directory(DOWNLOADS_DIR)
        self.organize_directory(DESKTOP_DIR)

    def organize_directory(self, target_path):
        for filename in os.listdir(target_path):
            file_path = os.path.join(target_path, filename)
            
            # Skip if it's a directory or the script itself
            if os.path.isdir(file_path) or filename.endswith(".py"):
                continue

            # Extract extension and check against the map
            extension = os.path.splitext(filename)[1].lower()
            moved = False

            for category, extensions in EXTENSION_MAP.items():
                if extension in extensions:
                    destination_dir = os.path.join(target_path, category)
                    
                    # Create the category folder if it doesn't exist
                    if not os.path.exists(destination_dir):
                        os.makedirs(destination_dir)
                    
                    try:
                        shutil.move(file_path, os.path.join(destination_dir, filename))
                        print(f"Moved: {filename} -> {category}")
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")
                    
                    moved = True
                    break
            
            # Optional: Move unknown file types to an 'Others' folder
            if not moved and extension != "":
                others_dir = os.path.join(target_path, "Others")
                if not os.path.exists(others_dir):
                    os.makedirs(others_dir)
                try:
                    shutil.move(file_path, os.path.join(others_dir, filename))
                except Exception as e:
                    print(f"Error moving {filename} to Others: {e}")

if __name__ == "__main__":
    event_handler = FileOrganizerHandler()
    observer = Observer()
    
    # Schedule monitoring for both Desktop and Downloads
    observer.schedule(event_handler, DOWNLOADS_DIR, recursive=False)
    observer.schedule(event_handler, DESKTOP_DIR, recursive=False)
    
    print(f"Watcher started: Monitoring Downloads and Desktop...")
    observer.start()

    try:
        while True:
            # Sleep prevents the loop from consuming too much CPU
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nStopping watcher...")
        observer.stop()
    
    observer.join()
