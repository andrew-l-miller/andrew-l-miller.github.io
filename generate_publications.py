import os
from datetime import datetime
import bibtexparser

bib_file = "/Users/andrewmiller/Desktop/h-index-calculation/europasscv_example.bib"
output_folder = "content/publication"

def format_title(title):
    if any(c in title for c in ['$', '\\', '^']):
        return f"'{title.strip()}'"
    else:
        return f'"{title.strip()}"'

def parse_date(entry):
    month_map = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }

    year = entry.get("year", "1900").strip()
    month = entry.get("month", "1").strip().lower().replace(".", "").replace('"', '')
    day = entry.get("day", "1").strip()

    try:
        year = int(year)
    except ValueError:
        year = 1900

    # Handle month as number or string
    if month.isdigit():
        month = int(month)
    else:
        month = month_map.get(month[:3], 1)

    try:
        day = int(day)
    except ValueError:
        day = 1

    return f"{year:04d}-{month:02d}-{day:02d}"

def bib_entry_to_markdown(entry):
    entry_id = entry['ID']
    title = format_title(entry.get("title", "No Title"))

    authors = [a.strip() for a in entry.get("author", "").replace('\n', ' ').split(" and ")]
    author_yaml = "\n  - " + "\n  - ".join(authors)

    date_str = parse_date(entry)

    publication = entry.get("journal", "") or entry.get("booktitle", "")
    publication = publication.replace(r"\&", "&")

    doi = entry.get("doi", "").strip()
    url_doi = f"https://doi.org/{doi}" if doi else "https://doi.org/"

    yaml = f"""---
title: {title}
authors:{author_yaml}
date: {date_str}
publication: "{publication}"
doi: "{doi}"
url_doi: "{url_doi}"
# generated_on: {datetime.now().isoformat()}
# featured: false
# summary: ""
# tags: []
# projects: []
---
"""
    return entry_id, yaml

with open(bib_file) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

for entry in bib_database.entries:
    entry_id, content = bib_entry_to_markdown(entry)
    out_dir = os.path.join(output_folder, entry_id)
    os.makedirs(out_dir, exist_ok=True)
    filepath = os.path.join(out_dir, "index.md")
    print(f"Writing to {os.path.abspath(filepath)}")
    with open(filepath, "w") as f:
        f.write(content)

print("✅ All publications generated with zero-padded dates and timestamp comments.")
