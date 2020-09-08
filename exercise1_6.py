def cube(number):
    return (number*number*number)

def by_Three (number):
    if ((number % 3) == 0):
        return cube(number)
    else:
        return 'false'

#print(by_Three(3))