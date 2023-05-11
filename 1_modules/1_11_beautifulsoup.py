# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.11: Beautifulsoup in Python 
# python 1_11_beautifulsoup.py
blank = "----------------------"

from bs4 import BeautifulSoup

# Beautifulsoup 
# Beautiful Soup is a Python package for parsing HTML and XML documents .
# (including having malformed markup, i.e. non-closed tags, so named after tag soup) 
# It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

##############################################################################################################

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seperate Ways</title>
</head>
<body>
    
    <h1 id="header">
        Seperate Ways
    </h1>

    <div class="group_1">
        <h2>
            He're we stand
        </h2>
       
        <ul> <!--like list-->
            <li>Worlds apart, hearts broken in two, two, two</li>
            <li>Sleepless nights</li>
            <li>Losing ground, I'm reachin' for you, you, you</li>
        </ul>
    </div>

    <div class="group_2">
        <h2>
            Feelin' that it's gone
        </h2>

        <ul>
            <li>Could change your mind</li>
            <li>If we can't go on</li>
            <li>To survive the tide, love divides</li>
        </ul>
    </div>

    <div class="group_3">
        <h2>
            Someday, love will find you
        </h2>

        <ul>
            <li>Break those chains that bind you</li>
            <li>One night will remind you</li>
            <li>How we touched and went our separate ways</li>
        </ul>
    </div>

    <!-- <img src="uncharted.jpg" alt=""> -->

</body>
</html>
"""

##############################################################################################################

# Usage of Beautifulsoup

soup = BeautifulSoup(html_doc, 'html.parser')
# result = soup.prettify() # normally our html_doc file content was incorrect but prettify regulates
# result = soup.title # gets whole title
# result = soup.head # gets whole head
# result = soup.body # gets whole body
# result = soup.title.name # gets label of "title"
# result = soup.title.string # gets what is written inside title
# result = soup.h1 # gets h1
# result = soup.h2 # gets first h2 
# result = soup.find_all('h2') # gets whole data labelled with h2 
# result = soup.find_all('h2')[0] # gets whole data labelled with h2 (first)
# result = soup.find_all('h2')[1] # gets whole data labelled with h2 (second)
# result = soup.div # gets first div
# result = soup.find_all('div')[1].ul # gets first div's ul
# result = soup.find_all('div')[1].ul.find_all('li') # gets first div's ul's whole li data
# result = soup.div.findChildren() # prints all child labels under div
result = soup.div.findNextSibling() # Now displays group_2
result = soup.div.findNextSibling().findNextSibling() # Now displays group_3
result = soup.div.findNextSibling().findPreviousSibling() # Now displays group_1



print(result)
print(blank)
