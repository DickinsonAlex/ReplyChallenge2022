from typing import List, Set
import glob
from functools import reduce
from math import sqrt


def get_file(path: str) -> List[str]:
    """Reads and returns the lines from the given path

    Args:
        path (str): The location of the file

    Returns:
        List[str]: The lines of the file
    """
    with open(path, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def write_file(path: str, data: List):
    """Writes a list of lines to a file

    Args:
        path (str): The location of the file
        data (List): The lines to write
    """
    with open(path, "w") as file:
        file.write("\n".join([str(x) for x in data]))


def get_input_files(folder: str) -> List[str]:
    """Returns a list of input files in the given folder

    Args:
        folder (str): The name of the folder

    Returns:
        List[str]: List of found folder paths
    """
    return glob.glob(f"{folder}/*.txt")


def get_file_choice(file_list: List[str]) -> str:
    """Displays a given list of paths, and returns the path of the chosen file

    Args:
        file_list (List[str]): The list of files to give the user

    Returns:
        str: The path of the chosen file
    """
    for i, file in enumerate(file_list):
        print(f"[{i+1}] {file}")

    choice = int(input("Please pick a number: "))

    return file_list[choice-1]


def get_input_path(folder) -> str:
    """Gives the user a choice of input files, and returns the path of the chosen file

    Args:
        folder ([type]): The folder to check for input files in

    Returns:
        str: The path of the chosen file
    """
    return get_file_choice(get_input_files(folder))


def get_factors(n: int) -> Set[int]:
    """Gets all the factors of the given number

    Args:
        n (int): The number to get the factors of

    Returns:
        Set[int]: The factors found
    """
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))
