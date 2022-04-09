# Python does not adapt varargout like MATLAB
# Not without complex debug stack manueveurs
# https://code.activestate.com/recipes/284742-finding-out-the-number-of-values-the-caller-is-exp/
# So the output is a list and you can 'deal' it to multiple variable with output list syntax
# like (pathname, filename) = fileparts(fullpath_name)
# If you just want the path, use 
# 1) extract_folder(), aka os.path.dirname()
# 2) fileparts(fullpath_name)[0]
# 3) pathname, _ = fileparts(fullpath_name)
from os.path import split    as path2folder_tail # break_path_into_folder_and_the_rest
from os.path import splitext as path2head_ext # break_path_into_the_rest_then_extension
def fileparts(fullpath):
    (folder, tail) = path2folder_tail(fullpath);
    (file_bare, extension) = path2head_ext(tail)
    return (folder, file_bare, extension)