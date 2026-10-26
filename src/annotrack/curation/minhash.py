from typing import List, Set, Tuple

class MinHashDeduplicator:
    def __init__(self, num_perm: int = 64, threshold: float = 0.85):
        self.num_perm = num_perm
        self.threshold = threshold

    def find_duplicates(self, texts: List[str]) -> List[Tuple[int, int]]:
        def get_shingles(text: str) -> Set[str]:
            words = text.lower().split()
            return set(words)

        shingles = [get_shingles(t) for t in texts]
        duplicates = []
        for i in range(len(texts)):
            for j in range(i + 1, len(texts)):
                s1, s2 = shingles[i], shingles[j]
                union_len = len(s1.union(s2))
                if union_len == 0:
                    continue
                jaccard = len(s1.intersection(s2)) / union_len
                if jaccard >= self.threshold:
                    duplicates.append((i, j))
        return duplicates
