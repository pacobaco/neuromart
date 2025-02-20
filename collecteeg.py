import random

# Simulated EEG data collection
def collect_eeg_data():
    data = {
        "theta": random.uniform(4, 8),  # Theta: relaxation
        "gamma": random.uniform(30, 100),  # Gamma: focus
        "delta": random.uniform(0.5, 4),  # Delta: deep sleep
    }
    return data

def evaluate_brainwaves(data):
    gamma_score = data["gamma"]
    if gamma_score > 60:  # Focus threshold
        return 10  # Reward tokens for high focus
    return 0
