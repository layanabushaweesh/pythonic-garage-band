from abc import abstractmethod


# class to make our data type for band
class Band:
    all_band=[]

    def __init__(self,name,member):
       self.name=name
       self.member=member
       Band.all_band.append({'name':name , 'member':member})

    def __str__(self):
        # pass
       return(f"My name is  {self.name} and I {self.member}" )

    def __repr__(self):

       return f"Band instance. name={self.name} , member={self.member}"

    def play_solos(self):
        # arr=[]
        # return[member.play_solos()]

    