from math import sqrt

def is_py_triple(a,b,c):
    """
    Function that checks whether a set of three numbers is a pythagorean triplet.

    Parameters
        a: length of one side of triangle
        b: length of other side of triangle
        c: length of hypotenuse

    Returns
        True if a,b,c is pythagorean triplet
        False if a,b,c is not pythagorean triplet
    """
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    
a = 3
b = 4
c = sqrt(a**2 + b**2)

found_answer = False

for a in range(3,1000):
    for b in range(4,1000):
        c = sqrt(a**2 + b**2)
        if a + b + c == 1000 and is_py_triple(a,b,c):
            found_answer = True
            break
    if found_answer:
        break

print(a * b * c)