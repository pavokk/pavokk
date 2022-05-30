import os
import shutil


def translate(text, conversion_dict):
    """
    Translate words from a text using a conversion dictionary

    Arguments:
        text: the text to be translated
        conversion_dict: the conversion dictionary
    """
    # if empty:
    if not text:
        return text
    # preliminary transformation:
    t = text
    for key, value in conversion_dict.items():
        t = t.replace(key, value)
    return t


def rename_files(path, name_map):
    increment = 1
    print('Start.')
    print(increment)
    for file in path:
        tmp = []
        for char in file:
            if char in name_map.keys():
                tmp.append(name_map[char])
            else:
                tmp.append(char)
        new_file_name = ''.join(tmp)
        os.rename(path + file, new_file_name)
        increment += 1
    print('Done.')


def list_unique_characters(og_list):
    """
    Return a list of unique characters from a list of strings

    Argument:
        The list to be sampled
    """
    listed_characters = ['']

    for text in og_list:
        for char in text:
            if char not in listed_characters:
                listed_characters.append(char)
    return listed_characters


def list_illegal_files(directory):

    files = []

    for filename in os.listdir(directory):
        legal = 1
        for char in filename:
            if char == 'Ã':
                legal = 0
        if legal == 0:
            files.append(filename)

    return files


def split_directory(directory, split_amount):
    '''
    Splits all files in a directory into several sub directories

    :param directory: Directory where files are located.
    :param split_amount: How many files for each sub directory.
    '''


    files = [os.path.join(directory, f) for f in os.listdir(directory)]

    i = 0
    curr_subdir = None
    files.sort()

    for f in files:
        if i % split_amount == 0:
            subdir_name = os.path.join(directory, '{0:03d}'.format(i // split_amount + 1))
            os.mkdir(subdir_name)
            curr_subdir = subdir_name

        # move file to current dir
        f_base = os.path.basename(f)
        shutil.move(f, os.path.join(subdir_name, f_base))
        i += 1