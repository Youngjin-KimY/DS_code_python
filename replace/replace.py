import sys
f = open("testfile","r")
start = sys.argv[1]
to = sys.argv[2]
lines = f.readlines()
f.close()

w = open("testfile","w")
for line in lines:
    line = line.replace(start,to)
    w.write(line)
w.close()