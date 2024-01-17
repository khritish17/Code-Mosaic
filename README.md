# Code Mosaic Documentation
### Overview
The Code Mosaic module is purpose-built to generate visual representations of source code files, presented as images for convenient sharing on social media platforms. It utilizes the Pygments library for syntax highlighting and color generation, producing vibrant and visually appealing images that reflect the source code.

## File: code_mosaic.py | Class: CodeMosaic
### Constructor
```
def __init__(self, height=500, width=1000, font_size=20, spacing=15, location="") -> None:
    """
    Initialize a CodeMosaic instance.

    Parameters:
    - height (int): Height of the generated image.
    - width (int): Width of the generated image.
    - font_size (int): Font size for text rendering in the image.
    - spacing (int): Spacing between lines in the image.
    - location (str): Absolute path of the code file.

    Example Usage:
    >>> CM = CodeMosaic(location=r"D:\Codes\Projects\Code Mosaic\test\test.py")
    """
```
## Methods
### color_codes()
```
def color_codes(self):
    """
    Assign unique colors to each token in the code.

    Returns:
    dict: A dictionary mapping tokens to their assigned colors.
    """
```
### get_token()
```
def get_token(self):
    """
    Tokenize the code using the identified lexer.

    Returns:
    list: A list of lists, where each inner list represents a line and contains tuples of (token, value).
    """
```
### detect_language()
```
def detect_language(self):
    """
    Determine the programming language of the file from its extension.

    Returns:
    str: The file extension representing the programming language.
    """
```
### code_ext_resolver()
```
def code_ext_resolver(self):
    """
    Resolve the lexer alias based on file extension.

    Returns:
    str: The lexer alias for the identified programming language.
    """
```
Example Usage
```
# Example usage
CM = CodeMosaic(location=r"D:\Codes\Projects\Code Mosaic\test\test.py")
This module creates a CodeMosaic instance, generates a mosaic image based on the provided code file, and saves the output image as "Code_Mosaic_Output.png." Adjust the parameters in the constructor for customization based on specific requirements.
```

## Image Generation Module
The image_generator module facilitates the generation of images from tokenized code lines with assigned colors. It creates visually appealing images that represent the syntax structure of source code. The module employs the Python Imaging Library (PIL) for image creation, utilizing various features such as text rendering, shapes, and color manipulation.

### File: image_generator.py | Function: build_frames
```
def build_frames(height, width, line_color, location, output_path="Untitled_image.png", font_size=20, spacing=15):
    """
    Generate each element for the final image creation.

    Parameters:
    - height (int): Height of the image.
    - width (int): Width of the image.
    - line_color (list): List of lines, where each line is a list of tuples (word, color).
    - location (str): Directory path where images will be saved.
    - output_path (str): File path for the final mosaic image (default: "Untitled_image.png").
    - font_size (int): Font size for text rendering in the image (default: 20).
    - spacing (int): Spacing between lines in the image (default: 15).
```
#### Parameters:
- height (int): Height of the image.
- width (int): Width of the image.
- line_color (list): List of lines, where each line is a list of tuples (word, color).
- location (str): Directory path where images will be saved.
- output_path (str): File path for the final mosaic image (default: "Untitled_image.png").
- font_size (int): Font size for text rendering in the image (default: 20).
- spacing (int): Spacing between lines in the image (default: 15).

The function generates frames with a terminal-like appearance, including a background color, window frame, and three dots representing the minimize, maximize, and close buttons. The code lines are rendered in the specified font size and color.

Each frame is saved as a separate PNG file in the specified directory. The final mosaic image is composed of these frames.
> Note: Ensure that the JetBrainsMono.ttf font file is available in the working directory for text rendering.

## Color Generator Module
The color_generator module provides a function to assign vibrant colors to different syntax categories of code tokens. The assigned colors enhance the visual representation of code in mosaic images, allowing users to distinguish between various token types.

### File: color_generator.py | Function: vibrant_color
```
def vibrant_color(token):
    """
    Assign vibrant colors to different syntax categories of code tokens.

    Parameters:
    - token (str): Code token in the format "category.subcategory.type".

    Returns:
    - tuple: RGB color tuple (red, green, blue).

    Example Usage:
    >>> vibrant_color("Keyword.Namespace")
    """
```
#### Parameters:
- token (str): Code token in the format "category.subcategory.type".
#### Returns:
- tuple: RGB color tuple (red, green, blue).
#### Example Usage:
```
vibrant_color("Keyword.Namespace")
```
The vibrant_color function assigns vibrant colors to different syntax categories of code tokens based on their hierarchical structure. It enhances the visual representation of code by providing distinct colors for keywords, literals, comments, and other categories.

### Color Assignment Logic:
#### Keywords:
If the token belongs to the "Keyword" category, it checks for specific subcategories:
- "Namespace": Assigned color - (238, 138, 248)
- Default color for other subcategories - (255, 117, 181)

#### Literals:
If the token belongs to the "Literal" category, it checks for specific subcategories:
- "String": Assigned color - (25, 249, 216)
- "Number": Assigned color - (255, 184, 108)
- Default color for other subcategories - (255, 255, 255)

#### Comments:
If the token belongs to the "Comment" category, it checks for specific subcategories:
- "Single": Assigned color - (103, 107, 121)
- "PreprocFile": Assigned color - (109, 238, 240)
- Default color for other subcategories - (255, 255, 255)

#### Default:
- If the token does not match any of the above categories, it returns the default color - (255, 255, 255).

### Example Usage:
```
# Example usage
color = vibrant_color("Keyword.Namespace")
print(color)  # Output: (238, 138, 248)
```
In this example, the vibrant_color function is used to assign a vibrant color to a code token in the "Keyword.Namespace" format. The assigned color is then printed.
