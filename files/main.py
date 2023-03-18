import pathlib
import os
import shutil
from zipfile import ZipFile


__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# cur_work_dir = pathlib.Path().absolute()
cur_work_dir = pathlib.Path("main.py").absolute()
path = "cache"
cache_dir = str(cur_work_dir.parent) + f"/{path}"
zip_file_loc = str(cur_work_dir) + "/data.zip"


def clean_cache():
    isExist = pathlib.Path(cache_dir).exists()
    print(f"directory exist is {isExist}")
    if not isExist:
        print(f"creating {cache_dir}")
        pathlib.Path(cache_dir).mkdir()
    else:
        print(f"removing  everything in {cache_dir}")
        pathlib.Path(cache_dir).rmdir()


# print(isExist)
# if not isExist:
#     pathlib.Path.mkdir(cache_dir)
# else:
#     for files in os.listdir(cache_dir):
#         path = os.path.join(cache_dir, files)
#         try:
#             # remove subdirectory
#             shutil.rmtree(path)
#         except OSError:
#             # remove file
#             os.remove(path)


# def cache_zip(zip_file_loc, cache_dir):
#     # loading the temp.zip and creating a zip object
#     with ZipFile(zip_file_loc, "r") as zObject:
#         # Extracting the zip
#         # into a specific location.
#         zObject.extractall(path=cache_dir)
#         zObject.close()


# def cached_files():
#     path = []
#     for files in os.listdir(cache_dir):
#         path.append(os.path.join(cache_dir, files))
#         # path.append(files)

#     return path


if __name__ == "__main__":
    print(cur_work_dir)
    # print(type(cur_work_dir))
    print(cache_dir)
    clean_cache()
    # cache_zip(zip_file_loc, cache_dir)
    # x = cached_files()
    # print(len(x))
