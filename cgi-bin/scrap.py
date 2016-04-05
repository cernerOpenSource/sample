import urllib
import re
htmlfile=urllib.urlopen("http://www.flipkart.com/apple-md760hn-a-macbook-air-4th-gen-ci5-4gb-128gb-flash-mac-os-x-mountain-lion/p/itmdna8yw3kfyvfw?pid=COMDNA7BNYHUSH7E&srno=b_1&ref=29aa9a92-803e-4da5-908b-d867817d45e8")
htmltext=htmlfile.read()
regex='<td class="specs-value fk-data">(.+?)</td>'
pattern=re.compile(regex)
brand=re.findall(pattern,htmltext)
print brand
