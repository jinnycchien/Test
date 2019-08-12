#!/usr/bin/python3
import argparse
import logging
import os
import time
import datetime

# Log setting and generate a logfile on the current place
logpath = os.getcwd() + "/test_logs"
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s', filename=logpath)
logger = logging.getLogger('test_logs')

now = (datetime.datetime.now())
currenttime = now.strftime("%H:%M")
next_hour = (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%H")

### Commandline Usage ###

# python scheduler.py --help

#  python scheduler.py --input <option> -time <current_time>
#  python scheduler.py --input <option>/<all>
#      Option 1 : 30 1 /bin/run_me_daily'
#      Option 2 : 45 * /bin/run_me_hourly
#      Option 3 : * * /bin/run_me_every_minute'
#      Option 4 : * 19 /bin/run_me_sixty_times'
#  python scheduler.py -input 1 -time <current_time>
#  python scheduler.py -input 2 -time <current_time>
#  python scheduler.py -input 3 -time <current_time>
#  python scheduler.py -input 4 -time <current_time>


def process_command():
    parser = argparse.ArgumentParser(prog='scheduler', description='scheduler command line functions')

    group = parser.add_argument_group('input')
    group.add_argument('-input', type=str, default=False, help='import configure option')
    group.add_argument('-time', type=str, default=False, help='import current time')

    return parser.parse_args()

def compare_option():

    if option == '1':
        time1 = '01:30'
        print('01:30' + ' ' + compare_date(time1) + ' ' + '/bin/run_me_daily')
    elif option == '2':
        time1 = '23:59'
        print(compare_hour() + ':45' + ' ' + compare_date(time1) + ' ' + '/bin/run_me_hourly')
    elif option == '3':
        time1 = '23:59'
        print(currenttime + ' ' + compare_date(time1)+' '+'/bin/run_me_every_minute')
    elif option == '4':
        time1 = '19:00'
        print(('19:00' + ' ' + compare_date(time1)+' '+'/bin/run_me_hourly'))
    elif option == 'all':
        print('01:30' + ' ' + compare_date('01:30') + ' ' + '/bin/run_me_daily')
        print(compare_hour() + ':45' + ' ' + compare_date('23:59') + ' ' + '/bin/run_me_hourly')
        print(currenttime + ' ' + compare_date('23:59')+' '+'/bin/run_me_every_minute')
        print(('19:00' + ' ' + compare_date('19:00')+' '+'/bin/run_me_hourly'))
    else:
        print('Please check your value')


def compare_date(time1):

    time2 = currenttime
    s_time = time.mktime(time.strptime(time1, '%H:%M'))
    e_time = time.mktime(time.strptime(time2, '%H:%M'))
    if s_time > e_time:
        return 'today'
    else:
        return 'tomorrow'

def compare_hour():
    time1 = '45'
    time2 = now.strftime("%M")
    s_time = time.mktime(time.strptime(time1, '%M'))
    e_time = time.mktime(time.strptime(time2, '%M'))
    if s_time > e_time:
        return now.strftime("%H")
    elif s_time == e_time:
        return now.strftime("%H")
    else:
        return next_hour

def compare_option2():

    if option == '1':
        time1 = '01:30'
        time2 = time
        print('01:30' + ' ' + compare_date2(time1, time2) + ' ' + '/bin/run_me_daily')
    elif option == '2':
        time1 = '23:59'
        time2 = time
        print(compare_hour2(time2) + ':45' + ' ' + compare_date2(time1, time2) + ' ' + '/bin/run_me_hourly')
    elif option == '3':
        time1 = '23:59'
        time2 = time
        print(time2 + ' ' + compare_date2(time1, time2)+' '+'/bin/run_me_every_minute')
    elif option == '4':
        time1 = '19:00'
        time2 = time
        print(('19:00' + ' ' + compare_date2(time1, time2)+' '+'/bin/run_me_hourly'))
    elif option == 'all':
        time2 = time
        print('01:30' + ' ' + compare_date2('01:30', time2) + ' ' + '/bin/run_me_daily')
        print(compare_hour2(time2) + ':45' + ' ' + compare_date2('23:59', time2) + ' ' + '/bin/run_me_hourly')
        print(time2 + ' ' + compare_date2('23:59', time2)+' '+'/bin/run_me_every_minute')
        print(('19:00' + ' ' + compare_date2('19:00', time2)+' '+'/bin/run_me_hourly'))
    else:
        print('Please check your value')


def compare_date2(time1, time2):

    if time1 > time2:
        return 'today'
    else:
        return 'tomorrow'

def compare_hour2(time2):
    s_time = '45'
    e_time = (time2[3:])
    if s_time > e_time:
        return time2[0:2]
    elif s_time == e_time:
        return time2[0:2]
    else:
        return next_hour

if __name__ == "__main__":
    args = process_command()
    if args.input and args.time:
        option = args.input
        time = args.time
        compare_option2()
    elif args.input:
        option = args.input
        compare_option()
    else:
        print('python scheduler.py -input <option> -time <value>')
        print('python scheduler.py -input <option>/<all>')
        print('Option 1 : 30 1 /bin/run_me_daily')
        print('Option 2 : 45 * /bin/run_me_hourly')
        print('Option 3 : * * /bin/run_me_every_minute')
        print('Option 4 : * 19 /bin/run_me_sixty_times')

