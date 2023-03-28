import seldom


class TestVedioMonitor(seldom.TestCase):
    def test_01_GetUserDeviceListG(self):
        url = 'https://patrol.iuoooo.com/api/StoreQuery/GetUserDeviceListG'
        data_ = {
                "appId": "9be42759-9686-4541-b5a4-2be15a5c7d73",
                "level": 0,
                "orgId": "7035c461-c80e-49ce-a7c8-5584f0453646",
                "pageIndex": 1,
                "pageSize": 10,
                "rtcType": "0",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        count = self.response["TotalCount"]
        assert int(count) >= 1

    def test_02_GetOperateInfo(self):
        url = 'https://ripx.iuoooo.com/api/UserManage/v2/GetOperateInfo'
        data_ = {
                "appId": "9be42759-9686-4541-b5a4-2be15a5c7d73",
                "clientType": "1",
                "isShowDisabled": "0",
                "orgId": "7035c461-c80e-49ce-a7c8-5584f0453646",
                "type": "0",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        count = self.jsonpath('$..Name')
        print(count)
        assert  len(count) >= 1
        self.assertPath("Message","操作成功")

    def test_03_GetUserAreaNew(self):
        url = 'https://ripx.iuoooo.com/api/Area/GetUserAreaNew'
        data_ = {
                "AppId": "9be42759-9686-4541-b5a4-2be15a5c7d73",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        count = self.jsonpath('$..Name')
        assert  len(count) >= 1
        self.assertPath("Message","操作成功")