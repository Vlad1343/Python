
## A Naive recursive Python program to find minimum number
## of operations to convert s1 to s2.


def editDistRec(s1, s2, m, n):
    if m == 0:
        return n

    if n == 0:
        return m
    
    if s1[m - 1] == s2[n - 1]:
        return editDistRec(s1, s2, m - 1, n - 1)

    return 1 + min(editDistRec(s1, s2, m, n - 1),
                   editDistRec(s1, s2, m - 1, n),
                   editDistRec(s1, s2, m - 1, n - 1))

def editDistance(s1, s2):
    return editDistRec(s1, s2, len(s1), len(s2))


if __name__ == "__main__":
    s1 = "vlad"
    s2 = "cold"

    print(editDistance(s1, s2))