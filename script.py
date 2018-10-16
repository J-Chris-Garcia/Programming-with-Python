# This script was made by Colton McAda and Chris Garcia (with maybe some help from the internet).



import os.path

import re

from datetime import date, datetime

import calendar

print("Please wait . . .")
print("")


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

    print("")

    print('Please wait . . .    This may take a few moments')

total_requests()


def check_file():

    if not os.path.exists('./october_94.txt'):
        file_count() 

    if not os.path.exists('./november_94.txt'):
        file_count()

    if not os.path.exists('./december_94.txt'):
        file_count()

    if not os.path.exists('./january_94.txt'):
        file_count()

    if not os.path.exists('./february_95.txt'):
        file_count()

    if not os.path.exists('./march_95.txt'):
        file_count()

    if not os.path.exists('./april_95.txt'):
        file_count()

    if not os.path.exists('./may_95.txt'):
        file_count()

    if not os.path.exists('./june_95.txt'):
        file_count()

    if not os.path.exists('./july_95.txt'):
        file_count()

    if not os.path.exists('./august_95.txt'):
        file_count()

    if not os.path.exists('./september_95.txt'):
        file_count()

    if not os.path.exists('./october_95.txt'):
        file_count()
  

# This code will go through the lines of logs, assign the file to a value in a list, then count how many times that value appears over 

# multiple lines. It also does this for status codes. 

def file_count():

    file_dict = {}

    date_dict = {}

    status_3 = []

    status_4 = []

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

        if date in date_dict:

            date_dict[date] += 1

        else:

            date_dict[date] = 1 



        date = str(pieces[1])



        month = re.findall(r'[A-Z][a-z][a-z]?\d*',date)

        year = re.findall(r'[0-9]?\d*',date)



## October 94 ##
   
        if month == ['Oct'] and year[6] == '1994':
            with open('october_94.txt' , 'a') as f:
                f.write(line)
## November 94

        if month == ['Nov'] and year[6] == '1994':
            with open('november_94.txt' , 'a') as f:
                f.write(line)

## December 94 ##
                
        if month == ['Dec'] and year[6] == '1994':
            with open('december_94.txt' , 'a') as f:
                f.write(line)

## January 95 ##

        if month == ['Jan'] and year[6] == '1995': 
            with open('january_94.txt' , 'a') as f:
                f.write(line)

## February 95 ##

        if month == ['Feb'] and year[6] == '1995':
            with open('febuary_95.txt' , 'a') as f:
                f.write(line)

## March 95 ##

        if month == ['Mar'] and year[6] == '1995':
            with open('march_95.txt' , 'a') as f:
                f.write(line)

## April 95 ##

        if month == ['Apr'] and year[6] == '1995':
            with open('april_95.txt' , 'a') as f:
                f.write(line)

## May 95 ##

        if month == ['May'] and year[6] == '1995':
            with open('may_95.txt' , 'a') as f:
                f.write(line)

## June 95 ##

        if month == ['Jun'] and year[6] == '1995':
            with open('june_95.txt' , 'a') as f:
                f.write(line)

## July 95 ##

        if month == ['Jul'] and year[6] == '1995':
            with open('july_95.txt' , 'a') as f:
                f.write(line)

## August 95 ##

        if month == ['Aug'] and year[6] == '1995':
            with open('august_95.txt' , 'a') as f:
                f.write(line)

## September 95 ##

        if month == ['Sep'] and year[6] == '1995':
            with open('september_95.txt' , 'a') as f:
                f.write(line)

## October 95 ##

        if month == ['Oct'] and year[6] == '1994':
            with open('october_95.txt' , 'a') as f:
                f.write(line)

## Status codes ##
    
        error = str(pieces[6])


        code = list(re.findall(r'[0-9]',error))


        first = code[0]
      

        if first == '3':

            status_3.append(first)


        elif first == '4':

            status_4.append(first)

  
    status_300 = len(status_3)

    status_400 = len(status_4)   

    

    percent300 = (status_300/726736) * 100

    percent400 = (status_400/726736) * 100


    print("")
    print("The total percent of requests that were not successful:            "  ,percent400)

    print("The total percent of requests that were redirected elsewhere:      " ,percent300)

            



    maximum = max(file_dict, key=file_dict.get)

    minimum = min(file_dict, key=file_dict.get)

    print("")

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


    print("")
    print('The average monday gets    ', avg_mon,  ' requests')

    print('The average tuesday gets   ', avg_tues, ' requests')

    print('The average wednesday gets ', avg_wed,  ' requests')
 
    print('The average thursday gets  ', avg_thur, ' requests')

    print('The average friday gets    ', avg_fri,  ' requests')

    print('The average saturday gets  ', avg_sat,  ' requests')

    print('The average sunday gets    ', avg_sun,  ' requests')






file_count()

print("")


input("Press ENTER button to quit. ")

