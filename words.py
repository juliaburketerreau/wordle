filehandle = open("words.txt", 'w')
for _ in range(5):
    words = str(input())
    filehandle.write(words+"\n")
filehandle.close()