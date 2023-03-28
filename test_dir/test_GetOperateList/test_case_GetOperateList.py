import seldom
from seldom import file_data


class TestGetOperateList(seldom.TestCase):
    def start(self):
        self.url = f"https://ripx.iuoooo.com/api/UserRole/GetOperateList"
        self.user1 = "6166b6d1-ccaf-47af-91b8-790c2a53445a"
        self.user2 = "b1a04ddb-cf05-45a4-bba8-3886e0ae84b2"

    @file_data("test_data/json_api.json", key="GetOperateList_case")
    def test_login(self, _, req, resp):
        data_ = {
                    "RoleName": req["RoleName"],
                    "appId": "b7859e86-edc7-4748-8896-9326ffab1930",
                    "businessId": "1060",
                    "clientType": "1",
                    "isShowDisabled": "0",
                    "orgId": "8d027728-cb05-4b88-8280-36083804166c",
                    "type": "0",
                    "userId":  req["userId"]
                }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            data = self.response["Data"]
            self.assertIsNotNone(data)
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

