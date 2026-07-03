w='''A paragraph is a self-contained unit of writing consisting of one or more
sentences that develop a single central idea. It serves to visually and thematically
organize extended prose, making the text structured and easier for the reader to digest
'''
cnt=w.split()
for i in cnt:
    print(i)
print(len(cnt))
wrd=input("Enter a word to be find:")
n=w.find(wrd)
if(n>0):
    print("Found")
else:
    print("Not Found")
