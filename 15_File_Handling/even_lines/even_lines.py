[print(f"{line.replace('-', '@').replace(',', '@').replace('.', '@').replace('!', '@').replace('?', '@').strip()}") for i, line in enumerate(open("text.txt", "r").readlines()) if i % 2 == 0]
