#!/usr/bin/python3
################################################################################
# Translates a LaTeX-formatted document to a Markdown-formatted document. It is 
# intended to be used to generate documentation ready for deployment on GitHub 
# Pages using Just The Docs (assumes support for HTML tags; includes Just The 
# Docs front matter).
#
# Inspired by latex2html.py, which was inspired by Latex2qwiki (Stanford).
#
# Usage:
#
#   latex2md.py <FILE>
#
# NOTE:
# - Assumes REFERENCES_DIR environment variable is defined and points to parent 
#   directory of references.bib on disk
#
# TODO:
# - Add support for rendered Markdown in collapsed sections (will require 
#   configuration changes: https://stackoverflow.com/questions/52944720/content-of-collapsible-sections-detailssummary-renders-markdown-in-gith#52962330)
#
################################################################################

import os, re, sys
from pathlib import Path
from shutil import rmtree


# Constants
#
ENV_MSG="Error: REFERENCES_DIR should be defined and point to parent directory of references.bib on disk"
FIG_WIDTH_PRECISION=2
JTD_LAYOUT="default" # Refers to Just The Docs layout: https://just-the-docs.com/docs/layout/layout/
USAGE_MSG="Usage: latex2md.py <FILE>"


# Variables
#
citations = []
code_block_mode = False
collapsed_section_mode = False
equation_count = 0
fig_caption = ""
fig_count = 0
fig_mode = False
file_contents = []
found_collapsed_section_heading = False
found_comment = False
html_only_mode = False
ifstream = None
infile = ""
infile_path = ""
img_srcs = []
latex_only_mode = False
list_type = [] # list of int: 1: unordered, 2: ordered
math_mode = False
md_only_mode = False
ofstream = None
parent_file_contents = []
parent_title = ""
title = ""
tmpifstream = None
tmpofstream = None


# Functions
#
def process_string(string):
    global equation_count

    # Less/greater than (need to do this before substitutions involving HMTL 
    # tags)
    #
    string = re.sub(r"<", r"&#60;", string)
    string = re.sub(r">", r"&#62;", string)

    # Aelig
    string = re.sub(r"\\ae", r"&#230;", string)

    # Ampersand
    string = re.sub(r"\\&", r"&#38;", string)

    # Em-Dash
    string = re.sub(r"--", r"&#8212;", string)

    # Emphasis
    #

    # Bold
    pattern = r"(.*)\\emph{(.*?)}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        string = match.group(1) + "**" + match.group(2) + "**" + match.group(3)
        match = prog.search(string)

    # Headings
    #
    string = re.sub(r"\\section{(.*?)}", r"# \1", string)
    string = re.sub(r"\\subsection{(.*?)}", r"## \1", string)
    string = re.sub(r"\\subsubsection{(.*?)}", r"### \1", string)

    # Italic
    pattern = r"(.*)\\it{(.*?)}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        string = match.group(1) + "*" + match.group(2) + "*" + match.group(3)
        match = prog.search(string)

    # Inline equation
    #
    pattern = r"(.*)\$(.*)\$(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        equation_count += 1
        string = match.group(1) + '<img src="https://latex.codecogs.com/gif.latex?' + match.group(2) + '" alt="Equation ' + str(equation_count) + '">' + match.group(3)
        match = prog.search(string)

    # Link
    #
    pattern = r"(.*)\\(href|url){(.*?)}{(.*?)}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        string = match.group(1) + '<a href="' + match.group(3) + '" target="_blank">' + match.group(4) + '</a>' + match.group(5)
        match = prog.search(string)

    pattern = r"(.*)\\(href|url){(.*?)}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        string = match.group(1) + '<a href="' + match.group(3) + '" target="_blank">' + match.group(3) + '</a>' + match.group(4)
        match = prog.search(string)

    # Percent
    string = re.sub(r"\\%", r"&#37;", string)

    # References
    #
    pattern = r"(.*)\\citep?{(.*?)}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        citations.append(match.group(2))
        string = match.group(1) + '[<a href="#references">*' + match.group(2) + '*</a>]' + match.group(3)
        match = prog.search(string)

    # Small
    pattern = r"(.*)\\small{(.*?)}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        string = match.group(1) + '<small>' + match.group(2) + '</small>' + match.group(3)
        match = prog.search(string)

    # Subscript
    pattern = r"(.*)\\textsubscript{(.*?)}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        string = match.group(1) + '<sub>' + match.group(2) + '</sub>' + match.group(3)
        match = prog.search(string)

    # Superscript
    pattern = r"(.*)\\textsuperscript{(.*?)}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        string = match.group(1) + '<sup>' + match.group(2) + '</sup>' + match.group(3)
        match = prog.search(string)

    # Underscore/Low Line
    string = re.sub(r"\\_", r"&#95;", string)

    # vspace
    pattern = r"(.*)\\vspace{(.*?)}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(string)
    while match:
        string = match.group(1) + '<div style="height:' + match.group(2) + '"></div>' + match.group(3)
        match = prog.search(string)

    # Line break
    #
    string = re.sub(r"\\\\", r"<br>", string) # (needs to come after other substitutions that include '\\')
    string = re.sub(r"\\newline", r"<br>", string)
    string = re.sub(r"\\hfill \\break", r"<br>", string)

    return string

