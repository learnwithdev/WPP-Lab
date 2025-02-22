class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def __add__(self, o):
        return self.salary+ o.salary
    def __sub__(self,o):
        return self.salary-o.salary
    def __gt__(self, o):
        if self.salary > o.salary:
            return f"{self.name}'s earns more than {o.name}"
        else:
            return f"{o.name}'s earns more than {self.name}"

e1=Employee('Dev',101)
e2=Employee('Manash',302)
print(f"Sum of salaries: {e1+e2}")
print(e1>e2)
