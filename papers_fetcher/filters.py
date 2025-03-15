from typing import List, Dict
import re

COMPANY_KEYWORDS = ["pharma", "biotech", "laboratories", "inc.", "ltd.", "gmbh", "corp", "s.a.", "s.r.l."]
ACADEMIC_KEYWORDS = ["university", "school", "institute"]
patterns = [r"\S+@\S+"]

def find_emails(text: str) -> str:
    # List of email patterns to look for
    patterns = [r"\S+@\S+"]
    
    for pattern in patterns:
        # Compile the pattern
        email_regex = re.compile(pattern)
        
        # Find all instances of the pattern in the text
        return ", ".join(email_regex.findall(text))
        


def identify_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Filter papers to include only those with at least one author from a non-academic institution."""
    filtered_papers = []
    
    for paper in papers:
        non_academic_authors = []
        company_affiliations = []
        author_email = []
        
        for author in paper["Authors"]:
            affiliation = author[1].lower()
            if any(keyword in affiliation for keyword in COMPANY_KEYWORDS) and not any(n_keyword in affiliation for n_keyword in ACADEMIC_KEYWORDS):
                non_academic_authors.append(author[0])
                company_affiliations.append(author[1])
                emails = find_emails(author[1])
                if emails != "":
                    author_email.append(emails)
                # author_email.append(find_emails(author[1]))

        if non_academic_authors:
            paper["Non-academic Authors"] = ", ".join(non_academic_authors)
            paper["Company Affiliations"] = ", ".join(company_affiliations)
            paper["Corresponding Author Email"] =", ".join(author_email)
            paper.pop("Authors")
            filtered_papers.append(paper)

    return filtered_papers