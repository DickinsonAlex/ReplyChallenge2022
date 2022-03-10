import math
import copy
import random

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
    EndPosition = [0,0,0]
    while Position[2] != len(Floors): #While not at the end
        MonsterPositions = []
        for row in range(0, len(Floors[Position[2]])):
            for col in range(0, len(Floors[Position[2]])):
                if Floors[Position[2]][row][col] == "I":
                    StartPosition = [row, col, Position[2]] #Find start position
                    Position = StartPosition
                elif Floors[Position[2]][row][col] == "O":
                    EndPosition = [row, col, Position[2]] #Find zombie position
                elif Floors[Position[2]][row][col] == "M":
                    MonsterPositions.append([row, col, Position[2]]) #Find start position
                
        for monster in MonsterPositions:
            #Add path to each monster
            while Position != monster:
                temp = copy.deepcopy(Position)
                if monster[0] < Position[0]:
                    temp[0] -= 1
                    if temp != StartPosition and temp != EndPosition:
                        Path += "U"
                        Position[0] -= 1
                elif monster[0] > Position[0]:
                    temp[0] += 1
                    if temp != StartPosition and temp != EndPosition:
                        Path += "D"
                        Position[0] += 1
                
                temp = copy.deepcopy(Position)
                if monster[1] > Position[1]:
                    temp[1] += 1
                    if temp != StartPosition and temp != EndPosition:
                        Path += "R"
                        Position[1] += 1
                elif monster[1] < Position[1]:
                    temp[1] -= 1
                    if temp != StartPosition and temp != EndPosition:
                        Path += "L"
                        Position[1] -= 1


        #Get the path to O
        while Position != EndPosition:
            temp = copy.deepcopy(Position)
            if EndPosition[0] < Position[0]:
                temp[0] -= 1
                if temp != StartPosition:
                    Path += "U"
                    Position[0] -= 1
            elif EndPosition[0] > Position[0]:
                temp[0] += 1
                if temp != StartPosition:
                    Path += "D"
                    Position[0] += 1
            temp = copy.deepcopy(Position)
            if EndPosition[1] > Position[1]:
                temp[1] += 1
                if temp != StartPosition:
                    Path += "R"
                    Position[1] += 1
            elif EndPosition[1] < Position[1]:
                temp[1] -= 1
                if temp != StartPosition:
                    Path += "L"
                    Position[1] -= 1
            
        
        print(Path + str(Position[2]))

        Position[2] += 1
        
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
                for col in range(0, Size):
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
        Answers.append(Path)
        
    WriteFile(OutputFileName,Answers)

if __name__ == '__main__':
    main()

