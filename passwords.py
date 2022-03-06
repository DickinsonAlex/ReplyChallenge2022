import glob
import itertools
import os

from typing import List
from concurrent.futures import ProcessPoolExecutor


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
        print(f"[{i + 1}] {file}")

    choice = int(input("Please pick a number: "))

    return file_list[choice - 1]


def get_input_path(folder) -> str:
    """Gives the user a choice of input files, and returns the path of the chosen file

    Args:
        folder ([type]): The folder to check for input files in

    Returns:
        str: The path of the chosen file
    """
    return get_file_choice(get_input_files(folder))


def read_file(filename):
    file = open(filename, "r")
    text = file.read()
    text = text.split("\n")
    file.close()
    return text


def get_input(filename):
    text = read_file(filename)
    number_of_cases = int(text[0])
    text.pop(0)
    cases = []
    last_case = 0
    for _ in range(0, number_of_cases):
        case = []
        temp_case = text[last_case:last_case + 2]
        n_m = temp_case[0].split(" ")
        n = int(n_m[0])
        m = int(n_m[1])
        case.append(n)
        case.append(m)
        case.append(temp_case[1])
        cases.append(case)
        last_case += 2
    return number_of_cases, cases


def write_file(filename, answers):
    file = open(filename + ".txt", "w")
    for answer in range(0, len(answers)):
        string = "Case #" + str(answer + 1) + ": " + str(answers[answer]) + "\n"
        file.write(string)
    file.close()


def solve_test_case(case):
    length_of_password = case[0]
    length_of_specific_number = case[1]
    specific_number = case[2]
    if length_of_specific_number > length_of_password:
        return 2 ** length_of_password
    else:
        all_possible_passwords = []
        for combo in itertools.product(['0', '1'], repeat=length_of_password):
            all_possible_passwords.append(''.join(list(combo)))
        return sum([1 for combo in all_possible_passwords if specific_number not in combo])


def solve_test_cases(cases):
    answers = []
    for case in cases:
        answers.append(solve_test_case(case))
    return answers


def chunk(lst, count):
    size = len(lst)/count
    for i in range(0, count):
        s = slice(round(i*size), None if i == count-1 else round((i+1)*size))
        yield lst[s]


def main():
    try:
        os.remove("output.txt")
    except FileNotFoundError:
        pass
    file = get_input_path("/home/scot/Downloads")
    try:
        no_cases, cases = get_input(file)
        # answers = list(map(solve_test_case, cases))
        cpus = os.cpu_count()
        data_gen = chunk(cases, cpus)
        futures = []
        with ProcessPoolExecutor(cpus) as executor:
            futures.append(executor.submit(solve_test_cases, next(data_gen)))
        answers = [future.result() for future in futures]
        write_file("output", answers)
    except Exception as e:
        os.remove(file)
        raise e
    os.remove(file)


if __name__ == "__main__":
    main()
