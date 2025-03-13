import pytest
from papers_fetcher.fetcher import fetch_paper_ids, fetch_paper_details

@pytest.fixture
def mock_paper_ids():
    return ["12345", "67890"]

@pytest.fixture
def mock_paper_details():
    return [
        {"PubmedID": "12345", "Title": "Cancer Research", "Publication Date": "2024-01-10", "Authors": []},
        {"PubmedID": "67890", "Title": "Gene Therapy Advances", "Publication Date": "2023-11-20", "Authors": []}
    ]

def test_fetch_paper_ids(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                pass
            def json(self):
                return {"esearchresult": {"idlist": ["12345", "67890"]}}
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    paper_ids = fetch_paper_ids("cancer")
    assert paper_ids == ["12345", "67890"]

def test_fetch_paper_details(monkeypatch, mock_paper_ids, mock_paper_details):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                pass
            def json(self):
                return {"result": {"12345": mock_paper_details[0], "67890": mock_paper_details[1]}}
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    papers = fetch_paper_details(mock_paper_ids)
    assert len(papers) == 2
    assert papers[0]["PubmedID"] == "12345"
