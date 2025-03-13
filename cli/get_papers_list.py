import argparse
import logging
from papers_fetcher.fetcher import fetch_paper_ids, fetch_paper_details
from papers_fetcher.filters import identify_non_academic_authors
from papers_fetcher.csv_writer import save_to_csv
from papers_fetcher.utils import setup_logging

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed with non-academic authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Save results to a CSV file.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    
    args = parser.parse_args()

    # Set up logging
    setup_logging(debug=args.debug)

    logging.info(f"Fetching papers for query: {args.query}")
    paper_ids = fetch_paper_ids(args.query)
    
    if not paper_ids:
        logging.warning("No papers found for the given query.")
        return

    papers = fetch_paper_details(paper_ids)
    filtered_papers = identify_non_academic_authors(papers)

    if not filtered_papers:
        logging.info("No papers found with non-academic authors.")
        return

    save_to_csv(filtered_papers, filename=args.file)

if __name__ == "__main__":
    main()
