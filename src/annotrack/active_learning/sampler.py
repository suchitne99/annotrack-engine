import math
from typing import List, Optional
from pydantic import BaseModel, Field

class UnlabeledSample(BaseModel):
    sample_id: str
    text: str
    probabilities: Optional[List[float]] = None
    predicted_probabilities: Optional[List[float]] = None

    def model_post_init(self, __context):
        if self.probabilities is None and self.predicted_probabilities is not None:
            self.probabilities = self.predicted_probabilities
        elif self.probabilities is not None and self.predicted_probabilities is None:
            self.predicted_probabilities = self.probabilities

class ActiveLearningSampler:
    @staticmethod
    def entropy_score(probs: List[float]) -> float:
        return -sum(p * math.log2(p) for p in probs if p > 1e-7)

    def select_uncertain_samples(self, samples: List[UnlabeledSample], strategy: str = "entropy", top_k: int = 1) -> List[UnlabeledSample]:
        if strategy == "entropy":
            scored = sorted(samples, key=lambda s: self.entropy_score(s.probabilities or [0.5, 0.5]), reverse=True)
            return scored[:top_k]
        return samples[:top_k]
