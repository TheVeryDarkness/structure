from math import sqrt, pi
def _λ(λ, fy, E):
    return λ / pi * sqrt(fy / E)
def φ(_λ, fy, ε0):
    tmp = 1 + (1 + ε0) / _λ ** 2
    return (tmp - sqrt(tmp ** 2 - 4 / _λ ** 2)) / 2