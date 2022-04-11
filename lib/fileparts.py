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

from .computer import computer
import os
def path2mount_tail(fullpath):
	# changed it from abspath to resolve symbolic links	
	fullpath = os.path.realpath(fullpath)
	
	os_type = computer('os').lower();
	if(os_type=='windows'):
		return os.path.splitdrive(fullpath)
	elif(os_type=='linux'):
		# https://stackoverflow.com/a/4453715
		def find_mount_point(p):
			while not os.path.ismount(p):
				# dirname remove 1 token/level from the end at a time				
				p = os.path.dirname(p)
			return p				
		mnt = find_mount_point(fullpath);
		tail = fullpath[len(mnt):]
		return (mnt, tail)
	else:
		raise f"Unexpected OS {os_type}"

	
def fileparts(fullpath):
    (folder, tail) = path2folder_tail(fullpath);
    (file_bare, extension) = path2head_ext(tail)
    return (folder, file_bare, extension)