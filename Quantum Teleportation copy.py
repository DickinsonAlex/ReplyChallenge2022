from typing import List

def readFile(file: str) -> List[str]:
    """Reads file - takes string in and claims to return list of string

    Args:
        file (str): The name of the file

    Returns:
        List[str]: List of the lines in the file
    """

    with open(file, 'r') as file: #uses with as removes need for manual file close
        lines = file.readlines()
        
    return [line.strip() for line in lines]

def writeFile(name: str, data: List):
    """Writes to given file

    Args:
        path (str): The file name
        data (List): The data to be put on the file as a list
    """

    with open(name, 'w') as file:
        file.write("\n".join([str(record) for record in data])) #adds new line to each data row to display an so of lines

def buildMatrix(size: str, start: str):
    """Builds matrix from size and start posiotion

    Args:
        size (str): String containing the size of the matrix (x y)
        start (str): String indication particle start

    Returns:
        Array[str]: Matrix size (x y) filled 0
    """

    grid = []
    grid_cols = size[:1]
    grid_rows = size[2:]

    for _r in range(0, int(grid_rows)):
        grid.append([0 for _c in range(0, int(grid_cols))])

    grid[int(start[2:])][int(start[:1])] = "start"

    return grid

def fillMatrix(data: str, matrix):
    """Adds portals to grid - inX and outX

    Args:
        data (str): List containing all testcases
        matrix (_type_): The matrix being operated on

    Returns:
        matrix: The matrix now with portals - inX and outX
    """

    for i in range(0, int(data.pop(0))): #loops from 0 to no of portals
        portal_pos = data.pop(0)
        matrix[int(portal_pos[2:3])][int(portal_pos[:1])] = f"in{i}"
        matrix[int(portal_pos[6:])][int(portal_pos[4:5])] = f"out{i}"

    return matrix

def main():
    data = readFile("data.txt") #Replace with file location
    output = []

    for i in range(0, int(data.pop(0))):
        grid_size = data.pop(0)
        start_pos = data.pop(0)
        grid = buildMatrix(grid_size, start_pos)
        grid = fillMatrix(data, grid)

    print('\n'.join(' '.join(str(x) for x in row) for row in grid))
    writeFile("output.txt", grid)

if __name__ == "__main__":
    main()
