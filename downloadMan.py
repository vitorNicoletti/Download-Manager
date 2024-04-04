import os
import shutil
DOWNLOAD_FOLDER = "D:/teste/"
DOWNLOAD_SORCE = "C:/Users/games/Downloads"
#List of extension types:
extList =[
    [
    "documents",
    ".doc",
    ".docx",
    ".odt",
    ".pdf",
    ".rtf",
    ".txt",
    ".wpd",
    ".xls",
    ".xlsx",
    ".xml",
    ".ppt",
    ".pptx",
    ".pps",
    ".ppsx",
    ".odp",
    ".csv",
    ".py",
    ".pyc",
    ".pyo",
    ".pyw",
    ".c",
    ".cc",
    ".cxx",
    ".h",
    ".hh",
    ".hpp",
    ".hxx",
    ".m",
    ".mm",
    ".pl",
    ".pm",
    ".pyc",
    ".pyo",
    ".rst",
    ".xhtml",
    ".yml",
    ".epub",
    ],
    ["audios",".mp3", ".wav", ".wma", ".aac", ".flac", ".ogg"],
    ["images"," .bmp", ".gif", ".jpg", ".jpeg", ".png", ".psd", ".tiff"],
    ["videos",".avi", ".flv", ".mov", ".mp4", ".mpg", ".rm", ".swf", ".wmv"],
    [
        "files",
        ".7z",
        ".arj",
        ".bz2",
        ".cab",
        ".gz",
        ".rar",
        ".tar",
        ".tgz",
        ".zip",
        ".deb",
        ".iso",
        ".exe",
        ".rpm",
        ".msi",
        ".AppImage",
        ".flatpakref",
    ],
    ["vpn",".ovpn"],
    ["fonts"," .ttf", ".otf", ".woff", ".woff2"]

]


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
        print(file)
        name, ext = os.path.splitext(file)
        target_dir = target_dir_og +'others'

        for extType in extList:
            if ext in extType:
                target_dir = target_dir_og + extType[0]
                break
        """
        if ext in images:
            target_dir = target_dir_og +'images'
        elif ext in files:
            target_dir = target_dir_og +'files'
        elif ext in ['.exe']:
            target_dir = target_dir_og + 'executables'
        elif ext in docs:
            target_dir = target_dir_og + 'texts'
        elif ext in video:
            target_dir = target_dir_og + 'videos'
        elif ext in audio:
            target_dir = target_dir_og + 'audios'
        else: 
            target_dir = target_dir_og + 'others'
        """
        #checks if the file needs to be moved
        if target_dir:
            create_folder(target_dir)
            os.chdir(target_dir)
            #n = number of conflicting archives with the same name of the file.
            n = check_for_same_name(name, ext, os.getcwd(), 0)
            os.chdir(source_path)
            try:
                if n != 0:
                    p = f'{name}({n}){ext}'
                    print(os.getcwd())
                    os.rename(os.path.join(source_path, file), os.path.join(os.getcwd(), p))
                    file = p
                
                shutil.move(os.path.join(source_path, file), target_dir)
                os.chdir(source_path)
            except:
                print(f"The file {file} could not be moved to {target_dir} or renamed.\n Try closing the file and run me again!")
