# Python OOPs Practice

This repository contains Python programs focused on learning and practicing **Object-Oriented Programming (OOPs)** concepts using Python.  
Each program is beginner-friendly and aligned with real-world scenarios and interview preparation.

---

## 📚 Topics Covered

- ✅ Class and Object  
- ✅ Constructor (`__init__`)  
- ✅ Instance Attributes  
- ✅ Instance Methods  
- ✅ Inheritance (`super()` usage)  
- 🔜 Coming Soon: Encapsulation, Polymorphism, Mini OOPs Projects  

---

## 🚀 About This Repository

This repo is a part of my **Python learning journey** as I prepare for a **fresher-level Data Engineer role**.  
I'm focusing on hands-on coding with strong concepts in:

- OOPs  
- Functions  
- File handling  
- Real-world logic building  

Feel free to **fork**, **clone**, or **use** this for your own learning or revision!

---

## 💡 Sample Code: Employee & Developer (with Inheritance)

```python
# Create a class Employee:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

# Create a child class Developer (inherits from Employee):
class Developer(Employee):
    def __init__(self, name, salary, tech):
        super().__init__(name, salary)
        self.tech = tech

    def full_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Technology:", self.tech)

# Create object and call method
d1 = Developer("Kavyansh", 80000, "Data science")
d1.full_info()
