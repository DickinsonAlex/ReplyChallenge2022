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

def Pathfinding(Floors, PlayerLevelGoal):
    PlayerLevel = 0
    Path = ""
    Position = [0,0,0]
    while Position[2] != len(Floors): #Clear each floor
        MonsterPositions = []
        for row in range(0, len(Floors[Position[2]])):
            for col in range(0, len(Floors[0])):
                if Floors[0][row][col] == "I":
                    Position = [row, col, Position[2]] #Find start position
                elif Floors[0][row][col] == "O":
                    EndPosition = [row, col, Position[2]] #Find zombie position
                elif Floors[0][row][col] == "M":
                    MonsterPositions.append([row, col, Position[2]]) #Find start position
                
        for monster in MonsterPositions:
            #Make path to each monster + store path while avoiding I or O
            pass

        #Find exit

        Position[2] += 1
        **
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
                    x[col] = Lines[Line + row+1].split(" ")[col]

                Floor.append(x) #Create empty array

            Floors.append(Floor)
            Line += 1 + int(FloorInformation[-1][1])
            if Line > MaxLine:
                MaxLine = Line

        for floor in Floors:
            print(floor)

        Position = [0,0,0]
        Path = ""

        Path += Pathfinding(Floors, PlayerLevelGoal)

        for x in range(0, MaxLine):
            Lines.pop(0)

        print(Path)
        #Answer.append(Path)
        
    WriteFile(OutputFileName,Answers)

if __name__ == '__main__':
    main()

