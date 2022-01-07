class ParkingGarage():

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "I9", "J10"]
        self.parkingSpaces = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "I9", "J10"]
        self.currentTicket = {
                            "False": "A1",
                            "False": "B2", 
                            "False": "C3", 
                            "False": "D4", 
                            "False": "E5", 
                            "False": "F6", 
                            "False": "G7", 
                            "False": "H8", 
                            "False": "I9", 
                            "False": "J10"
                            }

        
    #Take ticket should decrease amount of ticket and spaces by 1

    def takeTicket(self, tickets, parkingSpaces):
        print("Welcome to our parking garage! Please take a ticket and the corresponding space.")
        for tickets in self.tickets:
            self.tickets.remove(tickets)
        for parkingSpaces in self.parkingSpaces:
            self.parkingSpaces.remove(parkingSpaces)
    
    def payForParking(self):
        hours = input("How many hours were you parked? ")
        if int(hours) > 0:
            cost = int(hours) * 2
            print(f"Your ticket cost $", cost)
            response = input("Please type 'yes' to pay! " )
            if response.lower() == 'yes':
                print("Your ticket has been paid, you have 15 minutes to leave the garage")
                self.currentTicket["True"] = self.currentTicket.pop("False")
            elif response.lower() == 'no':
                noResponse = input("You may not leave the garage until your fine is paid. Please type 'yes' to pay!")
                if noResponse.lower() == 'yes':
                    print("Your ticket has been paid, you have 15 minutes to leave the garage")
                    self.currentTicket["True"] = self.currentTicket.pop("False")
                elif noResponse == 'no':
                    print("Too bad. You must pay your fine. You are now an employee! See you tomorrow at 8am!")
                    self.currentTicket["True"] = self.currentTicket.pop("False")
            else:
                print("Please enter a proper command.")
        else:
            print("We're sorry you've chosen not to park with us. Have a nice day!")
    
    def leaveGarage(self):
        if self.currentTicket:
            print("Thank you, have a nice day!")
        else:
            hours = input(int("How many hours were you parked? "))
            hourlyCost = 2
            if hours > 0:
                cost = int(hours) * hourlyCost
                print("Your ticket costs", cost)
                response = input("Please type 'yes' to pay! ")
                if response.lower() == 'yes':
                    print("Your ticket has been paid, you have 15 minutes to leave the garage")
                    self.currentTicket["True"] = self.currentTicket.pop("False")
                else:
                    print("Please enter a proper command.")
            else:
                print("Please enter a proper command.")
        for tickets in self.tickets:
            self.tickets.append(tickets)
        for parkingSpaces in self.parkingSpaces:
            self.parkingSpaces.append(parkingSpaces)

hertz = ParkingGarage([], [], {})

def run():
    while True:
        ticketResponse = input("Will you be parking today? Type 'yes' or 'no'. " )
        if ticketResponse.lower() == "yes":
            hertz.takeTicket([], [])
            while True:
                payResponse = input("Are you ready to pay your fine and leave? Type 'yes' or 'no'. ")
                if payResponse.lower() == "yes":
                    hertz.payForParking()
                    while True:
                        leaveResponse = input("Are you ready to leave? Type 'yes' or 'no'.")
                        if leaveResponse.lower() == "yes":
                            hertz.leaveGarage()
                            break
                        elif leaveResponse.lower() == "no":
                            print("Stay as long as you like, just keep track of your time!")
                            hertz.payForParking()
                        else:
                            print("Please enter a proper command.")
                elif payResponse.lower() == "no":
                    print("Stay as long as you like, just keep track of your time!")
                    hertz.payForParking
                else:
                    print("Please enter a proper command.")
        elif ticketResponse.lower() == "no":
            print("We're sorry you won't be parking with us! Have a nice day!")
            break
        else:
            print("Please enter a proper command.")

run()