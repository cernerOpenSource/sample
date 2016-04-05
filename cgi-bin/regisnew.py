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
import sqlite3
con = sqlite3.connect("PROJECT")
cur = con.cursor()
cursor = con.execute("SELECT username from userdata where username=? ",(uname,))
print "Content-Type: text/html"
print
if cursor.fetchone():
    
    print """
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
                <script language="javascript">
        function checkf(para,name)
        {
                if(para.value.length==0)
                        {
                document.getElementById("para").innerHTML="<br>*"+ name+ " field should not be left empty!!";
                para.focus();
                return false;
                        }
                else
                        {
                        document.getElementById("para").innerHTML=" ";
                        
                        
                        }
                
        return true;
        }
        function checkl(para,name)
        {
                if(para.value.length==0)
                        {
                document.getElementById("para1").innerHTML="<br>*"+ name+ " field should not be left empty!!";
                para.focus();
                return false;
                        }
                else
                        {
                        document.getElementById("para1").innerHTML="";
                        }
                
        return true;
        }
        function checku(para,name)
        {
                if(para.value.length==0)
                        {
                document.getElementById("para2").innerHTML="*"+ name+ " field should not be left empty!!";
                para.focus();
                return false;
                        }
                else
                        {
                        document.getElementById("para2").innerHTML=" ";
                        }
                
        return true;
        }

        function sizecheck(pass)
        {
        if(pass.length<6)
        {
        window.alert("Passwords must be minimum of 6 characters");
        }
        }
                
        function checke(para,name)
        {
                if(para.value.length==0)
                        {
                document.getElementById("para3").innerHTML="*"+ name+ " field should not be left empty!!";
                para.focus();
                return false;
                        }
                else
                        {
                        document.getElementById("para3").innerHTML=" ";
                        }
                
        return true;
        }
        function checkm(para,name)
        {
                if(para.value.length<10)
                        {
                document.getElementById("para4").innerHTML="*"+ name+ " number is not valid";
                para.focus();
                return false;
                        }
                else
                        {
                        document.getElementById("para4").innerHTML=" ";
                        }
                
        return true;
        }

                
        function password(pass,conf)
        {
        if(pass.length!=0&&conf.length!=0)
        {
        if(pass.length<6)
        window.alert("Passwords must be minimum of 6 characters");
         
                if(pass!=conf)
        document.getElementById("match").innerHTML="Passwords donot match";
        else
        document.getElementById("match").innerHTML="Passwords match";
        }
        }

        function finalcheck()
        {
        var a=document.reg.fname.value;
        var b=document.reg.lname.value;
        var c=document.reg.uname.value;
        var d=document.reg.pwd.value;
        var e=document.reg.cpwd.value;
        var f=document.reg.email.value;
        var g=document.reg.mobno.value;
        if(a.length==0||b.length==0||c.length==0||d.length==0||e.length==0||f.length==0||g.length==0)
        {
                alert("All fields marked as * are mandatory");
                return false;
        }
        if(d!=e)
        {alert("passwords dont match!!");
        return false;
        }
                }


        </script>
        <title>Spam Fighter</title>
        <link href="/style.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
                <!--top part start -->
                <div id="top">
          <a href="/homepage.html"><img src="/spamlogo.jpg" alt="individual" width="286" height="66" border="0" /></a>
          <ul>
          <li class="hover"><a href="/homepage.html">home</a></li>
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
            <blockquote>
            <form action="/cgi-bin/regisdb.py" method="get" name="reg" onsubmit="return finalcheck()"><fieldset><legend><p style="font-family:arial;color: #077733;font-size:18px;">REGISTRATION</p></legend>
         <center>
         <label style=color:red>*Username already exists</label>
         <br/><p> <font color="#7642A3"> Title</font><br>  <select name="title"  ><option>Mr.</option><option>Mrs.</option><option>Ms.</option></select></p>
         <p> <font color="#7642A3"> First name</font><br>
         <input style="border :1px; font-family : Verdana; color : purple; background: #E1D689;" name="fname" type="text" onblur=checkf(fname,"Firstname")
        <b><label style=color:red id="para"></label></b><br/></p>
         <font color="#7642A3"> Last name</font><br>
        <input style="border :1px; font-family : Verdana; color : purple; background: #E1D689;" name="lname" type="text" onblur=checkl(lname,"Lastname")>
        <b><label style=color:red id="para1"></label></b><br/></p>

        <p> <font color="#7642A3"> User name</font></font><br />
          <input style="border :1px; font-family : Verdana; color : purple; background: #E1D689;" name="uname" type="text" onblur=checku(uname,"Username")> </p>
        <b><label style=color:red id="para2"></label></b></p>

        <p> <font color="#7642A3"> Password</font><br>

        <input style="border :1px; font-family : Verdana; color : purple; background: #E1D689;" name="pwd" type="password" onblur=sizecheck(pwd)> </p>
        <p> <font color="#7642A3"> Confirm Password</font><br>
        <input style="border :1px; font-family : Verdana; color : purple; background: #E1D689;" name="cpwd" type="password" onKeyup=password(pwd.value,cpwd.value)> 
        <b><label id="match"></label></b></p>

        <p> <font color="#7642A3"> Email id</font><br>
        <input style="border :1px; font-family : Verdana; color : purple; background: #E1D689;" name="email" type="text" onblur=checke(email,"Email")> </p>
        <b><label style=color:red id="para3"></label></b></p>

         <font color="#7642A3"> Mobile No.</font><br>
        <input style="border :1px; font-family : Verdana; color : purple; background: #E1D689;" name="mobno" type="text" onblur=checkm(mobno,"Mobile")> </p>
        <b><label style=color:red id="para4"></label></b><br/></p>

         <input type="submit" name="submit" value="Register" >
        <input type="reset" name="submit" value="Reset" >
          </center>
          </fieldset>
        </form>
        </blockquote>
        </blockquote>
        </blockquote>
        </center>
        <br class="spacer" />
                </div>
                <!--body end -->
                <!--footer start --><!--footer end -->
        </body>
        </html>
        """
    con.close()
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
con.close()
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
    

