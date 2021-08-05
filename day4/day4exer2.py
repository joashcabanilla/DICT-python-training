# try:
#     file = open("data.txt", "r")
#     content = file.read()
#
#     print("This is the content:")
#     print(content)
#
#     file.close()
#
# except FileNotFoundError:
#     print("File is not Found.")

# try:
#     file = open("data.txt", "w")
#     msg = str(input("Enter message: "))
#
#     file.write(msg)
#     file.close()
# except FileNotFoundError:
#     print("File is not Found.")

try:
    file = open("data.txt", "a") #appending the content to a textfile
    msg = str(input("Enter message: "))

    file.write(msg + "\n")
    file.close()
except FileNotFoundError:
    print("File is not Found.")
