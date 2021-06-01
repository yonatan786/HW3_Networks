# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def simulation(T, l, Plist,u):
    number_of_packets = 0
    x = 0
    y = 0
    for i in range(0, T + 1):
        y_t,x_t = getIntoTheBuff(l, Plist, number_of_packets)
        x += x_t
        y += y_t
        number_of_packets -= u

# go over all the packets, and check if there is an error
def getIntoTheBuff(l, plist, number_of_packets):
    count_adding_to_buff = 0
    for i in range(0, l):
        if number_of_packets + count_adding_to_buff >= len(plist):
            return l - count_adding_to_buff, count_adding_to_buff
        if checkWithProbability(plist[count_adding_to_buff + number_of_packets]):
            count_adding_to_buff += 1
    return l - count_adding_to_buff, count_adding_to_buff

# return true with a probability of x
def checkWithProbability(x):
    x = numpy.random.choice(numpy.arange(1, 2), p=[x, 1 - x])
    return x == 0
