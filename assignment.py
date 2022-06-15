from collections import defaultdict
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
        self.rolls=defaultdict(lambda:0)
        with open("data.txt","r") as file:
            data=(file.readlines())
            for lines in data:
                lines=list(lines.split())
                self.rolls[lines[0]]=1
                self.details.append(lines)
                self.avg_maths+=int(lines[2])
                self.avg_physics+=int(lines[3])
                self.avg_chemistry+=int(lines[4])
            file.close()
        self.no_of_students=len(self.details)
        try:
            self.avgmarks=(self.avg_chemistry+self.avg_maths+self.avg_physics)/((3*self.no_of_students))
        except:
            print("Sorry there is no data of students available")
            return

    def reader(self,nam,typ,var=None):
        if typ=="alpha":
            var=input(nam)
            if var.isalpha():
                return var
            print("Enter proper input")
            return self.reader(nam,typ,var)
        else:
            var=input(nam)
            if var.isdigit():
                return var
            print("Enter proper input")
            return self.reader(nam,typ,var)


    def add(self,data):
        details=[data.roll_no,data.stu_name,data.maths_marks,data.physics_marks,data.chemistry_marks]
        if self.rolls[data.roll_no]:
            return False
        with open("data.txt",'a') as file:
            file.write("{} {} {} {} {}\n".format(*details))
            file.close()
        self.rolls[details[1]]=1
        self.details.append(details)
        self.avg_maths+=int(data.maths_marks)
        self.avg_physics+=int(data.physics_marks)
        self.avg_chemistry+=int(data.chemistry_marks)
        self.no_of_students+=1
        self.avgmarks=(self.avg_chemistry+self.avg_maths+self.avg_physics)/(3*self.no_of_students)
        return True
    def showdata(self,rank,details):
        if rank:
            print("Rank\t\tRoll.No\t\tName\t\tMaths\t\tPhysics\t\tChemistry")
            print("-"*(90))
            for details in details:
                print(rank,*details,sep=' '*13)
                rank+=1
        else:
            print("Roll.No\t\tName\t\tMaths\t\tPhysics\t\tChemistry")
            print("-"*(73))
            for detail in details:
                print(*detail,sep=' '*13)
    
    #show details of all students in alphabetical order
    def showBYOrder(self):
        self.details.sort(key=lambda details:details[0])
        print("showing details of all students in alphabetical order")
        self.showdata(0,self.details)
    
    #Give ranks to students (Based on total marks)
    def Rank(self,rev):
        self.details.sort(key=lambda details:sum([int(marks) for marks in details[2:]]),reverse=rev)
        print("Ranked Students on Total Marks")
        self.showdata(1,self.details)

    #Average marks of students in each subject
    def AvgMarksBySubject(self):
        print("Average marks in maths subject are: {}".format(self.avg_maths/self.no_of_students))
        print("Average marks in physics subject are: {}".format(self.avg_physics/self.no_of_students))
        print("Average marks in chemistry subject are: {}".format(self.avg_chemistry/self.no_of_students))
    
    #sort the students based on marks scored by user in that subject.
    def OrderBySubject(self,choice):
        print("Sorted the students based on marks scored by Students in {}".format(["maths","physics","chemistry"][abs(2-choice)]))
        self.details.sort(key=lambda detail:int(detail[choice]),reverse=True)
        self.showdata(0,self.details)

    #Show students who scored above average(total) marks
    def AboveAverage(self):
        self.aboveAvg=list(filter(lambda detail:(sum([int(marks) for marks in detail[2:]])/3>=self.avgmarks),self.details))
        self.aboveAvg.sort(key=lambda detail:(sum([int(marks) for marks in detail[2:]])/3),reverse=True)
        print("Showing students who scored above average(total) marks")
        self.showdata(0,self.aboveAvg)
        
    
    #Show students who scored 10% above/below average (total marks) marks
    def AboveBelowAverage(self):
        diff=0.1*(self.avgmarks)
        self.aboveAvg=list(filter(lambda detail:(sum([int(marks) for marks in detail[2:]])/3>=diff),self.details))
        self.belowAvg=list(filter(lambda detail:(sum([int(marks) for marks in detail[2:]])/3<=diff),self.details))
        self.aboveAvg.sort(key=lambda detail:(sum([int(marks) for marks in detail[2:]])/3),reverse=True)
        self.belowAvg.sort(key=lambda detail:(sum([int(marks) for marks in detail[2:]])/3),reverse=True)
        print("""Showing students who scored 10"%" above average (total marks) marks""")
        self.showdata(0,self.aboveAvg)
        print("""Showing students who scored 10"%" below average (total marks) marks""")
        self.showdata(0,self.belowAvg)

    #Show students who scored above average scores in maths but below average in physics
    def AboveAvgInMathsBelowAvgInPhysics(self):
        avg_maths=self.avg_maths/self.no_of_students
        avg_physics=self.avg_physics/self.no_of_students
        self.scores=list(filter(lambda detail:int(detail[2])>=avg_maths and int(detail[3])<=avg_physics,self.details))
        self.scores.sort(key=lambda detail:int(detail[2])>=avg_maths and  int(detail[3])<=avg_physics,reverse=True)
        print("Showing students who scored above average scores in maths but below average in physics")
        self.showdata(0,self.scores)
    
    #Number of students who scored above average in all the 3 subjects
    def AboveAverageCount(self):
        self.maths_count=len(list(filter(lambda detail:int(detail[2])>=self.avg_maths/self.no_of_students,self.details)))
        self.physics_count=len(list(filter(lambda detail:int(detail[3])>=self.avg_physics/self.no_of_students,self.details)))
        self.chemistry_count=len(list(filter(lambda detail:int(detail[4])>=self.avg_chemistry/self.no_of_students,self.details)))
        print("Number of students who scored above average in maths :{}".format(self.maths_count))
        print("Number of students who scored above average in physics :{}".format(self.maths_count))
        print("Number of students who scored above average in chemistry :{}".format(self.maths_count))

if __name__=="__main__":
    helper="""
I am here to help you 
Enter 1 To add student data
Enter 2 To show the students in alphabetical order
Enter 3 To Rank the students by total marks
Enter 4 To Get Average marks in each subject
Enter 5 To Get Order students by Respective Subject marks
Enter 6 To Get List of students who scored above average(total) marks
Enter 7 To Get List of students who scored above average scores in maths but below average in physics
press 0 to exit
Enter your choice here :"""
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
        elif choice==1:
            st_name=menu.reader("Enter Name of the student : ","alpha")
            st_roll=menu.reader("Enter Roll number of the student : "," ")
            st_maths=menu.reader("Enter maths marks of the student : "," ")
            st_physics=menu.reader("Enter physics marks of the student : "," ")
            st_chemistry=menu.reader("Enter chemistry  marks of the student : "," ")
            data=student(st_name,st_roll,st_maths,st_physics,st_chemistry)
            if menu.add(data):
                print("Data Added Sucessfully")
            else:
                print("Roll No is Already Available please Enter Valid Roll Number")
        elif menu.no_of_students:
            if choice==2:
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
            elif choice==6:
                menu.AboveAverage()
            elif choice==7:
                menu.AboveAvgInMathsBelowAvgInPhysics()
            elif choice==8:
                menu.AboveAverageCount()
            else:
                print("Invalid Choice")
        else:
            print("There exists No students data Please Choose 1 to add data")
            
        

