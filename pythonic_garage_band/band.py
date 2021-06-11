
from abc import abstractmethod
from typing import Counter
# abstractmethod mehod use to force the dev to defin method in sub class and we but it in base class as pass


# class to make our data type for band

class Band:

   all_band=[]
   count  =0
   def __init__(self,name,list):

      self.name=name
      self.member=list
      self.__class__.count += 1
      Band.all_band.append(self.__class__)

   def play_solos(self):
      #it will loop in array and append each item to new list that i crate
      # pass

      solo_list = []

      for mempers in self.member:

       solo_list.append(mempers.play_solos())

      return solo_list


   def __str__(self):
        # pass
      return(f"My name is  {self.name} and I {self.member}" )

   def __repr__(self):

      return f"Band instance. name={self.name} , member={self.member}"

   @classmethod
# class method to do somthing for the base class and hereh it is for return a list that previously created

   def to_list(cls):

      return cls.all_band


class Musician:

   def __init__(self,name):
    self.name=name


   def __str__(self):

      return f"My name is {self.name} and I play {self.get_instrument()}"
   
   def __repr__(self):

      # Bassist instance. Name = Meshell Ndegeocello => return as this sample Bassist the name of class it self

      return f"{self.__class__.__name__} instance. Name = {self.name}"

   @abstractmethod
   def get_instrument(self):
     pass

   @abstractmethod
   def play_solos(self):
      pass


#Guitarist,Bassist, and Drummer are inheritance from Musician class:

class Guitarist(Musician):

   def __init__(self,name):
      super().__init__(name)

   def get_instrument(self):
      return "guitar"

   def play_solos(self):
    return "face melting guitar solo"


class Bassist(Musician):

   def __init__(self,name):
      super().__init__(name)

   def get_instrument(self):
      return "bass"

   def play_solos(self):
    return "bom bom buh bom"

class Drummer(Musician):

   def __init__(self,name):
      super().__init__(name)

   def get_instrument(self):
      return "drums"

   def play_solos(self):
    return "rattle boom crash"





    


        

    