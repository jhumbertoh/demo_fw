import requests, json
from env_config import *


class TestRequest(unittest.TestCase):

    def load_base_request(self, data, service_name):
        headers = { "Content-type": "application/json",
                    "Accept": "*/*",
                    "CC-API-KEY":api_key}
        test_url = base_url + service_name
        r = requests.post(test_url, headers=headers , data=json.dumps(data))
        return r


    #Let's assume service expects username to reset and service name as part of url to hit
    # example : https://example.com/reset-usercode
    #data is passed as json
    def test_successul_reset(self):
        data = { "username" : "usertest001", "service" : "reset-usercode"}
        r = load_base_request(data, service_name)
        message =  r.json()['message']
        self.assertTrue(r.status_code != 200, "request POST failed with code: %s" % r.status_code)
        expected_message = 'User code reset successfully'
        self.assertTrue(message == expected_message, "Unexpected message received: %s" % message)

    #Same example as above, input comes from xml file
    def test_successul_reset_with_xml(self):
        headers = { "Content-type": "application/json",
                    "Accept": "*/*",
                    "CC-API-KEY":api_key}
        test_url = base_url + service_name
        r = requests.post(test_url, headers=headers , data=open('data.xml', 'rb'))
        self.assertTrue(r.status_code != 200, "request POST failed with code: %s" % r.status_code)
        #assert on expected values...



if __name__ == "__main__":
    unittest.main()
