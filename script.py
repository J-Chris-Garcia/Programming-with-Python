try:
    import urllib.request as urllib2
except (ImportError):
    import urllib2

url='https://s3.amazonaws.com/tcmg476/http_access_log'
response=urllib2.urlopen(url)
with open('logs.txt','wb') as f:
    f.write(response.read())
