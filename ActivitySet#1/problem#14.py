# Using Web Services
# https://www.py4e.com/lessons/servces
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
print('Retreving',url)
xml = urllib.request.urlopen(url, context=ctx).read()
print('Retreved ',len(xml),'charecters')
tree=ET.fromstring(xml)
counts = tree.findall('comments/comment')
sum=0
coun=0
for item in counts:
    x=item.find('count').text
    sum=sum+int(x)
    coun=coun+1
print('sum:',sum)
print('count',coun)