def strip_comment(string):
    global found_comment

    stripped_string = ""
    index_of_percent = string.find("%")
    if index_of_percent != -1:
        if index_of_percent == 0:
            found_comment = True
            stripped_string += "\n"
        elif string[index_of_percent - 1] != "\\":
            found_comment = True
            stripped_string = string[:index_of_percent] + "\n"
    else:
        stripped_string = string

    return stripped_string

# Check environment
#
try:
    REFERENCES_DIR = os.environ['REFERENCES_DIR']
except KeyError:
    print(ENV_MSG)
    exit(1)

if not (os.path.isdir(REFERENCES_DIR) and os.path.isfile(REFERENCES_DIR + "/references.bib")):
    print(ENV_MSG)
    exit(1)

# Handle arguments
#
if len(sys.argv) < 2:
    print(USAGE_MSG)
    exit(1)

if not os.path.isfile(sys.argv[1]):
    raise FileNotFoundError(USAGE_MSG)

infile = sys.argv[1]

# Set up I/O
#
infile_path = Path(infile)
ifstream = open(infile, 'r')
ofstream = open(str(infile_path.parent) + '/' + str(infile_path.stem) + '.md', 'w')

# Output Just The Docs front matter to file
#
ofstream.write("---\n")
ofstream.write("layout: " + JTD_LAYOUT + "\n")

file_contents = ifstream.readlines()

# Set title based on first heading found in input file
#
for line in file_contents:
    match = re.match(r"\\(sub)?(sub)?section{(.*)}", line)
    if match:
        title = process_string(match.group(3))
        break
ofstream.write("title: " + title + "\n")

# Check to see if this page has children (or has a parent page)
#
if infile_path.stem == "index":
    for file in os.listdir(infile_path.parent):
        if (
            file.endswith(".tex") and
            file != "index.tex" and
            os.path.isfile(infile_path.parent + "/" + file)
        ):
            ofstream.write("has_children: true" + "\n")
            break
