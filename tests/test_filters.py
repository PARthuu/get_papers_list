import pytest
from papers_fetcher.filters import identify_non_academic_authors

@pytest.fixture
def mock_papers():
    return [
        {"PubmedID": "12345", "Title": "Cancer Research", "Authors": [{"name": "Dr. Smith", "affiliation": "XYZ Pharma Inc."}]},
        {"PubmedID": "67890", "Title": "Gene Therapy Advances", "Authors": [{"name": "Dr. Jane", "affiliation": "University of Medicine"}]}
    ]

def test_identify_non_academic_authors(mock_papers):
    filtered = identify_non_academic_authors(mock_papers)
    print(filtered)
    assert len(filtered) == 1
    assert filtered[0]["PubmedID"] == "12345"
    assert "xyz pharma inc." in filtered[0]["Company Affiliations"]
