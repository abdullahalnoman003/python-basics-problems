students = {
    "003" : "Noman",
    "016" : "Reduan",
    "024" : "Adnan",
    "066" : "Rashed",
    "214" : "Asraful"
}
file = open("std.txt", "a")
for id, name in students.items():
    file.write("Id = " + id + " = " + "Name: " + name + "\n")
file.close()

file = open("std.txt", "r")

print("Students Id and Name: ")
print(file.read())