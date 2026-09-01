from pathlib import Path

# path to folder
root_folder = Path.home() / "Downloads"

folders = {
    "images": ["jpg", "jpeg", "png", "gif", "bmp"],
    "videos": ["mp4", "webm"],
    "audio": ["mp3", "ogg", "wav"],
    "documents": ["doc", "docx", "odt", "txt", "pdf"],
    "archives": ["zip", "7z", "tar", "gz", "rar"],
    "executables": ["exe"],
    "litematica schematics": ["litematic"],
    "jar files": ["jar"]
}

for item in root_folder.iterdir():
    if item.is_file():
        extension = item.suffix.lower().lstrip(".")
        is_moved = False

        for target_folder, extension_list in folders.items():
            if extension in extension_list:
                dest_dir = root_folder / target_folder
                dest_dir.mkdir(parents=True, exist_ok=True)
                item.rename(dest_dir / item.name)
                is_moved = True
                break

        if not is_moved:
            dest_dir = root_folder / "unsorted"
            dest_dir.mkdir(parents=True, exist_ok=True)
            item.rename(dest_dir / item.name)
