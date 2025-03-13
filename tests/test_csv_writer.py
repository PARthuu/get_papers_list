import os
import pytest
from papers_fetcher.csv_writer import save_to_csv

@pytest.fixture
def sample_data():
    return [
        {"PubmedID": "12345", "Title": "Cancer Research", "Publication Date": "2024-01-10", "Non-academic Authors": "Dr. Smith", "Company Affiliations": "XYZ Pharma"},
        {"PubmedID": "67890", "Title": "Gene Therapy Advances", "Publication Date": "2023-11-20", "Non-academic Authors": "Dr. Jane", "Company Affiliations": "ABC Biotech"}
    ]

def test_save_to_csv(sample_data, tmp_path):
    file_path = tmp_path / "output.csv"
    save_to_csv(sample_data, filename=str(file_path))
    assert os.path.exists(file_path)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.readlines()
    assert len(content) > 1  # At least a header + 1 row
