from random import choice

class Ticket:
    def __init__(self, my_ticket, winning_ticket):
        self.my_ticket = my_ticket
        self.winning_ticket = winning_ticket
        self.count = 1
    
    def lottery_analysis(self):
        if self.winning_ticket == self.my_ticket:

        else:
            self.count += 1
            self.winning_ticket = generate_lotto()
            return self.lottery_analysis()

def main():
    winner = False
    my_ticket = [1, 'A', 4, 'C']
    winning_ticket = generate_lotto()
    my_lottery = Ticket(my_ticket, winning_ticket)
    while winner == False:
        if my_lottery.my_ticket == my_lottery.winning_ticket:
            print(f"Congratulations! After {self.count} attempts your ticket is a lottery winner!")
            print(f"Congratulations! After {my_lottery.count} attempts your ticket is a lottery winner!")
            winner = True
        else:
            my_lottery.count += 1
            my_lottery.winning_ticket = generate_lotto()

def generate_lotto():
    winning_ticket = []
    lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'F']
    for _ in range(int(4)):
        winning_ticket.append(choice(lottery))
    return winning_ticket

if __name__ == "__main__":
    main()
