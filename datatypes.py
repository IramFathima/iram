# data types

#1)sting

a = [5,10,15,20,25,30,35,40]

# a[3] = 35
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

a = [5,10,15,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])


#2) numeric data
a = 6
print(a, "is of type", type(a))

a = 4.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

#2) numeric data
a = 3
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

#3) list

L1=[0,2,10,40,50]
L2=[0,5,60,10]
print(L1+L2)
#3) list

L1=[0,2,10,60,40,50]
L2=[60,10]
print(L1+L2)


#4) boolean
3+2==1+3
#the output will be false

#5) sets

S1={2,22,10,40}
S2={1,2,3,4,10}
print(S1^S2)

#5) sets

S1={2,21,10,40}
S2={1,2,3,40,10}
print(S1^S2)
