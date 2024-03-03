
# Create a file called numbers.dat
# Write the numbers from 1-100 to the file.
with open("./testfiles/numbers.dat", "w") as numbersFile:
    
    for number in range(100):
        # numbersFile.write("{}{}".format(number + 1, '\n' if number + 1 != 100 else ''))
        numbersFile.write(f"{number + 1}")
        if number + 1 != 100:
            numbersFile.write("\n")

# open the file for reading, and print all even numbers to the screen.
with open("testfiles/numbers.dat", "r") as numbersFile:
    for line in numbersFile:
        number = int(line.strip())
        if number % 2 == 0:
            print(number)