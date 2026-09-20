import sys
import numpy as np

print(f"Python version: {sys.version}")
print(f"Numpy version: {np.__version__}")
a=np.array([1, 2, 3])
print(f"Vector: {a} dot product with itself: {np.dot(a, a)}")


import torch
print(f"Torch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"MPS available: {torch.backends.mps.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
