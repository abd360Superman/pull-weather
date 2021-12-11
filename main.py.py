import json
import requests
from datetime import datetime

def main():
    APPID = '4d09820275977e4e908f2339f9467c82'

    location = 'mumbai'

    now = datetime.now()
    filename = f"data/output-{now.strftime('%d-%m-%Y %H-%M-%S')}.txt"

    url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, APPID)
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    main = data['main']
    report = data['weather']

    temp = round(main['temp'] - 273.15, 2)
    temp_min = round(main['temp_min'] - 273.15, 2)
    temp_max = round(main['temp_max'] - 273.15, 2)
    status = report[0]['main']

    output = open(filename, "w")
    lines = ["----- New Mumbai Weather Report ----- \n",
         "Status: %s \n" % status,
         "Temperature: %s \n" % temp,
         "Minimum Temperature: %s \n" % temp_min,
         "Maximum Temperature: %s" % temp_max]
    output.writelines(lines)
    output.close()

if __name__ == '__main__':
    main()
