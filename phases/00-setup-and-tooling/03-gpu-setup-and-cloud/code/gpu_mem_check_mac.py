import torch

print(f"MPS available: {torch.backends.mps.is_available()}")
print(f"MPS is_built: {torch.backends.mps.is_built()}")

if torch.backends.mps.is_available():
    print("GPU: Apple Silicon Metal Performance Shaders (MPS)")
    print("Memory: Unified Memory (shared with CPU)")
else:
    print("No GPU detected. That's fine for most lessons.")
    print("For GPU-heavy lessons, use Google Colab (free).")


if torch.backends.mps.is_available():
    device = torch.device("mps")
else:   
    device = torch.device("cpu")

print(f"Using device: {device}")