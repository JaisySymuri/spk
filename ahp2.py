import ahpy

# -----------------------------
# STEP 1: Criteria (EQUAL WEIGHT)
# -----------------------------
criteria = ahpy.Compare(
    name='Criteria',
    comparisons={
        ('Harga', 'Model'): 1,
        ('Harga', 'Reliability'): 1,
        ('Harga', 'Fuel'): 1,
        ('Model', 'Reliability'): 1,
        ('Model', 'Fuel'): 1,
        ('Reliability', 'Fuel'): 1
    }
)

# -----------------------------
# STEP 2: Pairwise comparisons for each criterion
# (Example values — you can adjust based on your judgment)
# -----------------------------

# HARGA (cheaper is better)
harga = ahpy.Compare('Harga', {
    ('A1', 'A2'): 3,
    ('A1', 'A3'): 1/3,
    ('A1', 'A4'): 5,
    ('A2', 'A3'): 1/5,
    ('A2', 'A4'): 5,
    ('A3', 'A4'): 5
})

# MODEL (subjective)
model = ahpy.Compare('Model', {
    ('A1', 'A2'): 1/3,
    ('A1', 'A3'): 1/5,
    ('A1', 'A4'): 1/3,
    ('A2', 'A3'): 1/3,
    ('A2', 'A4'): 3,
    ('A3', 'A4'): 3
})

# RELIABILITY
reliability = ahpy.Compare('Reliability', {
    ('A1', 'A2'): 1/3,
    ('A1', 'A3'): 1/3,
    ('A1', 'A4'): 1/3,
    ('A2', 'A3'): 1/3,
    ('A2', 'A4'): 3,
    ('A3', 'A4'): 3
})

# FUEL EFFICIENCY
bbm = ahpy.Compare('Fuel', {
    ('A1', 'A2'): 3,
    ('A1', 'A3'): 3,
    ('A1', 'A4'): 3,
    ('A2', 'A3'): 3,
    ('A2', 'A4'): 1/3,
    ('A3', 'A4'): 1/3
})

# -----------------------------
# STEP 3: Build hierarchy
# -----------------------------
criteria.add_children([harga, model, reliability, bbm])

# -----------------------------
# STEP 4: Results
# -----------------------------
print("Final Ranking:")
print(criteria.target_weights)

print("\nConsistency Ratios:")
print("Harga:", harga.consistency_ratio)
print("Model:", model.consistency_ratio)
print("Reliability:", reliability.consistency_ratio)
print("Fuel:", bbm.consistency_ratio)