def fileNameChange():
    file = input()
    loaded_file = open(file, "r")
    file_names = loaded_file.readlines()
    loaded_file.close()
    
    new_names = []
    for name in file_names:
        new_names.append(name.rstrip("_photo.jpg") + "_info.txt")
    
    loaded_file = open(file, "w")
    for name in new_names:
        loaded_file.write(name)
    loaded_file.close()

    return

if __name__ == '__main__':
    fileNameChange()