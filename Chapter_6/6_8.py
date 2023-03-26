def main():

    pet_1 = {'type' : 'dog', 'owner' : 'thomas'}
    pet_2 = {'type' : 'cat', 'owner' : 'everly'}
    pet_3 = {'type' : 'guppy', 'owner' : 'tanya'}

    Pets = [pet_1, pet_2, pet_3]
    pet_count = 0

    for pet in Pets:
        pet_len = len(pet_1)
        pet_count += 1
        dict_set = 0
        print('\n')
        print(f"Pet {pet_count}")
        for _ in range(17):
            print("_", end = "")
        print("")
        for _ in range(17):
            print(" ", end = "")
        print("|")
        for animal, identity in pet.items():
            pet_len -= 1
            dict_set += 2
            print(f"{animal.title()}:\t{identity.title()}\t |")
            if pet_len > 1:
                for _ in range(17):
                    print(" ", end = "")
                print("|")
                for _ in range(17):
                    print("_", end = "")
                print("|")  
            if pet_len > 0:
                for _ in range(17):
                    print(" ", end = "")
                print("|")
        for _ in range(17):
            print("_", end = "")
        print("|")

    print("")


main()