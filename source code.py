print("\n\n-------------------------------------------------------------------APS ANNACHI_STORES------------------------------------------------------------------------------")
import mysql.connector # this is used to connect sql with python
from datetime import date
mydb1 = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="annachi_stores")
mycursor = mydb1.cursor()
def staff():
    def billing():
        mycursor.execute("select * from items_in_store")
        myrecords = mycursor.fetchall()
        print("Items in the shop")
        print(f"{'Item.no':20s}{'Item name':20s}{'Price':20s}")
        for x in myrecords:
            s = str(x[0])
            s1 = str(x[2])
            print(f"{s:20s}{x[1]:20s}{s1:20s}")
        w = len(myrecords)
        print("NOTE")
        print('Enter 0 or other than item code\nFor \"Proceeding the bill\"')
        l = []
        l1 = []
        while True:
            c = int(input("Enter the Item_no of the product<1-"+str(w)+">:"))
            z = str(c)
            if z != "0" and c != l1 and c >= 1 and c <= w:
                n = int(input("Number of quantity of the product:"))
            if c >= 1 and c <= w and c != l1:
                l1.append(c)
            mycursor.execute("select item_name,price from items_in_store where item_no="+z)
            myrecords1 = mycursor.fetchall()
            for i in myrecords1:
                l.append(i+(n,))
            else:
                print("The bill is on process")
                break
        d ={}
        for i in range(1,len(l)+1):
            d[i]=l[i-1]
        return d
    def billingcon():
        a = billing()
        print("-------------------------------------------------------------------------------------------------")
        print(f"{'S.no':20s}{'Item name':20s}{'ItemPrice':20s}{'Quantity':20s}{'Total item price'}")
        print("-------------------------------------------------------------------------------------------------")
        k = 0
        for j in range(1,len(a)+1):
            b = str(j)
            c = a[j]
            p = c[1]
            e = c[2]
            f = p*e
            k = k+f
            print(f"{b:20s}{c[0]:20s}{str(p):20s}{str(e):20s}{str(f):20s}")
        print("-------------------------------------------------------------------------------------------------")
        print("TOTAL AMOUNT OF THE PURCHASE:",k)
        print("-------------------------------------------------------------------------------------------------")
        print("Thank you For purchasing VISIT AGAIN")
        return k
    def addingtotal():
        h = billingcon()
        mycursor.execute("select * from total_sales")
        myrecords = mycursor.fetchall()
        y = date.today()
        dat = str(y)
        for i in myrecords:
            if dat == i[0]:
                query = "update total_sales set total_amount = %s where date = %s"
                data = (i[1]+h,dat)
                mycursor.execute(query,data)
                break
        else:
            query = "insert into total_sales values(%s,%s)"
            data = (dat,h)
            mycursor.execute(query,data)
            mydb1.commit()
            print("Billing over")
    def addingitem():
        mycursor.execute("select * from items_in_store")
        myrecords = mycursor.fetchall()
        q = len(myrecords)
        print("NOTE: The item no. for the new product you are giving is:"+str(q+1))
        r = input("Enter the item name:")
        t = int(input("Enter the item price:"))
        query = "insert into items_in_store values(%s,%s,%s)"
        data = (str(q+1),r,str(t))
        mycursor.execute(query,data)
        mydb1.commit()
        print("Added item successfully")
    def updateprice():
        v = int(input("Enter the item no. where you want to edit the price:"))
        price = int(input("Enter the new price for the product:"))
        query = "update items_in_store set price = %s where item_no = %s"
        data = (price,v)
        mycursor.execute(query,data)
        mydb1.commit()
        print("successfully upadated")
    j = "y"
    while j == "y":
        print("CHOICES:")
        print('''1)Bill to customer
2)Adding a item to store
3)Updating price of the existing document
4)exit''')
        c = int(input("Enter your choice:"))
        if c == 1:
            while True:
                addingtotal()
                m = input("Whether you want bill for further more products:")
                if m == "Y" or m == "y" or m == "yes" or m == "Yes":
                    continue
                else:
                    break
        elif c == 2:
            mycursor.execute("select * from items_in_store")
            myrecords = mycursor.fetchall()
            print("Items in the shop")
            print(f"{'Item.no':20s}{'Item name':20s}{'Price':20s}")
            for x in myrecords:
                s = str(x[0])
                s1 = str(x[2])
                print(f"{s:20s}{x[1]:20s}{s1:20s}")
                while True:
                    addingitem()
                    k = input("Whether you want add items to the store further:")
                    if k == "Y" or k == "y" or k == "yes" or k == "Yes":
                        continue
                    else:
                        mycursor.execute("select * from items_in_store")
                        myrecords = mycursor.fetchall()
                        print("Items in the shop")
                        print(f"{'Item.no':20s}{'Item name':20s}{'Price':20s}")
                        for x in myrecords:
                            s = str(x[0])
                            s1 = str(x[2])
                            print(f"{s:20s}{x[1]:20s}{s1:20s}")
                        break
        elif c == 3:
            mycursor.execute("select * from items_in_store")
            myrecords = mycursor.fetchall()
            print("Items in the shop")
            print(f"{'Item.no':20s}{'Item name':20s}{'Price':20s}")
            for x in myrecords:
                s = str(x[0])
                s1 = str(x[2])
                print(f"{s:20s}{x[1]:20s}{s1:20s}")
                while True:
                    updateprice()
                    l = input("Whether you want update price of other products:")
                    if l == "Y" or l == "y" or l == "yes" or l == "Yes":
                        continue
                    else:
                        mycursor.execute("select * from items_in_store")
                        myrecords = mycursor.fetchall()
                        print("Items in the shop")
                        print(f"{'Item.no':20s}{'Item name':20s}{'Price':20s}")
                        for x in myrecords:
                            s = str(x[0])
                            s1 = str(x[2])
                            print(f"{s:20s}{x[1]:20s}{s1:20s}")
                        break
        elif c == 4:
            j = 'n'
        else:
            print("Wrong choice")
