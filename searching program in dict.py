students_DB = {}
while True:
    line = input("Enter id and name seprated by comma, or q to exit: ")
    if line == 'q':
        break;
    id, name = line.split(',')
    students_DB.update({id:name})
for x,y in students_DB.items():
    print(x,":",y);
key = input("Enter ID to search: ")
if key in students_DB:
    print("Key:",key,"'s value is:",students_DB[key])
else:
    print("Key not found")
