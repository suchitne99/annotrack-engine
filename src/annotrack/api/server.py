from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from annotrack.metrics.agreement import cohens_kappa
from annotrack.active_learning.sampler import ActiveLearningSampler, UnlabeledSample
from annotrack.curation.minhash import MinHashDeduplicator

app = FastAPI(title="Annotrack Engine API", version="1.2.0")
sampler = ActiveLearningSampler()
dedup = MinHashDeduplicator()

class AgreementRequest(BaseModel):
    rater_a: List[str]
    rater_b: List[str]

class SampleInput(BaseModel):
    sample_id: str
    text: str
    probabilities: List[float]

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "annotrack-engine", "version": "1.2.0"}

@app.post("/metrics/cohens-kappa")
def calculate_kappa(req: AgreementRequest):
    if len(req.rater_a) != len(req.rater_b):
        raise HTTPException(status_code=400, detail="Rater lists must be of identical length.")
    score = cohens_kappa(req.rater_a, req.rater_b)
    return {"cohens_kappa": score, "total_samples": len(req.rater_a)}

@app.post("/active-learning/sample")
def select_samples(samples: List[SampleInput], top_k: int = 5):
    inputs = [UnlabeledSample(sample_id=s.sample_id, text=s.text, predicted_probabilities=s.probabilities) for s in samples]
    selected = sampler.select_uncertain_samples(inputs, strategy="entropy", top_k=top_k)
    return {"selected_samples": [s.sample_id for s in selected], "strategy": "entropy"}

# Request logging middleware

# OpenAPI tag grouping

# Arrow format export

# Batch task submission

# FastAPI serialization optimization
# FastAPI server

# Logging handlers

# Serialization

# Arrow format
