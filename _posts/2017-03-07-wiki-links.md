---
layout: page
title: "Graphing Wikipedia: Six Degrees Confirmed?"
date: 2016-03-07
time: 1
categories: Report
image: graph-theory
permalink:  wikilinks
---
Have you ever played the "Wikipedia Game"? You know, the game where you try to find out how many clicks it takes you to get from one article on Wikipedia to another? That was the inspiration behind this project.

The goal: Create a graph of Wikipedia with articles as the nodes and links to other articles as directed edges.
$$diameter = \frac{\ln(n)}{\ln(K)}\approx average \ path \  length$$

$$\\ n = nodes \ in \ graph \\ K = average \ node \ degree$$

The results:

* A python script that parses the huge 50+ gigabyte XML dump of all of Wikipedia into a MySQL database.
* Said database is a series of one to many tables that contain article titles, links to other articles, and redirects (links that are titled one thing but lead to another (e.x. "1950's Cars" -> "Post WWII Automotive Boom")
* A breath first search loosely based on Dijkstra's algorithm to find the shortest path between two articles.
* Some neat data:

### Cool data


![Pie chart wikipedia articles linking to adolph hitler](/img/links-to-adolph.jpg)


There is also a Wikipedia page dedicated to the idea of "The Six Degrees of Wikipedia". On this page, users have posted interesting paths between articles. Others post record short paths between articles that they have found. I have been a frequent editor of this page lately.

### Ideas?

What would you do with a graph of Wikipedia?
Any particular path you want to see?

Let me know in the comments below and I'll do my best to reply.

### The future

Since we choose python for this project, migrating to flask and making this a web application is a possibility. However, without an SSD hosting the database or loading the whole 8 GB database into memory this program is incredibly slow. And SSD/+8 GB servers are not cheap.

David, my partner in this project, and I (with our naive understanding of graphs and databases) built a graph using MySQL. We are now aware of specialized graph theory databases like Neo4J that will make our program mush faster.

Finally, the database must be rebuilt every time Wikipedia releases a new XML dump for it to remain current. Otherwise, the path created may not be valid in practice. An automated program that looks for a new file then downloads and parses it into a new database is in order.

Its on my huge TODO list to port this to Neo4J and then to flask and make this tool available for free for everyone. Never again may you loose the Wikipedia game!
