from string import ascii_uppercase as abc

names = open("p022_names.txt", "r").read()
names = sorted([name.replace('"', "") for name in names.split(",")])

def getScore(name, pos):
    return sum([abc.index(letter)+1 for letter in name]) * pos

print sum([getScore(pos,name) for name,pos in enumerate(names,1)])