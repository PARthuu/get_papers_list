import csv
from typing import List, Dict, Optional

def save_to_csv(papers: List[Dict], filename: Optional[str]) -> None:
    """Save the list of papers to a CSV file or print to console."""
    fields = ["PubmedID", "Title", "Publication Date", "Non-academic Authors", "Company Affiliations"]
    
    if not papers:
        print("No papers found matching criteria.")
        return

    if filename:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(papers)
        print(f"Results saved to {filename}")
    else:
        for paper in papers:
            print(", ".join(str(paper.get(field, 'N/A')) for field in fields))
