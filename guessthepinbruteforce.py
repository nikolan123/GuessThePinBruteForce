import requests
import time

url = "https://www.guessthepin.com/prg.php"

for i in range(10000):

    payload = ("guess=" + str(i).zfill(4))
    # payload = "guess=" + guess
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, data=payload, headers=headers)
    rtext = response.text

    if "Sorry" in rtext:
        print(payload)
        print("incorrect")
    else:
        print(payload)
        print("umm correct lmao")
    time.sleep(0)
