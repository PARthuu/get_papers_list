import pytest
from papers_fetcher.filters import identify_non_academic_authors

@pytest.fixture
def mock_papers():
    return [
        {'PubmedID': '40087146', 'Title': 'Head & neck', 'Publication Date': '2025-03-14', 'Authors': [['Hsiao-Lan Wang', "University of Alabama at Birmingham  Birmingham  Alabama  USA | O'Neal Cancer Center  Birmingham  Alabama  USA"], ['Megan Heskett', 'University of South Florida  Tampa  USA'], ['Peng Li', 'University of Alabama at Birmingham  Birmingham  Alabama  USA'], ['Laura Dreer', 'University of Alabama at Birmingham  Birmingham  Alabama  USA'], ['David Vance', 'University of Alabama at Birmingham  Birmingham  Alabama  USA'], ['Susan McCammon', "University of Alabama at Birmingham  Birmingham  Alabama  USA | O'Neal Cancer Center  Birmingham  Alabama  USA"], ['Kailei Yan', 'University of South Florida  Tampa  USA'], ['Amanda Elliott', 'University of South Florida  Tampa  USA']]},
        {'PubmedID': '40087147', 'Title': 'Immunotherapy', 'Publication Date': '2025-03-14', 'Authors': [['Afroditi Ziogou', 'Department of Medical Oncology Biotech Metaxa Cancer Hospital of Piraeus  Piraeus  Greece']]}
    ]

def test_identify_non_academic_authors(mock_papers):
    filtered = identify_non_academic_authors(mock_papers)
    print(filtered)
    assert len(filtered) == 1
    assert filtered[0]["PubmedID"] == "40087147"
    assert "Department of Medical Oncology Biotech Metaxa Cancer Hospital of Piraeus  Piraeus  Greece" in filtered[0]["Company Affiliations"]
