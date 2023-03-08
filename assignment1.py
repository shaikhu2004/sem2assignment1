studentlist={}
studentlistfile=open('studentlist.txt','r+')


with open('studentlist.txt') as f:
    studentdetailstr = f.read().splitlines()

for line in studentdetailstr:
    studentdetails=eval(line)
    name=studentdetails['Name']
    studentlist[name]=studentdetails


def Addstudent_info(studentname):
    studentlistfilefn = open('studentlist.txt', 'a')

    IDno = int(input('enter student ID number:'))

    studentlist[studentname]=({'Name': studentname, 'ID': IDno})
    yearno = input('Enter Year Number:')
    year = str('Year ' + yearno)

    studentfallsubs = []
    studentFSsubnum = int(input('How many subjects in Fall?:'))

    while len(studentfallsubs) < studentFSsubnum:
        sub = input('Enter Subject Code:')

        valid = False
        while not valid:
            if checkprereqs(sub, studentname) == False:
                sub = input('Enter Subject Code:')
            else:
                valid = True

        if sub in studentfallsubs:
            print('You already took this subject')

        else:
            studentfallsubs.append(sub)

    studentspringsubs = []
    studentSSsubnum = int(input('How many subjects in Spring?:'))

    while len(studentspringsubs) < studentSSsubnum:
        sub = input('Enter Subject Code:')

        valid = False
        while not valid:
            if checkprereqs(sub, studentname) == False:
                sub = input('Enter Subject Code:')
            else:
                valid = True

        if sub in studentspringsubs:
            print('You already took this subject.')

        else:
            studentspringsubs.append(sub)

    studentsummersubs = []
    studentSumSsubnum = int(input('How many subjects in Summer?'))

    while len(studentsummersubs) < studentSumSsubnum:
        sub = input('Enter Subject Code:')

        valid = False
        while not valid:
            if checkprereqs(sub, studentname) == False:
                sub = input('Enter Subject Code:')
            else:
                valid = True

        if sub in studentsummersubs:
            print('You already took this subject')

        else:
            studentsummersubs.append(sub)

    studentlist[studentname][year] = {'Fall': studentfallsubs, 'Spring': studentspringsubs, 'Summer': studentsummersubs}

    studentlistfilefn.write(str(studentlist[studentname])+'\n')
    studentlistfilefn.close()


def checkprereqs(subcode,name):
    with open('prerequisites.txt') as f:
        mylist = f.read().splitlines()

    prerequisites = {}

    for line in mylist:
        if len(line) == 0:
            continue
        else:
            sub = line.split(':')[0]
            prereqs = eval(line.split(':')[1])
            prerequisites[sub] = prereqs

    if subcode in prerequisites:
        for prereq in prerequisites[subcode]:
            if prereq in str(studentlist[name]):
                continue
            else:
                print(prereq, 'has not yet been complete.')
                return False
    else:
        print('Incorrect Subject Code.')
        return False





def addCourses(studentname):
    studentlistfilefn = open('studentlist.txt', 'a')
    yearno = input('Enter Year Number:')
    year = str('Year ' + yearno)

    studentfallsubs = []
    studentFSsubnum = int(input('How many subjects in Fall?:'))

    while len(studentfallsubs) < studentFSsubnum:
        sub = input('Enter Subject Code:')

        valid = False
        while not valid:
            if checkprereqs(sub, studentname) == False:
                sub = input('Enter Subject Code:')
            else:
                valid = True

        if sub in studentfallsubs:
            print('You already took this subject')

        else:
            studentfallsubs.append(sub)

    studentspringsubs = []
    studentSSsubnum = int(input('How many subjects in Spring?:'))

    while len(studentspringsubs) < studentSSsubnum:
        sub = input('Enter Subject Code:')

        valid = False
        while not valid:
            if checkprereqs(sub, studentname) == False:
                sub = input('Enter Subject Code:')
            else:
                valid = True

        if sub in studentspringsubs:
            print('You already took this subject.')

        else:
            studentspringsubs.append(sub)

    studentsummersubs = []
    studentSumSsubnum = int(input('How many subjects in Summer?'))

    while len(studentsummersubs) < studentSumSsubnum:
        sub = input('Enter Subject Code:')

        valid = False
        while not valid:
            if checkprereqs(sub, studentname) == False:
                sub = input('Enter Subject Code:')
            else:
                valid = True

        if sub in studentsummersubs:
            print('You already took this subject')

        else:
            studentsummersubs.append(sub)

    studentlist[studentname][year] = {'Fall': studentfallsubs, 'Spring': studentspringsubs, 'Summer': studentsummersubs}

    with open("studentlist.txt", "r") as fp:
        lines = fp.readlines()

    with open("studentlist.txt", "w") as fp:
        for line in lines:
            if line.strip("\n") != str(studentlist[studentname])+'\n'):
                fp.write(line)

    fp.close()

def StudentListFns(FunctionInput):

    if FunctionInput == 1:
        name = input('Enter Student Name:')
        Addstudent_info(name)

    elif FunctionInput == 2:
        name = input('Enter Student Name:')
        addCourses(name)

    else:
        print("Error")

    choiceagain = input("Would you like to do another Function?(Function Number/n)")

    if choiceagain == 'n':
        print('Thank you for using.')

    else:
        valid = False
        while not valid:
            if choiceagain.isnumeric() and (int(choiceagain) > 0 and int(choiceagain) <= 9):
                StudentListFns(int(choiceagain))
                valid = True
            else:
                print('Please enter a number between 1 and 2')
                choiceagain = (input('Choose a function number:'))


print('Following is a list of functions')
print('1. Add a new student.')
print("2. Add to a student's courses.")


valid=False
while not valid:
    FNinput = (input('Choose a function number:'))
    if FNinput.isnumeric() and (int(FNinput) >0 and int(FNinput)<=9):
        StudentListFns(int(FNinput))
        valid=True
    else:
        print('Please enter a number between 1 and 9')
        FNinput = (input('Choose a function number:'))


studentlistfile.close()
