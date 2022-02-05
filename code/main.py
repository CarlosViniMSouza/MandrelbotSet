def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n - 1, c) ** 2 + c


print(z(2, 4))
# Output: 20

for n in range(10):
    print(f"z({n}) = {z(n, c=1)}")

"""
Output:

z(0) = 0
z(1) = 1
z(2) = 2
z(3) = 5
z(4) = 26
z(5) = 677
z(6) = 458330
z(7) = 210066388901
z(8) = 44127887745906175987802
z(9) = 1947270476915296449559703445493848930452791205
"""


def sequence(c):
    z = 0
    while True:
        yield z
        z = z ** 2 + c


for n, z in enumerate(sequence(c=1)):
    print(f"z({n}) = {z}")
    if n >= 9:
        break

"""
Output:

z(0) = 0
z(1) = 1
z(2) = 2
z(3) = 5
z(4) = 26
z(5) = 677
z(6) = 458330
z(7) = 210066388901
z(8) = 44127887745906175987802
z(9) = 1947270476915296449559703445493848930452791205
"""
