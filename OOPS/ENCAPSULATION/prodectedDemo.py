class Student :

    def __init__ (self) :

        self._name = "python"

    def _funName (self) :

        return "Method here"
    
class Sub(Student) : 

    pass

obj = Student()

obj1 = Sub()

print(obj._name)

print(obj._funName())

print(obj1._name)

print(obj1._funName())

