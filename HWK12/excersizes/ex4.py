# coding=utf-8
import bs4
import requests
import unidecode
import datetime
import json

def run_oghate_shari():

    req = requests.get('https://www.time.ir/')
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    soup.prettify()
    result_times = []
    needing_list = ["ephemerisAzanMorning", "ephemerisAzanSunrise", "ephemerisAzanMoon", "ephemerisAzanSunset",
                    "ephemerisAzanNight", "ephemerisMidNight"]
    needing_list_en = ["azane_sobh", "tolooe_khorshid", "azane_zohr", "ghoroobe_khorshid", "azane_maghreb", "nime_shab"]
    needing_list_fa_en = dict(zip(needing_list, needing_list_en))
    result = {}
    for key in needing_list:
        x = soup.find("span", {"class": f"{key}"})
        result[needing_list_fa_en[x["class"][1]]] = datetime.datetime.strptime(unidecode.unidecode(x.findNext("span").text),
                                                                               "%H : %M").strftime("%I:%M %p")
    with open("ex4_JSON_time.json", "w") as f:
        f.write(json.dumps(result))
    with open("ex4_JSON_time.json", "r") as m:
        x = dict(json.load(m))
        print(x)

if __name__ == '__main__':

    run_oghate_shari()