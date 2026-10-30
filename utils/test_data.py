import json
from pathlib import Path

TEST_DATA_DIR = Path(__file__).resolve().parent.parent / "test_data"


def load_test_data(name: str) -> dict:
    """Load a JSON fixture from test_data/ by file name (with or without .json)."""
    file_name = name if name.endswith(".json") else f"{name}.json"
    with open(TEST_DATA_DIR / file_name, encoding="utf-8") as fixture:
        return json.load(fixture)


def image_path(name: str) -> Path:
    return TEST_DATA_DIR / "images" / name
