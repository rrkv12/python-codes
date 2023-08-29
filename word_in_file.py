file = open("word.txt")
print(file.read())
search_word = input("enter a word you want to search in file: ")
if(search_word == file):
    print("word found")
else:
    print("word not found")
