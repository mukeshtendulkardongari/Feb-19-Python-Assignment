# 1. armstrong number

num=int(input("Enter a number:"))
temp=num
sum=0
power=(len(str(num)))
while num>0:
    digit=num%10
    sum+=digit**power
    num//=10
if temp==sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# OUTPUT:
# Enter a number:153
# Armstrong number
# Enter a number:56
# Not an Armstrong number

# 2. neon number

num=int(input("Enter a number:"))
temp=num**2
sum=0
while temp>0:
    digit=temp%10
    sum+=digit
    temp//=10
if num==sum:
    print("Neon number")
else:
    print("Not a neon number")

# OUTPUT:
# Enter a number:9
# Neon number
# Enter a number:7
# Not a neon number
# Enter a number:0
# Neon number

# 3. strong number 

num=int(input("Enter a number:"))
fact_sum=0
temp=num

while temp>0:
    digit=temp%10
    fact=1

    for i in range(1,digit+1):
        fact*=i
    fact_sum+=fact
    temp//=10

if fact_sum==num:
    print("Strong number")
else:
    print("Not a strong number")

# OUTPUT:
# Enter a number:145
# Strong number
# Enter a number:1
# Strong number
# Enter a number:67
# Not a strong number

# 4. perfect number

num=int(input("Enter a number:"))
temp=num
sum=0
for i in range(1,temp):
    if temp%i==0:
        sum+=i
if num==sum:
    print("Perfect number")
else:
    print("Not a perfect number")

# OUTPUT:
# Enter a number:28
# Perfect number
# Enter a number:5
# Not a perfect number
# Enter a number:6
# Perfect number

# 5. harshad number

num=int(input("Enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit
    temp//=10
if sum!=0 and num%sum==0:
    print("Harsed number")
else:
    print("Not a harshed number")

# OUTPUT:
# Enter a number:11
# Not a harshed number
# Enter a number:7
# Harsed number
# Enter a number:18
# Harsed number