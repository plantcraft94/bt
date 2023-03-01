f = open("Data.in", "r")
s = f.read()
s = s.split(" ")
a = 0
for i in range(0,200,2):
    if int(s[i]) % 5 == 0 or int(s[i]) % 3 == 1:
        a += 1
g = open("Data.out", "w")
g.write(str(a))
g.close()
