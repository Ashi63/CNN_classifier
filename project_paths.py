import os
from pathlib import Path

# url to download data from.
SOURCE_URL = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip"

# get the base directory of the project (directory where this script is located)
PROJECT_DIR = Path(__file__).parent
print('Project directory: ',PROJECT_DIR)

# directory to store the data file.
DATA_DIR = PROJECT_DIR/'data'
print('Data directory: ', DATA_DIR)

# directory to store the models built.
MODELS_DIR = PROJECT_DIR/'models'
print('Models directory: ', MODELS_DIR)

# directory to store the results.
RESULTS_DIR = PROJECT_DIR/'results'
print('Results directory: ',RESULTS_DIR)

# check a function to check if the paths are valid 
def validate_path():
    required_dirs = [DATA_DIR,MODELS_DIR,RESULTS_DIR]
    
    for directory in required_dirs:
        if not directory.exists():
            try:
                directory.mkdir(parents=True,exist_ok=True)
            except OSError as e:
                print(f"Error in creating directory '{directory}': {e}")
                return False
            
    return True

# If this script is executed directly, validate the paths
if __name__ == "__main__":
    if not validate_paths():
        print("Path validation failed. Please fix the issues before deploying.")
    else:
        print("Path validation successful. Ready to deploy!")
