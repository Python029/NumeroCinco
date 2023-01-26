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
        for x in range(0,len(alpha)):
            if(word[a] == alpha[x]):
                index = index + (x+1)
                sub = i*index
    index=0
    total = total+sub
    sub=0
    word.clear()
print(f"Total Score of All {len(names)} Names: {total}")
lst.close()