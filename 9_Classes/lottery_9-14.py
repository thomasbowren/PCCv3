from random import choice

def main():
    winning_ticket = generate_lotto()
    print(f"Any ticket with characters {winning_ticket} is a lottery winner!")

def generate_lotto():
    winning_ticket = []
    lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'F']
    for _ in range(int(4)):
        winning_ticket.append(choice(lottery))
    return winning_ticket

if __name__ == "__main__":
    main()
