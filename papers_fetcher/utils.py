import logging

def setup_logging(debug: bool = False):
    """Set up logging based on debug flag."""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=level)
