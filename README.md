# LUCID

### Prerequisites:
  - Virtualenv
  - Python3

#### To download the code into any directory on your disk:

  `$ git clone git@github.com:JinnyChien/LUCID.git`

#### Install Virtualenv
Virtualenv, a Virtual Environment is an isolated working copy of Python which allows you to work on a specific project without worry of affecting other projects. There are a number of ways to install virtualenv on your system.

  `sudo apt-get install python-virtualenv`
  
  `sudo easy_install virtualenv`
  
  `sudo pip install virtualenv`

#### Setup and Use Virtualenv

** Create a virtual Python environment in a directory named venv, activate the virtualenv and install required dependencies using pip: **
  
   `$ mkdir ~/venv`
  
  `$ virtualenv ~/venv/test`
  
  To begin working with your project, you have to cd into your directory (project) and activate the virtual environment.
  `$ cd ~/venv/test/bin`

  `$ source venv/bin/activate`

  `(venv) $ pip install -r requirements.txt`

#### Commandline Usage

  `(venv) $ python scheduler.py --help `
  
  `(venv) $ python scheduler.py -input <option/all> `
  
  `(venv) $ python scheduler.py -input <option/all> -time <value>`

#### Choose input option and the deafult time is current time 
Reduce end users to paste the long argument

    Option 1 : 30 1 /bin/run_me_daily'
    Option 2 : 45 * /bin/run_me_hourly
    Option 3 : * * /bin/run_me_every_minute'
    Option 4 : * 19 /bin/run_me_sixty_times'

  `$ python scheduler.py -input 1`
  
      (venv) $ python scheduler.py -input 1
      01:30 tomorrow /bin/run_me_daily
  
  `$ python scheduler.py -input 2`
  
      (venv)$ python scheduler.py -input 2
      22:45 today /bin/run_me_hourly
  
  `$ python scheduler.py -input 3`
  
      (venv)$ python scheduler.py -input 3
      22:14 today /bin/run_me_every_minute
  
  `$ python scheduler.py -input 4`
  
      (venv) $ python scheduler.py -input 4
      19:00 tomorrow /bin/run_me_hourly
  
  `$ python scheduler.py -input all`
  
      (venv) $ python scheduler.py -input all
      01:30 tomorrow /bin/run_me_daily
      22:45 today /bin/run_me_hourly
      22:15 today /bin/run_me_every_minute
      19:00 tomorrow /bin/run_me_hourly

#### Input option and type the time value

  `$ python scheduler.py -input 1 -time <value>`
  
      (test) $ python scheduler.py -input 1 -time 14:30
      01:30 tomorrow /bin/run_me_daily
  
  `$ python scheduler.py -input 2 -time <value>`
  
      (test) $ python scheduler.py -input 2 -time 14:30
      14:45 today /bin/run_me_hourly
  
  `$ python scheduler.py -input 3 -time <value>`
  
      (test) $ python scheduler.py -input 3 -time 14:30
      14:30 today /bin/run_me_every_minute
  
  `$ python scheduler.py -input 4 -time <value>`
  
      (test) $ python scheduler.py -input 4 -time 14:30
      19:00 today /bin/run_me_hourly
  
  `$ python scheduler.py -input all -time <value>`
  
      (test) $ python scheduler.py -input all -time 14:30
      01:30 tomorrow /bin/run_me_daily
      14:45 today /bin/run_me_hourly
      14:30 today /bin/run_me_every_minute
      19:00 today /bin/run_me_hourly
