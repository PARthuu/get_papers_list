import requests
import xml.etree.ElementTree as ET
import logging
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
EMAIL = "your_email@example.com"  # Required for PubMed API compliance

logging.basicConfig(level=logging.INFO)

def fetch_paper_ids(query: str, max_results: int = 160) -> List[str]:
    """Fetch paper IDs from PubMed based on a query."""

    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results,
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetch details for a list of PubMed paper IDs."""
    if not paper_ids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
    }
    response = requests.get(DETAILS_URL, params=params)
    response.raise_for_status()

    data = ET.fromstring(response.content)

    papers = []
    for articles in data.findall('PubmedArticle'):
        pmid = articles.find('MedlineCitation').find('PMID').text
        title = articles.find('MedlineCitation').find('Article').find('Journal').find('Title').text

        year = articles.find('MedlineCitation').find('DateRevised').find('Year').text
        month = articles.find('MedlineCitation').find('DateRevised').find('Month').text
        day = articles.find('MedlineCitation').find('DateRevised').find('Day').text

        date = year + '-' + month + '-' + day

        authors = []
        try:
            for author_info in articles.find('MedlineCitation').find('Article').find('AuthorList').findall('Author'):
                f_name = author_info.find('ForeName').text
                l_name = author_info.find('LastName').text


                affiliations = " | ".join(a.find('Affiliation').text.replace(", ", "  ")[:-1] for a in author_info.findall('AffiliationInfo'))
                
                authors.append([f_name + ' ' + l_name, affiliations])

            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": date,
                "Authors": authors,
            })

        except AttributeError as e:
            continue

    return papers
