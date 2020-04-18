import os


def load(name):
    """
    This method loads a new journal

    :param name: This is the base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    file_name = get_full_path(name)
    if os.path.exists(file_name):
        with open(file_name, "r") as fin:
            for line in fin.readlines():
                data.append(line.rstrip())
    return data


def save(name, journal_data):
    """
    This method creates and saves journal data
    :param name: This is the base name of the journal to save.
    :param journal_data: This is the data structure with journal data
    """
    file_name = get_full_path(name)
    print("...... saving to: {}".format(file_name))

    with open(file_name, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_path(name):
    """
    Private method
    :param name: The name to use to read and save the journal
    :return: The absolute path to the journal file
    """
    file_name = os.path.abspath(os.path.join("./journals/", name + ".jrl"))
    return file_name


def add_entry(text, journal_data):
    """
    Adds the journal entry to the data structure
    :param text: The text of the journal entry
    :param journal_data: The data structure used to store the journal entry
    """
    if text:
        journal_data.append(text)
    return
