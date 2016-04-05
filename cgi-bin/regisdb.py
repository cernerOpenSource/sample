#! c:\Python27\python.exe
#!/usr/bin/env python

import smtplib
# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage()

fname = form.getvalue('fname')
lname  = form.getvalue('lname')
uname=form.getvalue('uname')
pwd=form.getvalue('pwd')
email=form.getvalue('email')
mobno=form.getvalue('mobno')
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
  
  <li><a href="/homepage.html">about us</a></li>
  <li><a href="/aboutus.html">about us</a></li>
  <li><a href="/contactus.html">contact us</a></li>
  </ul>
	</div>
	<!--top part end -->
	<!--header start -->
	<div id="header">
	<h2><span>Why Spam Fighter???</span></h2>
	<p>It has become a common practice for people to read online opinions/reviews for different purposes. For example, if one wants to buy a product, one typically goes to a review site (e.g., amazon.com) to read some reviews of the product. If most reviews are positive, one is likely to buy the product. If most reviews are negative, one will almost certainly not buy it.Positive opinions can result in significant financial gains and/or fames for busineses, organizations and individuals. This, unfortunately, gives strong incentives for opinion spamming.</p>
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
    <form action="/cgi-bin/regisdb.py" method="get" name="reg" onsubmit="return finalcheck()" style="background-image:url(../../../../Desktop/images%20(1).jpg)"><fieldset><legend><p style="font-family:arial;color: #077733;font-size:18px;">

CONFIRMATION MAIL</p></legend>
<br class="spacer" />
<br class="spacer" />
 <center><font color="#7642A3" size="5px"> A confirmation mail has been sent to your mail id </font><br/><br class="spacer" /><font size="4px">""" + email+"""</font>
<br class="spacer" />
<br class="spacer" />
<br class="spacer" />
<a href="/homepage.html">LOGIN</a>
<br class="spacer" />
<br class="spacer" />

  </fieldset>
</form></blockquote></blockquote></center>


<br class="spacer" /><br class="spacer" />
<br class="spacer" />
<br class="spacer" />
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
import sqlite3

con = sqlite3.connect("PROJECT")
cur = con.cursor()
cur.execute("insert into userdata \
        values(?,?,?,?,?,?)",(uname,fname,lname,email,mobno,pwd))

con.commit()

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


msg = MIMEMultipart()
msg['From'] = 'divyaduraisamyd@gmail.com'
msg['To'] = 'ddduraisamy31@gmail.com'
msg['Subject'] = 'Registered Successfully!!'
message = """Hi """+uname+"""\nYou have successfully registered with Spam Fighter"""
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('divyaduraisamyd@gmail.com', 'grimmauld3107')

mailserver.sendmail('divyaduraisamyd@gmail.com','ddduraisamy31@gmail.com',msg.as_string())
mailserver.quit()


