# get_papers_list

---

## Pre-requisites

1. [Python](https://www.python.org/downloads/) version >= 3.13.
2. [Poetry](https://pypi.org/project/poetry/) module. `pip install poerty` can be used to download.

## Installation

1. Clone this repository using :

```
git clone https://github.com/PARthuu/get_papers_list.git
```

2. Get into the downloaded directory.

```
cd get_papers_list
```

3. Install all dependencies using :

```
poetry install
```

4. Run the following command to get started.

```
poetry run python get_papers_list.py -h
```

## Usage

Positional arguments:
`"query"`
Search your "query" from PubMed.

Options:
show this help message and exit
`-h, --help`
FILE Save results to a CSV file.
`-f, --file`
Enable debug mode.
`-d, --debug`

### Examples:

```
poetry run python get_papers_list.py "cancer AND cure"
```

Above command will print the results on the console.

```
poetry run python get_papers_list.py "cancer AND cure" -f output.csv
```

Above command will create a CSV file named `output.csv` as the output.

## Constraints

- _Pubmed_ allow only 3 requests per second without using signing in. As, there was no mention about the minimum requirement for the task, I went with the most simple solution.
- Execution requirement stated that _"Provide an executable command named get-papers-list via Poetry"_. Using this tool as `poetry run python get_papers_list.py` is what I came up with based on that.
