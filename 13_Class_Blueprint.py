# --- THE CLASS (The Blueprint) ---
class Student:
    # The __init__ method is a "constructor" that sets up the object
    def __init__(self, name, grade_level, tech_skill):
        self.name = name           # Attribute
        self.grade = grade_level   # Attribute
        self.skill = tech_skill    # Attribute

    # A method is a function that belongs to the object
    def introduce(self):
        print(f"Hi! I'm {self.name}. I'm in Grade {self.grade} and I love {self.skill}!")

# --- THE OBJECTS (The Instances) ---
# We use the blueprint to create specific students
student1 = Student("Alex", 9, "Python")
student2 = Student("Maya", 10, "Web Design")

# Now we tell the objects to perform their actions
student1.introduce()
student2.introduce()