import ahpy

# -----------------------------
# STEP 1: Define Criteria Weights (pairwise comparison)
# -----------------------------
# Scale: 1–9 (Saaty scale)

criteria_comparisons = {
    ('Price', 'Performance'): 3,     # Price slightly more important
    ('Price', 'Battery'): 5,
    ('Performance', 'Battery'): 2
}

criteria = ahpy.Compare(
    name='Criteria',
    comparisons=criteria_comparisons,
    precision=3,
    random_index='saaty'
)

# -----------------------------
# STEP 2: Alternatives under each criterion
# -----------------------------

# PRICE (lower is better → inverse logic)
price_comparisons = {
    ('A', 'B'): 3,   # A cheaper than B
    ('A', 'C'): 5,
    ('B', 'C'): 2
}

price = ahpy.Compare('Price', price_comparisons, precision=3)

# PERFORMANCE
performance_comparisons = {
    ('A', 'B'): 1/3,  # B better
    ('A', 'C'): 1/5,
    ('B', 'C'): 1/3
}

performance = ahpy.Compare('Performance', performance_comparisons, precision=3)

# BATTERY
battery_comparisons = {
    ('A', 'B'): 1/2,
    ('A', 'C'): 1/3,
    ('B', 'C'): 2
}

battery = ahpy.Compare('Battery', battery_comparisons, precision=3)

# -----------------------------
# STEP 3: Build Hierarchy
# -----------------------------
criteria.add_children([price, performance, battery])

# -----------------------------
# STEP 4: Get Results
# -----------------------------
print("=== FINAL PRIORITIES ===")
print(criteria.target_weights)

print("\n=== CONSISTENCY RATIO ===")
print("Criteria CR:", criteria.consistency_ratio)

print("\n=== FULL REPORT ===")
print(criteria.report())