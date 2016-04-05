#!c:\Python27\python.exe
#!/usr/bin/env python
import os
import cgi, cgitb 
import re
from nltk.corpus import stopwords
from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize import word_tokenize
from replacers import RegexpReplacer
replacer = RegexpReplacer()
import csv
from nltk.corpus import wordnet
from nltk.tokenize.punkt import PunktSentenceTokenizer
from replacers import SpellingReplacer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
form = cgi.FieldStorage()
f=open('name.txt','r')
for i in f:
    a=i
fileitem = form['file']
f1=open('file.txt','w')
fname=fileitem.filename
f1.write(fname)
print "Content-Type: text/html"
print
print """
    <html>
    <head>
    <title>Spam Fighter</title>
    <link href='/style.css' rel='stylesheet' type='text/css' />
    </head>
    <body>
            <!--top part start -->
            <div id="top">
    <a href="/homepage.html"><img src='/spamlogo.jpg' alt='individual' width='286' height='66' border='0' /></a>
      <ul>
      <li><a href="/homepage.html">home</a></li>
      <li><a href="/about.html">about us</a></li>
      <li><a href="/contactus.html">contact us</a></li>
      </ul>
            </div>
            <!--top part end -->
            <!--header start -->
            <div id="header">
            <h2><span>Why Spam Fighter???</span></h2>
            <p>It has become a common practice for people to read online opinions/reviews for different purposes. For example, if one wants to buy a product, one typically goes to a review site (e.g., amazon.com) to read some reviews of the product. If most reviews are positive, one is likely to buy the product. If most reviews are negative, one will almost certainly not buy it. Positive opinions can result in significant financial gains and/or fames for busineses, organizations and individuals. This, unfortunately, gives strong incentives for opinion spamming.</p>
            </div>
            <!--header end -->
            <!--body start -->
            <div id="body" style="color:#000">
            <br class="spacer" style="color:#000" />
      <!--left panel start --><!--left panel end -->
       <!--mid panel start --><!--mid panel end -->
        <!--right panel start --><!--right panel end -->
            <!--bodyBottom start --><!--bodyBottom end-->
            <blockquote>
             <blockquote>
            <font color="#7642A3" size="+2"> <b>Hello """+a+"""</font></b></center><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a><a href="/cgi-bin/backbutton.py"><img src='/back.jpg' align='right'></a>
<center>
        
         <center><b><font color="#7642A3">File uploaded successfully!!</font></b></center>
         <table width="200" border="1" cellpadding="25">
      <tr>
<td><center><a href="/cgi-bin/allfeaturefile.py" ><bold><font color="#7642A3">FAKE USERS(LIST)</font></bold></a></center></td>
<td><center><a href="/cgi-bin/plotuser.py" ><bold><font color="#7642A3">FAKE USERS(PLOT)</font></bold></a></center></td></tr>
     <tr><td><center><a href="/cgi-bin/reviewpolar.py" ><bold><font color="#7642A3">FAKE REVIEWS(LIST)</font></bold></a></center>
     </td>
     <td><center><a href="/cgi-bin/plotreview.py" ><bold><font color="#7642A3">FAKE REVIEWS(PLOT)</font></bold></a></center>
     </td>
    
     
     </tr>
    </table>
     </center>
      <center><a href="/cgi-bin/recommend.py" ><bold><font color="#7642A3">SAMPLE REVIEWS</font></bold></a></center>
     <center>
      </blockquote>
     </blockquote>
    <br class="spacer" />
    <br class="spacer" />
    <br class="spacer" />
    <br class="spacer" />
    <br class="spacer" />
    
    <br class="spacer" />
            </div>
            <!--body end -->
            <!--footer start --><!--footer end -->
    </body>
    </html>
    
"""

"""# open and read the csv file into memory
file = open(fileitem.filename)
reader = csv.reader(file)
# iterate through the lines and print them to stdout
# the csv module returns us a list of lists and we
# simply iterate through it
replacer = SpellingReplacer()
fo1=open("c-expansion.txt","a+")

fo6=open("h-synset.txt","a+")
fo5=open("g-spellcheck.txt","a+")
fo4=open("f-stemmingwords.txt","a+")
fo3=open("e-wordswithoutstopwords.txt","a+")
fo2=open("d-words.txt","a+")
fo=open("a-sentence.txt","a+")
for line in reader:
    a= PunktSentenceTokenizer().tokenize(line[7])
    fo.write('\n'.join(a))
    review='\n'.join(a)
    review = review.lower()
    #Convert www.* or https?://* to URL
    review = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',review)
    #Convert @username to AT_USER
    review = re.sub('@[^\s]+','AT_USER',review)
    #Remove additional white spaces
    review = re.sub('[\s]+', ' ', review)
    #Replace #word with word
    review = re.sub(r'#([^\s]+)', r'\1', review)
    review=re.sub('\.',' ',review)
    review=re.sub('\!','',review)
    review=re.sub('\,','',review)
    #trim
    review = review.strip('\'"')
    fo7=open("b-clean.txt","a+")
    fo7.write(review+"\n")
    q=replacer.replace(review)
    fo1.write(q)
    z= PunktSentenceTokenizer().tokenize(q)
    for m in z:
        b=word_tokenize(m)
        fo2.write('\n'.join(b)+"\n")
        
        for j in b:
            if j not in '\n'.join(english_stops):
                fo3.write(j+"\n")
                
                
            else:
                continue
            f=stemmer.stem(j)
            fo4.write(f+"\n")
            g=replacer.replace(f)
            fo5.write(g+"\n")
            if(not wordnet.synsets(g)):
                fo6.write(g+"\n")
            else:
                h=wordnet.synsets(g)[0].lemmas[0]
                fo6.write(h.name+"\n")
            
        
        
fo1.close()
fo.close()
fo2.close()
fo3.close()
fo4.close()
fo5.close()
fo6.close()
fo7.close()"""
