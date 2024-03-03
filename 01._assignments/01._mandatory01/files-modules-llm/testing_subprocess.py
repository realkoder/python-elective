import subprocess

# Using textmode -> encoding="utf-8" is set for run method
output_from_file = subprocess.run(["cat", "./another_os_exercise/another_exercise.txt"], capture_output=True, encoding="utf-8") 

# If in text mode, the .stdout attribute on a CompletedProcess is now a string and not a bytes object
print(output_from_file.stdout)

# Returned bytes can also be decoded by calling the .decode() method on the stdout attribute directly, without requiring text mode at all:
output_from_file = subprocess.run(["cat", "./another_os_exercise/another_exercise.txt"], capture_output=True)

print(output_from_file.stdout.decode("utf-8"))