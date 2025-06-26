# conditions inline
x = 10
s = "Even" if x % 2 == 0 else "Odd"
print(s)

# boucles while
i = 0
while i < 5:
    print(i)
    i = i + 1

# for ... in
l1 = [1, 2, 4, 8]
for x in l1:
    print(f"- {x=}")

l2 = "Hello World !"
for x in l2:
    print(f"- {x=}")

l3 = range(5,10)
for x in l3:
    print(f"- {x=}")
