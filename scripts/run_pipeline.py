import logging
# logging intitalization -2
import sys

from pathlib import Path

# Dynamically add project root to sys.path
def add_project_root_to_path():
    project_root = Path(__file__).resolve().parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

add_project_root_to_path()

# Import pipeline modules
from pipeline.ingest import load_raw_file
from pipeline.validate import validate_schema
from pipeline.transform import clean_data
from pipeline.export import save_clean_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

RAW_FOLDER = Path("data/raw")
PROCESSED_FOLDER = Path("data/processed")

required_columns = ["id", "name", "value"]

def run_pipeline(
    #input_file: str = "data/raw/sample_data.csv",
    #output_file: str = "data/processed/output.csv",
    #required_columns: list[str] = ["id", "name", "value"]


):
    """
    Run the full data pipeline:
    1. Load raw data
    2. Validate schema
    3. Clean data
    4. Export cleaned data
    """

    # Step 1: Load
    #df = load_raw_file(input_file)

    # Step 2: Validate
    #validate_schema(df, required_columns)

    # Step 3: Transform
    #df_clean = clean_data(df)

    # Step 4: Export
    #save_clean_data(df_clean, output_file)

    # Colletion of all csv's in raw folder
    files = RAW_FOLDER.glob("*.csv")

    # iterate every file in functions
    for file in files:

        logging.info(f"Processing file: {file}")

        # Step 1: Load
        df = load_raw_file(file)

        # Step 2: Validate
        validate_schema(df, required_columns)

        # Step 3: Transform
        df_clean = clean_data(df)

        # Step 4: Export
        output_file = PROCESSED_FOLDER / f"cleaned_{file.name}"
        save_clean_data(df_clean, output_file)

        logging.info(f"Saved cleaned file: {output_file}")


if __name__ == "__main__":
    run_pipeline()