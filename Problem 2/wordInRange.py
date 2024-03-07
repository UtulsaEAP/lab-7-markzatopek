def compare_words(word1:str, word2:str, mode:str="higher"):
    if mode == "lower":
        word3 = word1
        word1 = word2
        word2 = word3
    for i in range(10):
        if word1[i] > word2[i]:
            return True
        if word1[i] < word2[i]:
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
        print(word,end="")
        if compare_words(word, word1, "lower") and compare_words(word, word2):
            print(" - in range")
        else:
            print(" - not in range")
    return


if __name__ == '__main__':
    wordInRange()
