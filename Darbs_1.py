import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service,options=option)

url = "https://www.auto24.lv/kasutatud/nimekiri.php?bn=2&a=100&aj=&ssid=125727415&b=7&bw=2038&bi=EUR&ab=0&ab%5B%5D=-2&ae=1&af=50&otsi=mekl%C4%93t"
driver.get(url)
time.sleep(2)

# Open url and get data
find = driver.find_element(By.ID,"onetrust-reject-all-handler")
find.click()
time.sleep(2)

masinas = []

find = driver.find_element(By.ID,"usedVehiclesSearchResult-flex")
masinas = find.find_elements(By.XPATH,"./div")

json_file = "masinas.json"
data = []

n = 1
cena = 7000
nobraukums = 200000

with open(json_file, 'w') as file:
    for obj in masinas:
        print("Loading... " + str(n) + "/" + str(len(masinas)))
        try:
            description = obj.find_element(By.CLASS_NAME, "description")

            #Iegūst sludinājuma mašīnas nosaukumu
            title = description.find_element(By.CLASS_NAME, "title")
            title1 = title.find_element(By.CLASS_NAME, "main")
            title2 = title1.find_elements(By.TAG_NAME, "span")

            #Iegūst sludinājuma mašīnas cenu
            price = description.find_element(By.CLASS_NAME,"finance")
            price1 = price.find_element(By.CLASS_NAME,"pv")
            price2 = price1.find_element(By.CLASS_NAME,"price")
            price3 = price2.get_attribute("innerText")
            price3 = price3.replace("\u00a0\u20ac","")
            price3 = price3.replace("\u00a0","")

            #Iegūst sludinājuma mašīnas nobraukumu
            mileage = description.find_element(By.CLASS_NAME,"extra")
            mileage1 = mileage.find_element(By.CLASS_NAME,"mileage")
            mileage2 = mileage1.get_attribute("innerText")
            mileage2 = mileage2.replace("\u00a0\u20ac","")
            mileage2 = mileage2.replace("\u00a0","")

            #Iegūst sludinājuma linku
            link = obj.find_element(By.TAG_NAME,"a")
            link1 = link.get_attribute("href")

            if int(price3) <= cena and int(mileage2[:-2]) < nobraukums:
                data.append({
                    "Nosaukums": title2[0].text + title2[1].text,
                    "Cena": price3,
                    "Nobraukums": mileage2,
                    "Links": link1
                })
        except:
            print("Objekts nr." + str(n) + " nav mašīnas sludinājums vai arī tas nesatur pieprasīto informāciju.")
        finally:
            n += 1

    json.dump(data, file)
    print("Dati tika ielādēti failā 'masinas.json'")