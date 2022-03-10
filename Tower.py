import math
global Position

def ReadFile(FileName):
    File = open(FileName + ".txt","r")
    Text = File.read()
    Text = Text.split("\n")
    File.close()
    return Text

def WriteFile(FileName,Answers):
    file=open(FileName + ".txt","w")
    for answer in range(0,len(Answers)):
        String = "Case #"+str(answer+1)+": "+str(Answers[answer]) + "\n"
        file.write(String)
    file.close()

def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def LevelUp(Floors, PlayerLevelGoal):
    PlayerLevel = 0
    Path = ""
    for row in range(0, len(Floors[0])):
        for col in range(0, len(Floors[0])):
            if Floors[0][row][col] == "I":
                Position = [row, col]
                print(Position)

    while PlayerLevel != PlayerLevelGoal:


    return Path

def GetOut(Floors):
    Path = ""
    return Path

def main():
    InputFileName = "InputFile"
    OutputFileName = "OutputFile"

    Lines = ReadFile(InputFileName)
    Answers = []
    NumberOfTestCases = int(Lines[0])
    Lines.pop(0)

    for TestCase in range(0,NumberOfTestCases):
        #Get testcase layout information
        TowerInformation = Lines[0].split()
        NumberOfFloors = int(TowerInformation[0])
        PlayerLevelGoal = int(TowerInformation[1])
        MaxSteps = TowerInformation[2]
        FloorInformation = []
        Floors = []
        Line = 1
        MaxLine = 0

        #Store floor information
        for x in range(0, NumberOfFloors):
            FloorInformation.append(Lines[Line].split())
            Floor = []
            Size = int(FloorInformation[-1][1])
            for row in range(0, Size):
                x = [0 for Col in range(0, Size)]
                for col in range(0, Size-1):
                    x[col] = Lines[Line + row].split(" ")[col]

                Floor.append(x) #Create empty array

            Floors.append(Floor)
            Line += 1 + int(FloorInformation[-1][1])
            if Line > MaxLine:
                MaxLine = Line

        for floor in Floors:
            print(floor)

        Position = [0,0]
        Path = ""

        Path += LevelUp(Floors, PlayerLevelGoal)
        Path += GetOut(Floors)

        for x in range(0, MaxLine):
            Lines.pop(0)

        print(Path)
        #Answer.append(Path)
        
    WriteFile(OutputFileName,Answers)

if __name__ == '__main__':
    main()

