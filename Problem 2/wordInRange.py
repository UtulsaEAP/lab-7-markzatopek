def compare_words(word1:str, word2:str, mode:str=""):
    if mode == "lower":
        word3 = word1
        word1 = word2
        word2 = word3
    
    for i in range(10):
        if ord(word1[i]) < ord(word2[i]): # swapped >
            return True
        if ord(word1[i]) > ord(word2[i]): # swapped <
            return False
    
    return True
        
        
def wordInRange():
    file = input()
    word1 = input()
    word2 = input()
    
    loaded_file = open(file, "r")
    words = loaded_file.readlines()
    loaded_file.close()
    
    for word in words:
        
        word = word.rstrip("\n")
        if compare_words(word, word1, "lower") and compare_words(word, word2):
            word += " - in range"
        else:
            word += " - not in range"
        print(word)
    
    return


if __name__ == '__main__':
    wordInRange()
