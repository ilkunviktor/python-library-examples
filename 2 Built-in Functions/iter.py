import os

directory = os.path.dirname(__file__)

with open(directory + '/id.py') as f:
    for word in iter(f.readlines()):
        print(word, end='!')