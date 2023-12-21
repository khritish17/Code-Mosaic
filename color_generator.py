import random

def generate_vibrant_color():
    # Generate random RGB values
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    # Ensure the color is vibrant on a dark theme
    # You can adjust these conditions based on your preference
    while R + G + B < 300:  # Ensure sufficient brightness
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)

    return (R, G, B)
