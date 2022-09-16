import requests

def result_sunset_sunrise():


    test = requests.get('https://api.sunrise-sunset.org/json')
    result = test.json()
    result = dict(result["results"])
    DICT_RESULT = {}
    DICT_RESULT["sunrise"]=result["sunrise"]
    DICT_RESULT["sunset"]=result["sunset"]
    return DICT_RESULT.items()

def result_time_all():


    test = requests.get('https://api.sunrise-sunset.org/json')
    result = test.json()
    result = dict(result["results"])
    return result.items()

if __name__ == '__main__':

    for key,value in result_time_all():
        print(key," is : ",value)
    print("\n\nresults of excersise :\n\n")
    for key,value in result_sunset_sunrise():
        print(key," is : ",value)