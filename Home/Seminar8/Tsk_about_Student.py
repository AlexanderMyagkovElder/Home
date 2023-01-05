class Students():
    def __init__(self, numbers_of_student):
        self.numbers_of_student = int(input("enter number of student: "))
    def Enter_name(self,name_st):
        self.name_st=[]
        for i in range(self.numbers_of_student):
            self.name_st.append(input('enter fullname of students: '))
        self.name_st.sort()
a = Students('')
a.Enter_name('')
print(a.name_st)
