file = open("yoututbe.txt", "w")

try:
    file.write("me aur code")
finally:
    file.close()

with open("youtube.txt", "w") as file:
    file.write("me aur pyhton")