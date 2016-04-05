#!c:\Python27\python.exe
#!/usr/bin/env python

import nltk
import csv
file=open('name.txt','r')
for i in file:
    a=i
f=open('file.txt','r')
for j in f:
    b=j
    
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
                 <form><fieldset><legend><p style="font-family:arial;color: #077733;font-size:18px;">PROFILE</p></legend>
         <font color="#7642A3" size="+2"> <b>Hello"""+a+"""</font></b><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a><a href=""><img src='/back.jpg' align='right'></a> 
                <br>
                
                
                <center>
                <br class="spacer" />
                <br class="spacer" />
                <font color="#7642A3" size="+1"><bold>MOST RELIABLE REVIEWS</bold></font><br>
                <table style="border-style: groove" width="800px" height="300px">
                <tr align="center" bgcolor="#BCEBBC">
                <th width="230px">Username</th>
                <th>Product Id </th>
                <th>Review</th>
                </tr>
                
            

    """
fo = open(b)
reader = csv.reader(fo)
fi= open("pro.csv")
read = csv.reader(fi)
    
from textblob import TextBlob
for r in reader:
    review=TextBlob(r[7])
    w=0
    r=0
    if review.sentiment.subjectivity < 0.5:
       w=w+0.1
       
    else:
       w=w+0
    helpful=float(r[3])
    outof=int(r[4])
    if outof==0:
        w=w+0.1
    else:
        if outof < 9:
            value=helpful*outof
            ratio=value/outof
            if ratio<0.5:
                w=w+0.05
            else:
                w=w+0
        else:    
            value=helpful*outof
            ratio=value/outof
            if ratio>0.8:
                r=10
            else:
                w=0
    found=0
    star=0.0
    if review.sentiment.polarity>=0:
        flag="pos"
    else:
        flag="neg"
    for z in read:
        if str(z[0])==str(r[1]):
            star=float(z[5])
            found=1
    
    if found==0:
        star=float(3.5)
    if star<=3 and flag=="neg":
        w=w+0
    else:
        if star>3 and flag=="pos":
            w=w+0
        else:
            w=w+0.4
    
    fi.close()
    
    fi= open("pro.csv")

    read = csv.reader(fi)
    
    if r==10:
        print """
                    
                        
                            <tr align="center" bgcolor="#BCEBBC">
                            
                            <td>"""+r[0]+"""</td>
                            <td>"""+r[1]+"""</td>
                            <td>"""+r[7]+"""</td>
                            
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
    
    
    
        
        
        
  
