from PIL import Image, ImageDraw, ImageFilter

def create_rounded_box_image(background_color, box_color, width, height, corner_radius, output_path):
    # Create a new image with the specified background color and dimensions
    image = Image.new("RGB", (width, height), background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw a rounded rectangle (box) with the specified color and corner radius
    x = int(0.07*width)

    draw.rounded_rectangle([(x, x), (width - x, height - x)], fill=box_color, radius=corner_radius)
    
    y = x // 2
    center_x, center_y = x + y, x + y
    radius = y // 3
    z = 3*radius
    draw.ellipse([(center_x - radius, center_y - radius), (center_x + radius, center_y + radius)], fill=((255, 95, 86)), outline=None)
    draw.ellipse([(center_x + z - radius, center_y - radius), (center_x + z + radius, center_y + radius)], fill=((255, 189, 46)), outline=None)
    draw.ellipse([(center_x + 2*z - radius, center_y - radius), (center_x + 2*z + radius, center_y + radius)], fill=((39, 201, 63)), outline=None)
    # Save the image to the specified output path
    image.save(output_path)

# Example usage
background_color = (93, 94, 184)  # White background color (RGB format)
box_color = (41, 42, 43)  # Black box color (RGB format)
image_width = 1084
image_height = 720
corner_radius = 10
output_file_path = "rounded_box_image.png"

create_rounded_box_image(background_color, box_color, image_width, image_height, corner_radius, output_file_path)
