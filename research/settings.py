"""
settings for research module
"""
import sys
from pathlib import Path

# add to global path path to base dir for correct import
sys.path.insert(0, "../")

SOURCE_FOLDER = "resources"

PATH_TO_RESOURCE_FOLDER = Path(f"../{SOURCE_FOLDER}")
FIT_DF = PATH_TO_RESOURCE_FOLDER / Path("fit.csv")
