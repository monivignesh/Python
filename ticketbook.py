'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#sadhana added
#moni added

def create_arr(row,column):
    arr=[]
    for i in range(row):
        temp=[]
        for j in range(column):
            temp.append(1)
        arr.append(temp)
    return arr

def disp():
    for _ in seat_avail:
        print(_)

def availability(seat,row,column):
    r = ((seat+row)//column)
    c = seat - ((r-1)*column)
    if seat%column == 0:
        return (r-2,column-1)
    return (r-1,c-1)
fl=1
while(fl):
    row,column = map(int,input("Enter row and column size ").split())
    if row==0 or column==0:
        print("Invalid")
       # row,column = map(int,input("Enter row and column size ").split())
    else:
        fl=0
    
seat_avail = create_arr(row,column)
flag=1
xo=1
while(flag):
    #no_seat = int(input("Enter number of seats to book: ")) 
    while(xo):
        no_seat = int(input("Enter number of seats to book: ")) 
        if((no_seat<=(row*column)) and (no_seat!=0) and no_seat>0):
            while(no_seat):
                disp()
                seat = int(input("Enter seat number: "))
                r,c = availability(seat,row,column)
                print(r,c)
                if seat_avail[r][c] != 0 and (r != -1) and (c != -1):
                    print("Booked",seat)
                    seat_avail[r][c] = 0
                    no_seat -= 1
                else:
                    print("Already booked, choose another seat or Enter valid seat")
            xo=0
        else:
            print("Enter valid seat no")
    f = int(input("1.Continue Booking, 0.Exit "))
    if not f:
        flag = 0
disp()
flag2=1
while(flag2):
    seat_req = int(input("Enter number of seats to find possibility: "))
    possibility = 0
    stack=[]
    for lis in seat_avail:
        for x in lis:
            if x == 1:
                stack.append(x)
                if len(stack) == seat_req:
                    possibility += 1
                    stack.pop()
            else:
                stack.clear()
        stack.clear()
    print("Number of Possibilities for",seat_req,"is",possibility)
    f1 = int(input("1.Continue, 0.Exit "))
    if not f1:
        flag2 = 0