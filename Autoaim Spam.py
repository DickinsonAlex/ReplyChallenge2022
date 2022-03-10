from typing import List
import pprint

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

def build_matrix(cols, rows):
    grid = []
    
    for _r in range(0, int(rows)):
        grid.append(["null" for _c in range(0, int(cols))])

    return grid

def fill_matrix(filler, grid):
    for e in filler:
        grid[e.posX][e.posY] = int(e.id)
    return grid

def advance_enemies(enemies, grid):
    rows = len(grid)
    cols = len(grid[0])
    
    for _r in range(0, int(rows)):
        grid.append(["null" for _c in range(0, int(cols))])
    
    for e in enemies:
        e.posX -= 1

    return(fill_matrix(enemies, grid))

class enemy():
    def __init__(self, enemy_id, enemy_hp, x, y) -> None:
        self.id = enemy_id
        self.hp = enemy_hp
        self.posX = x
        self.posY = y
        self.pos = ((x,y))

def main():
    data = read_file("data.txt") #Replace with file location
    output = []
    
    for i in range(0, int(data.pop(0))):
        board_properties = data.pop(0).split(" ")
        board_grid = build_matrix(board_properties[1], board_properties[0])
        enemy_num = int(board_properties[2])
        ammo_cap = int(board_properties[3])
        ammo_dmg = int(board_properties[4])
        ammo_dropoff = int(board_properties[5])
        shots = 0
        turns = 0
        enemy_distances = []
        enemies = []
        
        for e in range(0, enemy_num):
            temp = data.pop(0).split(" ")
            temp_enemy = enemy(int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]))
            enemies.append(temp_enemy)
        
        board_grid = fill_matrix(enemies, board_grid)
        
        while enemy_num > 0:
            turns += 1
            
            #each turn
            for shot in range(0, ammo_cap):
                shotTaken = False
                for e in enemies:
                    enemy_distances.append(e.posX)
                closest = min(enemy_distances)
                for e in enemies:
                    if e.posX == closest and shotTaken == False:
                        shots += 1
                        shotTaken = True
                        e.hp = e.hp - (ammo_dmg - ammo_dropoff * e.posX)
                        if e.hp <= 0:
                            enemies.remove(e)
                            enemy_num -= 1
            advance_enemies(enemies, board_grid)
    
    print(shots, turns)
    #write_file("result.txt", shots)

if __name__ == "__main__":
    main()