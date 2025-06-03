import os
from datetime import datetime
import bibtexparser

# Path to your .bib file and Hugo content folder
bib_file = "/Users/andrewmiller/Desktop/h-index-calculation/europasscv_example.bib"
output_folder = "content/publication"

def format_title(title):
    """Quote YAML titles safely."""
    if any(c in title for c in ['$', '\\', '^']):
        return f"'{title.strip()}'"
    else:
        return f'"{title.strip()}"'

def bib_entry_to_markdown(entry):
    entry_id = entry['ID']
    title = format_title(entry.get("title", "No Title"))

    # Authors
    authors = [a.strip() for a in entry.get("author", "").replace('\n', ' ').split(" and ")]
    author_yaml = "\n  - " + "\n  - ".join(authors)

    # Date handling
    year = int(entry.get("year", "1900"))
    month = entry.get("month", "01").strip().replace(".", "")
    try:
        month = int(month)
    except ValueError:
        month = 1
    date_str = f"{year:04d}-{month:02d}-01"

    # Publication
    publication = entry.get("journal", "") or entry.get("booktitle", "")
    publication = publication.replace(r"\&", "&")

    # DOI and URL
    doi = entry.get("doi", "").strip()
    url_doi = f"https://doi.org/{doi}" if doi else "https://doi.org/"

    # YAML front matter
    yaml = f"""---
title: {title}
authors:{author_yaml}
date: {date_str}
publication: "{publication}"
doi: "{doi}"
url_doi: "{url_doi}"
# featured: false
# summary: ""
# tags: []
# projects: []
---
"""
    return entry_id, yaml

# Read .bib file
with open(bib_file) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Write .md files
for entry in bib_database.entries:
    entry_id, content = bib_entry_to_markdown(entry)
    out_dir = os.path.join(output_folder, entry_id)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.md"), "w") as f:
        f.write(content)

print("✅ All publications generated.")
