import os
import shutil
from datetime import date, timedelta

number_of_day = 0
today = date.today()


def get_modified_date(path):
    directory_date = os.path.getmtime(path)
    date_modified = date.fromtimestamp(directory_date)
    return date_modified


def remove_directory(directory, dry_pass=True):
    try:
        if not dry_pass:
            shutil.rmtree(directory)
        print(f'{directory},--> Directory has been deleted')

    except Exception as err:
        print(err)


def main(root_directory, days):
    candidate_list = []
    for path in os.listdir(root_directory):
        directory = os.path.join(root_directory, path)
        if os.path.isdir(directory):
            delta_time = date.today() - timedelta(days=days)
            date_modified = get_modified_date(directory)
            if delta_time > date_modified:
                candidate_list.append(directory)

    for directory in candidate_list:
        remove_directory(directory)


main('/Users/hossein/.Trash/', number_of_day)
