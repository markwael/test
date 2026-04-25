x = str (input(""))
y = ''.join([char for char in x if char.isalpha() or char == ' '])
words = y.split()
first_word = words[0][::-1]
second_word = words[1]
message = f"{first_word} {second_word}"
print(message) 

#approved---good job
