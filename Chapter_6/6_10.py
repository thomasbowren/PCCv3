def main():

    Favorite_Numbers = {
        'Harry' : [0],
        'Ron' : [1, 2, 4, 8, 16, 32, 64, 128,], 
        'Hermoine' : [256, 512, 1024, 2048, 4096, 8192, 16384, 32764,],}
    
    for friend in Favorite_Numbers.keys():
        print('\n')
        print(f"{friend}'s favorite numbers are:")
        count = len(Favorite_Numbers[friend])
        for numbers in Favorite_Numbers[friend]:
                print(f"{numbers}", end = "")
                count -= 1
                if count > 0:
                    print(f", ", end = "")

            

main()