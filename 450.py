class Person:
    def __init__(self, prefix, Fname, Lname, street, hphone, wphone, box, department):
        self.prefix = prefix
        self.Fname = Fname
        self.Lname = Lname
        self.street = street
        self.hphone = hphone
        self.wphone = wphone
        self.box = box
        self.department = department


def main():
    departments = int(input())
    personsArr = []
    for i in range(departments):
        department = input()
        line = ""
        while True:
            line = input()
            if line == "" or line == "\n":
                break
            inoputArr = line.split(",")
            inoputArr.append(department)
            person = Person(*inoputArr)
            personsArr.append(person)
    personsArr.sort(key=lambda x: x.Lname)
    for person in personsArr:
        print("----------------------------------------")
        print(person.prefix, person.Fname, person.Lname)
        print(person.street)
        print("Department:", person.department)
        print("Home Phone:", person.hphone)
        print("Work Phone:", person.wphone)
        print("Campus Box:", person.box)


while True:
    try:
        main()
    except EOFError:
        break
