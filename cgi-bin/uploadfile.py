#!c:\Python27\python.exe
#!/usr/bin/env python
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage()
f=open('name.txt','r')
for i in f:
    a=i
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
          <li class="hover">home</li>
          <li><a href="#">about us</a></li>
          <li><a href="#">contact us</a></li>
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
                
		<form enctype="multipart/form-data" action="processingfile.py" method="post"><fieldset><legend><p style="font-family:arial;color: #077733;font-size:18px;">UPLOAD FILE</p></legend>
         <font color="#7642A3" size="+2"> <b>Hello """+a+"""</font></b><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a><a href="/cgi-bin/backbutton.py"><img src='/back.jpg' align='right'></a> 
                <br><center>
                <br class="spacer" />
         <br class="spacer" />
            <p><b><font color="#7642A3">Upload a Review file: </font></b><input type="file" name="file"></p><br>
            <br>
<p><input type="submit" value="Upload"></p>
<br class="spacer" />
        <br class="spacer" />
         <br class="spacer" />
        <br class="spacer" />
        <br class="spacer" />
        <br class="spacer" />
</fieldset>
</form>
</blockquote>
</blockquote>


                </center>
       
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
