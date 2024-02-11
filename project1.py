import math
while True:
    print("1. Caculating angle of deviation ")
    print("2. Caculating refractive index of a prism")
    ch = int(input("Enter your choice :  "))
    if ch==1:
        print("===============================================")
        A = float(input("Enter angle of prism : "))
        u = float(input("Enter Refractive Index of prism : "))
        ia = float(input("Enter angle of incidence : "))
        A1 = (A*math.pi)/180
        i1 = (ia*math.pi)/180
        da = i1+math.asin(u*math.sin(A1-math.asin(i1)/u))-A1
        d1 = (da*180)/math.pi
        d2 = round(d1,0)
        print("Angle of Deviation :  ",d2)
        print("===============================================")
        input("press enter to continue")
        print("===============================================")
    if ch==2:
        print("===============================================")
        d = float(input("Enter minimum angle of deviation : "))
        A = float(input("Enter Angle of prism : "))
        d1 = d*math.pi/180
        A1 = A*math.pi/180
        u = (math.sin((A1+d1)/2))/(math.sin(A1/2))
        u2 = round(u,3)
        print("The Refractive Index of prism : ")
        print("===============================================")
        input("press enter to continue")
        print("===============================================")