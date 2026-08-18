"""
NeuroSync Paywall — simulated currency/crypto-to-EEG session conversion.

This module is intentionally a simulation. It allocates simulated,
consented demo subjects and generates synthetic synchronization metrics.
It does not control or entrain real human subjects.
"""

import random
import time
from typing import Dict, List

try:
    from collecteeg import collect_eeg_data  # Reuse existing simulator when available.
except ImportError:
    collect_eeg_data = None


SUBJECT_POOL = list(range(1, 101))

BAND_RATES = {
    "delta": 0.80,
    "theta": 0.60,
    "alpha": 0.50,
    "beta": 0.70,
    "gamma": 1.20,
}

CRYPTO_RATES = {
    "ETH": 3200.0,
    "USDC": 1.0,
    "NTK": 0.05,
}

BAND_FREQS = {
    "delta": 2.0,
    "theta": 6.0,
    "alpha": 10.0,
    "beta": 20.0,
    "gamma": 40.0,
}


def normalize_to_usd(amount: float, currency: str) -> float:
    """Convert a mock fiat/crypto amount to USD."""
    currency = currency.upper()
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if currency == "USD":
        return amount

    rate = CRYPTO_RATES.get(currency)
    if rate is None:
        raise ValueError(f"Unsupported currency: {currency}")

    return amount * rate


def quote_session(
    band: str,
    desired_subjects: int,
    duration_minutes: float,
) -> Dict:
    """Return a demo price quote."""
    band = band.lower()

    if band not in BAND_RATES:
        raise ValueError(f"Unsupported band: {band}")
    if desired_subjects < 2:
        raise ValueError("A synchronized multi-subject session requires at least 2 subjects")
    if duration_minutes <= 0:
        raise ValueError("Duration must be greater than zero")

    total_usd = BAND_RATES[band] * desired_subjects * duration_minutes

    return {
        "band": band,
        "subjects": desired_subjects,
        "duration_minutes": duration_minutes,
        "price_usd": round(total_usd, 2),
        "price_eth": round(total_usd / CRYPTO_RATES["ETH"], 6),
        "price_usdc": round(total_usd, 2),
        "price_ntk": round(total_usd / CRYPTO_RATES["NTK"], 2),
    }


def allocate_subjects(count: int) -> List[int]:
    """Allocate simulated subjects from the demo pool."""
    if count < 2:
        raise ValueError("At least two subjects are required")
    if count > len(SUBJECT_POOL):
        raise ValueError("Not enough simulated subjects available")

    return random.sample(SUBJECT_POOL, count)


def synchronize_subjects(
    subject_ids: List[int],
    band: str,
    duration_minutes: float,
) -> Dict:
    """
    Generate a simulated synchronized EEG session.

    The generated PLV, frequency, phase, and amplitude values are synthetic.
    No real human subject is controlled by this function.
    """
    band = band.lower()
    if band not in BAND_FREQS:
        raise ValueError(f"Unsupported band: {band}")
    if not subject_ids:
        raise ValueError("No subjects supplied")

    target_freq = BAND_FREQS[band]
    streams = []

    for sid in subject_ids:
        phase = random.uniform(0, 2 * 3.14159)
        coherence = random.uniform(0.75, 0.98)

        streams.append(
            {
                "subject_id": sid,
                "band": band,
                "frequency_hz": round(target_freq + random.uniform(-0.3, 0.3), 3),
                "phase": round(phase, 4),
                "plv": round(coherence, 3),
                "amplitude": round(random.uniform(10, 40), 3),
            }
        )

    print(
        f"[NeuroSync DEMO] Generating synthetic synchronization metrics "
        f"for {len(subject_ids)} simulated subjects on {band.upper()}."
    )

    # Accelerated demo runtime.
    time.sleep(min(duration_minutes * 0.1, 3))

    avg_plv = sum(s["plv"] for s in streams) / len(streams)

    return {
        "status": "simulated_synchronized",
        "band": band,
        "target_frequency_hz": target_freq,
        "subject_count": len(subject_ids),
        "subject_ids": subject_ids,
        "average_plv": round(avg_plv, 3),
        "streams": streams,
        "duration_minutes": duration_minutes,
        "message": (
            f"Generated synthetic synchronization metrics for "
            f"{len(subject_ids)} simulated subjects on {band} band"
        ),
    }


def convert_payment_to_subjects(
    amount: float,
    currency: str,
    band: str,
    duration_minutes: float = 10.0,
    max_subjects: int = 32,
) -> Dict:
    """
    Convert a payment value into a quantity of simultaneous simulated subjects.

    This is a demo marketplace calculation only.
    """
    band = band.lower()
    if band not in BAND_RATES:
        raise ValueError(f"Unsupported band: {band}")
    if max_subjects < 2:
        raise ValueError("max_subjects must be at least 2")
    if duration_minutes <= 0:
        raise ValueError("Duration must be greater than zero")

    usd = normalize_to_usd(amount, currency)
    rate = BAND_RATES[band]

    affordable = int(usd / (rate * duration_minutes))
    subject_count = min(affordable, max_subjects)

    if subject_count < 2:
        raise ValueError(
            "Insufficient payment for a simulated multi-subject session"
        )

    subjects = allocate_subjects(subject_count)
    session = synchronize_subjects(subjects, band, duration_minutes)

    return {
        "payment": {
            "amount": amount,
            "currency": currency.upper(),
            "usd_value": round(usd, 2),
        },
        "allocated_subjects": subject_count,
        "session": session,
    }


if __name__ == "__main__":
    print("=== NeuroMart NeuroSync Paywall Demo ===\n")

    result = convert_payment_to_subjects(
        amount=0.015,
        currency="ETH",
        band="alpha",
        duration_minutes=15,
    )
    print(result)

    print("\n" + "=" * 50 + "\n")

    result2 = convert_payment_to_subjects(
        amount=800,
        currency="NTK",
        band="gamma",
        duration_minutes=5,
    )
    print(result2)
