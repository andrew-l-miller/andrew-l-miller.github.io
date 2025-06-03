import os
from datetime import datetime
import bibtexparser
from bibtexparser.bparser import BibTexParser

bib_file = "/Users/andrewmiller/Desktop/h-index-calculation/europasscv_example.bib"
output_folder = "content/publication"

def format_title(title):
    # Strip wrapping braces or quotes
    title = title.strip()
    if title.startswith("{") and title.endswith("}"):
        title = title[1:-1]
    if title.startswith('"') and title.endswith('"'):
        title = title[1:-1]
    if any(c in title for c in ['$', '\\', '^']):
        return f"'{title}'"
    else:
        return f'"{title}"'

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

    if month.isdigit():
        month = int(month)
    else:
        month = month_map.get(month[:3], 1)

    try:
        day = int(day)
    except ValueError:
        day = 1

    return f"{year:04d}-{month:02d}-{day:02d}"

def get_case_insensitive(entry, key):
    for k in entry:
        if k.lower() == key.lower():
            return entry[k]
    return ""

def bib_entry_to_markdown(entry):
    entry_id = entry['ID']
    title = format_title(entry.get("title", "No Title"))

    authors = [a.strip() for a in entry.get("author", "").replace('\n', ' ').split(" and ")]
    author_yaml = "\n  - " + "\n  - ".join(authors)

    date_str = parse_date(entry)

    publication = entry.get("journal", "") or entry.get("booktitle", "")
    publication = publication.replace(r"\&", "&")

    doi = entry.get("doi", "").strip()
    url_doi = f"https://doi.org/{doi}" if doi else ""

    arxiv_id = get_case_insensitive(entry, "eprint").strip()
    archive_prefix = get_case_insensitive(entry, "archivePrefix").strip().lower()
    url_pdf = f"https://arxiv.org/pdf/{arxiv_id}.pdf" if archive_prefix == "arxiv" and arxiv_id else ""

    yaml = f"""---
title: {title}
authors:{author_yaml}
date: {date_str}
publication: "{publication}"
doi: "{doi}"
url_doi: "{url_doi}"
url_pdf: "{url_pdf}"
# generated_on: {datetime.now().isoformat()}
# featured: false
# summary: ""
# tags: []
# projects: []
---
"""
    return entry_id, yaml

# Load with common strings enabled
parser = BibTexParser(common_strings=True)
with open(bib_file) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

for entry in bib_database.entries:
    entry_id, content = bib_entry_to_markdown(entry)

    # Capitalize first letter of folder name
    folder_name = entry_id[0].upper() + entry_id[1:]
    out_dir = os.path.join(output_folder, folder_name)
    os.makedirs(out_dir, exist_ok=True)

    # Write index.md
    filepath = os.path.join(out_dir, "index.md")
    with open(filepath, "w") as f:
        f.write(content)
    print(f"📄 Writing {filepath}")

    # Write cite.bib
    cite_path = os.path.join(out_dir, "cite.bib")
    with open(cite_path, "w") as f:
        f.write(f"@article{{{entry['ID']},\n")
        for key, value in entry.items():
            if key != 'ID':
                f.write(f"  {key} = {{{value}}},\n")
        f.write("}\n")

print("✅ All publications generated with titles cleaned, arXiv links, and cite.bib files.")
