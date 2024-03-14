import os
import shutil

def create_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)

def check_for_same_name(file_name, file_extension, where_path, n):

    for files in os.listdir(where_path):
        if ( (file_name + file_extension == files and n == 0) or file_name + f'({n})' + file_extension == files ):
            n = check_for_same_name(f'{file_name}', file_extension, where_path, n + 1)
    return n
def download_manager(source_path, target_dir_og):

    os.chdir(source_path)

    for file in os.listdir():
        name, ext = os.path.splitext(file)
        target_dir = ''


        if ext in ['.png', '.jpg', '.hrif','.jpeg','.webp']:
            target_dir = target_dir_og +'images'
        elif ext in ['.zip', '.rar']:
            target_dir = target_dir_og +'compacted files'
        elif ext in ['.exe']:
            target_dir = target_dir_og + 'executables'
        elif ext in ['.txt','.docx','.pdf']:
            target_dir = target_dir_og + 'texts'
                
        #checks if the file needs to be moved
        if target_dir:
            create_folder(target_dir)
            os.chdir(target_dir)
            #n = number of conflicting archives with the same name of the file.
            n = check_for_same_name(name, ext, os.getcwd(), 0)
            if n != 0:
                p = f'{name}({n}){ext}'
                os.rename(os.path.join(source_path, file), os.path.join(os.getcwd(), p))
                file = p
            shutil.move(os.path.join(source_path, file), target_dir)
            os.chdir(source_path)

download_manager("C:/Users/games/Downloads","D:/teste/")