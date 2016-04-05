#!c:\Python27\python.exe
#!/usr/bin/env python
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage()

print "Content-Type: text/html"
print
print """
        <html>
        <head>
        <title>Individual</title>
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
                <p>It has become a common practice for people to read online <span>opinions/reviews</span> for different purposes. For example, if one wants to buy a product, one typically goes to a review site (e.g., amazon.com) to read some reviews of the product. If most <span>reviews are positive,</span> one is likely to buy the product. If most <span>reviews are negative,</span> one will almost certainly not buy it. <span>Positive opinions</span> can result in significant financial gains and/or fames for busineses, organizations and individuals. This, unfortunately, gives strong incentives for opinion spamming.</p>
                </div>
                <!--header end -->
                <!--body start -->
                <div id="body" style="color:#000">
                <br class="spacer" style="color:#000" />
          <!--left panel start --><!--left panel end -->
           <!--mid panel start --><!--mid panel end -->
            <!--right panel start --><!--right panel end -->
                <!--bodyBottom start --><!--bodyBottom end-->
                <center>
		<form enctype="multipart/form-data" action="processingfile.py" method="post">
                <fieldset><legend></legend>
                <span>FILE SUCCESSFULLY UPLOADED</span>
            <br>
</fieldset>
</form>
                </center>
        <br class="spacer" />
        <br class="spacer" />
        <br class="spacer" />
        <br class="spacer" />
        <br class="spacer" />
        <br class="spacer" />
        <br class="spacer" />
        <br class="spacer" />
        <br class="spacer" />
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
