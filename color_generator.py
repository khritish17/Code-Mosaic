def vibrant_color(token):
    token = str(token).split(".")
    if token[1] == "Keyword":
        try:
            if token[2] == "Namespace":
                return (238, 138, 248)
        except:
            return (255, 117, 181)
    # elif token[1] == "Name":
    #     try:
    #         if token[2] == "Function":
    #             return (161, 250, 79)
    #         if token[2] == "Class":
    #             return (115, 43, 245)
    #     except:
    #         return (25, 249, 216)
    elif token[1] == "Literal":
        try:
            if token[2] == "String":
                return (25, 249, 216)
            if token[2] == "Number":
                return (255, 184, 108)
        except:
            return (255, 255, 255)
    elif token[1] == "Comment":
        try:
            if token[2] == "Single":
                return (103, 107, 121)
            if token[2] == "PreprocFile":
                return (109, 238, 240)
        except:
            return (255, 255, 255)
    # elif token[1] == "Text":
    #     return (255, 255, 255)
    # elif token[1] == "Operator":
    #     return (0, 162, 232)
    else:
        return (255, 255, 255)