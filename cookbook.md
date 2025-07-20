

Cookbook
========

This "cookbook" demonstrates how to exploit content-negotiation techniques against the HTTP server at http://carrrels.distantreader.org from the command-line within your terminal. 


Getting Started
---------------

First, you will need a command-line user-agent application. Install an application called "curl", a very well respected piece of software. See https://curl.se.

Next, open up your terminal application, and request content from the server. By default, the server will respond with a stream of HTML intended to be rendered by a Web browser such as Chrome, Firefox, or Safari. The stream is a list ("catalog") of all study carrels and the briefest of descriptions of each:

	curl http://carrels.distantreader.org

Now, do the same thing, but specifically request HTML content:

	curl -H "Accept: text/html" http://carrels.distantreader.org

If you request a type of content that is not valid for any reason, then the server will return HTTP error 406 (Not Acceptable) as well as an HTML snippet outlining that content types are acceptable:

	curl -H "Accept: foo/bar" http://carrels.distantreader.org

Power users may way to add the -I switch to the command, and the result will be a bit more computer-friendly, but not necessarily more readable:

	curl -I -H "Accept: foo/bar" http://carrels.distantreader.org

Keep the -I switch in mind for future debugging purposes.


CSV Output
----------

The HTML output is fine and serves many use cases very well, but requesting content more suitable for computer processing has many advantages. Comma-separated values (CSV) streams are well understood by many people, and to get a list of all study carrels in the form of a CSV stream, submit:

	curl -H "Accept: text/csv" http://carrels.distantreader.org

Do the same thing, but this time, redirect the stream to a file, and then open the file ("catalog.csv") in your favorite spreadsheet application or analysis program (like [OpenRefine](https://openrefine.org/)):

	curl -H "Accept: text/csv" http://carrels.distantreader.org > catalog.csv

A suite of software called "csvkit" is a set of command-line scripts written in Python, and the scripts eat CSV lunch. See https://csvkit.readthedocs.io and install csvkit:

	pip install csvkit

Now, in the form of a CSV stream, request a list of all study carrels, pipe the result to a csvkit tool called "csvlook", and pipe the result to a pager called "less". Browsing the result ought to be now much easier:

	curl -H "Accept: text/csv" http://carrels.distantreader.org | csvlook | less -S


JSON Output
-----------

CSV is a well-understood content type, but JSON is often deemed easier to use. That said, request a list of all of the server's study carrels in the form of a JSON stream:

	curl -H "Accept: application/json" http://carrels.distantreader.org

Csvkit is to CSV as jq is to JSON. In other words, a program called "jq" is an application which takes JSON as input and provides a means to read/analyze it. See https://jqlang.org and install jq. I'll wait.

After installing jq, repeat the previous request, pipe the result to jq, and pipe that result to less for the purposes of browsing. Take note of the response's structure:

	curl -H "Accept: application/json" http://carrels.distantreader.org | jq | less -S


Filtering JSON Output
---------------------

Each study carrel is described and characterized in a number of ways, as the the following JSON snippet illustrates:

`  {
    "id": "author-homer-gutenberg",
    "type": "author",
    "title": "Homer",
    "source": "gutenberg",
    "items": 48,
    "words": 272735,
    "flesch": 76,
    "browse": "http://carrels.distantreader.org/author-homer-gutenberg/index.xml",
    "download": "http://carrels.distantreader.org/author-homer-gutenberg/index.zip",
    "read": "http://carrels.distantreader.org/author-homer-gutenberg/index.htm",
    "bibliography (JSON)": "http://carrels.distantreader.org/author-homer-gutenberg/index.json",
    "bibliography (plain text)": "http://carrels.distantreader.org/author-homer-gutenberg/index.txt",
    "metadata": "http://carrels.distantreader.org/author-homer-gutenberg/index.csv",
    "provenance": "http://carrels.distantreader.org/author-homer-gutenberg/index.tsv",
    "gml (Graph Modeling Language)": "http://carrels.distantreader.org/author-homer-gutenberg/index.gml",
    "RDF/XML": "http://carrels.distantreader.org/author-homer-gutenberg/index.rdf",
    "keywords": "son; trojans; ulysses; achaeans; man; ships; hector",
    "date": "2024-12-20"
  }`


---
Eric Lease Morgan &lt;eric_morgan@infomotions.com&gt;  
July 20, 2025
