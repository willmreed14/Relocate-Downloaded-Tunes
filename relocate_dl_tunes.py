import os
import shutil
import time

# Paths
downloads_folder = "/Users/willreed/Downloads"
music_folder = "/Users/willreed/Documents/music/Downloaded Tunes"

# List of music file extensions to look for
music_extensions = ['.mp3', '.wav', '.flac', '.aac', '.m4a', '.ogg', '.wma']

def move_music_files():
    # Get list of files in the downloads folder
    for file_name in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, file_name)

        # Skip if it's not a file
        if not os.path.isfile(file_path):
            continue

        # Check if the file has a music extension
        if any(file_name.lower().endswith(ext) for ext in music_extensions):
            destination_path = os.path.join(music_folder, file_name)

            if os.path.exists(destination_path):
                # If the file already exists, delete the duplicate
                print(f"Duplicate found, deleting: {file_name}")
                os.remove(file_path)
            else:
                try:
                    # Move the file to the music folder
                    shutil.move(file_path, music_folder)
                    print(f"Moved: {file_name}")
                except Exception as e:
                    print(f"Failed to move {file_name}: {e}")

if __name__ == "__main__":
    print("Monitoring downloads folder for music files...")
    try:
        while True:
            move_music_files()
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("Script terminated by user.")
