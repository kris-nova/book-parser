import sys

words = {}


# Parse a line of text
def parse_line(line):
    list = line.split()
    for word in list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1


# Book parsing
path = "john_dies_at_the_end.txt"
f = open(path, 'r')

# Operate on lines instead of the entire file so we don't have a memory overflow
while True:
    line = f.readline()
    parse_line(line)

# Output here

print json.dumps(words, sort_keys=True, indent=4, separators=(',', ': '))
