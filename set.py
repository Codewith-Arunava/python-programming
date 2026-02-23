# collection={1,2,3,4}
# print(collection)
# print(type(collection))
# print(len(collection))

# collection.add(5)
# print(collection)
# collection.remove(2)
# print(collection)
# collection.pop()
# print(collection)



# set1={1,2,3}
# set2={3,4,5}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))


#practice question 1

#store the following word meanings in a python dict:
# table:"a piece of furniture","list of facts &figures"
# cat:"a small animal"

dict={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts &figures"]
}
print(dict)


#assume one classroom is required for 1 classroom .how many classrooms are needed by all students
#"python",""java,"c++","javascript","java","python","java","c++","c"

students={"python","java","c++","javascript","java","python","java","c++","c"}
print(len(students))

#WAP to enter marks of 3 subs from the user and store them in s dict.start with an empty dict & add one by one.use subject name as key & marks as value.

marks={}

x=int(input("enter marks of phy:"))
marks.update({"phy":x})

y=int(input("enter marks of chem:"))
marks.update({"chem":y})

z=int(input("enter marks of math:"))
marks.update({"math":z})

print(marks)