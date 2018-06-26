heads=35
legs=94
lckn=2
lrab=4
for i in range(1,heads):
    for j in range(1,heads):
        if((lckn*i)+(lrab*j) == legs):
            if(i+j==heads):
                print ('There are '+str(i)+' chickens and '+str(j)+ ' rabbits ')
            
