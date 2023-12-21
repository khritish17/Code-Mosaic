from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Token, string_to_tokentype
import os
import color_generator as cg

class CodeMosaic:
    def __init__(self, location="") -> None:
        # Store the absolute path of the code file
        self.location = os.path.abspath(location)

        # Determine the file extension to identify the programming language
        self.code_extension = self.detect_language()

        # Get the lexer alias for the identified programming language
        alias = self.code_ext_resolver()
        self.lexer = get_lexer_by_name(alias, stripall=True)

        # Read the code from the file into memory
        self.code = self.get_code()

        # Tokenize the code using the identified lexer
        self.tokens = list(lex(self.code, self.lexer))

        # Assign unique colors to each token
        self.token_color = self.color_codes()
        

    def color_codes(self):
        # Assign unique colors to each token
        token_color = {}
        visited_color = []
        for token, _ in self.tokens:
            try:
                _ = token_color[token]
            except KeyError:
                # Generate a vibrant color and ensure it is unique
                color = cg.generate_vibrant_color()
                while color in visited_color:
                    color = cg.generate_vibrant_color()
                token_color[token] = color
                visited_color.append(color)
        return token_color

    def get_code(self):
        # Read the code from the specified file
        file = open(self.location, "r")
        code = file.read()
        return code

    def detect_language(self):
        # Determine the programming language of the file from its extension
        code_extension = self.location.split(".")[-1]
        return code_extension

    def code_ext_resolver(self):
        # Resolve the lexer alias based on file extension
        file = open("extension.txt", "r")
        lines = file.readlines()
        for line in lines:
            ext, alias = line.rstrip('\n').split(',')
            if ext == self.code_extension:
                return alias
        file.close()

# Example usage
CM = CodeMosaic(location=r"D:\Codes\Projects\Code Mosaic\test.c")


