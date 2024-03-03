import os

# Do the following task using the os module
# create a folder and name the folder 'os_exercises.'                                                  

if not os.path.exists("./os_exercises"):
    os.mkdir("./os_exercises") # Default mode for os.mkdir is 0o777 = read, write, and execute permissions to the owner, group, and others.

# In that folder create a file. Name the file 'exercise.py'
with open("./os_exercises/exercise.txt", "w") as file:
    # get input from the console and write it to the file.
    providedInput = input("Please type something: ")
    file.write(providedInput)

# repeat step 2 and 3 (name the file something else).                                                  
if not os.path.exists("./another_os_exercise"):
    os.mkdir("./another_os_exercise")

with open("./another_os_exercise/another_exercise.txt", "w") as file:
    # get input from the console and write it to the file.
    providedInput = input("Please type something: ")
    file.write(providedInput)


# read the content of the files and and print it to the console
with open("./os_exercises/exercise.txt", "r") as firstFile:
    for line in firstFile:
        print(line)

with open("./another_os_exercise/another_exercise.txt", "r") as secondFile:
    for line in secondFile:
        print(line)