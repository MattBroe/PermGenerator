#PermGenerator.py
#Author: Matt Broe
#August 2016
#All code is original. I came up with the algorithm independently, though
#it's probably been used before.

#The idea behind it is placing an order on the permutations of a given string.
#For example, if the string s is "1234567", and p, q are two permutations, then
#we say that p > q if when you reorder the letters of s according to p, the resulting
#string of digits represents a greater number than the string of digits you get
#by reordering the letters according to q. You can apply the same ordering to
#permutations of any string of seven letters, simply by letting 1 correspond to
#the first letter of the string, 2 correspond to the second letter, and so on,
#and associating each permutation of s with the same permutation applied to the
#corresponding string of digits. This generalizes to strings of any length.

#What the algorithm does is print the full list of permutations of s, one after
#the other, in the order described above. The slightly tricky part is figuring out
#how to generate each permutation's successor in this list, and this is what
#the bulk of the code is doing.

#Note that the runtime is O(n*n!) where n = len(s): this is the best possible
#runtime for a program generating a list of all permutations, I think.

def PermGenerator(s):

    
    reordered = []

    permList = [s]
    #By the time the code finishes, permList contains all permutations of s, in
    #the order described above
    
    order = {}
    

    print(s)
    
    for i in range(len(s)):
        order[i] = s[i]
        reordered += [i]

    #The list reordered contains the numbers that correspond to the letters of s.
    #We permute the elements of reordered directly, then use the correspondence
    #to induce a permutation on the letters of s. The dict order encodes this
    #correspondence, using numbers as keys and characters of s as values.
        
    while True:
        i = len(s) - 1

        #Iterate from right to left over the list reordered, stopping once you
        #find an element that is less than its preceding element

        while i > 0 and reordered[i - 1] > reordered[i]:
            i -= 1
        
        if i == 0:
            #This only occurs when the elements of reordered are in decreasing
            #order, i. e. we have reached the final permutation
            
            break
        firstDecrease = i - 1
        
        i = len(s) - 1

        while reordered[i] < reordered[firstDecrease]:
            i -= 1

        #First, swap reordered[firstDecrease] with the rightmost element of
        #reordered that exceeds it. Then, reverse the sublist of reordered that
        #lies to the right of the index firstDecrease. This is how you generate
        #the successor permutation.
        
        reordered[firstDecrease], reordered[i] = reordered[i], reordered[firstDecrease]
        reordered[firstDecrease + 1:len(s)] = reordered[len(s) - 1: firstDecrease: -1]

        permutedLetters = []

        #Use the correspondence between chars and numbers to induce the permutation
        #on the chars of s
        
        for j in range(len(s)):
            permutedLetters += [str(order[reordered[j]])]

        permList += ["".join(permutedLetters)]
        print("".join(permutedLetters))

    return permList
        
        
