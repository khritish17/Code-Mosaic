import api_code_mosaic as api 
print("WELCOME TO THE CLI MODULE OF CODE MOSAIC")
# print("enter q + ENTER to quit")
while True:
    inp = input(">_ Press 'p' to proced or 'q' to quit: " )
    if inp in "qQ":
        break
    else:
        location = input("\n>_ Input the full path of the source code:\n")
        print("\nThe default parameters for the output image:\n[1] Height: 500px\n[2] Width: 500px\n[3] Font Size: 20px\n[4] Spacing between lines: 15px")
        print("\nEnter the following to change the output image parameters:")
        print("-> Press 'h' or 'H' to change Height")
        print("-> Press 'w' or 'W' to change Width")
        print("-> Press 'f' or 'F' to change Font Size")
        print("-> Press 's' or 'S' to change Spacing")
        print("-> Press 'c' or 'C' to continue")
        
        height, width, font_size, spacing = 500, 1000, 20, 15
        while True:
            commands = input(">_ Provide your input for changes: ")
            if commands in "hH":
                while True:
                    try:
                        height = int(input(">_ Enter the Height: "))
                        break
                    except:
                        print("[x] Provide a proper height, try again...")
            elif commands in "wW":
                while True:
                    try:
                        width = int(input(">_ Enter the Width: "))
                        break
                    except:
                        print("[x] Provide a proper width, try again...")
            elif commands in "fF":
                while True:
                    try:
                        font_size = int(input(">_ Enter the Font Size: "))
                        break
                    except:
                        print("[x] Provide a proper height, try again...")
            elif commands in "sS":
                while True:
                    try:
                        spacing = int(input(">_ Enter the Spacing: "))
                        break
                    except:
                        print("[x] Provide a proper spacing, try again...")
            elif commands in "cC":
                print("Continuing")
                break
            else:
                print("Enter a correct command")
        try:
            api.generate_image(location= location, height= height, width = width, font_size=font_size, spacing=spacing)
            print("\nImage succesfully created at the same location as the source code\n")
        except:
            print("Something wrong, please report mail: khritish.official@gmail.com or raise issue in github: https://github.com/khritish17/Code-Mosaic.git")