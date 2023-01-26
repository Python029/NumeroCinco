import string

alpha = list(string.ascii_uppercase)
word = []
index=0
sub=0
total =0
lst = open("names.txt", "r")
names = lst.read().split(',')
names = sorted(names)

for i in range(0,len(names)):
    for a in range(0, len(names[i])):
        for letter in names[i]:
            word.append(letter)
        #Each letter coresponds to a number (Its position in the alphabet)
        for x in range(0,len(alpha)):
            if(word[a] == alpha[x]):
                #Subtotaling the score of each word
                index = index + (x+1)
                #Multiply each word's score by its position in the names list
                sub = i*index
    index=0
    total = total+sub
    sub=0
    word.clear()
print(f"Total Score of All {len(names)} Names: {total}")
lst.close()