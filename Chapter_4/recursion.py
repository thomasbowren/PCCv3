def recursion(n):
    if n > 0:
        print('Hello World')
        return recursion(n - 1)
    else:
        return 0

def main():

    n = int(input('Pick a number: '))

    recursion(n)

main()
