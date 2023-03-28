import seldom


class TestStoreList(seldom.TestCase):
    def test_01_GetBookExhibitByAppId(self):
        url = 'https://patrol.iuoooo.com/api/Release/GetBookExhibitByAppId'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "type": 1
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        count = self.jsonpath('$..ExText')
        assert  len(count)>= 1
        self.assertPath("Message","获取成功")

    def test_02_getStoreFilterInfos(self):
        url = 'https://patrol.iuoooo.com/api/StoreQuery/getStoreFilterInfos'
        data_ = {
                "getStoreFilterInfosSearchDTO": {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "areaCode": "2-110100",
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
                }
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        count = self.jsonpath('$..groupName')
        assert len(count) >1

    def test_03_GetFssStoreList(self):
        url = 'https://patrol.iuoooo.com/api/StoreQuery/GetFssStoreList'
        data_ = {
                    "storeListSearchDTO": {
                        "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                        "areaCode": "2-110100",
                        "filter": {
                            "areaCode": "",
                            "businessstatusvalue": "",
                            "distance": "",
                            "govGrade": "",
                            "labelIds": [],
                            "marketCode": "",
                            "newlableid": "",
                            "operateType": [],
                            "restaurantType": "",
                            "risklevel": "",
                            "storescore": "",
                            "tradeAreaCode": ""
                        },
                        "isSearchRiskLevelCount": False,
                        "lat": "40.055227",
                        "lng": "116.303105",
                        "pageIndex": 1,
                        "pageSize": 20,
                        "searchContent": "",
                        "storescorecode": "4",
                        "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
                    }
                }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        count = self.jsonpath('$..storeName')
        assert len(count) >1