#!c:\Python27\python.exe
#!/usr/bin/env python
import cgi, cgitb
import sqlite3
con = sqlite3.connect('PROJECT')

#cursor = conn.execute("SELECT *from userdata ")

file=open('name.txt','r')
# Create instance of FieldStorage 
form = cgi.FieldStorage()
for i in file:
    a=i
cursor = con.execute("SELECT *from userdata where username=?",(a,))
for row in cursor:
   uname=row[0]
   fname=row[1]
   lname=row[2]
   email=row[3]
   mobno=row[4]
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
         <font color="#7642A3" size="+2"> <b>Hello """+a+"""</font></b><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a><a href=""><img src='/back.jpg' align='right'></a> 
                <br>
                
                
                <center>
                <br class="spacer" />
                <br class="spacer" />
                <table style="border-style: groove" width="600px" height="300px">
                <tr align="center" bgcolor="#BCEBBC">
                <td >Username:</td>
                <td>"""+uname+"""</td>
                </tr>
                <tr align="center" bgcolor="#61D16A">
                <td>First Name:</td>
                <td>"""+fname+"""</td>
                </tr>
                <tr align="center" bgcolor="#BCEBBC">
                <td>Last Name:</td>
                <td>"""+lname+"""</td>
                </tr>
                <tr align="center" bgcolor="#61D16A">
                <td>Email ID:</td>
                <td>"""+email+"""</td>
                </tr>
                <tr align="center" bgcolor="#BCEBBC">
                <td>Mobile Number:</td>
                <td>"""+mobno+"""</td>
                </tr>
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
