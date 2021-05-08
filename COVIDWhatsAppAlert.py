from datetime import date
import datetime
import requests
from twilio.rest import Client

currentDate = date.today()
# print("Today's date:", currentDate)

nDaysAhead = 14
dateList = []
for i in range(1, 15):
    newDate = currentDate + datetime.timedelta(days=i)
    dateList.append(newDate)
districtList = [265, 294]

# Search for Delhi District for the next 2 weeks
for i in dateList:
    day = i.day
    month = i.month
    year = i.year
    checkDate = str(day) + "-" + str(month) + "-" + str(year)
    print("ForDate:::", checkDate)
    for j in districtList:
        print("District::", j)
        response = requests.get(
            "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=" + str(
                j) + "&date=" + str(checkDate)).json()
        if (len(response['sessions']) > 0):
            for k in range(0, len(response['sessions'])):
                if (response['sessions'][k]['min_age_limit'] == 18):
                    account_sid = 'ACfc80ef50f32429f971f3bdebde26a997'
                    auth_token = '0adf1745a0013eb9b3232b38ddcd768a'
                    client = Client(account_sid, auth_token)

                    Name = response['sessions'][k]['name']
                    Address = response['sessions'][k]['address']
                    Pincode = str(response['sessions'][k]['pincode'])
                    vaccineDate = checkDate
                    print("Found", Name, " ", Address, " ", Pincode)
                    message = client.messages.create(
                        from_='whatsapp:+14155238886',
                        body='Your vaccine appointment at ' + Name + ":: " + Address + ":: " + Pincode + " on " + vaccineDate + ' is now open',
                        to='whatsapp:+919901595582'
                    )