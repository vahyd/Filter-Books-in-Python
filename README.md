# Filter Books

The program reads in records from three diffeernt input files and then outputs the list with command line options to sort or filter them.

The format of the input files are,

pipe:
First name | Last name | Book Title | Book Publication Date

slash:
Book Publication Date/First name/Last name/Book Title

csv:
Book Title, Last Name, First name, Book Publication Date


Here is the program signature:

usage: books.py [-h] [--filter FILTER] [--year] [--reverse]

Show a list of books, alphabetical ascending by author's last name

optional arguments:
  -h, --help       show this help message and exit
  --filter FILTER  show a subset of books, looks for the argument as a substring of any of the fields
  --year           sort the books by year, ascending instead of default sort
  --reverse        reverse sort

Here are some sample runs of the program

python books.py --filter 199 --reverse
McConnell, Steve, Code Complete, 1993
Fowler, Martin, Refactoring, 1999

python books.py --filter er --year
Fowler, Martin, Refactoring, 1999
Fowler, Martin, Patterns of Enterprise Application Architecture, 2002
Beck, Kent, Implementation Patterns, 2007
Martin, Robert, Clean Code, 2008

python books.py
Beck, Kent, Test-Driven Development, 2002
Beck, Kent, Implementation Patterns, 2007
Brooks, Fred, The Mythical Man-Month, 1975
Crockford, Douglas, Javascript: The Good Parts, 2008
Fowler, Martin, Refactoring, 1999
Fowler, Martin, Patterns of Enterprise Application Architecture, 2002
Martin, Robert, Clean Code, 2008
McConnell, Steve, Code Complete, 1993
Shore, James, The Art of Agile Development, 2008

Filter_Books.ipynb shows the output without considering filters!