else:
    # If an index.tex exists in parent directory get its title (could be 
    # hardcoded in Markdown, or we may need to parse it from LaTeX). Otherwise, 
    # assume that only a manually-generated index.md exists and get its title.
    #
    if os.path.isfile(str(infile_path.parent) + "/index.tex"):
        parentifstream = open(str(infile_path.parent) + "/index.tex", 'r')
        parent_file_contents = parentifstream.readlines()
        for line in parent_file_contents:
            match = re.match(r"title: (.*)", line)
            if match:
                parent_title = match.group(1)
                break

            match = re.match(r"\\(sub)?(sub)?section{(.*)}", line)
            if match:
                parent_title = process_string(match.group(3))
                break
    else:
        parentifstream = open(str(infile_path.parent) + "/index.md", 'r')
        parent_file_contents = parentifstream.readlines()
        for line in parent_file_contents:
            match = re.match(r"title: (.*)", line)
            if match:
                parent_title = match.group(1)
                break

    parentifstream.close()
    if parent_title != "":
        ofstream.write("parent: " + parent_title + "\n")

ofstream.write("NOTE: This file was generated automatically by running bin/latex2jtd.py. To make changes, edit the corresponding <FILE>.tex file and commit the changes to the repository.\n")
ofstream.write("---\n")

# Process file contents
#
print("Converting " + infile)

