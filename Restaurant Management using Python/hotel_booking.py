import datetime
r_no=int(input("enter the room no u want to choose:"))
food=input("choose bf or 1unch or dinner:")
title=print("           Vineeth Hotel")
print('-'*40)
Name=input("Name:")
Address=input("Address:")
phno=int(input("Phn_no:"))
uid=int(input("uid:"))
r={1:200,2:400}
f={'bf':100,'lunch':200,'dinner':500}
rrate=0
food_price=0
for i in range(1,2):
    sno=i
    if r==1:
        rrate=r['1']
    elif r==2:
        rrate=r['2']
for j in range(1,2,3):
    if j==1:
        food_price=f.get(11)
    elif f==2:
        food_price=f.get(2)
    elif f==3:
        food_price=f.get(3)
T=rrate+food_price
g=T/3
Final_amount=T+g
rows=print("S.no"," "*5,"Rooms"," "*7,"Meals"," "*10,"Total"," "*12)
print('sno'," "*10,'rrate'," "*11,'food_price'" "*11,'T')
print(" ")
print(" ")
print(" "*20,"gst:",g)
print(" "*20,"Final:",Final_amount)
print(" ")
print(" "*15,"Thank you for Visiting🙏")