import seldom


class TestLiveManage(seldom.TestCase):
    def test_01_GetEnterChainDeviceList(self):
        """获取门店和所有下级的门店设备"""
        url = 'https://patrol.iuoooo.com/api/StoreQuery/GetEnterChainDeviceList'
        data_ = {
                    "chainList": [],
                    "isCascade": 1,   # 1:获取级联下级门店 2:获取当前门店的数据
                    "pageIndex": 1,
                    "pageSize": 10,
                    "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                    "storeName": ""
                }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess",True)

    def test_02_getStoreEquipmentList(self):
        """门店直播信息"""
        url = 'https://patrol.iuoooo.com/api/StoreDetail/getStoreEquipmentList'
        data_ = {
                "equipmentStatus": 0,
                "mapType": "10",
                "rtcType": 0,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_03_GetEnterChainListById(self):
        """获取级联下级的门店"""
        url = 'https://patrol.iuoooo.com/api/Simple/GetEnterChainListById'
        data_ = {
                "state": 2,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess",True)
        count = self.jsonpath('$..storeId')
        if count not in (False,None) and len(count)<0:
            raise AssertionError

    def test_04_GetIsSelfCheck(self):
        """获取设备自检能力"""
        url = 'https://lvc.iuoooo.com/Jinher.AMP.LVC.SV.JHDeviceQuerySV.svc/GetIsSelfCheck'
        data_ = {"sn": "021b57e2f9"}
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","设备支持自检")

    def test_05_CommandDeviceSelfCheck(self):
        """进行设备自检"""
        url = 'https://lvc.iuoooo.com/Jinher.AMP.LVC.SV.JHDeviceQuerySV.svc/CommandDeviceSelfCheck'
        data_ = {"sn": "021b57e2f9"}
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","自检操作失败")

    def test_06_GetCloudStorageService(self):
        """获取云回放服务"""
        url = 'https://patrol.iuoooo.com/api/CacheEquManage/GetCloudStorageService'
        data_ = {
                "mac": "1b57e2f9",
                "no": "1",
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Mac","1b57e2f9")

    def test_07_getDeviceAbility(self):
        """获取设备能力"""
        url = 'https://patrol.iuoooo.com/api/StoreDetail/getDeviceAbility'
        data_ = {"deviceAbilityHash": "JH0SHZ-W856RT-WF-02T"}
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")