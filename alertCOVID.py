from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from twilio.rest import Client
import time

driver = webdriver.Chrome(ChromeDriverManager(version="90.0.4430.24").install())
driver.get("https://under45.in/")
link = driver.find_element_by_link_text('Where are the slots?')
link.click()
time.sleep(1.5)
inputElement = driver.find_element_by_xpath('//*[@id="history_filter"]/label/input')
city = 'Kolkata'
inputElement.send_keys(city)
FindListElement = driver.find_element_by_xpath('//*[@id="history_info"]')
NumberOfEntries = FindListElement.text
res = [int(i) for i in NumberOfEntries.split() if i.isdigit()]
if res[1] > 0:
    account_sid = 'ACfc80ef50f32429f971f3bdebde26a997'
    auth_token = '0adf1745a0013eb9b3232b38ddcd768a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your vaccine appointment at ' + city + ' is now open',
        to='whatsapp:+919901595582'
    )
else:
    account_sid = 'ACfc80ef50f32429f971f3bdebde26a997'
    auth_token = '0adf1745a0013eb9b3232b38ddcd768a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='NO SLOTS OPEN YET for ' + city + ' Keep Checking',
        to='whatsapp:+919901595582'
    )
driver.quit()