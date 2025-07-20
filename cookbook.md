

Cookbook
========

This "cookbook" demonstrates how to exploit content-negotiation techniques against the HTTP server at http://carrrels.distantreader.org from the command-line within your terminal. 


Getting Started
---------------

First, you will need a command-line user-agent application. Install an application called "curl", a very well respected piece of software. See https://curl.se.

Next, open up your terminal application, and request content from the server. By default, the server will respond with a stream of HTML intended to be rendered by a Web browser such as Chrome, Firefox, or Safari:

	curl http://carrels.distantreader.org

Now, do the same thing, but specifically request HTML content:

	curl -H "Accept: text/html" http://carrels.distantreader.org

If you request a type of content that is not valid for any reason, then the server will return HTTP error 406 (Not Acceptable) as well as an HTML snippet outlining that content types are acceptable:

	curl -H "Accept: foo/bar" http://carrels.distantreader.org

Power users may way to add the -I switch to the command, and the result will be a bit more computer-friendly, but not necessarily more readable:

	curl -I -H "Accept: foo/bar" http://carrels.distantreader.org


# CSV output

# in the form of CSV, get a list of all carrels
curl -L -H "Accept: text/csv" http://carrels.distantreader.org

# do the same but save the result to a file
curl -L -H "Accept: text/csv" http://carrels.distantreader.org > catalog.csv

# install csvkit, a software suite for CSV manipulation
pip install csvkit

# get a list of all carrels and pipe the to csvlook for browsing purposes
curl -L -H "Accept: text/csv" http://carrels.distantreader.org | csvlook | less -S


# JSON output; CVS output is okay, but JSON is often more preferable

# in the form of JSON, get a list of all carrels
curl -L -H "Accept: application/json" http://carrels.distantreader.org

# install jq, a software suite for JSON manipulation; see https://jqlang.org

# get a list of all carrels and pipe the result to jq for browsing purposes
curl -L -H "Accept: application/json" http://carrels.distantreader.org | jq | less -S

---
Eric Lease Morgan &lt;eric_morgan@infomotions.com&gt;  
July 20, 2025
