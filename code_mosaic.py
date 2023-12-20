from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Token, string_to_tokentype
import os

class CodeMosaic:
    def __init__(self, location = "") -> None:
        self.location = os.path.abspath(location)
        self.code_extension = self.detect_language()
        alias = self.code_ext_resolver()
        self.lexer = get_lexer_by_name(alias, stripall = True)
        self.code = self.get_code()
        self.tokens = list(lex(self.code, self.lexer))
        # print(self.tokens)
        temp = {}
        for token, val in self.tokens:
            try:
                temp[token].append(val)
            except:
                temp[token] = [val]
        for key, val in temp.items():
            print(f"{key}:{val}")
    
    def get_code(self):
        file = open(self.location, "r")
        code = file.read()
        return code
    
    def detect_language(self):
        # detects the programming language of the file from its  
        code_extension = self.location.split(".")[-1]
        return code_extension
    
    def code_ext_resolver(self):
        with open('extension.txt', "r") as extension_file:
            ext, alias = extension_file.readline().rstrip("\n").split(",")
            if ext == self.code_extension:
                return alias


        


CM = CodeMosaic(location="D:\Codes\Projects\Code Mosaic\code_mosaic.py")

