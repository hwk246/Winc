__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
from zipfile import ZipFile

# create cache folder in case not existing. deletes content of cache folder in case existing
def clean_cache():
    if os.path.exists(absolute_path_cache) or os.path.isdir(absolute_path_cache):
        files_in_directory = os.listdir(absolute_path_cache)
        for file in files_in_directory:
            os.remove(os.path.join(absolute_path_cache, file))
    else: os.mkdir(absolute_path_cache)

# extracts zip folder in cache directory
def cache_zip(zip_dir, storage_dir):
    
    with ZipFile(zip_dir, 'r') as zipObj: # 'r' -> mode='read'
        zipObj.extractall(storage_dir)

# creates list of files in cache folder as absolute path
def cached_files():
    cached_files_list = []
    files_in_directory = os.listdir(absolute_path_cache)
    for file in files_in_directory:
        cached_files_list.append(os.path.join(absolute_path_cache, file))
        
    return cached_files_list

# finds 'password' in zip folder files content
def find_password(cached_files_list):
    for file_path in cached_files_list:
        file_content = open(file_path).readlines()
        for line in file_content:
            if line.find('password') == 0:
                return (line[line.find(' ')+1: line.find('\n')])
               

pwd_files = os.path.abspath('files') # pwd -> path working directory used in 'clean_cache()' and 'cach_zip()'
absolute_path_cache = os.path.join(pwd_files, 'cache')  # used in 'cached_files()' and' clean_cache()'
absolute_path_zip = os.path.join(pwd_files, 'data.zip' ) # used in 

if __name__ == '__main__':
    clean_cache()
    cache_zip(absolute_path_zip, absolute_path_cache)
    cached_files()
    print(find_password(cached_files()))