# this is comment

# sequences

names = ["MD", "Shahidul", "Islam", "Raihan"]

for name in names:
    print(name)


# nested loop

for name in names:
    print(name)
    for character in name:
        print(character)

# range(initial,end,increment or decrement)

for i in range(1,10):
    if i % 5 == 0: 
        print(i)

