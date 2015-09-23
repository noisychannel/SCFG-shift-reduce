#!/usr/bin/env python

# U and L store the left and the right most index of source side
# spans that are aligned to phrases on the target side
U = set()
L = set()


def drawAlignmentMatrix(A, E, F):
    """
    Produces an alignment matrix based on the alignment data
    """
    for f in reversed(F):
        output = ""
        for e in E:
            output += "* " if (e, f) in A else ". "
        print output.strip()


def minF():
    """
    For a target side phrase [x,y], this returns the index of
    the left most word on the source side which is aligned to any
    word in [x,y]
    """
    pass


def maxF():
    """
    For a target side phrase [x,y], this returns the index of
    the right most word on the source side which is aligned to any
    word in [x,y]
    """
    pass


def countEmissions(A, E, F):
    """
    Counts the number of links emitted by each prefix of the source
    and the target
    Pre-computes these in O(n + m + |A|) time
    """
    F_c = {x: 0 for x in range(1, len(F) + 1)}
    E_c = {x: 0 for x in range(1, len(E) + 1)}
    for (i, j) in A:
        E_c[i] += 1
        F_c[j] += 1
    count = 0
    for j in range(1, len(F) + 1):
        tmpCount = count
        count += F_c[j]
        F_c[j] += tmpCount
    count = 0
    for i in range(1, len(E) + 1):
        tmpCount = count
        count += E_c[i]
        E_c[i] += tmpCount

    return F_c, E_c


A = {(1, 6), (2, 5), (2, 7), (3, 4), (4, 1), (4, 3), (5, 2), (6, 1), (6, 3)}
E = list(range(1, 7))
F = list(range(1, 8))

F_c, E_c = countEmissions(A, E, F)
U_cache = {(x, x): 0 for x in range(1, len(E) + 1)}
L_cache = {(x, x): 1e10 for x in range(1, len(E) + 1)}
for (i, j) in A:
    U_cache[(i, i)] = max(U_cache[(i, i)], j)
    L_cache[(i, i)] = min(L_cache[(i, i)], j)

print F_c
print E_c
print U_cache
print L_cache

X = [1]
for y in range(2, len(E) + 1):
    X.append(y)
    for x in reversed(X):
        u = max(U_cache[(x, x)], U_cache[(x + 1, y)]) if x <= y \
            else U_cache[(x, x)]
        l = min(L_cache[(x, x)], L_cache[(x + 1, y)]) if x <= y \
            else L_cache[(x, x)]
        U_cache[(x, y)] = u
        L_cache[(x, y)] = l
        if (F_c[u] - F_c[l - 1] - (E_c[y] - E_c[x - 1])) == 0:
            print (x, y)

drawAlignmentMatrix(A, E, F)
print countEmissions(A, E, F)
