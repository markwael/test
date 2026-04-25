x = "Amit_ml@gmail.edu"
def con(c):    
    if '@' and '.' in x:
        print(True)
    else:
        print("Invalid email") 
    if True:
        y = x.split('@') 
        z = x.split('.')
        print("Extract Username:" , y[0])
        print("Extract Domain:" ,z[1])
        
    if z[1] == "edu":
        print("Educational Domain")
    elif z[1] == "com":
        print("Commercial Domain")
    else:
        print("Other Domain")
     
print (con(x))

'''
here your output
True
Extract Username: Amit_ml
Extract Domain: edu
Educational Domain

'''
# Great job thank you now i think you can convert this code to be a function """"DONE""""
