from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
full_file_path = BASE_DIR / "quotes.txt"

print(f"__init__ path lives here: {full_file_path}")

with open(full_file_path, "rt") as f:
    quotearr = [line.strip() for line in f]
