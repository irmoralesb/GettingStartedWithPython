import os
import subprocess
import platform

import cat_service


def main():
    print("hello from main")
    folder = get_or_create_output_folder()
    print("Found or created folder: " + folder)
    download_cats(folder)
    display_cats(folder)


def print_header():
    print("--------------------------------")
    print("        CAT FACTORY")
    print("--------------------------------")


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = "lolcat{}".format(i)
        cat_service.get_cat(folder, name)


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = "cat_pictures"
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creating new directory at {}".format(full_path))
        os.mkdir(full_path)
    return full_path


def display_cats(folder):
    print("Displaying cats.")
    current_system = platform.system()
    if current_system == "Dwarwin":
        subprocess.call(["open", folder])
    elif current_system == "Windows":
        subprocess.call(["explorer", folder])
    elif current_system == "Linux":
        subprocess.call(["xdg-open", folder])
    else:
        print("We don't support your operating system")


if __name__ == "__main__":
    main()
