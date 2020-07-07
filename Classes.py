class Flight:
    def __init__(self,capacity):
        self.capacity = capacity
        self.persons = {}
    
    def check_avilable(self):
        if self.capacity > len(self.persons):
            return True
        return False

    def add_persons(self,name,address):
        if self.check_avilable() == False:
            print("Sorry, no avilable seets")
        else:
            self.persons[name] = address
            print("Congrats!!")


flight = Flight(3)

name= input("Enter your name: ")
address = input("Enter your address: ")

flight.add_persons(name,address)
