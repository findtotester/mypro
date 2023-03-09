import seldom
from seldom.utils import cache
from seldom import depend


class TestSearchStore(seldom.TestCase):
    def start(self):
        self.store_id = "ff223c14-aacb-4a3d-be72-548000c617d6"
        self.store_name = "金玉食府"

    def test_01_GetConfigMapKeywords(self):
        url = "https://map.iuoooo.com/api/MapDataConfig/GetConfigMapKeywords"
        data_ = {
                "CenterLat": 39.95993,
                "CenterLon": 116.298262,
                "ClientType": 0,
                "Code": "110108",
                "ElevatorCompanyList": [],
                "Level": 3,
                "LocationLat": 40.055178,
                "LocationLon": 116.302901,
                "MapDataRange": "1",
                "MapDataTypeInfoList": [{
                    "MapDataType": 80,
                    "RoleCode": 0
                }, {
                    "MapDataType": 5,
                    "RoleCode": 0
                }, {
                    "MapDataType": 72,
                    "RoleCode": 0
                }],
                "MapId": "3b000b7a-11a8-49c8-a71b-c27fd6fbd0ed",
                "MapType": 0,
                "NortheastLat": 40.16097,
                "NortheastLon": 116.39509,
                "OrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "RoleType": 0,
                "SearchText": "金玉食府",
                "SouthwestLat": 39.88672,
                "SouthwestLon": 116.04882,
                "StoreFilter": {
                    "FilterList": [],
                    "IsHasSelect": False
                },
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        store_id = self.jmespath("Content[0].StoreId")
        store_name = self.jmespath("Content[0].StoreName")
        if store_id in (None,False):
            store_id = self.store_id
            store_name = self.store_name
        cache.set({"store_id": store_id})
        cache.set({"store_name": store_name})


    @depend("test_01_GetConfigMapKeywords")
    def test_02_GetConfigMap(self):
        store_id = cache.get("store_id")
        print("123", store_id)
        url = "https://map.iuoooo.com/api/MapDataConfig/GetConfigMap"
        data_ = {
                "CenterLat": 39.95993,
                "CenterLon": 116.298262,
                "ClientType": 0,
                "Code": "110108",
                "ElevatorCompanyList": [],
                "Level": 3,
                "LocationLat": 40.055178,
                "LocationLon": 116.302901,
                "MapDataRange": "1",
                "MapDataTypeInfoList": [{
                    "MapDataType": 80,
                    "RoleCode": 0
                }, {
                    "MapDataType": 5,
                    "RoleCode": 0
                }, {
                    "MapDataType": 72,
                    "RoleCode": 0
                }],
                "MapId": "3b000b7a-11a8-49c8-a71b-c27fd6fbd0ed",
                "MapType": 0,
                "NortheastLat": 40.16097,
                "NortheastLon": 116.39509,
                "OrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "RoleType": 0,
                "SouthwestLat": 39.88672,
                "SouthwestLon": 116.04882,
                "StoreFilter": {
                    "FilterList": [],
                    "IsHasSelect": False
                },
                "StoreIds": [store_id],
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
            }
        r = self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Content.MapAnnotationInfoList[0].MapAnnotationList[0].AnnotationId", store_id)
        oper_id = r.json()["Content"]["MapAnnotationInfoList"][0]["MapAnnotationList"][0]["StoreSecTypeId"]
        equipment_status = r.json()["Content"]["MapAnnotationInfoList"][0]["MapAnnotationList"][0]["Status"]
        cache.set({"oper_id": oper_id})
        cache.set({"equipment_status": equipment_status})

    @depend("test_02_GetConfigMap")
    def test_03_GetAppId(self):
        store_id = cache.get("store_id")
        if store_id is None:
            store_id = "ff223c14-aacb-4a3d-be72-548000c617d6"
            cache.set({"store_id": store_id})

        url = f"https://patrol.iuoooo.com/api/SynPatrol/GetAppId"
        data_ = {
                "StoreId": store_id
                }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', "成功")

    @depend("test_02_GetConfigMap")
    def test_04_getStoreDetailPavConfig(self):
        store_id = cache.get("store_id")
        url = f"https://patrol.iuoooo.com/api/ModuleLayOutDetail/getStoreDetailPavConfig"
        data_ = {
                "storeId": store_id,
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', "获取成功")

    @depend("test_02_GetConfigMap")
    def test_05_getStoreDetailConfig(self):
        store_id = cache.get("store_id")
        store_name = cache.get("store_name")
        oper_id = cache.get("oper_id")
        url = f"https://patrol.iuoooo.com/api/ModuleLayOutDetail/getStoreDetailConfig"
        data_ = {
                "configPara": {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "operId": oper_id,
                    "shopAppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "storeAppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "storeId": store_id,
                    "storeName": store_name,
                    "storeState": 200
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', "获取成功")

    @depend("test_05_getStoreDetailConfig")
    def test_06_GetMapStoreBase(self):    # 地图上的门店卡片
        store_id = cache.get("store_id")
        equipment_status = cache.get("equipment_status")
        url = f"https://patrol.iuoooo.com/api/StoreDetail/GetMapStoreBase"
        data_ = {
                "equipmentStatus": equipment_status,
                "lat": "40.05518",
                "lng": "116.3029",
                "storeId": store_id,
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', "获取成功")

