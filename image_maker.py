from PIL import Image, ImageDraw, ImageFilter, ImageFont

def build_frames(height, width, tokens, token_color, output_path = "Unititled_image.png", font_size = 20, spacing = 15, startIndex = 0, call_count = 0):
    # Create a new image with the specified background color and dimensions
    background_color = (93, 94, 184) # purple color
    image = Image.new("RGB", (width, height), background_color)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("JetBrainsMono.ttf", font_size)
    letter = tokens[0][0][1]
    letter_height = draw.textlength(letter, font=font)
    
    # create the terminal window
    r = (letter_height + spacing )* len(tokens)
    x = int(0.06*width)
    y = x//2
    # k = (height - r - 2*y) // 2
    k = x
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
    count = 0
    for token in tokens[startIndex:]:
        x_pos = 0
        # if y_pos <= k + y + r:
        for key, val in token:
            # color = token_color[key]
            color = (255, 255, 255)
            if draw.textlength(val, font=font) + x + y + x_pos <= width - x- y:
                draw.text(xy= [x + y + x_pos, k + y + 2*radius + y_pos], text=val, font=font, fill=color)
                x_pos += draw.textlength(val, font=font)
            else:
                x_pos = 0
                y_pos += letter_height + spacing
        # else:
        #     build_frames(height=height, width=width, tokens=tokens, token_color=token_color, output_path=f"perfect_{call_count + 1}.png", startIndex=count, call_count= call_count + 1)
        #     break
        count += 1 
        y_pos += letter_height + spacing

    
    image.save(output_path)


