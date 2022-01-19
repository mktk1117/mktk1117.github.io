#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re
from LaTexAccents import AccentConverter

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

author_name = "Takahiro Miki"


def export_to_md(title, authors, booktitle, year, dumped):
    md_text = "---\n"
    md_text += "title: \"{}\"\n".format(title)
    md_text += "date: {}-01-01\n".format(year)
    md_text += "venue: {}\n".format(booktitle)
    md_text += "citation: {}\n".format(authors)
    md_text += "---\n"
    md_text += "{}\n".format(authors)
    md_text += "## Bibtex\n"
    md_text += "```\n{}\n```".format(dumped)

    clean_title = title.replace("{", "").replace("}","").replace("\\","").replace(" ","-")    
    url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
    url_slug = url_slug.replace("--","-")
    md_filename = "{}-{}.md".format(year, url_slug)
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md_text)


def is_main_author(author):
    main = author_name.split(" ")
    author_split = author.split(" ")
    author_split = list(filter(None, author_split))
    matched = True
    l = min(len(author_split), len(main))
    for i in range(l):
        if main[i] != author_split[i]:
            matched = False
    return matched


def parse_author(author_str):
    authors = author_str.split('and')
    clean_authors = ""
    converter = AccentConverter()
    for i, author in enumerate(authors):
        author = converter.decode_Tex_Accents(author)
        author = author.split(",")
        clean_author = ""
        for s in reversed(author):
            clean_author += s
        if i > 0:
            clean_authors += ","
        if is_main_author(clean_author):
            clean_author = "<b>{}</b>".format(clean_author)
        clean_authors += clean_author
    return clean_authors

with open("../_data/publications.bib", encoding = 'utf-8') as f:
    bibtex_database = bibtexparser.load(f)


for entry in bibtex_database.entries:
    entry_type = entry["ENTRYTYPE"]
    title = entry["title"]
    authors = parse_author(entry["author"])
    year = entry["year"]
    booktitle=u""
    if entry_type == "inproceedings":
        booktitle = entry["organization"] + ", " + entry["booktitle"]
    elif entry_type == "article":
        booktitle = entry["journal"]
    elif entry_type == "misc":
        booktitle = entry["note"]
    elif entry_type == "misc":
        booktitle = entry["note"]
    writer = BibTexWriter()
    writer.indent = '    '     # indent entries with 4 spaces instead of one
    writer.comma_first = True  # place the comma at the beginning of the line
    db = BibDatabase()
    db.entries = [entry]
    dumped = writer.write(db)
    export_to_md(title, authors, booktitle, year, dumped)


# ---
# title: "Paper Title Number 1"
# date: 2009-10-01
# venue: 'Journal 1'
# citation: 'Your Name, You.'
# ---

# print(bibtex_database)
# publist = bibtex_database.entries_dict
# 
# 
# html_escape_table = {
#     "&": "&amp;",
#     '"': "&quot;",
#     "'": "&apos;"
#     }
# 
# def html_escape(text):
#     """Produce entities within text."""
#     return "".join(html_escape_table.get(c,c) for c in text)
# 
# 
# for pubsource in publist:
#     parser = bibtex.Parser()
#     bibdata = parser.parse_file(publist[pubsource]["file"])
# 
#     #loop through the individual references in a given bibtex file
#     for bib_id in bibdata.entries:
#         #reset default date
#         pub_year = "1900"
#         pub_month = "01"
#         pub_day = "01"
#         
#         b = bibdata.entries[bib_id].fields
#         
#         try:
#             pub_year = f'{b["year"]}'
# 
#             #todo: this hack for month and day needs some cleanup
#             if "month" in b.keys(): 
#                 if(len(b["month"])<3):
#                     pub_month = "0"+b["month"]
#                     pub_month = pub_month[-2:]
#                 elif(b["month"] not in range(12)):
#                     tmnth = strptime(b["month"][:3],'%b').tm_mon   
#                     pub_month = "{:02d}".format(tmnth) 
#                 else:
#                     pub_month = str(b["month"])
#             if "day" in b.keys(): 
#                 pub_day = str(b["day"])
# 
#                 
#             pub_date = pub_year+"-"+pub_month+"-"+pub_day
#             
#             #strip out {} as needed (some bibtex entries that maintain formatting)
#             clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    
# 
#             url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
#             url_slug = url_slug.replace("--","-")
# 
#             md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
#             html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")
# 
#             #Build Citation from text
#             citation = ""
# 
#             #citation authors - todo - add highlighting for primary author?
#             for author in bibdata.entries[bib_id].persons["author"]:
#                 citation = citation+" "+author.first_names[0]+" "+author.last_names[0]+", "
# 
#             #citation title
#             citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""
# 
#             #add venue logic depending on citation type
#             venue = publist[pubsource]["venue-pretext"]+b[publist[pubsource]["venuekey"]].replace("{", "").replace("}","").replace("\\","")
# 
#             citation = citation + " " + html_escape(venue)
#             citation = citation + ", " + pub_year + "."
# 
#             
#             ## YAML variables
#             md = "---\ntitle: \""   + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + '"\n'
#             
#             md += """collection: """ +  publist[pubsource]["collection"]["name"]
# 
#             md += """\npermalink: """ + publist[pubsource]["collection"]["permalink"]  + html_filename
#             
#             note = False
#             if "note" in b.keys():
#                 if len(str(b["note"])) > 5:
#                     md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
#                     note = True
# 
#             md += "\ndate: " + str(pub_date) 
# 
#             md += "\nvenue: '" + html_escape(venue) + "'"
#             
#             url = False
#             if "url" in b.keys():
#                 if len(str(b["url"])) > 5:
#                     md += "\npaperurl: '" + b["url"] + "'"
#                     url = True
# 
#             md += "\ncitation: '" + html_escape(citation) + "'"
# 
#             md += "\n---"
# 
#             
#             ## Markdown description for individual page
#             if note:
#                 md += "\n" + html_escape(b["note"]) + "\n"
# 
#             if url:
#                 md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n" 
#             else:
#                 md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"} for full citation"
# 
#             md_filename = os.path.basename(md_filename)
# 
#             with open("../_publications/" + md_filename, 'w') as f:
#                 f.write(md)
#             print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
#         # field may not exist for a reference
#         except KeyError as e:
#             print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
#             continue
