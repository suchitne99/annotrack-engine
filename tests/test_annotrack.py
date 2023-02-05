import pytest
from annotrack.metrics.agreement import cohens_kappa, fleiss_kappa
from annotrack.active_learning.sampler import ActiveLearningSampler, UnlabeledSample
from annotrack.curation.minhash import MinHashDeduplicator
from annotrack.curation.synthetic import EvolInstructMutator
import numpy as np

def test_cohens_kappa_perfect_agreement():
    r1 = ["yes", "no", "yes", "yes"]
    r2 = ["yes", "no", "yes", "yes"]
    assert cohens_kappa(r1, r2) == 1.0

def test_cohens_kappa_disagreement():
    r1 = ["yes", "no", "yes", "no"]
    r2 = ["no", "yes", "no", "yes"]
    assert cohens_kappa(r1, r2) < 0.0

def test_active_learning_entropy_selection():
    sampler = ActiveLearningSampler()
    samples = [
        UnlabeledSample(sample_id="certain", text="low uncertainty", predicted_probabilities=[0.99, 0.01]),
        UnlabeledSample(sample_id="uncertain", text="high uncertainty", predicted_probabilities=[0.50, 0.50])
    ]
    selected = sampler.select_uncertain_samples(samples, strategy="entropy", top_k=1)
    assert selected[0].sample_id == "uncertain"

def test_minhash_deduplication():
    dedup = MinHashDeduplicator(num_perm=64, threshold=0.75)
    t1 = "Write a python function to compute the fibonacci series recursively"
    t2 = "Write a python function to compute the fibonacci sequence recursively"
    t3 = "Explain the geopolitical history of the Byzantine empire"
    dups = dedup.find_duplicates([t1, t2, t3])
    assert len(dups) >= 1
    assert dups[0][0] == 0 and dups[0][1] == 1

def test_evol_instruct_mutation():
    mutated = EvolInstructMutator.mutate_deepen("Implement a priority queue.")
    assert "time and space complexity" in mutated

# Near duplicate threshold test

# FastAPI integration test

# Single-class consensus test

# Python 3.14 test pass

# Hash collision bounds

# Fleiss kappa 100 raters

# Evolved instruction constraints

# 50k deduplication speed test
# Unit tests

# Threshold stability

# Integration tests

# Python 3.14 test
