x = str (input(""))
y = ''.join([char for char in x if char.isalpha() or char == ' '])
words = y.split()
first_word = words[0][::-1]
second_word = words[1]
z = second_word.replace ( "I" , "E" ).replace ( "O" , "U" )
message = f"{first_word} {z} "
print(message) 

#approved ---good job
