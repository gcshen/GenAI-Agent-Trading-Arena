import argparse
import os, sys
import os.path as osp
import random
import time
import json
from pathlib import Path

PROJ_BASE = Path(__file__).resolve().parent.parent
print(f">>> PROJ_BASE: {str(PROJ_BASE)}\n") ##LOG

sys.path.insert(0, str(PROJ_BASE))
print(sys.path)

import _paths

print(_paths.PROJ_BASE)