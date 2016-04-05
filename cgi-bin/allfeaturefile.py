#!c:\Python27\python.exe
#!/usr/bin/env python
import cgi, cgitb
import csv
import collections
import sqlite3
import nltk
import numpy
file=open('name.txt','r')
for i in file:
    a=i
#normalised length
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
                 <form><fieldset><legend><p style="font-family:arial;color: #077733;font-size:18px;">FAKE REVIEW IDENTIFICATION</p></legend>
         <font color="#7642A3" size="+2"> <b>Hello"""+a+"""</font></b><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a><a href=""><img src='/back.jpg' align='right'></a> 
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
    file = open("userrev.csv","rb")
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
        cur.execute("insert into feature4length \
        values(?,?)",(k,status))
        con.commit()
    #for k in fakereviewer:
        #x=x+1
     #   cur.execute("insert into feature1brand \
      #  values(?,?)",(a,status))
    
        #print k
    #print x
#Average rating using star
def star_feature(filename):
    file = open("userrev.csv","rb")

    f1=open("pro.csv")
    c=csv.reader(f1)
    q=0
    f=0
    c1 = csv.reader(file)
    unor=[]
    for row in c1:
        unor.append(row[0])
    b=set(unor)
    file.close()
    file = open("userrev.csv")
    c2 = csv.reader(file)
    l=[]
    con = sqlite3.connect("PROJECT")
    cur = con.cursor()
    for a in b:
        #print a,
        for row1 in c2:
            if str(a)==str(row1[0]):
                #print row1[1],
                for row2 in c:
                    if str(row1[1])==str(row2[0]):
                        #print row2[5],
                        x1=int(float(row2[5]))
                        x2=int(float(row1[4]))
                        if x1==0:
                            x1=3.5
                        star=x2/x1*100
                        if star<=50:
                            stat="yes"
                        else:
                            stat="no"
                        #print stat
                        l.append(stat)    
                    
                        break
                        
                        
                f1.close()
                f1=open("pro.csv")
                c=csv.reader(f1)
        for i in l:
            #print i
            if str(i)==str("yes"):
                q=q+1
            f=f+1
        l=[]
        #print q,f
        if q>=f:
            status="yes"
        else:
            status="no"
        q=0
        f=0
        #print a,status
        cur.execute("insert into feature2stars \
                values(?,?)",(a,status))
        con.commit()
        #print "\n"
        file.close()
        file = open("userrev.csv")
        c2 = csv.reader(file)
                
    file.close()

#Pronoun ratio
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
                cursor = con.execute("SELECT uid,status from feature3pronoun where uid=?",(row[0],))
                if cursor.fetchone():
                    cursor.execute("UPDATE feature3pronoun SET status=? WHERE uid=?", (status, row[0]))
                else:
                    cursor.execute("insert into feature3pronoun \
                        values(?,?)",(row[0],status))
                con.commit()
        file.close()
        file = open(filename)
        c2 = csv.reader(file)
            
    file.close()
#Brand id
def brand_feature(filename):
    file = open(filename)
    c = csv.reader(file)

    f1=open("pro.csv")
    c1=csv.reader(f1)

    unor=[]
    for row in c:
        unor.append(row[0])
    b=set(unor)
    file.close()
    file = open(filename)
    c = csv.reader(file)
    l=[]
    import sqlite3
    con = sqlite3.connect("PROJECT")
    cur = con.cursor()
    for a in b:
        #print a,
        for row1 in c:
            if str(a)==str(row1[0]):
                #print row1[1],
                for row2 in c1:
                    if str(row1[1])==str(row2[0]):
                        #print row2[2],
                        if row2[2]==0:
                            row2[2]=1
                        l.append(row2[2])
                        break
                f1.close()
                f1=open("pro.csv")
                
                c1=csv.reader(f1)
        new=collections.Counter(l)
        length=len(l)
        
        m=new.values()
        #print m
        for d in m:
                z=(d/length)*100
                
                if z>=40:
                    status="no"
                else:
                    status="yes"
        cur.execute("insert into feature1brand \
            values(?,?)",(a,status))
        con.commit()
        l=[]
        #print "\n"
        file.close()
        file = open(filename)
        c = csv.reader(file)
                
    file.close()
f=open('file.txt','r')
for i in f:
    a=i
length_feature(a)
star_feature(a)
pronoun_feature(a)
brand_feature(a)
file = open(a)

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
    cursor = con.execute("SELECT status from feature1brand where uid=?",(a,))
    for row in cursor:
        status1=row[0]
    #w=0.4
    cursor = con.execute("SELECT status from feature2stars where uid=?",(a,))
    for row in cursor:
        status2=row[0]
    #w=0.2
    cursor = con.execute("SELECT status from feature3pronoun where uid=?",(a,))
    for row in cursor:
        status3=row[0]
    #w=0.1
    cursor = con.execute("SELECT status from feature4length where uid=?",(a,))
    for row in cursor:
        status4=row[0]
    w1=w2=w3=w4=0
    if status1=="yes":
        w1=0.3
    if status2=="yes":
        w2=0.4
    if status3=="yes":
        w3=0.2
    if status4=="yes":
        w4=0.1
    total=w1+w2+w3+w4
    #print a,total
    cursor.execute("insert into final \
                        values(?,?)",(a,total))
    con.commit()
    
cursor = con.execute("SELECT uid,weight from final")


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

        
        



