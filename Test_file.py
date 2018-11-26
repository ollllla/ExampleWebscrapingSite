import urllib.request
import urllib.parse
import re           #regular equatuions

url = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D1%96%D0%B2'
values = {'s': 'basics',
      'submit':'search'}        #this is how you search on most websites
data = urllib.parse.urlencode(values)
data= data.encode('utf-8')
req = urllib.request.Request('url', 'data')
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
for eachP in paragraphs:
    print(eachP)
