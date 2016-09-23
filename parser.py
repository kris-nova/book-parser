import sys
import json
from collections import OrderedDict

def parse_line(line):
    list = line.split()
    if len(list) == 0:
        return False
    global lines
    global words
    lines += 1

    #print "Lines: " + str(lines)
    for word in list:
        print "*",
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return True


# Book parsing
path = "john_dies_at_the_end.txt"
f = open(path, 'r')
lines = 0
words = {}
# Operate on lines instead of the entire file so we don't have a memory overflow
line = f.readline()
while parse_line(line):
    line = f.readline()


# Output here
sortedWords = OrderedDict(sorted(words.items(), key=lambda x: x[1]))
raw = json.dumps(sortedWords, indent=4, separators=(',', ': '))
text_file = open("Output.json", "w")
text_file.write(raw)
text_file.close()


# Lets have some fun
for word in sortedWords:
    print word + "  :  " + str(sortedWords[word])
