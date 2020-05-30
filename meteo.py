import argparse
import datetime as dt
import sys
import meteomatics.api as api
from dateutil.parser import parse
import os

###Credentials:
username = 'python-community'
password = 'Umivipawe179'

def SaveLine(line):
	if not os.path.exists('temps_2019.txt'):
		my_file = open('temps_2019.txt', 'w')
		my_file.close()
	with open('temps_2019.txt', 'a') as my_file:
		my_file.write(line + '\n')
	my_file.close()


def getData(d):
    now = dt.datetime.utcnow().replace(hour=12, minute=12, second=0, microsecond=0)
    startdate_ts = d 
    startdate_ts.replace(hour=12, minute=12, second=0, microsecond=0)
    enddate_ts = startdate_ts + dt.timedelta(days=1)
    interval_ts = dt.timedelta(hours=1)
    coordinates_ts = [(51.507351, -0.127758), (50., 10.)] # London
    parameters_ts = ['t_2m:C']
    model = 'mix'
    ens_select = None  # e.g. 'median'
    cluster_select = None  # e.g. "cluster:1", see http://api.meteomatics.com/API-Request.html#cluster-selection
    interp_select = 'gradient_interpolation'
    limits = api.query_user_features(username, password)
    try:
        df_ts = api.query_time_series(coordinates_ts, startdate_ts, enddate_ts, interval_ts, parameters_ts,
                                      username, password, model, ens_select, interp_select,
                                      cluster_select=cluster_select)
        print (df_ts.head(13))
        line = str(df_ts.head(13)).replace('lat       lon       validdate                        ','')
        line = line.replace('                                               t_2m:C','')
        line = line.replace('51.507351 -0.127758 ','')
        line = line.replace('+00:00     ',',')
        line = line.replace('+00:00    ',',')
        line = line.replace('                    ','')
        line = str(line).replace('\n\n','')
        if line != '':
            SaveLine(line)
    except Exception as e:
        print("Failed, the exception is {}".format(e))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', default=username)
    parser.add_argument('--password', default=password)
    arguments = parser.parse_args()

    username = arguments.username
    password = arguments.password

    if username is None or password is None:
        print(
        "missing credentials")
        sys.exit()

    line = '"date","value"'
    SaveLine(line)
    d = dt.datetime.strptime('2019-03-01', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-02', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-03', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-04', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-05', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-06', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-07', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-08', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-09', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-10', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-11', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-12', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-13', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-14', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-15', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-16', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-17', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-18', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-19', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-20', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-21', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-22', '%Y-%m-%d') 
    getData(d)   
    d = dt.datetime.strptime('2019-03-23', '%Y-%m-%d') # Lockdown date in London
    getData(d)
    d = dt.datetime.strptime('2019-03-24', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-03-25', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-03-26', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-03-27', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-03-28', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-03-29', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-03-30', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-03-31', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-01', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-02', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-03', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-04', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-05', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-06', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-07', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-08', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-09', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-10', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-11', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-12', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-13', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-14', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-15', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-16', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-17', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-18', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-19', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-20', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-21', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-22', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-23', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-24', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-25', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-26', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-27', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-28', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-29', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-04-30', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-01', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-02', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-03', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-04', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-05', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-06', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-07', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-08', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-09', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-10', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-11', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-12', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-13', '%Y-%m-%d') # end of lockdown
    getData(d)
    d = dt.datetime.strptime('2019-05-14', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-15', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-16', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-17', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-18', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-19', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-20', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-21', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-22', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-23', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-24', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-25', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-26', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-27', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-28', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-29', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-30', '%Y-%m-%d')
    getData(d)
    d = dt.datetime.strptime('2019-05-31', '%Y-%m-%d')
    getData(d)