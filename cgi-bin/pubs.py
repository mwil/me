#! /usr/local/bin/python

# Supported field values:
# - command: {bibentry, listbib}
# - bibkey:  fetch single bibkey item from the .bib file and send its plaintext contents
#

import cgi
import cgitb

import errno
import os
import re
import sys

cgitb.enable()
#cgi.test()

def get_key(bibkey):
	entry     = ""
	process_entry = False

	try:
		bib_file = open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mwil.bib")), "r")
	
		for line in bib_file:
			if not process_entry:
				if re.search("^@.*%s.*,"%(bibkey), line):
					process_entry = True
					entry += line

			else:
				if line != "}\n":
					entry += line
				else:
					entry += "}"
					break

		bib_file.close()

	except IOError:
		print "IOError!"

	if not entry:
		entry = "No entry found!"

	return entry

chars = {
	r"\\emph{and}": "and",
	r'{\\"u}': "ü",
	r'{\\"a}': "ä",
	r'{\\"o}': "ö",
	r"\\,": " ",
	"{" : "",
	"}" : "",
	"---": "&mdash;",
	"--": "&ndash;",
	"\\&": "&amp;",
	"\\\\slash ": "/",
	"~": "&nbsp;",
	
}

months = {
	"jan": "January",
	"feb": "February",
	"mar": "March",
	"apr": "April",
	"may": "May",
	"jun": "June",
	"jul": "July",
	"aug": "August",
	"sep": "September",
	"oct": "October",
	"nov": "November",
	"dec": "December"
}

evtitles = {
	"\\\&": "&amp;",
	" ":   "&nbsp;"
}

def replace_chars(match):
	char = match.group(0)
	return chars[char.encode('string_escape')]

def replace_months(match):
	month = match.group(0)
	return months[month]

def replace_evtitle(match):
	evtitle = match.group(0)
	return evtitles[evtitle.encode('string_escape')]


def get_biblist():
	html           = ""
	return html

	process_entry  = False
	entry_complete = False
	entry          = ""
	curr_year      = None

	try:
		bib_file = open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mwil.bib")), "r")
	
		for line in bib_file:
			if process_entry:
				if line != "}\n":
					entry += line
				else:
					process_entry = False
					entry_complete = True

			else:
				if re.search("^@.*,", line):
					entry += line
					process_entry = True

			if entry_complete:
				reftype, bibkey  = re.search("^@(\S+)\s*{\s*(\S+)\s*,", entry).groups()
				authors, = re.search("author\s*=\s*{(.*)}", entry).groups()
				if authors.count(" and ") > 1:
					authors  = authors.replace(" and ", ", ", authors.count(" and ")-1).replace(" and ", ", and ", 1)
				
				# search for the title field and replace BibTex-Characters with HTML equivalents
				title, = re.search("\s+title\s*=\s*{(.*)}", entry).groups()
				title  = re.sub('(' + '|'.join(chars.keys()) + ')', replace_chars, title)

				month, = re.search("month\s*=\s*(\w+)", entry).groups()
				month  = re.sub('(' + '|'.join(months.keys()) + ')', replace_months, month)

				year,  = re.search("year\s*=\s*(\d+)", entry).groups()

				if year != curr_year:
					html += '<li data-role="list-divider">%s</li>' % (year)
					curr_year = year

				try:
					doi, = re.search("doi\s*=\s*{(.*)}", entry).groups()
				except AttributeError:
					doi = None

				try:
					arxiv, = re.search("eprint\s*=\s*{(.*)}", entry).groups()
				except AttributeError:
					arxiv = None

				html += '<li>'

				if doi:
					html += '<a href="http://dx.doi.org/%s" target="_blank">' % (doi)
				elif arxiv:
					html += '<a href="http://arxiv.org/abs/%s" target="_blank">' % (arxiv)
				else:
					html += '<a href="#" target="_blank">'

				html += '%s. ' % (authors)

				if not title.endswith("?"):
					html += '<span class="title">%s</span>. ' % (title)
				else:
					html += '<span class="title">%s</span> ' % (title)

				if reftype == "inproceedings":
					conf,  = re.search("booktitle\s*=\s*{(.*)}", entry).groups()
					conf   = re.sub('(' + '|'.join(chars.keys()) + ')', replace_chars, conf)

					cname, = re.search("eventtitle\s*=\s*{(.*)}", entry).groups()
					cname  = re.sub('(' + '|'.join(evtitles.keys()) + ')', replace_evtitle, cname)

					pages  = re.search("pages\s*=\s*{(.*)}", entry).groups()[0].replace("--", "&ndash;")

					if re.search("&ndash;", pages):
						html += 'In&nbsp;<span class="conf">%s (%s)</span>, pages %s. ' % (conf, cname, pages)
					else:
						html += 'In&nbsp;<span class="conf">%s (%s)</span>, page %s. ' % (conf, cname, pages)

				elif reftype == "article":
					journal, = re.search("journal\s*=\s*{(.*)}", entry).groups()
					volume,  = re.search("volume\s*=\s*(.*),", entry).groups()

					try:
						number = "(%s)" % (re.search("number\s*=\s*(.*),", entry).groups()[0])
					except AttributeError:
						number = ""

					pages    = re.search("pages\s*=\s*{(.*)}", entry).groups()[0].replace("--", "&ndash;")

					html += '<span class="conf">%s</span>, %s%s:%s. ' % (journal, volume, number, pages)

				elif reftype == "techreport":
					html += '<span class="conf">Technical Report arXiv:%s</span>. ' % (arxiv)

				if reftype == "inproceedings":
					publisher, = re.search("\s+publisher\s*=\s*{(.+)}", entry).groups()

					html += '%s, %s %s.' % (publisher, month, year)
				elif reftype == "article":
					html += '%s %s.' % (month, year)
				else:
					html += 'TU Kaiserslautern, Germany, %s %s.' % (month, year)

				html += '</a>'
				html += '<a href="#" class="bibtex-btn" data-bibkey="%s">BibTeX</a>' % (bibkey)
				html += '</li>'

				entry_complete = False
				entry = ""

	except IOError:
		print "IOError in get_biblist!"

	return html



# ---------------------------------------- #
form    = cgi.FieldStorage()
command = form.getvalue("command", "")

if command == "bibentry":
	print "Content-Type: text/plain"
	print # blank line, end of headers

	bibkey = form.getvalue("bibkey", "")

	if bibkey:
		print get_key(bibkey),

elif command == "listbib":
	print "Content-Type: text/html"
	print # blank line, end of headers
	print get_biblist(),
else:
	print "Content-Type: text/plain"
	print # blank line, end of headers
	print "Unknown command ", command

