# Replace FILE_NAME  to change file to analyze
FILE_NAME = 'test.txt'

Reserved_Words = ["class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static",
                  "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"]
Symbols = ["(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"]

Comments = ["//", "/*", "*/", "/**"]

def analyze_file(fileName):
    # Main body of code that opens the file, splits it into individual lexemes, then runs lex() on them
    # opens File and creates object for it
    file = open(fileName)

    # loop that reads through the file one line at a time
    for line in file:
        # code that runs on each line like separating it by spaces

        words = line.split()
        for word in words:
            if ";" in word:
                print("bruh")
            lex(word)


    file.close()


def lex(lexeme):
    # runs through the lexeme to see what kind of token it is
    # (i.e. int literal, reserved word, identifier, etc.)
    # also prints all the stuff to the console probably
    print(lexeme)


def lookup(string):
    # run the lookup code that checks for reserved words
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    analyze_file(FILE_NAME)
