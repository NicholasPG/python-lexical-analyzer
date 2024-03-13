# Replace FILE_NAME  to change file to analyze
FILE_NAME = 'SquareGame.jack'

# creates new file for xml Output
xmlFileName = FILE_NAME.removesuffix(".jack") + "T.xml"
xmlFile = open(xmlFileName, "w")
xmlFile.truncate(0)

# list of reserved words for lookup
Reserved_Words = ["class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static",
                  "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"]
# list of symbols in Jack
Symbols = ["(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"]
# list of digits
Digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# list of comment signifiers
Comments = ["//", "/*", "*/", "/**"]


def analyze_file(fileName):
    # opens File and creates object for it
    file = open(fileName)

    multi_line_comment = False
    string_constant_bool = False
    string_constant = "None"

    # print("<tokens>")
    xmlFile.write("<tokens>\n")
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

            # seperate symbols from words before running lex function
            a = "None"

            if string_constant_bool:
                string_constant += " "

            for x in word:
                if x == "\"":
                    if string_constant_bool:
                        string_constant_bool = False
                        lex(string_constant)
                        string_constant = "None"
                        continue
                    else:
                        string_constant_bool = True;

                        if string_constant == "None":
                            string_constant = x
                        else:
                            string_constant += x
                        continue

                if string_constant_bool:
                    if string_constant == "None":
                        string_constant = x
                        continue

                    string_constant += x
                    continue

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

    # print("</tokens>")
    xmlFile.write("</tokens>\n")
    file.close()


def lex(lexeme):
    # runs through the lexeme to see what kind of token it is
    # (i.e. int literal, reserved word, identifier, etc.)
    # also prints all the stuff to the console probably

    # checks if token is a symbol and prints it
    if lexeme in Symbols:
        if lexeme == "<":
            lexeme = "&lt;"
        elif lexeme == ">":
            lexeme = "&gt;"
        elif lexeme == "&":
            lexeme = "&amp;"
        # print("<symbol> " + lexeme + " </symbol>")
        content = "<symbol> " + lexeme + " </symbol>\n"
        xmlFile.write(content)
        return
    elif lexeme in Reserved_Words:
        # print("<keyword>", lexeme, "</keyword>")
        content = ("<keyword> " + lexeme + " </keyword>\n")
        xmlFile.write(content)
        return
    elif any(lexeme.startswith(d) for d in Digits):
        # print("<integerConstant>", lexeme, "</integerConstant>")
        content = ("<integerConstant> " + lexeme + " </integerConstant>\n")
        xmlFile.write(content)
        return
    elif lexeme.startswith("\""):
        lexeme = lexeme.removeprefix("\"")
        # print("<stringConstant>", lexeme, "</stringConstant>")
        content = ("<stringConstant> " + lexeme + " </stringConstant>\n")
        xmlFile.write(content)
        return
    else:
        # print("<identifier>", lexeme, "</identifier>")
        content = ("<identifier> " + lexeme + " </identifier>\n")
        xmlFile.write(content)


if __name__ == '__main__':
    analyze_file(FILE_NAME)
