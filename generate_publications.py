import os
from datetime import datetime
import bibtexparser
from bibtexparser.bparser import BibTexParser

bib_file = "/Users/andrewmiller/Desktop/WEBSITE/h-index-calculation/europasscv_example.bib"
output_folder = "content/publication"

def format_author_name(name):
    if ',' in name:
        last, first = name.split(',', 1)
        return first.strip() + " " + last.strip()
    return name.strip()

def format_title(title):
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

    raw_authors = entry.get("author", "").replace('\n', ' ').split(" and ")
    authors = [format_author_name(a) for a in raw_authors]

    

    # Ensure your name matches exactly
    authors = [
        "Andrew L. Miller" if a.lower().replace('.', '').strip() in ["andrew l miller", "miller andrew l", "A. Miller"] else a
        for a in authors
    ]
    def is_self(name):
        name_clean = name.lower().replace(".", "").strip()
        return any(variant in name_clean for variant in [
            "andrew l miller",
            "miller andrew l",
            "a miller",
            "miller a"
        ])

    author_yaml = "\n  - " + "\n  - ".join(
        "admin" if is_self(a) else a
        for a in authors
    )


    date_str = parse_date(entry)

    journal = entry.get("journal", "") or entry.get("booktitle", "")
    journal = journal.replace(r"\&", "&").strip()
    volume = entry.get("volume", "").strip()
    number = entry.get("number", "").strip()
    pages = entry.get("pages", "").strip()

    publication_parts = [f"*{journal}*"] if journal else []
    if volume:
        vol_str = f"**{volume}**"
        if number:
            vol_str += f"({number})"
        publication_parts.append(vol_str)
    if pages:
        publication_parts.append(pages)

    publication = " ".join(publication_parts)

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

def generate_publication_pages(overwrite=False):
    parser = BibTexParser(common_strings=True)
    with open(bib_file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    for entry in bib_database.entries:
        entry_id, content = bib_entry_to_markdown(entry)

        folder_name = entry_id[0].upper() + entry_id[1:]
        out_dir = os.path.join(output_folder, folder_name)

        os.makedirs(out_dir, exist_ok=True)

        filepath = os.path.join(out_dir, "index.md")
        cite_path = os.path.join(out_dir, "cite.bib")

        if not overwrite and os.path.exists(filepath):
            print(f"⏭️ Skipping {folder_name} — already exists.")
            continue

        # Write index.md
        with open(filepath, "w") as f:
            f.write(content)
        print(f"📄 Writing {filepath}")

        # Write cite.bib
        with open(cite_path, "w") as f:
            f.write(f"@article{{{entry['ID']},\n")
            for key, value in entry.items():
                if key.lower() not in ['id', 'addendum']:
                    f.write(f"  {key} = {{{value}}},\n")

            f.write("}\n")

    print("✅ All publications generated with titles cleaned, arXiv links, and cite.bib files.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate publication folders and index.md files from a .bib file.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing publication folders.")
    args = parser.parse_args()

    generate_publication_pages(overwrite=args.overwrite)
