import os
extensions = {}
file_names = [file for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))) for file in files]
[extensions.setdefault(file.split('.')[1], []).append(file.split('.')[0]) for file in file_names]
sd = {k: sorted(v) for k, v in sorted(extensions.items())}
with open("report.txt", "w") as file: [file.write(f".{key}\n" + "".join([f"- - - {value}.{key}\n" for value in values])) for key, values in sorted(sd.items())]
