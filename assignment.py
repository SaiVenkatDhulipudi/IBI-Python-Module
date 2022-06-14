class student:
    def __init__(self,*args) -> None:
        self.stu_name=args[0]
        self.roll_no=args[1]
        self.maths_marks=args[2]
        self.physics_marks=args[3]
        self.chemistry_marks=args[4]

class Menu:
    def __init__(self):
        self.details=list()
        self.avg_maths=0
        self.avg_physics=0
        self.avg_chemistry=0
        self.no_of_students=0
        with open("data.txt","r") as file:
            data=(file.readlines())
            for lines in data:
                lines=list(lines.split())
                self.details.append(lines)
                self.avg_maths+=int(lines[2])
                self.avg_physics+=int(lines[3])
                self.avg_chemistry+=int(lines[4])
                self.no_of_students+=1


    def add(self,data):
        details=[data.stu_name,data.roll_no,data.maths_marks,data.physics_marks,data.chemistry_marks]
        with open("data.txt",'a') as file:
            file.write("{} {} {} {} {}\n".format(*details))
            file.close()
        self.details.append(details)
        self.avg_maths+=int(data.maths_marks)
        self.avg_physics+=int(data.physics_marks)
        self.avg_chemistry+=int(data.chemistry_marks)
        self.no_of_students+=1
    
    def showdata(self,rank):
        if rank:
            for details in self.details:
                print(rank,*details,sep='-')
                rank+=1
        else:
            for detail in self.details:
                print(*detail,sep='-')
    
    #show details of all students in alphabetical order
    def showBYOrder(self):
        self.details.sort(key=lambda details:details[0])
        self.showdata(0)
    
    #Give ranks to students (Based on total marks)
    def Rank(self,rev):
        self.details.sort(key=lambda details:sum([int(marks) for marks in details[2:]]),reverse=rev)
        self.showdata(1)

    #Average marks of students in each subject
    def AvgMarksBySubject(self):
        print("Average marks in maths subject are: {}".format(self.avg_maths/self.no_of_students))
        print("Average marks in physics subject are: {}".format(self.avg_physics/self.no_of_students))
        print("Average marks in chemistry subject are: {}".format(self.avg_chemistry/self.no_of_students))
    
    #sort the students based on marks scored by user in that subject.
    def OrderBySubject(self,choice):
        self.details.sort(key=lambda detail:int(detail[choice]),reverse=True)
        self.showdata(0)

if __name__=="__main__":
    helper="""
    I am here to help you 
    Enter 1 To add student data
    Enter 2 To show the students in alphabetical order
    Enter 3 To Rank the students by total marks
    Enter 4 To Get Average marks in each subject
    Enter 5 To Get Order students by Respective Subject marks
    press 0 to exit
    enter your choice here :"""
    helper2="""
    Enter 1 To Sort by Maths marks
    Enter 2 To Sort by Physics marks
    Enter 3 To Sort by Chemistry marks 
    Enter your Choice Here : """
    helper3="""
    Enter 0 for Ascending 
    Enter 1 for Descending 
    Enter your choice here : """
    menu=Menu()

    while True:
        choice=int(input(helper)) 
        print()
        if choice==0:
            exit() 
        if choice==1:
            st_name=input("enter Name of the student : ")
            st_roll=input("enter Roll number of the student : ")
            st_maths=input("enter maths marks of the student : ")
            st_physics=input("enter physics marks of the student : ")
            st_chemistry=input("enter chemistry marks of the student : ")
            data=student(st_name,st_roll,st_maths,st_physics,st_chemistry)
            menu.add(data)
            print("Data Added Sucessfully")
        elif choice==2:
            if menu.no_of_students:
                menu.showBYOrder()
            else:
                print("Sorry there is no data of students available")
        elif choice==3:
            reverse=int(input(helper3))
            menu.Rank(reverse)
        elif choice==4:
            if menu.no_of_students:
                menu.AvgMarksBySubject()
            else:
                print("Sorry there is no data of students available")
        elif choice==5:
            menu.OrderBySubject(int(input(helper2))+1)
        