for line in file_contents:
    ############################################################################
    # Process multi-line blocks and other special conditions
    ############################################################################
    if collapsed_section_mode:
        if re.search(r"%__@COLLAPSED_SECTION_END@__", line):
            collapsed_section_mode = False
            ofstream.write("</details>\n")
            continue

        if not found_collapsed_section_heading:
            match = re.match(r"\\(sub)?subsection{(.*)}", line)
            if match:
                heading = match.group(2)
            else:
                print("Warning: collapsed sections should start with a \\subsection or \\subsubsection heading")
                heading = "Read More"
            found_collapsed_section_heading = True
            ofstream.write("<summary><strong>" + match.group(2) + "</strong></summary>\n")
            continue

    if latex_only_mode:
        if re.search(r"%__@LATEX_ONLY_END@__", line):
            latex_only_mode = False
            ofstream.write("\n")
        continue
    elif html_only_mode:
        if re.search(r"%__@HTML_ONLY_END@__", line):
            html_only_mode = False
            ofstream.write("\n")
        else:
            ofstream.write(line[1:]) # Strip leading '%'
        continue
    elif md_only_mode:
        if re.search(r"%__@MARKDOWN_ONLY_END@__", line):
            md_only_mode = False
            ofstream.write("\n")
        else:
            ofstream.write(line[1:]) # Strip leading '%'
        continue
    elif code_block_mode:
        # We need to echo these lines verbatim
        #
        pattern = r"(.*)\\end{verbatim}"
        prog = re.compile(pattern)
        match = prog.search(line)
        if match:
            code_block_mode = False
            ofstream.write(match.group(1) + "\n")
            ofstream.write("````\n")
        else:
            ofstream.write(line)
        continue
    elif math_mode:
        pattern = r"(.*)\\end{equation}(.*)"
        prog = re.compile(pattern)
        match = prog.search(line)
        if match:
            math_mode = False
            ofstream.write(equation + match.group(1).strip() + '" alt="Equation ' + str(equation_count) + '"></div>')
        else:
            equation += line.strip()
        continue
    elif fig_mode:
        # NOTE: The following,
        # - assumes that \end{figure} is on its own line
        # - does not handle optional parameters to \includegraphics
        # - does not handle positioning environments like \begin{center}
        # - assumes that \caption is on its own line
        # - assumes that there is only one caption per figure
        # - assumes caption should appear after images
        #
        if re.search(r"\\end{figure}", line):
            format_string = "{:." + str(FIG_WIDTH_PRECISION) + "f}"
            img_width = format_string.format(1 / len(img_srcs) * 100)
            fig_count += 1
            ofstream.write("<div style=\"display:flow-root\">")
            for img_src in img_srcs:
                img_alt = Path(img_src).stem
                ofstream.write('<img style="float:left;width:' + str(img_width) + '%" src="' + img_src + '" alt="Figure ' + str(fig_count) + ': ' + img_alt + '">')
            ofstream.write("</div>")
            if fig_caption != "":
                ofstream.write(fig_caption)

            # Reset figure-related variables
            fig_caption = ""
            fig_mode = False
            img_srcs = []
            continue

        pattern = r"\\includegraphics(\[.*\])?{(.*)}"
        prog = re.compile(pattern)
        match = prog.search(line)
        if match:
            img_srcs.append(match.group(2))
            continue

        pattern = r"\\caption{(.*)}"
        prog = re.compile(pattern)
        match = prog.search(line)
        if match:
            fig_caption = match.group(1)

            # Parse citations (same processing as below)
            #
            # TODO: Make this a function for reusability
            #
            pattern = r"\\citep?{(.*?)}"
            prog = re.compile(pattern)
            match = prog.search(fig_caption)
            while match:
                citations.append(match.group(1))
                fig_caption = prog.sub(r'[<a href="#references">*\1*</a>]', fig_caption)
                match = prog.search(fig_caption)

            # NOTE: For some reason, emphasized text in Markdown (\it might be included in \caption) will not be properly parsed if wrapped in a <div>, so we wrap instead in a <span>
            fig_caption = '<span style="display:block;width:100%;text-align:center"><small>' + fig_caption + '</small></span>'
            continue

        continue # Skip over lines like \begin{center}
    else:
        # Lists
        #
        if len(list_type) != 0:
            if re.search(r"\\begin{itemize}", line):
                list_type.append(1)
                continue
            elif re.search(r"\\begin{enumerate}", line):
                list_type.append(2)
                continue
            elif re.search(r"\\end{(itemize|enumerate)}", line):
                del list_type[-1]
                continue
            else:
                # Process list item
                if list_type[-1] == 1:
                    list_item_marker = "-"
                else:
                    list_item_marker = "1."

                prog = re.compile(r"\s*\\item\s*")
                line = prog.sub("  " * (len(list_type) - 1) + list_item_marker + " ", line)
        else:
            # Start processing list
            if re.search(r"\\begin{itemize}", line):
                ofstream.write("\n")
                list_type.append(1)
                continue
            elif re.search(r"\\begin{enumerate}", line):
                ofstream.write("\n")
                list_type.append(2)
                continue

    # Start of LaTeX-only section
    if re.search("%__@LATEX_ONLY_START@__", line):
        latex_only_mode = True
        ofstream.write("\n")
        continue

    # Start of HTML-only section
    if re.search("%__@HTML_ONLY_START@__", line):
        html_only_mode = True
        ofstream.write("\n")
        continue

    # Start of Markdown-only section
    if re.search("%__@MARKDOWN_ONLY_START@__", line):
        md_only_mode = True
        ofstream.write("\n")
        continue

    # Start of collapsed section
    if re.search(r"%__@COLLAPSED_SECTION_START@__", line):
        collapsed_section_mode = True
        found_collapsed_section_heading = False
        ofstream.write("<details>\n")
        continue

    # Code block that is contained on a single line
    pattern = r"\\begin{verbatim}(.*)\\end{verbatim}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(line)
    if match:
        ofstream.write("\n\n")
        ofstream.write("````\n")
        ofstream.write(match.group(1) + "\n")
        ofstream.write("````" + match.group(2))
        continue

    # Start of code block
    pattern = r"\\begin{verbatim}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(line)
    if match:
        code_block_mode = True
        ofstream.write("\n\n")
        ofstream.write("````")
        # Handle case where there is text on same line as \begin{verbatim}
        if match.group(1) != "\n":
            ofstream.write("\n")
        ofstream.write(match.group(1))
        continue

    # Equation that is contained on a single line
    pattern = r"(.*)\\begin{equation}(.*)\\end{equation[*]*}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(line)
    if match:
        equation_count += 1
        ofstream.write("\n")
        ofstream.write('<div align="center"><img src="https://latex.codecogs.com/gif.latex?' + match.group(2).strip() + '" alt="Equation ' + str(equation_count) + '"></div>')
        ofstream.write(match.group(3))
        continue

    # Start of equation
    pattern = r"\\begin{equation}(.*)"
    prog = re.compile(pattern, flags=re.DOTALL)
    match = prog.search(line)
    if match:
        math_mode = True
        equation_count += 1
        ofstream.write("\n")
        equation = '<div align="center"><img src="https://latex.codecogs.com/gif.latex?' + match.group(1)
        continue

    # Start of figure
    #
    # NOTE: 
    # - Not currently handling parameter that determines figure positioning
    # - Assuming \begin{figure} is on line by itself
    #
    if re.search(r"\\begin{figure}(\[.*\])?.*", line):
        fig_mode = True
        ofstream.write("\n")
        continue

    ############################################################################
    # Process single line
    ############################################################################

    # Split line, printing inline code as is and otherwise processing as needed
    #
    line_processed = ""
    pattern = r"\\verb@(.*?)@"
    if re.search(pattern, line):
        cursor = 0
        right_index_of_last_match = 0
        found_comment = False
        matches = re.finditer(pattern, line, flags=re.DOTALL)
        count = 0
        for match in matches:
            if match.span()[0] == 0:
                cursor = match.span()[1]
            else:
                if cursor < match.span()[0]:
                    substring = line[cursor:match.span()[0]]

                    # Need to strip comments
                    #
                    substring = strip_comment(substring)
                    line_processed += process_string(substring)
                    if found_comment:
                        break # Don't need to process rest of line

                    cursor = match.span()[1]
            line_processed += "`" + match.group(1) + "`"
        if not found_comment:
            # Process any characters after last match, but only if we didn't 
            # break early because of encountering a comment
            line_processed += process_string(line[cursor:len(line)])
    else:
        # No matches, so process entire line
        line_processed = strip_comment(line)
        line_processed = process_string(line_processed)

    ofstream.write(line_processed)

