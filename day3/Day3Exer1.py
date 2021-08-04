# i = 1
# while i <= 5:
#     print(i, end="\t")
#     i = i + 1

# i = 1
# print("number \t\t square \t cube")
# while i <= 3:
#     print(f"{i} \t\t {i*i} \t\t{i*i*i}")
#     i = i+1

# i = 5
# while i >= 1:
#     print(i, end="")
#     i = i-1

# n = int(input("Enter a number: "))
# i = 1
# f = 1
# while i <= n:
#     f = f * i
#     i = i + 1
# print(f"The factorial of {n} is {f}")

# s = int(input("Enter side: "))
# i = 1
# while i <= (s*s):
#     if i % s == 0:
#         print("*")
#     else:
#         print("*", end=" ")
#     i += 1

n = int(input("Enter side: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print("*", end=" ")
        j += 1
    print()
    i += 1