v = 'MJDA19210622'
def owner():
    def income1(d1):
        mycursor.execute("select * from total_sales")
        myrecords = mycursor.fetchall()
        e = True
        for i in myrecords:
            if d1 == i[0]:
                print("The overall sales happened in the day:",d1,"is:",i[1])
                e = False
                break
        if e == True:
            print("No sales happened in that day")
    def income2(d1,d2):
        query = "select * from total_sales where date between %s and %s"
        data = (d1,d2)
        mycursor.execute(query,data)
        myrecords = mycursor.fetchall()
        if myrecords == []:
            print("No sales happened in these days")
        else:
            print(f"{'Date':20s}{'Amount':20s}")
        for i in myrecords:
            s = str(i[1])
            print(f"{i[0]:20s}{s:20s}")
    def income():
        a = 'y'
        while a == "y":
            print("""CHOICES:
        1)Total Sales in a specified day
        2)Total Sales in a range of days
        3)Exit""")
            c = int(input("Enter your choice:"))
            if c == 1:
                j = 'y'
                while j == 'y' or j == "Y":
                    d0 = input("Enter the date in which you need the total sales <YYYY-MM-DD>:")
                    income1(d0)
                    j = input("Whether you want to see sales for any other day:")
            elif c == 2:
                j = 'y'
                while j == 'y' or j == "Y":
                    d0 = input("Enter the starting date from which you need the total sales <YYYY-MM-DD>:")
                    d00 = input("Enter the ending date to which you need the total sales <YYYY-MM-DD>:")
                    income2(d0,d00)
                    j = input("Whether you want to see sales for any other range of days:")
            elif c == 3:
                a = 'n'
            else:
                print("Wrong Choice")
    def staff1():
        mycursor.execute("select idno from staff’s")
        myrecords = mycursor.fetchall()
        n = input("Enter the staff name:")
        idno = int(input("Enter the idno:"))
        gender = input("Enter the gender<m/f>:")
        salary = int(input("Enter the salaray:"))
        shift = input("Enter the shift he is working<m/e>:")
        y = 'y'
        while y == 'y':
            for i in myrecords:
                if i[0] == idno:
                    print("Already an person with this id number is present")
                    y = 'n'
                    break
            else:
                query = "insert into staff’s values(%s,%s,%s,%s,%s)"
                data = (idno,n,gender,shift,salary)
                mycursor.execute(query,data)
                mydb1.commit()
                y = 'n'
                print("Added staff successfully")
    def staff2():
        l = 'y'
        while l == 'y':
            idno = int(input("Enter the id number of the staff:"))
            mycursor.execute("select * from staff’s")
            myrecords = mycursor.fetchall()
            for i in myrecords:
                if idno == i[0]:
                    sal = int(input("Enter the new salary:"))
                    query = "update staff’s set salary = %s where idno = %s"
                    data = (sal,idno)
                    mycursor.execute(query,data)
                    mydb1.commit()
                    print("Staff's salary got successfully modified")
                    l = 'n'
                    break
            else:
                print("There is no Staff with this id")
                print("Please Enter the id correctly")
    def staff3():
        mycursor.execute("select * from staff’s")
        myrecords = mycursor.fetchall()
        print(f"{'idno':20s}{'Name':20s}{'Gender':20s}{'Shift':20s}{'Salary':20s}")
        for i in myrecords:
            s = str(i[0])
            s1 = str(i[4])
            print(f"{s:20s}{i[1]:20s}{i[2]:20s}{i[3]:20s}{s1:20s}")
    def staff4():
        mycursor.execute("select idno from staff’s")
        myrecords = mycursor.fetchall()
        d = int(input("Enter the staff id number:"))
        for i in myrecords:
            if i[0] == d:
                query = "Delete from staff’s where idno = %s"
                data = (str(d),)
                mycursor.execute(query,data)
                mydb1.commit()
                print("The information of the staff got deleted")
                break
        else:
            print("There is no staff with this id")
    def staffmanagement():
        d = 'y'
        while d == 'y':
            print("""CHOICES:
            1)Add a new staff
            2)Modifying a staff's salary
            3)Displaying all the staff’s information
            4)Delete the staff's information
            5)Exit""")
            ch = int(input("Enter your choice:"))
            if ch == 1:
                f = 'y'
                while f == 'y':
                    staff1()
                    f = input('Whether you want to add any other staff:')
            elif ch == 2:
                k = 'y'
                while k == "y":
                    staff2()
                    k = input("Whether you want to modify any other staff's salary:")
            elif ch == 3:
                staff3()
            elif ch == 4:
                q = 'y'
                while q == "y":
                    staff4()
                    q = input("Whether you want to delete any other staff's information:")
            elif ch == 5:
                d ='n'
            else:
                print("Wrong choice")
    s = 'y'
    while s == "y":
        print("""CHOICES:
    1)Enquire about income
    2)Staff details
    3)Exit""")
        choi = int(input("Enter you choice:"))
        if choi == 1:
            income()
        elif choi == 2:
            staffmanagement()
        elif choi == 3:
            s = 'n'
        else:
            print("Wrong choice")
kd = 'y'
while kd == 'y':
    print("""CHOICES:
1)staff
2)owner
3)Exit""")
    cho = int(input("Enter your choice:"))
    if cho == 1:
        staff()
    elif cho == 2:
        print("We want to verify that you are the owener")
        password = input("So please enter the password(this is case sensitive):")
        if password == v:
            owner()
        else:
            print("Sorry password is wrong")
            print("Please enter the password correctly")
    elif cho == 3:
        kd = 'n'
        print("BYE!! BYE!!")
    else:
        print("Wrong choice")
