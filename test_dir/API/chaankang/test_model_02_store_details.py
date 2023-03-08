import seldom
from seldom.utils import cache

class TestStoreDetails(seldom.TestCase):

    def start(self):
        self.store_id = cache.get("store_id")
        self.store_name = cache.get("store_name")
        self.equipment_status = cache.get("equipment_status")

    def test_01_getStoreMaterArea(self):   # 门店直播信息
        url = "https://iustore.iuoooo.com/Jinher.AMP.Store.SV.StoreDetailSv.svc/getStoreMaterArea"
        data_ = {
                "storeId": self.store_id,
                "newVersionNum": "170",
                "modelCode": "playAreaCorner",
                "equipmentStatus": self.equipment_status
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_02_getStoreBaseInfoArea(self):   # 门店基本信息
        url = "https://iustore.iuoooo.com/Jinher.AMP.Store.SV.StoreDetailSv.svc/getStoreBaseInfoArea"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "storeId": self.store_id,
                "lng": "116.3033",
                "lat": "40.05526",
                "equipmentStatus": self.equipment_status
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("storeName", self.store_name)

    def test_03_getStoreReportInfo(self):   # 监督电话
        url = "https://iustore.iuoooo.com/Jinher.AMP.Store.SV.StoreDetailSv.svc/getStoreReportInfo"
        data_ = {"shopAppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    def test_04_getStoreAttLevelList(self):   # 资质证照
        url = "https://iustore.iuoooo.com/Jinher.AMP.Store.SV.StoreDetailSv.svc/getStoreAttLevelList"
        data_ = {"storeId": self.store_id}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    def test_05_getStoreRestInfoArea(self):   # 餐厅介绍
        url = "https://iustore.iuoooo.com/Jinher.AMP.Store.SV.StoreDetailSv.svc/getStoreRestInfoArea"
        data_ = {"storeId": self.store_id}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")
