'''
pertains to a minecraft mod, forestry
A little experiment to help determine the equation for the number of traits that the offspringwill
retain from parent a after breeding with genotype b after g generations divided by the total number of genes analyzed

pro tip: turns out to be p^g, n is not 
Another fact: the percentage of specimens perfectly preserving a's genotype will be p^(gn)
'''

import random

#test parameters
p = 0.5    #probability of a gene switching when list a breeds with list b
n = 3      #number of different genes per each parent
g = 2      #number of generations the test is run for
t = 100000 #number of iterations to run the test

#run a single iteration of the test
def runTest(t, a, b):
    for i in range(t):
        for j in range(n):
            res = random.randint(0, 99) #p resolution 10^-2, not worth making variable
            if(res < p * 100):
                a[j] = b[j]

#finds the number of elements in list l that match key k
#modifies the list operated on
def findMatches(l, k):
    original = len(l)
    while k in l:
        l.remove(k)
    
    return original - len(l)

#find the average value of a list of numeric values
def avg(l):
    a = 0.0
    for x in l:
        a = a + x
    return a / len(l)

#main loop for running t tests
def __main__():
    scores = []
    perfect = 0.0
    for x in range(t):
        a = []
        b = []

        #populate lists with genes, 'a's represents the original genotype of parent a, 'b' for parent b
        for i in range(n):
            a.append('a')
            b.append('b')
        
        #run a single iteration and record the fraction of 'a' genes remaining
        runTest(g, a, b)
        matches = findMatches(a, 'a')
        if matches == n:
            perfect = perfect + 1
        scores.append(matches / (0.0 + n))

    print('avg \'a\' remaining after ' + str(g) + ' gens: ' + str(100 * avg(scores)) + "%")
    print(str(p) + "^" + str(g) + ": " + str(p ** g * 100) + "%")
    print("specimens with perfect 'a' genotype: " + str(100 * perfect / t) + "%")
    print(str(p) + "^(" + str(g) + "*" + str(n) + "): " + str(p ** (g * n) * 100) + "%")

if __name__ == '__main__':
    __main__()



