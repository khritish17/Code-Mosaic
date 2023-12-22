from PIL import Image, ImageDraw, ImageFilter, ImageFont

def build_frame(height, width, lines, output_path = "Untitled Image.png"):

    # Create a new image with the specified background color and dimensions
    background_color = (93, 94, 184) # purple color
    image = Image.new("RGB", (width, height), background_color)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    font_size = 20
    font = ImageFont.truetype("JetBrainsMono.ttf", font_size)
    
    # create the terminal window
    spacing = 15
    letter = list(lines[0])[0]
    letter_height = draw.textlength(letter, font=font)
    # r = len(lines) * font_size
    r = (letter_height + spacing )* len(lines)
    x = int(0.06*width)
    y = x//2
    k = (height - r - 2*y) // 2
    box_color = (41, 42, 43)
    corner_radius = 15
    draw.rounded_rectangle([(x, k), (width - x, height + spacing - k)], fill=box_color, radius=corner_radius)

    
    # create the three circles
    radius = y//3
    z = 3.5 * radius
    draw.ellipse([(x + y, k + y), (x + y + 2*radius, k + y + 2*radius)], fill=((255, 95, 86)), outline=None)
    draw.ellipse([(x + y + z, k + y), (x + y + 2*radius + z, k + y + 2*radius)], fill=((255, 189, 46)), outline=None)
    draw.ellipse([(x + y + 2*z, k + y), (x + y + 2*radius + 2*z, k + y + 2*radius)], fill=((39, 201, 63)), outline=None)
    
    # writing area starts from [x + y, k + y + 2*radius]
    # write the text
    y_pos = spacing
    for line in lines:
        draw.text(xy= [x + y, k + y + 2*radius + y_pos], text=line, font=font)
        y_pos += letter_height + spacing

    # saving the image
    image.save(output_path)
message = ["draw.ellipse([(x + y + 2*z, k + y), (x + y + 2*radius + 2*z, k + y + 2*radius)], fill=((39, 201, 63)), outline=None)", "  id: 5678,", "   username: 'khritish17'", "  name: 'Khritish'", "};"]
build_frame(height=500, width=1000, lines=message, output_path = "code_mosaic.png")