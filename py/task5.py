import os
import random
path = "D:/AMIT/AMIT_1/dd" 
directory = "D:/AMIT/AMIT_1/dd/222"
if not os.path.exists(directory):
    os.makedirs(directory)
else:
    print("Directory already exists:", directory)
#create number of files inside floder
for i in range(20):
    inner_path = os.path.join(path, "dir_" + str(i)+".txt")
    if not os.path.exists(inner_path):
        os.mkdir(inner_path)
path = "D:\AMIT\AMIT_1\dd\aa.txt"
with open("D:/AMIT/AMIT_1/dd/aa.txt", "a") as file: 
    file.write(" New line added\n")  
    file.seek(0)  
#func to  check the len of files in that folder
def check_len(z):
# check the len of files in that folder 
#input path 
#return len
    path = r'D:/AMIT/AMIT_1/dd'
    z= len (os.listdir(path))
    if len(os.listdir(path)) == 0:
         print("Directory is empty")
    else:
        print("Directory contains files\n"+ path)
        return z
print(check_len(path))



folder_path = r'D:/AMIT/AMIT_1/dd'

# Get a list of all files in the folder
files = [f for f in os.listdir(folder_path) 
         if os.path.isfile(os.path.join(folder_path, f))]

num_files_to_delete = len(files) // 2

files_to_delete = random.sample(files, num_files_to_delete)

# Delete the selected files
for file_name in files_to_delete:
    file_path = os.path.join(folder_path, file_name)
    try:
        os.remove(file_path)
        print(f'Deleted: {file_path}')
    except Exception as e:
        print(f'Error deleting {file_path}: {e}')
print(check_len(path))

#great job you can convert this code to be  function take your path and number of folders .......  """DONE"""
