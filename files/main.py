import glob
import os
from zipfile import ZipFile


__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# cur_work_file_dir = os.path.realpath(__file__)
cur_work_dir = os.path.dirname(__file__)
cache_dir_name = "cache"
cache_path = os.path.join(cur_work_dir, cache_dir_name)
zip_file_loc = os.path.join(cur_work_dir, "data.zip")
pattern = os.path.join(cache_path, "*")


def clean_cache():
    isExist = os.path.exists(cache_path)
    # print(f"directory exist is {isExist}")
    if not isExist:
        # print(f"creating {cache_path}")
        os.makedirs(cache_path)
    else:
        for file in glob.iglob(pattern, recursive=True):
            # print(file)
            os.remove(file)


def cache_zip(zip_file_loc, cache_path):
    # loading the temp.zip and creating a zip object
    with ZipFile(zip_file_loc, "r") as zObject:
        # Extracting the zip
        # into a specific location.
        zObject.extractall(path=cache_path)
        # zObject.close()


def cached_files():
    path = []
    for files in os.listdir(cache_path):
        path.append(os.path.join(cache_path, files))
        # path.append(files)
    return path


def find_password(cached_files):
    string_to_find = ""
    for file in glob.iglob(pattern, recursive=True):
        # print(file)
        with open(file) as f:
            # print(file)
            lines = f.read().splitlines()
            for i in lines:
                try:
                    converted = float(i)
                    if isinstance(converted, float):
                        None
                except ValueError:
                    string_to_find = i
            # print(lines)
        # f.close()
    find_space_index = string_to_find.find(" ")
    password = string_to_find[find_space_index + 1 :]
    # print(password)
    return password


if __name__ == "__main__":
    clean_cache()
    cache_zip(zip_file_loc, cache_path)
    find_password(cache_path)
