from PIL import Image, ImageDraw, ImageFilter, ImageFont

def build_frames(height, width, line_color, output_path = "Untitled_image.png"):
    file_name = output_path.split(".")[0]
    
    def frames(height, width, line_color, count, font_size = 20, spacing = 15):
        # line_color is an array: [(word, color)]
        # Create a new image with the specified background color and dimensions
        background_color = (93, 94, 184) # purple color
        image = Image.new("RGB", (width, height), background_color)

        # Create a drawing object
        draw = ImageDraw.Draw(image)
        
        # set font
        font = ImageFont.truetype("JetBrainsMono.ttf", font_size)
        
        # create the terminal window
        x = int(0.06*width)
        box_color = (41, 42, 43)
        corner_radius = 15
        draw.rounded_rectangle([(x, x), (width - x, height  - x)], fill=box_color, radius=corner_radius)
        
        # create the three dots
        p = x // 3
        radius = p // 2
        z = 3.5 * radius
        draw.ellipse([(x + p, x + p), (x + p + 2*radius, x + p + 2*radius)], fill=((255, 95, 86)), outline=None)
        draw.ellipse([(x + p + z, x + p), (x + p + 2*radius + z, x + p + 2*radius)], fill=((255, 189, 46)), outline=None)
        draw.ellipse([(x + p + 2*z, x + p), (x + p + 2*radius + 2*z, x + p + 2*radius)], fill=((39, 201, 63)), outline=None)

        # writing area
        color = (255, 255, 255)
        r = width - 2*(x + p)
        v = height - 2*(x + p + radius)
        y_pos = spacing
        # draw.text(xy= [x + p + x_pos, x + p + 2*radius + y_pos], text="Hello", font=font, fill=color)
        for i in range(len(line_color)):
            line = line_color[i]
            x_pos = 0
            # print(line)
            if y_pos <= v - draw.textlength(line[0][0][0], font=font):
                for word, color_ in line:
                    curr_word_length = draw.textlength(word, font=font)
                    if x_pos + curr_word_length <= r:
                        draw.text(xy= [x + p + x_pos, x + p + 2*radius + y_pos], text=word, font=font, fill=color)
                        x_pos += curr_word_length
                    else:
                        if y_pos <= v - draw.textlength(line[0][0][0], font=font):
                            y_pos += spacing + draw.textlength(word[0], font=font)
                            x_pos = 0
                            draw.text(xy= [x + p + x_pos, x + p + 2*radius + y_pos], text=word, font=font, fill=color)
                            x_pos += curr_word_length
                        else:
                            print("Try Increasing the height of the image")
                y_pos += spacing + draw.textlength(word[0], font=font)
            else:
                # saving the image
                image.save(f"{file_name}_part{count}.png")
                return i
        # saving the image
        image.save(f"{file_name}_part{count}.png")
        return None
            

        
    count = 1
    status = frames(height=height, width=width, line_color = line_color, count= count)
    while True:
        if status == None:
            break
        else:
            count += 1
            status = frames(height=height, width=width, line_color = line_color[status:], count= count)
            

        