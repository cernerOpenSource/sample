#!c:\Python27\python.exe
#!/usr/bin/env python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage()

    

uname = form.getvalue('name')
pwd = form.getvalue('pwd')
file=open('name.txt','w')
file.write(uname)
file.close()
import sqlite3
con = sqlite3.connect("PROJECT")
cur = con.cursor()
print "Content-Type: text/html"
print
cursor = con.execute("SELECT username, pwd, fname, lname from userdata where username=? and pwd=?",(uname,pwd,))
if cursor.fetchone():
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
          <li><a href="/aboutus.html">about us</a></li>
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
                <font color="#7642A3" size="+2"> <b>Hello """+uname+"""</font></b></center><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a>
<center>
            
             
             <table width="200" border="0" cellpadding="25">
          <tr>
            <td><a href="/cgi-bin/display.py" ><img src=' /update1.png ' onmouseover="this.src=' /update2.jpg '" onmouseout="this.src=' /update1.png  '"  /></a></td>
          <td><a href="/cgi-bin/uploadfile.py" ><img src=' /file1.jpg ' onmouseover="this.src=' /file2.jpg '" onmouseout="this.src=' /file1.jpg  '"  /></a></td>
          <td><a href="/cgi-bin/uploadlink.py" ><img src=' /link1.jpg ' onmouseover="this.src=' /link2.jpg '" onmouseout="this.src=' /link1.jpg  '"  /></a></td>
          </tr>
         
        </table>
         </center>
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
else:
    print """
        <html>
        <head>
        <title>Spam Fighter</title>
        <link href='/style.css' rel='stylesheet' type='text/css' />
        </head>
        <body>
	<!--top part start -->
	<div id="top">
      <a href="homepage.html"><img src="/spamlogo.jpg" alt="individual" width="286" height="66" border="0" /></a>
      <ul>
      <li><a href="/homepage.html">home</a></li>
      <li><a href="/aboutus.html">about us</a></li>
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
            <div id="body">
            <br class="spacer" />
      <!--left panel start -->
      <div id="left">
      <h2><strong>Opinion Spamming</strong></h2>
      <p class="lftText">It refers to &quot;illegal&quot; activities (e.g.,&nbsp;<em>writing fake reviews</em>, also called&nbsp;<em>shilling</em>) that try to mislead readers or automated&nbsp;<a href="http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html"><span>opinion mining and sentiment analysis</span></a>&nbsp;systems by giving undeserving positive opinions to some target entities in order to promote the entities and/or by giving false negative opinions to some other entities in order to damage their reputations.</p>
      <p class="lftText">Opinion spam has many forms, e.g.,&nbsp;<em>fake reviews</em>&nbsp;(also called&nbsp;<em>bogus reviews</em>),&nbsp;<em>fake comments</em>,&nbsp;<em>fake blogs</em>,&nbsp;<em>fake social network postings</em>,&nbsp;<em>deceptions</em>, and&nbsp;<em>deceptive messages</em></bold></em>.</p>
      <div id="leftBottom">
        <p class="top1"></p>
        <p class="lftBottomText"><img src="/images/home_center.jpg" width="302" height="162" alt=""/></p>
      <p class="bot1"></p>
    </div>
      <br class="spacer" />
      </div>
       <!--left panel end -->
       <!--mid panel start -->
       <div id="mid">
       <h2>whats' new</h2>
       <p><img src="/images/trip-advisor-fake-reviews.png" width="700" height="448" alt=""/></p>
       <h3>Spam fighter success story</h3>
       <p class="midText">Filtered around 200 reviews posted on various online shopping websites like flipkart.com</p>
       <p class="midText">&nbsp;</p>
       <p class="midText"><br class="spacer" />
       </p>
       </div>
       <!--mid panel end -->
        <!--right panel start -->
        
            <div id="right">
            <h2 class="mem">Member Login</h2>
           
            <form action="/cgi-bin/login.py" method="get" name="login">
             <center><b><font color="#D3690C" size="1px">WRONG USER ID OR PASSWORD!!</font></b></center>
        <font color="#F5F5F5">Username:</font>
            <input type="text" name="name" class="txtBox" />
        <font color="#F5F5F5">Password:</font>
            <input type="password" name="pwd" class="txtBox" />
            <a href="register.html">Register here</a>
            <input class="login" type="submit"  name="submit"/>
            <br class="spacer" />
            </form>
            <p class="bottom2"></p>
            <h2 class="solution">Solutions</h2>
            <ul>
            <li><a href="#">Detect spams from uploaded file</a></li>
	<li><a href="#">Detect spams in product URL</a></li>
	<li><a href="#">Know about the product true quality</a></li>
	<li><a href="#">80% Spam detection</a></li>
	<li><a href="#">Get full details of spam review</a></li>
	<li><a href="#">Data preprocessing</a></li>
	<li class="noImg"><a href="#">Use of visualisation tools </a></li>
            </ul>
            <br class="spacer" />
            </div>
            <!--right panel end -->
            <!--bodyBottom start --><!--bodyBottom end-->
            <br class="spacer" />
            </div>
            <!--body end -->
            <!--footer start --><!--footer end -->
    </body>
    </html>
"""



con.close()
