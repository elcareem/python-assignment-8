"""
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.

Example Usage:
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}
"""
class AttendanceRegister:
    def __init__(self):
        self.records = {}

    def mark_present(self, student):
        if student not in self.records:
            self.records.update({student: "Present"})
        else:
            print(f"Student {student} has already marked attendance")


    def mark_absent(self, student):
        if student not in self.records:
            self.records.update({student: "Absent"})
        else:
            print(f"Student {student} has already marked attendance")


    def get_status(self, student):
        if student in self.records:
            return self.records[student]
        else:
            return f"Student {student} is not on the attendance register"


    def show_register(self):
        return self.records

register = AttendanceRegister()
register.mark_present("John")
register.mark_absent("Mary")
print(register.get_status("John"))   
print(register.show_register())     
register.mark_present("John")
register.mark_absent("Mary")

