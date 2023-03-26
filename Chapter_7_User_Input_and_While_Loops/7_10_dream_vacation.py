def main():


    dream_vacations = {}
    keep_asking = True

    while keep_asking:
        traveler = input("\nWhat is your name? ")
        dream_vacation = input("\nIf you could visit one place in the world, where would you go? ")
        another_question = input("\nAre there any other travelers? Enter 'yes' or 'no'. ")
        dream_vacations[traveler] = dream_vacation
        if another_question.lower() == 'no':
            keep_asking = False

    for traveler, dream_vacation in dream_vacations.items():
        print(f"\n{traveler} would like to visit {dream_vacation}. How neat!")

    print('')

if __name__ == "__main__":
    main()
