# Neuro-Mining Cryptocurrency Ecosystem + NeuroSync Paywall

This is a minimal proof of concept for a neuro-mining cryptocurrency ecosystem.
Users earn **NeuroTokens (NTK)** from simulated EEG activity (Gamma focus / Theta relaxation).

## New Feature — v0.2 NeuroSync Paywall

The update adds a **simulated** marketplace flow that converts fiat/crypto payment values into a requested quantity of simultaneous, consented simulated EEG subjects and produces synchronized-band/phase-locking metrics.

> **Safety / scope:** This repository update is simulation/demo logic. It does not control, entrain, synchronize, or otherwise manipulate real human brains. A real-world system would require explicit informed consent, appropriate ethics/IRB review, privacy protections, medical-device/regulatory review where applicable, and secure handling of EEG data.

### Key Features

- EEG Data Collection (Gamma, Theta, Delta) — simulated or real collection can be integrated separately
- ERC-20 NeuroToken (NTK) on an Ethereum testnet
- Reward mining based on simulated brainwave thresholds
- **NEW: Currency/Crypto → Simulated Synchronized Subjects**
  - Pay with ETH, USDC, NTK, or simulated USD
  - Request N concurrent simulated subjects on a chosen EEG band
  - Simulated inter-subject phase synchronization (PLV)
  - On-demand session through a demo paywall
- Blockchain integration via `web3.py`
- Minimal web dashboard

## NeuroSync Flow

1. User selects an EEG band, subject count/payment amount, and duration.
2. The system quotes the value in USD, ETH, USDC, or NTK using mock exchange rates.
3. Simulated subjects are allocated from a consented demo pool.
4. The simulator generates streams around the selected target band and phase/coherence values.
5. A live-style multi-subject result and average PLV are returned.
6. The simulated session ends automatically.

## Requirements

Use the repository's existing requirements plus any dependencies already specified by the project.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python neurosync_paywall.py
```

Or append `neuromart_neurosync_section.html` to the existing dashboard.

## Important Implementation Note

The existing blockchain integration sends native ETH rather than NTK. A production NTK payment flow would need the deployed ERC-20 contract address, ABI, wallet handling, allowance/transferFrom logic, transaction confirmation, and appropriate security controls.

## License

MIT
