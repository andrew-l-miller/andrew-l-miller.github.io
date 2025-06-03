import bibtexparser
import os

input_bib = "/Users/andrewmiller/Desktop/h-index-calculation/europasscv_example.bib"  # Path to your .bib file
output_dir = "content/publication"

with open(input_bib) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

for entry in bib_database.entries:
    slug = entry.get('ID', 'untitled').replace(':', '-').replace('/', '-').lower()
    title = entry.get('title', '').replace('{', '').replace('}', '')
    authors = [a.strip() for a in entry.get('author', '').split(' and ')]
    year = entry.get('year', '2020')
    month = entry.get('month', '01')  # Optional: parse to number if needed
    date = f"{year}-{month}-01"
    journal = entry.get('journal', '') or entry.get('booktitle', '')
    volume = entry.get('volume', '')
    number = entry.get('number', '')
    doi = entry.get('doi', '')

    pub_str = f"{journal}"
    if volume:
        pub_str += f", {volume}"
    if number:
        pub_str += f"({number})"

    folder = os.path.join(output_dir, slug)
    os.makedirs(folder, exist_ok=True)

    content = f"""---
title: "{title}"
authors:
"""
    for author in authors:
        content += f"  - {author}\n"

    content += f"""date: {date}
publication: "{pub_str}"
doi: "{doi}"
url_doi: "https://doi.org/{doi}"
# featured: false
# summary: ""
# tags: []
# projects: []
---
"""

    with open(os.path.join(folder, "index.md"), "w") as f:
        f.write(content)

print("✅ Finished generating publications.")
