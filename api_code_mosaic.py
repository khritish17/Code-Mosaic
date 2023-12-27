import code_mosaic as CM

def generate_image(location="", height=500, width=1000, font_size=20, spacing=15):
    # Create an instance of the CodeMosaic class with specified parameters
    CM.CodeMosaic(height=height, width=width, font_size=font_size, spacing=spacing, location=location)

# Example usage to generate an image with custom parameters
generate_image(location=r"D:\Codes\Projects\Code Mosaic\test\test.py", width=1500, font_size=30)
