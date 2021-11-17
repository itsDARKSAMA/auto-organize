## https://github.com/itsDARKSAMA
import os
from posixpath import split
import shutil

# To Do : improve file Extensions and categories

# a.almajayda : current directory path , if you want to get it by user -
# - just comment this line and uncomment the next one.
current_dir = os.getcwd()
# current_dir = input('Enter The Path : ')
current_file = os.path.realpath(__file__)
result_num = 0

# a.almajayda : file Extensions
images_ex = ['jpg', 'png', 'svg', 'jpeg', 'gif', 'tif',
             'tiff', 'bmp', 'raw', 'cr2', 'nef', 'orf', 'sr2', 'svgs']

videos_ex = ['mp4', 'mkv', 'avi', 'm4v', 'wmv',
             'mov', 'flv', 'avchd', 'webm', '3gp']

audios_ex = ['mp3', 'm4a', 'flac', 'wav', 'wma',
             'acc', 'flv', 'avchd', 'webm', 'opus', 'ogg']

code_ex = ['java', 'class', 'html', 'css', 'py', 'js', 'rb', 'c',
           'cs', 'cpp', 'sh', 'asp', 'aspx', 'pl', 'lua', 'php', 'dart', 'json', 'm']

compressed_ex = ['zip', 'rar', 'tar', '7z', 'iso', 'gz', 'z',
                 'tgz', 'bz2', 'tbz2', 'xz', 'zst', 'txz', 'tlz', 'lz']

design_ex = ['psd', 'xd', 'ai', 'xcf', 'ae', 'pr', 'c4d',
             'psb', 'eps', 'indd', 'u3d', 'dwg', 'dwt', 'dxf', 'dwf', 'dst', 'cdr']

docs_ex = ['pdf', 'epub', 'ppt', 'pptx', 'doc', 'odt', 'txt', 'wps',
           'xps', 'rtf', 'docm', 'docx', 'dot', 'dotm', 'dotx', 'csv', 'dbf', 'ods',
           'prn', 'slk', 'xla', 'xlam', 'xls', 'xlsb', 'xlsm', 'xlsx', 'xlt',
           'xltm', 'xltx', 'xltw', 'odp', 'pot','odg']

# a.almajayda : get the directory name
def dir_names(fileExtension):
    if fileExtension in images_ex:
        return 'Images'
    elif fileExtension in audios_ex:
        return 'Audios'
    elif fileExtension in videos_ex:
        return 'Videos'
    elif fileExtension in code_ex:
        return 'Codes'
    elif fileExtension in compressed_ex:
        return 'Arcives'
    elif fileExtension in design_ex:
        return 'Design'
    elif fileExtension in docs_ex:
        return 'Documents'
    else:
        return 'Other'

# a.almajayda : Organizing files by directory names
def organize():
    global result_num
    for fileName in os.listdir(current_dir):
        # a.almajayda : Spliting file name to get the file extension
        fileNamesList = fileName.split('.')
        fileExtension = fileNamesList[-1]
        # a.almajayda : Get directory name By executing the function
        dirName = dir_names(fileExtension.lower())
        # a.almajayda : Check if directory exists or not
        if not os.path.exists(dirName):
            os.mkdir(dirName)

        # a.almajayda : Check if this Extension is a directory and is not current python file code
        if os.path.isfile(fileName) and fileName != __file__.split('/')[-1]:
            try:
                # a.almajayda : copy file and delete the old copy
                shutil.copy(fileName, dirName)
                os.remove(fileName)
                result_num = result_num + 1

            # a.almajayda : handling exceptions
            except shutil.SameFileError:
                print(fileName, "| Source and destination represents the same file.")

            # a.almajayda : If there is any permission issue
            except PermissionError:
                print(fileName, "| Permission denied.")

            # a.almajayda : For other errors
            except:
                print(fileName, "| Error occurred while copying file.")

print('[!] Start orgnazing , Please Don\'t close this window')
organize()
print('[!] Done !!! ,', result_num, 'files has been moved')
