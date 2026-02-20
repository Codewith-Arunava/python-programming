# info={
#     "key": "value",
#     "name": "John Doe",
#     "learning": "Python",
#     "topics": ["Data Structures", "OOP", "Web Development"]
# }
# print(info)
# print(type(info))
# print(info["name"])
# info["name"] = "arunava"
# print(info)


#NESTED DICTIONARY
student={
    "name": "John Doe",
    "age": 20,
    "courses": {
        "course1": "Data Structures",
        "course2": "OOP",
        "course3": "Web Development"
    }
}
print(student)
print(student["courses"])
print(student["courses"]["course2"])

print(list(student.keys()))
print(len(student))

print(student.values())

pairs=list(student.items())
print(pairs[2])

print(student.get("name"))


student.update({"city": "barasat"})
print(student)