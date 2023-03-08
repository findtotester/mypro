import seldom
from seldom.utils import cache
from seldom import depend


class Testqiyechaxun(seldom.TestCase):

    def test_01_GetTagStoreNum(self):
        url = "https://ripx.iuoooo.com/api/Enterprise/V2/GetTagStoreNum"
        data_ = {
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "scaleLevels": ["0", "1", "2", "3", "4"],
                "clientInfo": {
                    "device": "ios",
                    "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "versionNum": 180,
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                    "version": "1.8.0"
                },
                "MaxComplete": "100",
                "BusinessStates": ["0", "5"],
                "QueryType": "0",
                "OrgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "MinComplete": "0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_02_GetEnterpriseModule(self):
        url = 'https://ripx.iuoooo.com/api/Enterprise/GetEnterpriseModule'
        data_ = {
                "RateState": 1,
                "PageSize": 10,
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "PageIndex": 1
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_03_GetUserAreaNew(self):
        url = 'https://ripx.iuoooo.com/api/Area/GetUserAreaNew'
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_04_GetTotalTagStoreNum(self):
        url = 'https://ripx.iuoooo.com/api/Enterprise/V2/GetTotalTagStoreNum'
        data_ = {
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "scaleLevels": [0, 1, 2, 3, 4],
                "MaxComplete": "100",
                "BusinessStates": ["0", "5"],
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "QueryType": "0",
                "OrgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "MinComplete": "0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')
        TotalCount = self.jsonpath('$..TotalCount')
        print(TotalCount)

    def test_05_StoreFilterNew(self):
        url = 'https://ripx.iuoooo.com/api/InspectEnforce/StoreFilterNew'
        data_ = {
                "commonParam": {
                    "inspectEnum": 2,
                    "RiskLevel": None,
                    "LabelId": "00000000-0000-0000-0000-000000000000",
                    "storeTypeId": "",
                    "LabelLevel": 0,
                    "ratestate": None,
                    "pageNo": 1,
                    "clientType": 2,
                    "allStoreCount": None,
                    "fuel": "0",
                    "locationLevel": 0,
                    "count": 10,
                    "MaxComplete": "100",
                    "keywords": "",
                    "locationId": "",
                    "locations": None,
                    "scaleLevels": [0, 1, 2, 3, 4],
                    "MinComplete": "0",
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "StoreStatus": "0,5",
                    "orgId": "ab9d121e-0145-41d8-b787-460480290d42",
                    "storeTypeLevel": 0,
                    "QueryType": "0",
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')
        id = self.response["Content"][0]["Id"]
        opid = self.response["Content"][0]["StoreSecTypeId"]
        cache.set({'id': id})
        cache.set({'opid': opid})

    @depend("test_05_StoreFilterNew")
    def test_06_getsp_data(self):
        id = cache.get('id')
        url = 'https://ripx.iuoooo.com/api/InspectEnforce/getsp_data'
        data_ = {
                "StoreId": id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Data.r0[0].store_id', id)

    @depend("test_05_StoreFilterNew")
    def test_07_getStoreDetailConfig(self):
        id = cache.get('id')
        opid = cache.get('opid')
        url = "https://patrol.iuoooo.com/api/ModuleLayOutDetail/getStoreDetailConfig"
        data_ = {
                "configPara": {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "storeId": id,
                    "storeState": "170",
                    "versionType": 1,
                    "operId": opid
                }
            }

        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            msg = self.response['Message']
            if msg not in ('获取成功', '没有配置布局，请仔细检查！', '请配置经营业态'):
                print('接口异常')
                return False
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    @depend("test_05_StoreFilterNew")
    def test_08_GetSupervisor(self):
        id = cache.get('id')
        url = 'https://ripx.iuoooo.com/api/User/GetSupervisor'
        data_ = {
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "OrgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "StoreId": id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    @depend("test_05_StoreFilterNew")
    def test_09_GetSelfSupervise(self):
        id = cache.get('id')
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/GetSelfSupervise'
        data_ = {
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "levelId": "899f03f9-c2c8-44e0-9561-7acfc76ea2d1",
                "isOneLevel": "0",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "storeId": id,
                "type": "9"
}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('storeId', id)

    @depend("test_05_StoreFilterNew")
    def test_10_GetStoreSchemaInfo(self):
        id = cache.get('id')
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/GetStoreSchemaInfo'
        data_ = {
                    "storeId": id
                }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('IsSuccess', True)
