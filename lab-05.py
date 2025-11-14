#program1
a = {'one': 1, 'two': 2, 'three': 3}
print(a)

#program2
b = {1: 'apple', 2: 'banana', 3: 'cherry'}
b.pop(1)
b.append(4, 'date')
print(b)
            
#program3
n = {11,55,33,77,55,11}
maximum = max(n)
minimum = min(n)
print("Max:", maximum)
print("Min:", minimum)

#program4
c = {'a', 'b', 'c'}
reverse = c [::-1]
print("Reversed:", reverse)

#program5
n = {1,2,3,4,5}
freq = {}
for i in n:
    freq[i] = freq.get(i,0) + 1 
print("Frequency:", freq)
    
#program6
ch = input("Enter a character: ")
count =0

if ch in 'AEIOUaeiou':
       count +=1
       print(f"{ch} is a vowel. Count:", count)         


#program7
def palindrome(s):
    return s==s[::-1]
print(palindrome("madam"))  

#program8
import string

text = "Hello, world! How's everything?"

result = ""
for char in text:
    if char not in string.punctuation:
        result += char

print(result)

#program9
text = "I love programming in Python"

words = text.split()   # split into words
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

text = "I love programming in Python"

words = text.split()   # split into words
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

text = "I love programming in Python"

words = text.split()   # split into words
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

#program10
# creating and writing to the file
file = open("myfile.txt", "w")
file.write("Hello! This is a sample text file.\nWelcome to Python file handling.")
file.close()

# reading and displaying the content
file = open("myfile.txt", "r")
content = file.read()
print("File Content:\n")
print(content)
file.close()

#program11
# append data to an existing file
with open("myfile.txt", "a") as f:
    f.write("\nThis is the new line added to the file.")

print("Data appended successfully!")

#program12
count = 0

with open("myfile.txt", "r") as f:
    for line in f:
        count += 1

print("Number of lines in file:", count)

#program13
with open("myfile.txt", "r") as f:
    count = 0
    for line in f:
        count += 1

print("Number of lines:", count)

#program14
from collections import Counter

# read file
with open("myfile.txt", "r") as f:
    text = f.read()

# split into words
words = text.split()

# count frequency
freq = Counter(words)

# display frequency
for word, count in freq.items():
    print(word, ":", count)

#program15
# open source file (the file to read)
with open("source.txt", "r") as f1:
    data = f1.read()

# open destination file (the file to write/copy into)
with open("destination.txt", "w") as f2:
    f2.write(data)

print("Content copied successfully!")
