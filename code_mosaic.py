from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Token, string_to_tokentype
import os
import color_generator as cg
import image_generator as ig

class CodeMosaic:
    def __init__(self, height=500, width=1000, font_size=20, spacing=15, location="") -> None:
        # Store the absolute path of the code file
        self.location = os.path.abspath(location)

        # Determine the file extension to identify the programming language
        self.code_extension = self.detect_language()

        # Get the lexer alias for the identified programming language
        alias = self.code_ext_resolver()
        self.lexer = get_lexer_by_name(alias)

        # Tokenize the code using the identified lexer
        self.tokens = self.get_token()

        # Assign unique colors to each token
        self.token_color = self.color_codes()

        # Prepare line_color for image generation
        line_color = []
        for line in self.tokens:
            arr = []
            for token, val in line:
                arr.append((val, self.token_color[token]))
            line_color.append(arr)

        # Generate the image frames
        ig.build_frames(height=height, width=width, line_color=line_color, location=self.location,
                        output_path="Code_Mosaic_Output.png", font_size=font_size, spacing=spacing)

    def color_codes(self):
        # Assign unique colors to each token
        token_color = {}
        for tokens in self.tokens:
            for token, _ in tokens:
                token_color[token] = cg.vibrant_color(token)
        return token_color

    def get_token(self):
        # Read the code from the specified file
        file = open(self.location, "r")
        lines = file.readlines()
        tokens = []
        for line in lines:
            token = list(lex(line, self.lexer))
            if token[-1][1] == "\n":
                tokens.append(token[:-1] + [(token[-1][0], " ")])
            elif token[-1][1][-1:] == "\n":
                tokens.append(token[:-1] + [(token[-1][0], token[-1][1][:-1])])
            else:
                tokens.append(token)
        return tokens

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
# CM = CodeMosaic(location=r"D:\Codes\Projects\Code Mosaic\test\test.py")
