import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    file_list = os.listdir(path)
    result_list = list()
    for file_name in file_list:
        new_file_name = os.path.join(path, file_name)
        if os.path.isfile(new_file_name):
            if new_file_name.endswith(suffix):
                result_list.append(new_file_name)
        else:
            sub_result_list = find_files(suffix, new_file_name)
            result_list += sub_result_list

    return result_list


print(find_files(".c", "."))
