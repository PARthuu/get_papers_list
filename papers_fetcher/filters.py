from typing import List, Dict

COMPANY_KEYWORDS = ["pharma", "biotech", "laboratories", "inc.", "ltd.", "gmbh", "corp", "s.a.", "s.r.l."]
ACADEMIC_KEYWORDS = ["university", "school", "institute"]

def identify_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Filter papers to include only those with at least one author from a non-academic institution."""
    filtered_papers = []
    
    for paper in papers:
        # print(paper)
        non_academic_authors = []
        company_affiliations = []
        
        for author in paper["Authors"]:
            # print(author)
            affiliation = author[1].lower()
            if any(keyword in affiliation for keyword in COMPANY_KEYWORDS) and not any(n_keyword in affiliation for n_keyword in ACADEMIC_KEYWORDS):
                non_academic_authors.append(author[0])
                company_affiliations.append(author[1])
            

        if non_academic_authors:
            paper["Non-academic Authors"] = ", ".join(non_academic_authors)
            paper["Company Affiliations"] = ", ".join(company_affiliations)
            paper.pop("Authors")
            filtered_papers.append(paper)

    return filtered_papers