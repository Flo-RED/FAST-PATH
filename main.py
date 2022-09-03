import os, time, func, webbrowser

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: variables
path_data = []
web_data = []
path_list = []
print_list = []
s_list = []
exit = False

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: read + save pathes
with open("data.txt", "r") as data:
    file = data.readlines()
row = []
for y in file:
    row.append(y.replace("\n", ""))
for y in range(len(row)):
    if row[y] == ". . . . . . . . . . . . . . . . .":
        path_data.append([row[y + 1], row[y + 2].split()[0], row[y + 3]])
        if len(row[y + 2].split()) > 1:
            s_list.append(row[y + 2])

    elif row[y] == ". . . . . . . . . . . . . . . . w":
        web_data.append([row[y + 1], row[y + 2].split()[0], row[y + 3], row[y + 4]])
        
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: main loop
while True:

    # ......................................................... update interface
    func.update(exit, print_list)
    i = input("\n: ").lower()

    if i != "":
        i = i.split()
        exit = False
        s = False

        # ...................................................... if input is web
        if i[0] == "w":
            # .... add file path command
            res = func.fix_error_data(i[1], web_data)
            if res:
                final_path = ""
                final_print = ""
                if res[2][:5] == "https": # if link includes https
                    final_path += res[2]
                else:                     # if not then add it
                    final_path += f"https://www.{res[2]}"
                final_print += res[0]
                # .... check if there is search
                if len(i) > 2:
                    final_path += f"{res[3]}{i[2]}"
                    final_print += f" : {i[2]}"
                # add to the main list
                print_list += [final_print]
                path_list += [final_path]

        # ..................................................... if input is file
        else:
            # .... add file path command
            res = func.fix_error_data(i[0], path_data)
            if res:
                # s time
                for x in s_list:
                    if x.split()[0] == res[1]:
                        si = input("\n: ")
                        if si == "123":
                            s = True
                        break
                else:
                    s = True
                # if the input has more than one diractory
                if s:
                    if len(i) > 1:
                        final_path = res[2]
                        final_print = res[0]
                        # loop thro the input
                        for a in range(len(i)):
                            try:
                                # correct input error
                                res_2 = func.fix_error_dir(i[a+1], os.listdir(f"{final_path}"))
                                # if corrected input exists
                                if res_2:
                                    final_path += f"\\{res_2}"
                                    final_print += f" : {res_2}"
                            except IndexError:
                                pass
                        path_list += [final_path]
                        print_list += [final_print]
                    else:
                        path_list += [res[2]]
                        print_list += [res[0]]

        # ............................................. delete last path command
        if i[0] == "-":
            if path_list:
                path_list.pop()
                print_list.pop()

    # ............................................................. exit command
    else:
        if print_list or exit:
            break
        else:
            exit = True
    if print_list:
        exit = False

# ------------------------------------------------------------------- run pathes
for x in path_list:
    if x[:5] == "https":
        webbrowser.open_new_tab(x)
    else:
        os.startfile(x)
