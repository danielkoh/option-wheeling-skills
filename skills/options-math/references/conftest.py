# Make `from bsm import ...` work when pytest is run from the repo root.
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
