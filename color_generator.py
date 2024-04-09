def vibrant_color(token):
    # Split the token into parts
    token = str(token).split(".")
    # print(token)

    # Check if the token belongs to the "Keyword" category
    if token[1] == "Keyword":
        try:
            # Check if it is a "Namespace" Keyword
            if token[2] == "Namespace":
                return (238, 138, 248)  # Return a specific color
        except:
            return (255, 117, 181)  # Return a default color

    # Check if the token belongs to the "Literal" category
    elif token[1] == "Literal":
        try:
            # Check if it is a "String" Literal
            if token[2] == "String":
                return (25, 249, 216)  # Return a specific color
            # Check if it is a "Number" Literal
            # if token[2] == "Number":
            #     return (255, 184, 108)  # Return a specific color
        except:
            return (255, 184, 108)
            # return (255, 255, 255)  # Return a default color

    # Check if the token belongs to the "Comment" category
    elif token[1] == "Comment":
        try:
            # Check if it is a "Single" Comment
            if token[2] == "Single":
                return (103, 107, 121)  # Return a specific color
            # Check if it is a "PreprocFile" Comment
            if token[2] == "PreprocFile":
                return (109, 238, 240)  # Return a specific color
        except:
            return (103, 107, 121)
            return (255, 255, 255)  # Return a default color
    elif token[1] == "Text":
        return (0, 207, 255)
    elif token[1] == "Name":
        try:
            if token[2] == "Function":
                return (255, 184, 108)
                # return (255, 64, 8)
            if token[2] == "Builtin":
                return (255, 64, 8)
        except:
            pass
        # return (255, 184, 108)
        return (255, 255, 255)
    elif token[1] == "Operator":
        return (164, 250, 0)
    elif token[1] == "Punctuation":
        return (56, 109, 255)
    else:
        return (255, 255, 255)  # Return a default color if no category matches
