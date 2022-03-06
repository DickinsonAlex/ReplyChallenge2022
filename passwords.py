def read_file(filename):
    file = open(filename + ".txt", "r")
    text = file.read()
    text = text.split("\n")
    file.close()
    return text


def write_file(filename, answers):
    file = open(filename + ".txt", "w")
    for answer in range(0, len(answers)):
        string = "Case #" + str(answer + 1) + ": " + str(answers[answer]) + "\n"
        file.write(string)
    file.close()
