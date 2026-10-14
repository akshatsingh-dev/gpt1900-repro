import argparse
import gc
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
import traceback
import uuid
from datetime import datetime, timezone
import torch
from huggingface_hub import HfApi, snapshot_download

# nanochat is not pip-installable. It lives inside upstream's pinned clone, so
# that folder has to be on the import path before the import runs.
sys.path.insert(0, "/expanse/lustre/projects/sdp197/asingh59/gpt1900/upstream/gpt1900")
from nanochat.engine import Engine


print("IS cuda available?", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("bf16 supported:", torch.cuda.is_bf16_supported(including_emulation=False))
print("Platform:", platform.platform())
print("Python version:", sys.version)
print("PyTorch version:", torch.__version__)
#print("Hugging Face version:", huggingface_hub.__version__)
#print("NanoChat version:", nanochat.__version__)



print("Current working directory:", os.getcwd())
