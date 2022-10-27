import os
from datetime import date, timedelta

number_of_day = 100
today = date.today()


def get_delta_time(days):
    delta_time = date.today() - timedelta(days=days)
    return delta_time


def get_modified_date(path):
    directory_date = os.path.getmtime(path)
    date_modified = date.fromtimestamp(directory_date)
    return date_modified


def is_remove_candidate(date_modified, delta_time):
    if date_modified > delta_time:
        return True
    else:
        return False


def remove_directory(directory):
    # shutil.rmtree(directory)
    print(f'{directory}, Directory has been deleted')


def main(root_directory, days):
    candidate_list = []
    for path in os.listdir(root_directory):
        directory = os.path.join(root_directory, path)
        if os.path.isdir(directory):
            delta_time = get_delta_time(days)
            date_modified = get_modified_date(directory)
            candidate_status = is_remove_candidate(date_modified, delta_time)
            if candidate_status is True:
                candidate_list.append(directory)
                remove_directory(directory)
    # print(candidate_list)


main('/Users/hossein/Documents/', number_of_day)
