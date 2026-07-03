s="i am a e python programmer am"
#print(s.count(" am"))
# aeiou
cnt=0
for i in s:
        if(i in 'aeiou' ):
        print(i)
        cnt=cnt+1
print("Number of vowels:=",cnt)
