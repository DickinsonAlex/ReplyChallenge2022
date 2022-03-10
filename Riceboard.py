import math
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


def main():
    InputFileName = "InputFile"
    OutputFileName = "OutputFile"

    Lines = ReadFile(InputFileName)
    Answers = []
    NumberOfTestCases = int(Lines[0])
    Line = 0
    for TestCase in range(0,NumberOfTestCases):
        Line += 1
        Numbers = Lines[Line].split(" ")

        Multiplier = int(Numbers[0])
        WidthHeight = int(Numbers[1])
        BagCapacity = int(Numbers[2])
        CellCount = WidthHeight**2
        RiceCount = 1
    
        for x in range(1,CellCount):
            RiceCount = RiceCount + Multiplier **x
        Remainder = RiceCount % BagCapacity
    
        print(Remainder)
        Answers.append(Remainder)
        
    WriteFile(OutputFileName,Answers)

if __name__ == '__main__':
    main()

