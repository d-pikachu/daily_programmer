#https://www.reddit.com/r/dailyprogrammer/comments/7x81yg/20180213_challenge_351_easy_cricket_scoring/
i = input()

p = []
b = 0
e = 0
s = [0,0]

'''
1.2wW6.2b34 
Output description
Individual scores of batsman that have played and number of extras. For example:

 P1: 7  
 P2: 2  
 P3: 9  
 Extras: 2
 '''
for x in i:
	if b==6: 
	    b=0
	    s.reverse()
		
	if x=="W":
	    p.append(s[0])
	    s[0] = 0
	    b+=1
	
	if x>="1" and x<="9":
		s[0] += int(x)
		if int(ord(x)%2)!=0:
		    s.reverse()
	if x in ".b":
            b+=1
        if x=='b':
            s.reverse()
	if x in "wb": e+=1
	
if s[1]>0: p.append(s[1])
if s[0]>0: p.append(s[0])

for i,x in enumerate(p):
    print("P"+str(i+1)+": "+str(x))
print("Extras: "+str(e))
