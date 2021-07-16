# multiplication table

print ("print multiplication table")
for x in range (1, 10):
    print("======[" + str(x) + " Times Table]======")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("============")