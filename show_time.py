
import calendar
from datetime import date
import datetime

e = datetime.datetime.now()

print ("Current date and time = %s" % e)

print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
today = date.today()
print(calendar.day_name[today.weekday()])
