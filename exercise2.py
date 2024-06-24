from abc import ABC,abstractmethod
class Person(ABC):
  def __init__(self, name, yob):
    self._name=name
    self._yob=yob
  @abstractmethod
  def describe(self):
    pass
  def get_yob(self):
    return self._yob
  def get_name(self):
    return self._name
class Student(Person):
  def __init__(self, name, yob, grade):
    super().__init__(name=name,yob=yob)
    self.__grade=grade
  def describe(self):
    print(f"Student - Name: {self._name}, YOB: {self._yob}, Grade: {self.__grade}")


class Doctor(Person):
  def __init__(self, name, yob, specialist):
    super().__init__(name=name,yob=yob)
    self.__specialist=specialist
  def describe(self):
    print(f"Doctor - Name: {self._name}, YOB: {self._yob}, Grade: {self.__specialist}")

class Teacher(Person):
  def __init__(self, name, yob, teacher):
    super().__init__(name=name,yob=yob)
    self.__teacher=teacher
  def describe(self):
    print(f"Doctor - Name: {self._name}, YOB: {self._yob}, Grade: {self.__teacher}")

class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = list()

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f'Name: {self.__name}')
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                counter += 1
        return counter

    def sort_yob(self):
        self.__list_people.sort(key=lambda x: x.get_yob(), reverse = True)
    def compute_average(self):
      counter = 0
      total = 0
      for p in self.__list_people:
          if isinstance(p, Teacher):
            counter+=1
            total += p.get_yob()
      return total / counter
student1=Student('Hien',2004,'A')
student1.describe()

doctor1=Doctor('Hien',2004,'Computer Science')
doctor1.describe()

teacher1=Teacher('Hien',2004,'Chemistry')
teacher1.describe()

ward1 = Ward('Ward1')
ward1.add_person(student1)
ward1.add_person(doctor1)
ward1.add_person(teacher1)
ward1.count_doctor()
ward1.describe()
ward1.sort_yob()
ward1.describe()
ward1.compute_average()
