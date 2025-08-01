

Reader Content-Negotiation
==========================

This software suite describes and demonstrates how to apply an HTTP application programmer interface called "content-negotiation" against the root as well as the underlying content of http://carrels.distantreader.org. Equipped with a knowledge of this interface, the developer will be able to compute against Distant Reader content in whatever programming language they desire. More importantly, the developer will be able to read, use, understand, and create alternative interfaces to the 100's of thousands of items in the Reader's library. 


Introduction
------------

At its core, HTTP is a client-server protocol. A client application -- often called the "user-agent" -- sends a request to a server application. This request takes the form of a URL. The server processes the request and returns the result. The result is usually HTML intended to be rendered by the user-agent -- usually your Web browser.

But such is an overly simplified interpretation of HTTP. In reality user-agent requests can include a great deal more information than a simple URL, and most user-agents do send a great deal more information. For example, user-agents may send information naming the user-agent: Chrome, Firefox, Safari, etc. User-agents may send creditials for the purposes of access control (authentication and authorization). The most common type of additional information is used to elaborate on the given URL usually for the purposes supporting search.

For the purposes of this software suite, we are interested in the user-agent requesting a URL as well as a content-type; we want to specify the format of result, and again, this is called "content-negotiation". Put another way, HTML is not always the most desireable format of the returned result because HTML is not as machine-readable as to be expected; while HTML can be both well-formed and valid, it is usually not, and if it is, parsing it is usually overly complicated. (This is why I usually run the other way when a project requires screen scraping.)

"So," you might ask, "what kinds of formats might the user-agent request?" The short answer is, "Formats easily readable by computer applications." The longer answer is, "Highly structured formats such as but not limited to: comma-separated values (CVS), tab-separated values (TSV), Extensible Mark-up Langauge (XML), well-formed and valid HTML (XHTML), JavaScript Object Notation (JSON), or Graph Modeling Language (GML) formats. Other, less computable but often very useful formats include plain text, compressed zip, and Portable Document Format (PDF) formats."

And then you might say, "So what? Why should I care?" To which I reply, "Information is manifested in many formats, and different formats lend themselves to different intepretations of the given information. By requesting different content-types from an HTTP server, the developer -- working in conjuction with domain experts -- is empowered to interpret the given information in their own ways and/or enabled to create interfaces to the information which the developer (and domain expert) find more useful.

For more detail regarding the why's and wherefore's of content-negotiation, see: 1) [the official documentation](https://www.rfc-editor.org/rfc/rfc9110.html#name-content-negotiation), 2 [content-negotiation as implemented with the Apache HTTP server](https://httpd.apache.org/docs/current/content-negotiation.html), or a [more readable description](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation) from the Mozilla Foundation.

"Okay. I'm sold. Now what?" Read on.


Reader Implemented Content-Types
--------------------------------

The HTTP server at http://carrels.distantreader.org hosts a collection of approximately 3,000 data sets affectionately called "study carrels". As data sets, the study carrels are designed to be read by computer applications as well as people. More importantly, each study carrel is rooted in one or more narrative documents (PDF files, Word files, email messages, plain text files, etc.) and modeled in a variety of ways. Through the exploitation of study carrels the student, researcher, or scholar can read, use, and understand large volumes of content quickly and easily. For more detail about study carrels, see an [example readme file](./etc/readme.txt) associated with each carrrel.

The HTTP server at http://carrels.distantreader.org has been configured to accept and process a variety of different content-types, and each type is associated with a different format of information. Given the root URL -- http://carrels.distantreader.org -- and the content-types listed below, the developer can download, interact with, and intepret study carrel information in ways only limited by their imagination. The configured content-types and formats are listed here:

| content-types         | formats                       |
| --------------------- | ----------------------------- |
| application/json      | JSON                          |
| application/xhtml+xml | well-formed and valid HTML    |
| application/xml       | RDF/XML                       |
| application/zip       | compressed zip                |
| text/csv              | comma-separated values (CSV)  |
| text/gml              | Graph Modeling Language (GML) |
| text/html             | generic HTML                  |
| text/plain            | plain text                    |
| text/tsv              | tab-separated values (TSV)    |
| text/xml              | generic XML                   |

So how can this be exploited? Well, for example, we can employ a user-agent called "[curl](https://curl.se)" to request an HTML version of the content at the root of http://carrels.distantreader.org:

	curl -L -H 'Accept: text/html' http://carrels.distantreader.org

The result will be a very long HTML stream listing all of the study carrels in the collection and the briefest of descriptions of each. This result is intended to be rendered by forgiving and Javascript-enable Web browsers like Chrome, Firefox, or Safari.

But HTML is often verbose and not easily parsable. To overcome this limitation, we can request a CSV version of the same data:

	curl -L -H 'Accept: text/csv' http://carrels.distantreader.org

Or, if you prefer, a JSON version:

	curl -L -H 'Accept: application/json' http://carrels.distantreader.org

In either case, the result is a set of well-structured information easily parsable by any number of computer programming language libraries and/or desktop applications. For example, the the CSV format output can be directed to a file and then opened in your favorite spreadsheet application or analysis program (like [OpenRefine](https://openrefine.org)):

	curl -L -H 'Accept: text/csv' http://carrels.distantreader.org > carrels.csv

Summary
-------

The host at http://carrels.distantreader.org/ is configured to support an HTTP protocol called "content negoitation". Send it a GET request and an Accept header, and the host will respond with different models of the given resource. This works for the root node, the second-level resource nodes, and most of the third level study carrel directories. 

Next Steps
----------

Practice with this distribution's [Cookbook](./cookbook.md) where you will find one-liner techniques of getting content from the server. Once you get that far, peruse the [collection of Python](./bin) scripts to see how the content can get got and then processed.

---
Eric Lease Morgan &lt;eric_morgan@infomotions.com&gt;  
July 19, 2025

