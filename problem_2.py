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
    if suffix == "":
        print("Error, suffix should not be empty")
        return []
    if suffix is None or path is None:
        print("Error, Args should not be None")
        return []
    if os.path.isdir(path):
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
    else:
        print("it is not a valid path")
        return []


# Test 1: Default test
print(find_files(".c", "."))  # print a list of paths with the suffix of ".c"

# Test 2
print(find_files(".test", "."))  # print a list of paths with the suffix of ".h"

# Test 3
print(find_files("", "."))  # print error and an empty list

# Test 4
print(find_files(None, "."))  # print error and an empty list

# Test 5
print(find_files(".c", ""))  # not a valid path
