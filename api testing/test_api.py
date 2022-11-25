import requests


def test_first_api():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    res = response.json()
    print(res)
    print(type(res))
    # for i in range(len(res)):
    #     k = res['entries'][i]['API']
    #     print(k)
