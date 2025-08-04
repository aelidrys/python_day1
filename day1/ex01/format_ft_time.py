import time
import datetime

dtime = datetime.datetime.now()
formatted_time = dtime.strftime("%b %d %Y")
timeNow = time.time() 
scientific_notation_timeNow = "{:.2e}".format(timeNow)
timeNow = "{:,.4f}".format(timeNow)

print(f"Seconds since January 1, 1970: {timeNow} or {scientific_notation_timeNow} in scientific notation")
print(formatted_time)
