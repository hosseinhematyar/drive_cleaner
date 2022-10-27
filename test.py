from pathlib import Path

root_folder = '/Users/hossein/Desktop/drive/'


def listdirs(root_folder):
    for path in Path(root_folder).iterdir():
        if path.is_dir():
            print(path)
            listdirs(path)


listdirs(root_folder)
