from typing import List

def read_file(file: str) -> List[str]:
    """Reads file - takes string in and claims to return list of string

    Args:
        file (str): The name of the file

    Returns:
        List[str]: List of the lines in the file
    """
    with open(file, 'r') as file: #uses with as removes need for manual file close
        lines = file.readlines()
        
    return [line.strip() for line in lines]

def write_file(name: str, data: List):
    """Writes to given file

    Args:
        path (str): The file name
        data (List): The data to be put on the file as a list
    """

    with open(name, 'w') as file:
        file.write("\n".join([str(record) for record in data])) #adds new line to each data row to display an so of lines

def main():
    data = read_file("{data.txt}") #Replace with file location
    output = []
    
    for i in range(0, int(data.pop(0))):
        #Code here
        pass
    
    write_file("{result.txt}", output)

if __name__ == "__main__":
    main()
