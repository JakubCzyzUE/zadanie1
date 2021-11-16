class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def is_passed(self) -> bool:
        print(self.name)
        if(self.marks > 50):
            print("ocena " + self.name + " studenta jest większa niż 50")
            return True
        elif(self.marks < 50):
            print("ocena " + self.name + " studenta jest mniejsza niż 50")
            return False
