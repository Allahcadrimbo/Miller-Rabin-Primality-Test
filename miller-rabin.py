from random import randrange

'''
1. Find n - 1 = 2^k * m
2. Choose a: 1 <
'''


def miller_rabin(n, w, witnesses):
    # If n is even then it is composite
    if n % 2 == 0:
        return False

    k = 0
    q = n - 1
    while q % 2 == 0:  # If s mod 2 is not equal to 3 that means there is going to be a remainder. This means the next value of k in 2^k would result in not an int so we stop here
        q //= 2  # We do floor division be cause we only want integers
        k += 1

    assert n - 1 == 2 ** k * q  # Step 2

    print("k: " + str(k) + " q: " + str(q))

    for i in range(w):
        a = randrange(2, n - 1)
        print("a: " + str(a))
        rule_1 = pow(a, q, n)
        print("rule 1: " + str(rule_1))
        if rule_1 == 1 or rule_1 == n - 1:
            witnesses.append(a)
            continue

        for j in range(k):
            rule_2 = pow(rule_1, 2, n)
            print("rule 2: " + str(rule_2))

            if rule_2 == 1:
                print(str(a))
                witnesses.append(a)
                return False
                # composite
            elif rule_2 == n - 1:
                witnesses.append(a)
                # probs prime

    return True

    # choose a where 1 < a < n - 2
    # if 2**s mod n is congruent to 1 or -1 might be prime so go check next value
    # if failed above check 2**s*2 if +1 its composite if -1 porbs prime
    # list of witnesses and value of composite proof


if __name__ == '__main__':
    while True:
        num = int(input("Enter a number to be tested for primality: "))
        num_witnesses = int(input("Enter the number of witnesses you want to test for: "))
        witnessesList = list()
        # Find n -1 = 2^k * q
        if miller_rabin(num, num_witnesses, witnessesList):
            print("The number " + str(num) + " is probably prime. Here are its "
                  + str(num_witnesses) + " non-witnesses: " + str(witnessesList[:]))
        else:
            print("The number " + str(num) + " is composite here is its witness of compossitness: "
                  + str(witnessesList[-1:]))
