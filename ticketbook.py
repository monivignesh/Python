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

row,column = map(int,input("Enter row and column size ").split())
seat_avail = create_arr(row,column)
flag=1

while(flag):
    no_seat = int(input("Enter number of seats to book: "))
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