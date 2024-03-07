def fileNameChange():
    file = input()
    loaded_file = open(file, "r")
    file_names = loaded_file.readlines()
    loaded_file.close()
    
    new_names = []
    for name in file_names:
        name.rstrip("\n")
        print(name[:-10] + "_info.txt")

    return

if __name__ == '__main__':
    fileNameChange()