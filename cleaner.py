import os
from datetime import date, timedelta

number_of_day = 100
today = date.today()
candidate_list = []


def get_modified_date(path, days):
    delta_time = date.today() - timedelta(days=days)
    directory_date = os.path.getmtime(path)
    date_modified = date.fromtimestamp(directory_date)
    return delta_time, date_modified


def is_remove_candidate(directory, date_modified, delta_time):
    if date_modified < delta_time:
        candidate_list.append(directory)
    return candidate_list


def remove_directory(remove_list):
    for directory in range(len(remove_list)):
        removed_directory = candidate_list[directory]
        print(f'{removed_directory}Directory has been deleted')

        # os.chdir(drive)
        # shutil.rmtree('testFolder')
        # print(file_list)
        # print('Directory has been deleted')


def main(root_directory, days):
    for path in os.listdir(root_directory):
        directory = os.path.join(root_directory, path)
        if os.path.isdir(directory):
            delta_time, date_modified = get_modified_date(directory, days)
            remove_list = is_remove_candidate(directory, delta_time, date_modified)
            remove_directory(remove_list)
    # print(candidate_list)


main('/Users/hossein/Documents/', number_of_day)
