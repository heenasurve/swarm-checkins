import foursquare;
import json;
import datetime;
from pytz import timezone;

# JSON file
f = open ('data/secrets.json', "r")
# Reading from file
mydata = json.loads(f.read())

# Construct the client object
client = foursquare.Foursquare(access_token=mydata.access_token)

# Get the user's data
user = client.users()

start_date = '2020-01-01';
end_date = '2020-06-30';
start_ts = int(datetime.datetime.strptime(start_date, '%Y-%m-%d').replace(tzinfo=timezone('US/Eastern')).timestamp())
end_ts = int(datetime.datetime.strptime(end_date, '%Y-%m-%d').replace(tzinfo=timezone('US/Eastern')).timestamp())

# Get the check-ins using afterTimestamp and beforeTimestamp to filter the result
c = client.users.checkins(params={'afterTimestamp': start_ts, 'beforeTimestamp': end_ts})


# with open('data/checkins_2020_FH.json', 'a+') as fp:
#    json.dump(c['checkins']['items'], fp)



