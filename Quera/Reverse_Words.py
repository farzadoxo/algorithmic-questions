
def reverse_word(n:int,words:str):
    if len(words.split(" ")) != n :
           return -1
    else:
        word_list = words.split(" ")
        word_list.reverse()
        return " ".join(word_list)
