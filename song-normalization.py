import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))
def manhattan_distance(p1, p2):
    return np.sum(np.abs(p1 - p2))
def chebyshev_distance(p1, p2):
    return np.max(np.abs(p1 - p2))
# Features of two songs (Tempo, Energy, Dance)
song1 = np.array([120, 0.80, 0.70])
song2 = np.array([90, 0.40, 0.30])

# Without normalization
print("Without normalization:")
print(f"Euclidean: {euclidean_distance(song1, song2):.2f}")
print(f"Manhattan: {manhattan_distance(song1, song2):.2f}")
print(f"Chebyshev: {chebyshev_distance(song1, song2):.2f}")
# With Min-Max normalization
def normalize(data, min_vals, max_vals):
    return (data - min_vals) / (max_vals - min_vals)
min_vals = np.array([85, 0.30, 0.20])
max_vals = np.array([145, 0.95, 0.92])
song1_norm = normalize(song1, min_vals, max_vals)
song2_norm = normalize(song2, min_vals, max_vals)
print("\nWith normalization:")
print(f"Euclidean: {euclidean_distance(song1_norm, song2_norm):.2f}")