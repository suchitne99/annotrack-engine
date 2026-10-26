from typing import List

def cohens_kappa(r1: List[str], r2: List[str]) -> float:
    if len(r1) != len(r2) or len(r1) == 0:
        return 1.0
    cats = list(set(r1).union(set(r2)))
    n = len(r1)
    po = sum(1 for a, b in zip(r1, r2) if a == b) / n
    pe = sum((sum(1 for a in r1 if a == c) / n) * (sum(1 for b in r2 if b == c) / n) for c in cats)
    return float((po - pe) / (1.0 - pe)) if pe != 1.0 else 1.0

def fleiss_kappa(matrix: List[List[int]]) -> float:
    n_subjects = len(matrix)
    if n_subjects == 0:
        return 1.0
    n_categories = len(matrix[0])
    n_raters = sum(matrix[0])
    if n_raters <= 1:
        return 1.0
    
    p_j = [sum(matrix[i][j] for i in range(n_subjects)) / (n_subjects * n_raters) for j in range(n_categories)]
    p_e = sum(p**2 for p in p_j)
    p_i = [(sum(matrix[i][j]**2 for j in range(n_categories)) - n_raters) / (n_raters * (n_raters - 1)) for i in range(n_subjects)]
    p_bar = sum(p_i) / n_subjects
    
    if p_e == 1.0:
        return 1.0
    return float((p_bar - p_e) / (1.0 - p_e))
