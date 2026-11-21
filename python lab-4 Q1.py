# Log File Reader

file = open("log.txt", "r")

print("Log File Contents:")

for line in file:
    print(line.strip())

file.close()
