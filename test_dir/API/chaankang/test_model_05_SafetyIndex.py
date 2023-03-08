import seldom
from seldom.utils import cache
from seldom import depend


class TestSafetyIndex(seldom.TestCase):

    def start(self):
        self.store_id = cache.get("store_id")
        self.store_name = cache.get("store_name")
        self.oper_id = cache.get("oper_id")

    def test_01_GetFoodSafetyIndex_Store_out(self):    # 门店安康指数
        url = f"http://dss.iuoooo.com/CockpitMobile/GetFoodSafetyIndex_Store_out"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "IndexCode": 4,
                "StoreId": self.store_id,
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('SCater.Data.FoodSafetyIndex_StoreList[0].IndexNameText', "当前企业安康指数")

    # 企业信息
    def test_02_Company_html(self):
        url = "http://dss.iuoooo.com/Html/map/Company/Company.html?newpage=1&curChangeOrg=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&changeOrg=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&storeId=ff223c14-aacb-4a3d-be72-548000c617d6&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&shopOrgId=ab9d121e-0145-41d8-b787-460480290d42&isLogin=1&hidjhnavigation=1&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&IndexCode=4&roleName=%E7%AE%A1%E7%90%86%E5%91%98&RiskType=0&account=18800000064&relationOId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
        self.get(url)
        self.assertStatusCode(200)

    def test_03_PermissionHuzhou(self):
        url = "http://dss.iuoooo.com/CockpitMobile/PermissionHuzhou"
        data_ = {"AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                 "StoreId": self.store_id
                 }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_04_OperateFoodSafety(self):
        url = "http://dss.iuoooo.com/CockpitMobile/OperateFoodSafety"
        data_ = {"IndexCode": 4,
                 "StoreId": self.store_id,
                 "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                 "EBCOrganizationId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
                 }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_05_GetStorDataInfo(self):
        url = "http://dss.iuoooo.com/CockpitMobile/GetStorDataInfo"
        data_ = {
                 "StoreId": self.store_id
                 }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("RM.Code", 200)

    def test_06_RankDistance(self):
        url = "http://dss.iuoooo.com/CockpitMobile/RankDistance"
        data_ = {"IndexCode": 4,
                 "StoreId": self.store_id,
                 "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                 "EBCOrganizationId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
                 }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_07_OperateFoodDiagnostic(self):
        url = "http://dss.iuoooo.com/CockpitMobile/OperateFoodDiagnostic"
        data_ = {"IndexCode": 4,
                 "StoreId": self.store_id,
                 "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                 "EBCOrganizationId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
                 }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    # 动态排行
    def test_08_RankDistanceOut(self):
        url = "https://dss.iuoooo.com/CockpitMobile/RankDistanceOut"
        data_ = {
                "IndexCode": 4,
                "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "storeid": self.store_id
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath("SCater.Code", 200)
            count = len(self.jsonpath("$..Id"))
            if count < 0:
                print("获取门店数据失败")
                raise AssertionError
        except AssertionError as e:
            print('执行结果:Failed')
            raise e



