from random import choice

class Ticket:
    """Creates the ticket class for playing the lottery."""
    def __init__(self, my_ticket, winning_ticket):
        """Initializes lottery ticket attributes and instantiates ticket-object."""
        self.my_ticket = my_ticket
        self.winning_ticket = winning_ticket
        self.count = 1

    def lottery_analysis(self):
        """Compares lottery numbers selected by player to winning ticket numbers and displays the numbers of plays attempted before winning."""
        winner = False
        while winner == False:
            if self.my_ticket == self.winning_ticket:
                print(f"Congratulations! After {self.count} attempts your ticket is a lottery winner!")
                winner = True
            else:
                self.count += 1
                #print(f"Lottery ticket -  {self.count}")
                self.winning_ticket = generate_lotto()

def main():
    my_ticket = [1, 'A', 4, 'C']
    winning_ticket = generate_lotto()
    my_lottery = Ticket(my_ticket, winning_ticket)
    my_lottery.lottery_analysis()

def generate_lotto():
    """Generates the winning lottery ticket values."""
    winning_ticket = []
    lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'F']
    for _ in range(int(4)):
        winning_ticket.append(choice(lottery))
    return winning_ticket

if __name__ == "__main__":
    main()
