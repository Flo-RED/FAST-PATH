import os, time, webbrowser


# :::::::::::::::::::::::::::::::::::::::::::::::::: function : update interface
def update(exit, print_list):
    os.system("cls")
    if exit:
        print("         ■■■■ ■■ ■ ■■■■ ■■■■    ■■■■")
        print("         ■■■   ■■   ■■   ■■       ■■")
        print("         ■■    ■■   ■■   ■■      ■  ")
        print("         ■■■■ ■ ■■ ■■■■  ■■        ■")
    else:
        print("■■■■  ■■■ ■■■■ ■■■■      ■■■■  ■■■ ■■■■ ■■ ■")
        print("■■   ■■ ■ ■■    ■■       ■■ ■ ■■ ■  ■■  ■■■■")
        print("■■■■ ■■■■   ■■  ■■       ■■■■ ■■■■  ■■  ■■ ■")
        print("■■   ■■ ■ ■■■■  ■■       ■■   ■■ ■  ■■  ■■ ■")
    print("\n")
    for x in print_list:
        print(x)


# ::::::::::::::::::::::::::::::::::::::::::::::::::: function : fix input error
def fix_error_data(input, list):
    input_splited = [char for char in input]
    # check if the exact input exists in the list
    for x in list:
        if input == x[1]:
            return x
    # correct the error loop
    for x in list:
        # if the word data is bigger or equal to the length of the input
        if len(x[1]) >= len(input)-1 and len(x[1]) > 2:
            right_count = 0
            x_splited = [char for char in x[1]]
            # loop thro every char in the input
            for char_input in input_splited:
                # loop thro every char in the word data
                for char_x in x_splited:
                    if char_input == char_x:
                        right_count += 1
            # make a correction percentage
            right_percent = right_count/len(x_splited)
            if right_percent >= 0.75:
                return x


# ::::::::::::::::::::::::::::::::::::::::::::::::::: function : fix input error
def fix_error_dir(input, list):
    input_splited = [char for char in input]
    # check if the exact input exists in the list
    for x in list:
        # ................................................... clean list content
        x2 = x.lower()
        x2 = x2.replace(" ", "")
        x2 = x2.replace("[", "")
        x2 = x2.replace("]", "")
        # .... delete file type
        if len(x2) >= 4:      # if the file is atleast 4 chars long
            if x2[-4] == ".": # if the file is not a folder
                x2 = x2[:-4]  # delete the file type
        # if the file is the exact input
        if input == x2:
            return x # return the original file name
    # ................................................... correct the error loop
    for x in list:
        # ................................................... clean list content
        x2 = x.lower()
        x2 = x2.replace(" ", "")
        x2 = x2.replace("[", "")
        x2 = x2.replace("]", "")
        # .... delete file type
        if len(x2) >= 4:      # if the file is atleast 4 chars long
            if x2[-4] == ".": # if the file is not a folder
                x2 = x2[:-4]  # delete the file type
        # if the file is the exact input
        if input == x2:
            return x # return the original file name
        # ..................................................... correct the word
        # if the word data is bigger or equal to the length of the input
        if len(x2) >= len(input)-1 and len(x2) > 1:
            right_count = 0
            x_splited = [char for char in x2]
            # loop thro every char in the input
            for char_input in input_splited:
                # loop thro every char in the word data
                for char_x in x_splited:
                    if char_input == char_x:
                        right_count += 1
            # make a correction percentage
            right_percent = right_count/len(x_splited)
            if right_percent >= 0.75:
                return x





# ░▒▓▓▓▓▒░░▒▓▓▓▒░▒▓▓▓▓▒░▒▓▓▓▓▒░ ░▒▓▓▓▓▒░░▒▓▓▓▒░▒▓▓▓▓▒░▒▓▓▒▓▒░
# ░▒▓▓▒░░░▒▓▓▒▓▒░▒▓▓▒░░░░▒▓▓▒░  ░▒▓▓▒▓▒░▒▓▓▒▓▒░░▒▓▓▒░░▒▓▓▓▓▒░
# ░▒▓▓▓▓▒░▒▓▓▓▓▒░░░▒▓▓▒░░▒▓▓▒░  ░▒▓▓▓▓▒░▒▓▓▓▓▒░░▒▓▓▒░░▒▓▓▒▓▒░
# ░▒▓▓▒░░░▒▓▓▒▓▒░▒▓▓▓▓▒░░▒▓▓▒░  ░▒▓▓▒░░░▒▓▓▒▓▒░░▒▓▓▒░░▒▓▓▒▓▒░
