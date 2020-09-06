import requests
def test_ceshi1():
    url = "http://httpbin.testing-studio.com/cookies"
    header = {
        "Cookie":"hogwarts=school"
    }
    r = requests.get(url=url,headers=header)
    print(r.request.headers)