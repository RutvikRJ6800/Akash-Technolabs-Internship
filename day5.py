# 1. Create a class cal1 that will calculate sum of three numbers. 
# Create setdata() method which has three parameters that 
# contain numbers. 
# Create display() method that will calculate sum and display sum.


class cal1:
    def setdata(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def display(self):
        result = self.num1 + self.num2 + self.num3
        print("Sum of theree number is : ",result)

# c1 = cal1()
# c1.setdata(1,2,3)
# c1.display()


#2. Create a class cal2 that will calculate area of a circle. 
# Create setdata() method that should take radius from the user. 
# Create area() method that will calculate area . 
# Create display() method that will display area .

class cal2:

    def setdata(self):
        radius = float(input("Enter radius...\n"))
        self.radius = radius

    def area(self):
        result = (3.14)*(self.radius)**2
        self.result = result

    def display(self):
        print("Area of the circule is : ",self.result)

# c2 = cal2()
# c2.setdata()
# c2.area()
# c2.display()

# 3. Create a class cal3 that will calculate simple interest. 
# Create constructor method which has three parameters .
# Create calInterest() method that will calculate Interest . 
# Create display() method that will display Interest.

class cal3:
    def __init__(self,p,r,n) -> None:
        self.p = p
        self.r = r 
        self.n = n
    
    def callInterest(self):
        self.interst = (self.p*self.r*self.n) / 100

    def display(self):
        print("Interest is equal to : ",self.interst)

# c3 = cal3(100,10,1)
# c3.callInterest()
# c3.display()


# 4. Create a class cal4 that will calculate square of a number.
#  Create setdata() method which has one parameters that contain number. 
# Create display() method that will calculate sum.(Function should return value)

class cal4:

    def setdata(self,num):
        self.num = num

    def display(self):
        result = self.num**2
        print("Square of the number is: ",result)

# c4 = cal4()
# c4.setdata(2)
# c4.display()


# 5. Consider an employee class, which contains fields such as name and designation. 
# And a subclass, which contains a field salary.
#  Write a program for inheriting this relation.

class employee:

    def __init__(self,name,designation) -> None:
        self.name = name
        self.designation = designation

class subclass(employee):

    def __init__(self, name, designation,salary) -> None:
        super().__init__(name, designation)
        self.salary = salary

# s1 = subclass('rutvik','ML engineer',100000)
# print(s1.__dict__)


# 6. Create a class cal5 that will calculate area of a rectangle.
#  Create constructor method which has two parameters 
# .Create calArea() method that will calculate area of a rectangle. 
# Create display() method that will display area of a rectangle.

class cal5:

    def __init__(self,length,width) -> None:
        self.length = length
        self.width = width

    def calArea(self):
        self.result = self.length * self.width

    def display(self):
        print("Area of the Rectangle is : ",self.result)

# c5 = cal5(5,5)
# c5.calArea()
# c5.display()



# 7. Create a class cal6 that will calculate area of a square.
#  Create setdata() method that should take length from the user.
#  Create area() method that will calculate area . 
# Create display() method that will display area .


class cal6:
    def setdata(self)       :
        length = int(input("Enter the length of square "))
        self.length = length

    def area(self):
        self.result = self.length**2

    def display(self):
        print("Area of the square id: ",self.result)

# c6 = cal6()
# c6.setdata()
# c6.area()
# c6.display()

# 8. Write a program with use of inheritance: 
# Define a class publisher that stores the name of the title. 
# Derive two classes book and tape, which inherit publisher. 
# Book class contains member data called page no and tape class contain time for playing. 
# Define functions in the appropriate classes to get and print the details.

class Publisher:
    def __init__(self,title):
        self.title = title

    def print(self):
        print("title of the book is: ",self.title)

class Book(Publisher):
    def __init__(self, title,pageNo):
        super().__init__(title)
        self.pageNo = pageNo

    def print(self):
        super().print()
        print("pages: ",self.pageNo)

class Tape(Publisher):
    def __init__(self, title, time):
        super().__init__(title)
        self.time = time

    def print(self):
        super().print()
        print("time: ",self.time)


# cBook = Book('Into to Algorithms',1300)
# cBook.print()
# cTape = Tape('The C Programming','5 PM')
# cTape.print()


# 9. Create a class called scheme with
#  scheme_id, scheme_name,outgoing_rate, and message_charge.
#  Derive customer class form scheme and include cust_id, name and mobile_no data.
# Define necessary functions to read and display data.

class Scheme:
    def __init__(self,scheme_id, scheme_name,outgoing_rate, message_charge) -> None:
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.outgoing_rate = outgoing_rate
        self.message_charge = message_charge

    def print(self):
        print("scheme_id: ",self.scheme_id)
        print("scheme_name: ",self.scheme_name)
        print("scheme_rate: ",self.outgoing_rate)
        print("scheme_charge: ",self.message_charge)

class Customer(Scheme):
    def __init__(self, scheme_id, scheme_name, outgoing_rate, message_charge,cust_id, name, mobile_no) -> None:
        super().__init__(scheme_id, scheme_name, outgoing_rate, message_charge)
        self.cust_id = cust_id
        self.name = name
        self.mobile_no = mobile_no

    def print(self):
        super().print()
        print("customer_id: ",self.cust_id)
        print("customer_name: ",self.name)
        print("mobile_no: ",self.mobile_no)
# cust1 = Customer(123,'Full Talktime1','0.10 rs/min','1 rs/sms',123,'XYZ',9876543210)
# cust1.print()

# 10.Create a arith class. The class should have a parameterized constructor 
# and methods to add, subtract and multiply two numbers and 
# to return the answers.

class Arith:
    def __init__(self,num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def print(self):
        print("Addition is: ",self.num1 + self.num2)
        print("Subtraction is: ",self.num1 - self.num2)
        print("Multiplication is: ",self.num1 * self.num2)
        
a1 = Arith(10,5)
a1.print()
