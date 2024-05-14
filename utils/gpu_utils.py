import torch


def perform_cuda_checks():
    # Perform Cuda checks
    print(f"Torch version: {torch.__version__}")
    print(f"Is CUDA available for torch? {torch.cuda.is_available()}")
    print(f"Torch CUDA version: {torch.version.cuda}")