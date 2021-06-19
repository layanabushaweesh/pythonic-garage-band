
from abc import abstractmethod,ABC
from typing import Counter
# abstractmethod mehod use to force the dev to defin method in sub class and we but it in base class as pass


# class to make our data type for band

class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)

    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(self):
       #it will loop in array and append each item to new list that i crate
      # pass

      solo_list = []

      for item in self.members:

            solo_list.append(item.play_solo())

      return solo_list

    def __str__(self):
        # pass
      return(f"My name is  {self.name} and I {self.members}" )

    def __repr__(self):

      return f"Band instance. name={self.name} , member={self.members}"

# class method to do somthing for the base class and hereh it is for return a list that previously created
  


class Musician():

   def __init__(self,name):
    self.name=name


   def __str__(self):

      return f"My name is {self.name} and I play {self.get_instrument()}"
   
   def __repr__(self):

      # Bassist instance. Name = Meshell Ndegeocello => return as this sample Bassist the name of class it self

      return f"{type(self).__name__} instance. Name = {self.name}"

   @abstractmethod
   def get_instrument(self):
     pass

   @staticmethod
   def play_solos(self):
      pass


#Guitarist,Bassist, and Drummer are inheritance from Musician class:

class Guitarist(Musician):

   def __init__(self,name):
      super().__init__(name)

   def get_instrument(self):
      return "guitar"

   def play_solo(self):
    return "face melting guitar solo"


class Bassist(Musician):

   def __init__(self,name):
      super().__init__(name)

   def get_instrument(self):
      return "bass"

   def play_solo(self):
    return "bom bom buh bom"

class Drummer(Musician):

   def __init__(self,name):
      super().__init__(name)

   def get_instrument(self):
      return "drums"

   def play_solo(self):
    return "rattle boom crash"





    


        

    