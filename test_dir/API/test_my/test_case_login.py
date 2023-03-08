import seldom
from seldom import file_data


class TestCaseLogin(seldom.TestCase):
    def start(self):
        self.url = f"https://aup.iuoooo.com/Jinher.AMP.App.SV.UserAppSV.svc/UserLoginNew"

    @file_data("test_data/json_api.json", key="login_case")
    def test_login(self, _, req, resp):
        data_ = {
            "dto": {
                  "AppId": req["AppId"],
                  "Account": req["Account"],
                  "Password": req["Password"]
              }
        }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath("Message", resp["Message"])
            self.assertPath("IsSuccess", resp["IsSuccess"])
            self.assertPath("StatusCode", resp["StatusCode"])
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

