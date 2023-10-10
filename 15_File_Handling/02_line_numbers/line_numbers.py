import string
with open("text.txt", "r") as file: lines = file.readlines()
with open("output.txt", "w") as output_file: [output_file.write(f"Line {i}: {line.strip()} ({sum(1 for char in line.strip() if char.isalpha())})({sum(1 for char in line.strip() if char in string.punctuation)})\n") for i, line in enumerate(lines, start=1)]
