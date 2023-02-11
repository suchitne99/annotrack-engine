import math
from typing import List
from pydantic import BaseModel

class UnlabeledSample(BaseModel):
    sample_id: str
    text: str
    probabilities: List[float]

class ActiveLearningSampler:
    @staticmethod
    def entropy_score(probs: List[float]) -> float:
        return -sum(p * math.log2(p) for p in probs if p > 1e-7)

# K-means

# Vectorized entropy
