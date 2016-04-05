#!c:\Python27\python.exe
#!/usr/bin/env python
import cgi, cgitb
import csv
import collections
import sqlite3
import re
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
         <font color="#7642A3" size="+2"> <b>Hello</font></b><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a><a href=""><img src='/back.jpg' align='right'></a> 
                <br>
                
                
                <center>
                <br class="spacer" />
                <br class="spacer" />
                <font color="#7642A3" size="+1"><bold>LIST OF FAKE USERS</bold></font><br>
                <table style="border-style: groove" width="300px" height="300px">
                <tr align="center" bgcolor="#BCEBBC">
                <th >Username:</th>
                
                </tr>
            

    """

def sameuserid_feature(filename):
    file = open(filename)
    c = csv.reader(file)
    unor=[]
    i=0
    for row in c:
        unor.append(row[0])
    b=set(unor)
    i=len(b)
    
    file.close()
    file = open(filename)
    c = csv.reader(file)
    con = sqlite3.connect("PROJECT")
    cursor = con.cursor()
    for a in b:
        count=0
        for row in c:
            if str(a)==str(row[0]):
                count=count+1
        weight=float((count*100))/float(i)
        
        
        cursor.execute("insert into urlweight \
                        values(?,?)",(a,weight))
        con.commit()
        
        file.close()
        file = open(filename)
        c = csv.reader(file)
def star_feature(filename):
    file = open(filename)
    c=csv.reader(file)
    f1=open("pro.csv")
    c1=csv.reader(f1)
    unor=[]
    for row in c:
        unor.append(row[0])
    b=set(unor)
    file.close()
    file = open(filename)
    c = csv.reader(file)
    con = sqlite3.connect("PROJECT")
    cursor= con.cursor()
    for r in c1:
        avgstar=int(float(r[5]))
    w=0
    count=0
    for a in b:
        for row in c:
            if str(a)==str(row[0]):
                d=row[5].strip('stars')
                x1=int(float(d))
                if x1==0:
                    x1=3.5
                w=w+x1
                count=count+1
        if (float(w)/float(count))<avgstar:
            status="yes"
        else:
            status="no"
        cursor.execute("insert into urlstar \
                        values(?,?)",(a,status))
        con.commit()
        
        file.close()
        file = open(filename)
        c = csv.reader(file)
def length_feature(filename):
    mainlist=[]
    con = sqlite3.connect("PROJECT")
    cur = con.cursor()
    file = open(filename,"rb")
    c = csv.reader(file)
    i=0
    a=[]
    total=0
    for row in c:
        total=total+len(row[6])
        i=i+1
        mainlist.append(row[0])
    i=i-1
    mean=total/i
    main=set(mainlist)
    #print mean
    file.close()
    file = open(filename,"rb")
    c = csv.reader(file)
    for col in c:
        l=len(col[6])
        if l<=mean/2:
           a.append(col[0])
    fakereviewer=set(a)
    x=0
    for k in main:
        #print k
        if k in fakereviewer:
            status="yes"
        else:
            status="no"
        cur.execute("insert into urllength \
        values(?,?)",(k,status))
        con.commit()       
def pronoun_feature(filename):
    file = open(filename)
    c = csv.reader(file)
    unor=[]
    for row in c:
        unor.append(row[0])
    b=set(unor)
    #print b
    file.close()
    file = open(filename)
    c2 = csv.reader(file)
    con = sqlite3.connect("PROJECT")
    cursor = con.cursor()
    for a in b:
        for row in c2:
            if str(a)==str(row[0]):
                
                tagged_sent = nltk.pos_tag(row[6].split())
                
                personalpronoun=[word for word, pos in tagged_sent if pos == 'PRP']
                status="no"
                for i in personalpronoun:
                    count=0
                    c=0
                    if i.lower()=='i' or i.lower()=='me' or i.lower()=='myself' or i.lower=='we' or i.lower()=='our' or i.lower()=='ourself':
                        count=count+1
                    else:
                        c=c+1
                    
                    if c>count:
                        status="yes"    
                    
                        
                #print row[0],status
                cursor = con.execute("SELECT uid,status from urlpronoun where uid=?",(row[0],))
                if cursor.fetchone():
                    cursor.execute("UPDATE urlpronoun SET status=? WHERE uid=?", (status, row[0]))
                else:
                    cursor.execute("insert into urlpronoun \
                        values(?,?)",(row[0],status))
                con.commit()
        file.close()
        file = open(filename)
        c2 = csv.reader(file)
            
    file.close()            
        
                
        
sameuserid_feature('userrev.csv')

star_feature('userrev.csv')

length_feature('userrev.csv')
pronoun_feature('userrev.csv')
file = open('userrev.csv')
c = csv.reader(file)
#calculating weights
unor=[]
for row in c:
    unor.append(row[0])
b=set(unor)
con = sqlite3.connect("PROJECT")
cursor = con.cursor()
for a in b:
    #w=0.3
    cursor = con.execute("SELECT weight from urlweight where uid=?",(a,))
    for row in cursor:
        weight=row[0]
    #w=0.4
    cursor = con.execute("SELECT status from urlstar where uid=?",(a,))
    for row in cursor:
        status2=row[0]
    #w=0.2
    cursor = con.execute("SELECT status from urllength where uid=?",(a,))
    for row in cursor:
        status3=row[0]
    #w=0.1
    cursor = con.execute("SELECT status from urlpronoun where uid=?",(a,))
    for row in cursor:
        status4=row[0]
    w1=w2=w3=w4=0
    if weight>0.5:
        w1=0.33
    if status2=="yes":
        w2=0.27
    if status3=="yes":
        w3=0.25
    if status4=="yes":
        w4=0.15
    total=w1+w2+w3+w4
    #print a,total
    print 
    cursor.execute("insert into urlfinal \
                        values(?,?)",(a,total))
    con.commit()
cursor = con.execute("SELECT uid,weight from urlfinal")


for row in cursor:
    
    if row[1]>0.5:
        
        print """
                
                    
                        <tr align="center" bgcolor="#BCEBBC">
                        
                        <td>"""+row[0]+"""</td>
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

        
        



    
    

    
