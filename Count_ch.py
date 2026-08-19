# Count the character in sentence or in paragraph

# word

count = 0
word = "abcdefghijklmnopqrstuvwxyzabcadefaghiajklmnaopqarstuavwaxtaz"

for ch in word:
    if (ch == "a"):
        count += 1
        
print("Total count of a = ", count)