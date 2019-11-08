"""
Author: Grant
Date: 11/7/19

Algorithm:
    - Retrieve two user inputs
        - n: An integer to be tested for primality
        - w: The number of witnesses to check for the compositness of num
    - Perform Miller-Rabin Test
        - Find n - 1 = 2^k * q with q odd
            - q := (n-1)/2^k
        - Choose an integer a where 1 < a < n - 2 and repeat this w times over
             - If n is prime and gcd(a, n) = 1 then one of the following rules holds:
                - rule 1: a^q (mod n) = 1 or -1
                - rule 2: (a^(2^i)*q) = -1 for some 0 <= i <= k - 1
             - Compute rule_1  = a^q mod n
                - If rule_1 is equal to 1 or n-1
                    - This value is a non-witness for the compositeness of n
                    - Add the value a to our witness list
                    - continue to the next value of a
                - Else compute rule_2 and do this k - 1 times over
                    - rule_2 = rule_1^2 mod n
                        - If rule_2 == 1
                            - This value a is a witness for the compositeness of n
                            - return False as we know n is composite
                        - If rule_2 == n-1
                            - This value a is a non-witness for the compositeness of n
        - Return True, none of the w a values were witnesses
        - If n was probably prime print the entire list (non witnesses)
        - If n was composite print the last element in the list, which is a witness for compositness
"""
from random import randrange


# Tests for the primality of the inputted number n using the Miller-Rabin test.
# @:param n The integer being tested
# @:param witnesses The list hold the witnesses/non-witnesses
# @:return True if it is probably prime and False if it is composite"""
def miller_rabin(n, w, witnesses):
    # If n is even then it is composite. No need to continue.
    if n % 2 == 0:
        return False

    k = 0
    q = n - 1
    # Finds the largest value of k that satiates n - 1 = 2^k * q
    while q % 2 == 0:
        q //= 2  # Use the floor division operator to ensure integer division
        k += 1

    assert n - 1 == pow(2, k) * q

    for i in range(w):
        a = randrange(2, n - 1)
        rule_1 = pow(a, q, n)

        # Rule 1 check
        if rule_1 == 1 or rule_1 == n - 1:
            # might be prime
            witnesses.append(a)
            continue

        # Rule 2 check
        for j in range(k):
            rule_2 = pow(rule_1, 2, n)

            if rule_2 == 1:  # n is composite
                witnesses.append(a)
                return False
            elif rule_2 == n - 1:  # might be prime
                witnesses.append(a)

    return True


if __name__ == '__main__':
    while True:
        num = int(input("Enter a number to be tested for primality: "))
        num_witnesses = int(input("Enter the number of witnesses you want to test for: "))

        witnessesList = list()

        if miller_rabin(num, num_witnesses, witnessesList):
            # n is probably prime
            print("The number " + str(num) + " is probably prime. Here are its "
                  + str(num_witnesses) + " non-witnesses: " + str(witnessesList[:]))
        else:
            # n is not prime
            print("The number " + str(num) + " is composite here is its witness of compositeness: "
                  + str(witnessesList[-1:]))
