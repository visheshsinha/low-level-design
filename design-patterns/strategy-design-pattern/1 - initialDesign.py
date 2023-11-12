"""
Problem Statement - When few of the child classes have similar custom code which the parent class didn't have, we will have code duplicacy. 
For this we use the Strategy Design Pattern 
"""

import random, string

class SupportTicket:
    def __init__(self, customer, issue) -> None:
        self.customer = customer
        self.issue = issue
        self._id = generateId()

class CustomerSupport:
    def __init__(self, processingStrategy: str = 'FIFO') -> None:
        self.tickets = []
        self.processingStrategy = processingStrategy
    
    def createTickets(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))
    
    def processTickets(self):
        if len(self.tickets) == 0:
            print('No tickets available to be processed')
            return
        
        if self.processingStrategy == "fifo":
            for ticket in self.tickets:
                self.processingTicket(ticket)
        elif self.processingStrategy == "filo":
            for ticket in reversed(self.tickets):
                self.processingTicket(ticket)
        elif self.processingStrategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.processingTicket(ticket)

    def processingTicket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket._id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")

def generateId(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


if __name__ == '__main__':
    app = CustomerSupport("random")

    app.createTickets("John Smith", "My computer makes strange sounds!")
    app.createTickets("Linus Sebastian", "I can't upload any videos, please help.")
    app.createTickets("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    app.processTickets()