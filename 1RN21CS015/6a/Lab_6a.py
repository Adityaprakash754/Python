fname  = input("Enter file name: ")
infile = open(fname,"r")
line = int(input("Enter number of lines to read: "))

for x in range (line):
    a = infile.readline()
    print(x+1,":",a)

infile.seek(0)
word = input("Enter word to search for: ")
cnt = 0
for line in infile :
    r = line.split()
    cnt += r.count(word)

print("The word" , word , "apperas" , cnt , "times in the file." ) 