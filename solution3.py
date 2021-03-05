import copy

class Employee:
    def __init__(self):
        self._name = ""
        self._age = None
        self._salary = None
        self._emailid = ""

    def setName(self, name):
        self._name = name
    
    def setAge(self, age):
        self._age = age
    
    def setSalary(self, salary):
        self._salary = salary
        
    def setEmail(self, emailid):
        self._emailid = emailid

    def __str__(self):
        return f"Employee name is {self._name} and email id is {self._emailid}"

if __name__ == "__main__":
    
    emp1 = Employee()
    emp1.setName("Sonali Prasad")
    emp1.setEmail("sonali.prasad17@gmail.com")

    emp2 = copy.deepcopy(emp1)
    emp2.setName("TestName")
    emp2.setEmail("Test.Name@emailid.com")

    print(emp1)
    print(emp2)
