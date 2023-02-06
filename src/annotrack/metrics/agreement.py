from typing import List

def cohens_kappa(r1: List[str], r2: List[str]) -> float:
    if len(r1) != len(r2) or len(r1) == 0: return 1.0
    cats = list(set(r1).union(set(r2)))
    n = len(r1)
    po = sum(1 for a, b in zip(r1, r2) if a == b) / n
    pe = sum((sum(1 for a in r1 if a == c)/n) * (sum(1 for b in r2 if b == c)/n) for c in cats)
    return float((po - pe) / (1.0 - pe)) if pe != 1.0 else 1.0

# Krippendorff

# Contingency table
