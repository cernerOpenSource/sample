#!c:\Python27\python.exe
#!/usr/bin/env python

import nltk
import csv
n=0
f=open('name.txt','r')
for i in f:
    a=i
fname="BADREVIEW.csv"
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
        <a href="homepage.html"><img src='/spamlogo.jpg' alt='individual' width='286' height='66' border='0' /></a>
          <ul>
          <li><a href="homepage.html">home</a></li>
          <li><a href="about.html">about us</a></li>
          <li><a href="contactus.html">contact us</a></li>
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
                 <form><fieldset><legend><p style="font-family:arial;color: #077733;font-size:18px;">REVIEW LIST</p></legend>
         <font color="#7642A3" size="+2"> <b>Hello """+a+"""</font></b><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a><a href="/cgi-bin/backbutton.py"><img src='/back.jpg' align='right'></a> 
                <br>
                
                
                <center>
                <br class="spacer" />
                <br class="spacer" />
                <font color="#7642A3" size="+1"><bold>LIST OF SAMPLE REVIEWS</bold></font><br>
                <table style="border-style: groove" width="800px" height="300px">
                <tr align="center" bgcolor="#BCEBBC">
                <th width="230px">Username</th>
                <th>Product Id </th>
                <th>Review</th>
                </tr>
                
            

    """
fo = open(fname)
reader = csv.reader(fo)
fi= open("pro.csv")
read = csv.reader(fi)
n=0    
from textblob import TextBlob
for r in reader:
    review=TextBlob(r[5])
    w=0
    if review.sentiment.subjectivity < 0.5:
       w=w+10
       
    else:
       w=w+0
    helpful=float(r[6])
    outof=int(r[7])
    if outof==0:
        w=w+0.1
    else:
        if outof < 9:
            value=helpful*outof
            ratio=value/outof
            if ratio<0.8:
                w=w+0.05
            else:
                w=w+10
        else:    
            value=helpful*outof
            ratio=value/outof
            if ratio<0.8:
                w=w+0.2
            else:
                w=w+10
    found=0
    star=0.0
    if review.sentiment.polarity>=0:
        flag="pos"
    else:
        flag="neg"
    for z in read:
        if str(z[0])==str(r[0]):
            star=float(z[5])
            found=1
    
    if found==0:
        star=float(3.5)
    if star<=3 and flag=="neg":
        w=w+10
    else:
        if star>3 and flag=="pos":
            w=w+10
        else:
            w=w+0.4
    
    fi.close()
    
    fi= open("BAD.csv")

    read = csv.reader(fi)
    if w>=30 and n<5:
        n=n+1
        print """
                    
                        
                            <tr align="center" bgcolor="#BCEBBC">
                            
                            <td>"""+r[0]+"""</td>
                            <td>"""+r[2]+"""</td>
                            <td>"""+r[5]+"""</td>
                            
                            </tr>
                """
    
print """

                    </table>
                    </center>
                    
                  
        </form><center>

        </blockquote> 
                        
                <br class="spacer" />
                <br class="spacer" />
                <br class="spacer" />
              
                
                        </div>
                        <!--body end -->
                        <!--footer start --><!--footer end -->
                </body>
                </html>
                
            """
    
    
    
        
        
        
  