# Process citations
#
if len(citations) > 0:
    # NOTE: You must have bibtex and detex installed for the following to work
    #
    #   macOS
    #   - MacTeX    : http://www.tug.org/mactex/index.html
    #   - opendetex : http://macappstore.org/opendetex/
    #
    print("Processing citations for " + infile)

    # Create aux file
    #
    os.mkdir("./tmp")
    tmpofstream = open("./tmp/tmp.aux", 'w')
    tmpofstream.write("\\bibstyle{plain}\n")
    tmpofstream.write("\\bibdata{" + REFERENCES_DIR + "/references}\n")
    for citation in citations:
        tmpofstream.write("\\citation{" + citation + "}\n")
    tmpofstream.close()

    # Create bbl file
    #
    os.system("bibtex ./tmp/tmp > /dev/null 2>&1")
    os.system('cat ./tmp/tmp.bbl | /usr/bin/grep -v "begin{thebibliography}" > ./tmp/tmp.bbl2')

    # Create tex file
    #
    tmpofstream = open("./tmp/tmp.tex", 'w')
    tmpofstream.write("\documentclass[letterpaper]{report}\n")
    tmpofstream.write("\\begin{document}\n")
    tmpofstream.write("\\begin{thebibliography}\n")
    with open('./tmp/tmp.bbl2') as tmpifstream:
        for line in tmpifstream: 
            tmpofstream.write(line)
    tmpofstream.write("\\end{document}\n")
    tmpofstream.close()

    # Convert tex file to plain text
    os.system("detex -n ./tmp/tmp.tex > ./tmp/tmp.txt")

    # Write out citations
    #
    ofstream.write("\n## References\n")

    citation = ""
    with open('./tmp/tmp.txt', 'r') as tmpifstream:
        for line in tmpifstream:
            if line == "\n":
                if citation != "":
                    ofstream.write(citation + "\n")
                citation = ""
                continue
            if citation == "":
                citation = "-"
            citation = citation + " " + line

    # Cleanup temp files
    rmtree("./tmp")

# I/O cleanup
#
ofstream.close()
ifstream.close()
