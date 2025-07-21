

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


Filtering JSON Output: Getting Study carrel Identifiers
-------------------------------------------------------

Each study carrel is described and characterized with a number of metadata elements, as the the following JSON snippet illustrates:

<pre>  {
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
  }</pre>

Elaborating on the meaning of each metadata element is beyond the scope of this document. That said, one has to choose a specific study carrel identifier ("id") in order to go forward. Enumerating identifiers and narrowing them down to a more managable number can be done through the use of jq "filters". Alas, filters are also beyond the scope of this document. Still, the following command will output a list of study carrel identifiers containing "homer":

    curl -H "Accept: application/json" http://carrels.distantreader.org | jq -r '.[]|.id' | grep homer
 
The result ought to be a list of study carrel identifiers and look something like this:

<pre>
  author-homer-freebo
  author-homer-gutenberg
  author-homer_austen_and_thoreau-gutenberg
  subject-homer-gutenberg
</pre>

Filters can be quite expressive, and here is a command which searches the catalog for items described with the keyword "knowledge", returns the associated identifiers and keywords, and pipes the result to less for browsing:

	curl -H "Accept: application/json" http://carrels.distantreader.org | jq -r '.[]|[.id,.keywords]|@tsv' | grep knowledge | less -S -x 64

Repeat the previous two commands with different search terms. Such will give you flavor for the scope of the study carrels. For extra credit, read and practice on jq filters. By design, there is no search interface to the study carrels at http://carrels.distantreader.org. See http://catalog.distantreader.org or http://index.distantreader.org instead.


Exploring and Reading Specific Study Carrels
--------------------------------------------

Once you have identified a study carrel of interest, the full functionality of content-negotiaion comes into play. Thus, this section introduces how to explore and read specific study carrels.

Remember, study carrels are data sets, and each study carrel is rooted in exactly the same data structure. See an [example readme file](./etc/readme.txt) associated with each study carrel to learn about this structure.

Now, for fun, let's use English translations of Homer's Iliad and Odyssey as an example. The identifier in question is author-homer-gutenberg. First, request a summary of the carrel's content, and the result will be an HTML stream intended to be rendered by the typical Web browser:

	curl -H 'Accept: text/html' http://carrels.distantreader.org/author-homer-gutenberg/

This same resource -- http://carrels.distantreader.org/author-homer-gutenberg/ -- has been modeled in a number of different ways and for different purposes. For example, a plain text version of the resource returns a bibliographic descxription of each item in the carrel:

	curl -H 'Accept: text/plain' http://carrels.distantreader.org/author-homer-gutenberg/

The same information can be garnered as JSON, and one can then use jq filters extract and reformat the results:

	curl -H 'Accept: application/json' http://carrels.distantreader.org/author-homer-gutenberg/ | \
	jq | \
	less -S

For example you can merely output all of the identifiers in the carrel:

	curl -H 'Accept: application/json' http://carrels.distantreader.org/author-homer-gutenberg/ | \
	jq -r '.[].id'
	
Many, if not most or all, of the carrels are associated with linked data (RDF/XML) files. To get the RDF/XML file of this carrel, try:

	curl -H 'Accept: application/xml' http://carrels.distantreader.org/author-homer-gutenberg/

For extra credit, pipe the result through a utility called "xmllint" and then your pager for better readability:

	curl -H 'Accept: application/xml' http://carrels.distantreader.org/author-homer-gutenberg/ | \
	xmllint --format - | \
	less -S

Get the whole carrel:

	curl -H 'Accept: application/zip' http://carrels.distantreader.org/author-homer-gutenberg/ > author-homer-gutenberg.zip

---
Eric Lease Morgan &lt;eric_morgan@infomotions.com&gt;  
July 20, 2025
