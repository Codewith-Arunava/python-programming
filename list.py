marks=[33,44,55,66,77]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student=["sachin",45,5.6,"mumbai"]
print(student)
print(type(student))
print(student[0])
student[0]="sachin tendulkar"
print(student)

marks=[33,44,55,66,77]
print(marks[-4:-1])
marks.append(88)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
print(marks.reverse())
print(marks)
marks.insert(2,100)
print(marks)
marks.remove(55)
print(marks)