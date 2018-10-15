# This script was made by Colton McAda and Chris Garcia (with maybe some help from the internet).

import os.path
import re
from datetime import date, datetime
import calendar

# This is function pulls the logs from the website and saves into a file if the log file is not currently in the directory.
def savelogs():
    if not os.path.exists('./logs.txt'):
        import urllib.request
        urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log','logs.txt')

savelogs()

# This function will return the answer to how many requests were made in the log. Note that any corrupt requests were thrown out.
def total_requests():
    num_lines = 0
    with open('logs.txt','r') as f:
        for i in f:
            num_lines += 1

    avg_week = num_lines/50.4286
    avg_mon = num_lines/11.5921
    print('This is the total amount of requests in the log file: ',num_lines)
    print('This is the average amount of requests for a week: ', avg_week)
    print('This is the average amount of requests for a month: ', avg_mon)
total_requests()

# This code will go through the lines of logs, assign the file to a value in a list, then count how many times that value appears over 
# multiple lines. It also does this for status codes. 
def file_count():
    file_dict = {}
    status_dict = {}
    date_dict = {}
    for line in open('logs.txt'):
        pieces = re.split('.*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*', line)
        try:
            file = pieces[4]
            status = pieces[6]
            date = pieces[1]
        except IndexError:
            continue
        if file in file_dict:
            file_dict[file] += 1
        else:
            file_dict[file] = 1
        if status in status_dict:
            status_dict[status] += 1
        else:
            status_dict[status] = 1
        if date in date_dict:
            date_dict[date] += 1
        else:
            date_dict[date] = 1

# This code gets the number of times an error code or redirect code appears in the status dictionary.
    error = 0
    redirect = 0
    for k in status_dict.keys():
        if k.startswith('4'):
            error += status_dict.get(k)
        elif k.startswith('3'):
            redirect += status_dict.get(k)
        else:
            continue

# This code turns that number into a percent against the total amount of status codes we were able to retrieve.
    perc_error = (error/sum(status_dict.values())) * 100
    perc_redirect = (redirect/sum(status_dict.values())) * 100

# The code below prints the answers to questions 3-6.
    print(perc_error,' percent of the requests were not successful.')
    print (perc_redirect,' percent of the requests were redirected elsewhere.')

    maximum = max(file_dict, key=file_dict.get)
    minimum = min(file_dict, key=file_dict.get)
    print('The most requested file is ', maximum,' with ', file_dict[maximum],' requests.')
    print('The least requested file is ', minimum,' with ', file_dict[minimum],' requests.')

    mon_req=[]
    tues_req=[]
    wed_req=[]
    thur_req=[]
    fri_req=[]
    sat_req=[]
    sun_req=[]
    day='placeholder'

    for d in date_dict.keys():
        datetime_obj=datetime.strptime(d, '%d/%b/%Y')
        day=calendar.day_name[datetime_obj.weekday()]
        if day=='Monday':
            mon_req.append(date_dict.get(d))
        elif day=='Tuesday':
            tues_req.append(date_dict.get(d))
        elif day=='Wednesday':
            wed_req.append(date_dict.get(d))
        elif day=='Thursday':
            thur_req.append(date_dict.get(d))
        elif day=='Friday':
            fri_req.append(date_dict.get(d))
        elif day=='Saturday':
            sat_req.append(date_dict.get(d))
        else:
            sun_req.append(date_dict.get(d))
        
    avg_mon= sum(mon_req)/len(mon_req)
    avg_tues= sum(tues_req)/len(tues_req)
    avg_wed= sum(wed_req)/len(wed_req)
    avg_thur= sum(thur_req)/len(thur_req)
    avg_fri= sum(fri_req)/len(fri_req)
    avg_sat= sum(sat_req)/len(sat_req)
    avg_sun= sum(sun_req)/len(sun_req)

    print('The average monday gets', avg_mon, ' requests')
    print('The average tuesday gets', avg_tues, ' requests')
    print('The average wednesday gets', avg_wed, ' requests')
    print('The average thursday gets', avg_thur, ' requests')
    print('The average friday gets', avg_fri, ' requests')
    print('The average saturday gets', avg_sat, ' requests')
    print('The average sunday gets', avg_sun, ' requests')



file_count()
