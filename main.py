# Replace FILE_NAME  to change file to analyze
FILE_NAME = 'test.txt'
# list of reserved words for lookup
Reserved_Words = ["class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static",
                  "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"]
# list of symbols in Jack
Symbols = ["(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"]

Comments = ["//", "/*", "*/", "/**"]


def analyze_file(fileName):
    # opens File and creates object for it
    file = open(fileName)

    multi_line_comment = False

    # loop that reads through the file one line at a time
    for line in file:
        single_line_comment = False
        # splits the line into individual words divided by spaces
        words = line.split()
        # loop that goes through each of the separated words
        for word in words:
            # sets bool variables that allow for skipping of comments
            if "//" in word:
                single_line_comment = True
            if "/*" in word:
                multi_line_comment = True
            if "*/" in word:
                multi_line_comment = False
                continue

            # skips words that are part of comments
            if single_line_comment:
                continue
            if multi_line_comment:
                continue

            #seperate symbols from words before running lex function
            a = "None"
            for x in word:
                if x in Symbols:
                    if a != "None":
                        lex(a)
                        a = "None"
                    lex(x)
                    continue

                if a == "None":
                    a = x
                    continue

                a += x

            if a != "None":
                lex(a)

    file.close()


def lex(lexeme):
    # runs through the lexeme to see what kind of token it is
    # (i.e. int literal, reserved word, identifier, etc.)
    # also prints all the stuff to the console probably

    print(lexeme)
    # loops through each character of the word
    a = 0
    for x in lexeme:
        a+= 1



# returns 1 if reserved word, 0 if identifier
def lookup(string):
    # run the lookup code that checks for reserved words
    if string in Reserved_Words:
        return 1
    else:
        return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    analyze_file(FILE_NAME)
