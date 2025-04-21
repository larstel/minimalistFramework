import os
from utils.logging import *

def change_to_directory_of_file(file):
    script_dir = os.path.dirname(file)
    os.chdir(script_dir)

    logging.debug(f"Working directory changed to: {script_dir}")