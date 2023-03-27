import requests
import json
import jsonpath


class TestSampleApi:
    def test_first_api(self):
        response = requests.get('https://reqres.in/api/users?page=2')
        res = response.json()
        print(res)
        print(type(res))
        for i in res:
            print(f"{str(i)}: ", res[i])
        # for i in range(len(res)):
        #     k = res['entries'][i]['API']
        #     print(k)

    def test_get_single_user(self):
        response = requests.get('https://reqres.in/api/users/2')
        res = response.json()
        print(res)
        email = res["data"]["email"]
        print("email: " + email, ", url: " + res["support"]["url"], "and text: " + res["support"]["text"])

    def test_single_user_not_found(self):
        response = requests.get('https://reqres.in/api/users/23')
        res = response.status_code
        assert res == 404, "The request is not giving correct response"
        print(res)

    def test_list_resources(self):
        response = requests.get('https://reqres.in/api/unknown')
        res = response.json()
        s_code = response.status_code
        print(s_code, res)
        json_response = json.loads(response.text)
        new_res = jsonpath.jsonpath(json_response, 'total_pages')
        print(new_res[0])

    def test_create_user(self):
        with open('C:/Users/mahes/PycharmProjects/python-API-Testing/TestData/create_user.json', 'r') as file:
            payload = json.loads(file.read())
        response = requests.post('https://reqres.in/api/users', payload)
        res = response.json()
        print(response.status_code, res['id'])
        assert response.status_code == 201
        headers = response.headers
        print(headers.get('Content-Length'), len(headers))

    def test_update_user(self):
        with open('C:/Users/mahes/PycharmProjects/python-API-Testing/TestData/create_user.json', 'r') as file:
            payload = json.loads(file.read())
        response = requests.put('https://reqres.in/api/users/2', payload)
        res = response.json()
        print(response.status_code, res['job'])
        assert response.status_code == 200
        headers = response.headers
        print(headers, len(headers))

    def test_update_user_entity(self):
        with open('C:/Users/mahes/PycharmProjects/python-API-Testing/TestData/update_user.json', 'r') as file:
            payload = json.loads(file.read())
        response = requests.patch('https://reqres.in/api/users/2', payload)
        res = response.json()
        print(response.status_code, res['job'])
        assert response.status_code == 200
        headers = response.headers
        print(headers, len(headers))
