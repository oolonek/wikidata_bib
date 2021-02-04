# Wikidata Bib Manager v0

This repo is a propotype for bibliography management using Wikidata. 

The overarching goal is to leverage linked open data to navigate your studies and personal notes. 

For this prototype, I will select some of the papers from the list of "[The top 100 papers:
Nature explores the most-cited research of all time](https://www.nature.com/news/the-top-100-papers-1.16224)" list from 2014 and take notes on them. 

Moreover, I will add some of my notes on other topics to see how it scales.  

# Repository structure

- toread.md
- read.ttl
- read.csv
- notes
    - Q1123.md
    - Q2234.md
    - etc
    - other.md

### Explanation

- toread.md

A markdown stack/list of titles of papers. It does not need to be formated, it is mostly a dump of articles that you will want to read.

- read.ttl

An RDF file linking the wikidata URIs for the articles you are reading to your notes. 
Each note file will have an URI. For now I`ll use the property wb:has_notes, where wb is this repository URL

- read.csv 

A csv file linking article titles/human readable info to Wikidata ids.

- notes
A folder containing markdown notes for each article. Each article get its on file, named by Wikidata ID. 
If the material does not fit on Wikidata, just add it as a new header to other.md.

## Notes structure

# The title of the work
    The citation in [Manubot](https://manubot.org/) syntax

## A header saying "Highlights"

Copy-and-pasted highlighs from the text. Do not highlight too much and no copy right is infringed. 

--> Any comments made by you should be preceeded by an arrow. And
    if they take another line, it is enough that they are indented.

And then you can continue highlighting

## A header saying "Comments"
Any general comments that did not fit inlinely. 

(now the explanation is over, back to the README we go)

## Features yet to be implemented
- Recording of claims: claims and the papers that support them
- Recording of conceps: concepts and the papers that introduce (or use) them 


