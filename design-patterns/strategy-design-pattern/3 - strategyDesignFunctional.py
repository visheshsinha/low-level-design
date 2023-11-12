# Functional Programming Approach to Strategy Design Pattern instead of Class based Abstraction

import random, string
from typing import List
from abc import ABC, abstractmethod

class SupportTicket:
    def __init__(self, customer, issue) -> None:
        self.customer = customer
        self.issue = issue
        self._id = generateId()


def FIFOCreateOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    return list.copy()

def FILOCreateOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    listCopy = list.copy()
    listCopy.reverse()
    return listCopy

def RandomCreateOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    listCopy = list.copy() 
    random.shuffle(listCopy)
    return listCopy


class CustomerSupport:
    def __init__(self, processingStrategyFunction) -> None:
        self.tickets = []
        self.processingStrategyFunction = processingStrategyFunction
    
    def createTickets(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))
    
    def processTickets(self):
        ticketsList = self.processingStrategyFunction(self.tickets)

        if len(ticketsList) == 0:
            print("There are no tickets to process!")
            return

        for ticket in ticketsList:
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
    strategy = FILOCreateOrdering
    app = CustomerSupport(strategy)

    app.createTickets("John Smith", "My computer makes strange sounds!")
    app.createTickets("Linus Sebastian", "I can't upload any videos, please help.")
    app.createTickets("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    app.processTickets()