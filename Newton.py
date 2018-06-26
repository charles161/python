tc = input("Enter the number of test cases: ")
mass=[]
force=[]
for i in range(tc):
    mass.append(input("Enter the mass of "+str(i+1)+ " test case: "))
    force.append(input("Enter the force of "+str(i+1)+ " test case: "))
for i,m in enumerate(mass):
    print str(i+1)+' Acceleration: '+str(force[i]/m)
