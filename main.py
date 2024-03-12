# Replace File Name in Main to change file to analyze


def analyze_file(fileName):
    # Main body of code that opens the file, splits it into individual lexemes, then runs lex() on them
    # opens File and creates object for it
    file = open(fileName)

    # reads line (once a line is read, you have to specify the line to get it back)
    line = file.readline()

    print(line)  # Press Ctrl+F8 to toggle the breakpoint.

    # loop that reads through the file one line at a time
    for line in file:
        # code that runs on each line like separating it by spaces

        # loop goes by one character at a time
        for x in line:
            
            print(x)

    file.close()


def lex(lexeme):
    # runs through the lexeme to see what kind of token it is
    # (i.e. int literal, reserved word, identifier, etc.)
    # also prints all the stuff to the console probably
    print()


def lookup(string):
    # run the lookup code that checks for reserved words
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    FILE_NAME = 'SquareGame.jack'

    analyze_file(FILE_NAME)
