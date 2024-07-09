#euclidean algorithm. Values will loop through the else statment until a=0. g, x, and y will then be passed through the return function of the else statment the same amount of times it was looped through the if statement.
#once the return looping is complete the g, x, y values are passed back to the extended_gcd call in the mod_inverse function.
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(e, phi_n):
#pass e and phi_n to euclidean algorithm
    g, x, y = extended_gcd(e, phi_n)
#Extended portion of euclidean algorithm. Checking for modular inverse.
    if g != 1:
        raise Exception('Modular inverse does not exist')
#if inverse exists, return x mod phi_n to the mod_inverse call statement
    else:
        return x % phi_n
#Define known values.
e = 
p = 
q = 
phi_n = (p-1)*(q-1)


d = mod_inverse(e, phi_n)
print(d)
