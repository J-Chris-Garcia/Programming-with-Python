# This script was made by Colton McAda and Chris Garcia

# This is function pulls the logs from the website and saves into a file.
def savelogs():
    try:
        import urllib.request as urllib2
    except (ImportError):
        import urllib2

    url='https://s3.amazonaws.com/tcmg476/http_access_log'
    response=urllib2.urlopen(url)
    
    with open('logs.txt','wb') as f:
        f.write(response.read())

savelogs()

# This function will take that log file and delete any bad lines
def clean_logs():
    with open("cleanlogs.txt", "w") as out:
        with open("logs.txt") as f:
            for line_no, line in enumerate(f):
                if len(line.strip()) > 38:
                    out.write(line)

clean_logs()
