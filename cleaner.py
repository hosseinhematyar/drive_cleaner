import os
from datetime import date, timedelta
from pathlib import Path

drive = '/Users/hossein/Desktop/drive/'
number_of_day = 1000
today = date.today()
candidate_list = []


def get_folder_list(directory):
    date_modified = get_date_modified(directory)
    for folder_path in Path(directory).iterdir():
        if folder_path.is_dir():
            # print(date_modified, folder_path)
            get_folder_list(folder_path)
    return date_modified, directory


def get_date_modified(directory):
    directory_date = os.path.getmtime(directory)
    date_modified = date.fromtimestamp(directory_date)
    return date_modified


def date_check():
    delta_time = date.today() - timedelta(days=number_of_day)
    print('Delta Date: -->', delta_time)

    date_modified, directory = get_folder_list(drive)
    print('Date Modified: -->', date_modified)
    print('Folder: -->', directory)

    # if delta_time < date_modified:
    #     candidate_list.append(directory)
    #     print(candidate_list)
    # else:
    #     print('ERROR!')


# def remove():
#     os.chdir(drive)
#     shutil.rmtree('testFolder')
#     file_list = os.listdir('.')
#     print(file_list)


get_folder_list(drive)
date_check()
