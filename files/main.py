__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
from zipfile import ZipFile


def clean_cache():
    if os.path.exists(absolute_path_cache) or os.path.isdir(absolute_path_cache):
        files_in_directory = os.listdir(absolute_path_cache)
        for file in files_in_directory:
            os.remove(os.path.join(absolute_path_cache, file))
    else: os.mkdir(absolute_path_cache)


def cache_zip(zip_file, place_of_storage):
    zip_dir = os.path.join(pwd_files, zip_file )
    storage_dir = os.path.join(pwd_files, place_of_storage )
    with ZipFile(zip_dir, 'r') as zipObj: # 'r' -> mode='read'
        zipObj.extractall(storage_dir)

  
def cached_files():
    cached_files_list = []
    files_in_directory = os.listdir(absolute_path_cache)
    for file in files_in_directory:
        cached_files_list.append(os.path.join(absolute_path_cache, file))
        
    return cached_files_list


def find_password(cached_files_list):
    for file_path in cached_files_list:
        file_content = open(file_path).read()
        if 'password' in file_content:
            password_in =  file_content
            break

    return password_in[password_in.find('c'):password_in.find('le')+2]
 

pwd_files = os.path.abspath('files')                    # pwd -> path working directory used in 'clean_cache()' and 'cach_zip()'
absolute_path_cache = os.path.join(pwd_files, 'cache')  # used in 'cached_files()' and' clean_cache()'

if __name__ == '__main__':
    clean_cache()
    cache_zip('data.zip', 'cache')
    cached_files()
    find_password(cached_files())