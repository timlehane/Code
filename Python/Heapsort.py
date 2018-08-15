""" Heapsort and randomised testing

"""

import random #for generating random lists for tests, and for quicksort
import copy #to generate copies, so that we don't sort a previously sorted list
import time #for evaluating the runtime of the methods


""" Heapsort a list, in place. """
def heapsort(inlist):

    #first treat the inlist as the input stream to build a *max* priority queue
    #maintain the PQ in the same list, gradually growing from the front.
    #that means each item to be added will already be in the starting point
    #   bubbling up the heap
    #Once the PQ is complete, we need to reverse it.
    #Gradually shring the PQ by removing the *max* item, and place it in the
    #   cell at the end of the PQ just vacated

    length = len(inlist)
    for i in range(length):
        #print('add', inlist[i], 'to the virtual heap')
        bubbleup(inlist,i)
    for i in range(length):
        #elt to be moved up is in position len(list)-1 - i
        #max elt being shifted is in position 0, and is going to len(list)-1-i
        #so start by swapping them, and then bubbling down the new elt in pos 0
        #print('shifting', inlist[0], 'to cell', (length-1-i))
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist,0, length-2-i)

""" Bubble up an item in pos i in a max heap. """
def bubbleup(inlist, i):
    while i > 0:
        parent = (i-1) // 2
        if inlist[i] > inlist[parent]:
            #print('swapping:', inlist[i], 'with its parent:', inlist[parent])
            inlist[i], inlist[parent] = inlist[parent], inlist[i]
            i = parent
        else:
            i = 0

""" Bubble down an item in pos i in a max heap. """
def bubbledown(inlist, i, last):
    while last > (i*2):  #so at least one child
        lc = i*2 + 1
        rc = i*2 + 2
        maxc = lc   #start by assuming left child is the max child
        if last > lc and inlist[rc] > inlist[lc]:  #rc exists and is bigger
            maxc = rc
        if inlist[i] < inlist[maxc]:
            #print('swapping:', inlist[i], 'with its child:', inlist[maxc])
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last

""" Test heapsort on an input list. """
def test(inlist):
    start_time = time.perf_counter()
    heapsort(inlist)
    end_time = time.perf_counter()
    res = sortingerrorcheck(inlist, heapsort)
    if res == -1:
        return res
    return (end_time - start_time)

""" Test heapsort on a randomised list of the first n integers. """
def testrandom(n):
    testlist = [i for i in range(n)]
    random.shuffle(testlist)
    return test(testlist)

""" Test heapsort on a set of randomised lists.

    n is the size of the list (which contains the first n integers).
    number is the number of lists in the set.
    The function returns the mean runtime.
"""
def testaverage(n, number):
    sum = 0;
    for i in range(number):
        sum += testrandom(n)
    print(sum/number, ":", n, number)

""" Check that a sorted list is actually sorted.

    testlist is the list being checked
    f is the function that tried to sort it.
    Return 0 if no errors; -1 if there is an error (and prints a message)
"""
def sortingerrorcheck(testlist, f):
    errors = False
    firsterror = -1
    i = 0
    end  = len(testlist)-1
    while i < end and errors == False:
        if testlist[i] > testlist[i+1]:
            errors = True
            firsterror = i
        i += 1
    if errors:
        print('    ERROR: first position:', firsterror, 'with value',
              testlist[firsterror],
              'followed by', testlist[firsterror+1])
        print('using algorith:', f.__name__)
        print(testlist)
        return -1
    else:
        return 0
