import seldom
from seldom.utils import cache

"""门店管理"""
class TestStoreManage(seldom.TestCase):
    def start(self):
        self.AppId = "2fd5f092-d360-4783-b95c-6d47ee5cac44"
        self.OrgId = "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
        self.FWID = "9b8bb73f-7783-4800-8f7b-f91b0def0fa4"
        self.FWSID = "1e310325-5737-4057-89be-c54281d5b67a"
        self.SID = "50220da6-9649-40db-b38c-9aa3181146ac"
        self.StoreId = "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
        self.StoreName = "白兔咖啡"
        self.OperId = "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc"
        self.UserId = "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
        self.Account = "18800000064"
        self.Menu = "组织管理"

    def test_01_GetUserOrgRoles(self):
        """获取门店placeId"""
        url = 'https://layouts.iuoooo.com/api/FormWork/GetUserOrgRoles'
        data_ = {
                "AppId": self.AppId,
                "Entry": 1,
                "IsBiggerThan25": "1",
                "IsEnable": 1,
                "IsEnableC": 1,
                "OperId": self.OrgId,
                "OrgId": self.OrgId,
                "RoleName": "管理员",
                "RoleNameList": [],
                "RoleTypeClient": "2",
                "SelectedOrgId": self.OrgId,
                "ShopId": self.AppId,
                "StoreId": self.StoreId,
                "Type": 2,
                "UserAccount": self.Account,
                "UserId": self.UserId
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        placeId = self.jsonpath(f'$..[?(@.storeName=="{self.StoreName}")].placeId')
        if placeId not in (None,False):
            cache.set({"placeId": placeId[0]})
        else:
            placeId = self.AppId
            cache.set({"placeId": placeId})
            raise AssertionError

    def test_02_getCooperateStepList(self):
        """获取门店信息维护项"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/getCooperateStepList'
        data_ = {
                "appId": placeId,
                "isOneLevel": 0,
                "levelId": self.OperId,
                "storeId": self.StoreId,
                "type": "8",
                "userId": self.UserId
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message','获取成功')
        Code = self.jsonpath('$..Code')
        if len(Code)<2:
            raise AssertionError

    def test_03_GetStoreOrgByIdInfo(self):
        """获取门店组织信息"""
        url = 'https://patrol.iuoooo.com/api/SynPatrol/GetStoreOrgByIdInfo'
        data_ = {
                "storeId": self.StoreId,
                "type": "1"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('orgId', self.OrgId)

    def test_04_GetInStep(self):
        """基本信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/GetInStep'
        data_ = {
                "appId": self.AppId,
                "isOneLevel": 0,
                "levelId": self.OperId,
                "moduleCode": "se_baseinfo",
                "placeId": placeId,
                "readOnly": 0,
                "storeId": self.StoreId,
                "storeStatus": 1,
                "userId": self.UserId,
                "clientInfo": {
                    "device": "android",
                    "version": "6.309.797",
                    "versionNum": "180",
                    "appid": self.AppId
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_05_getTwoLevelOperateTypeList(self):
        """获取二级业态"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/getTwoLevelOperateTypeList'
        data_ = {
                    "appId": placeId,
                    "operateType": "7d6815f0-09cb-47a0-aa08-6be84d138a80",
                    "userId": self.UserId
                }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_06_getStreetInfos(self):
        """获取省市区街道的数据"""
        url = 'https://patrol.iuoooo.com/api/BusinessEnterQuery/getStreetInfos'
        data_ = {
                "districtCode": "632224"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_07_getCommunityByLocationId(self):
        """获取社区数据"""
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/getCommunityByLocationId'
        data_ = {
                    "locationId": "348eb972-2e13-11eb-a1b1-7cd30ae45db0"
                }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_08_getLabelList(self):
        """获取兼营范围"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/SynPatrol/getLabelList'
        data_ = {
                "appId": placeId,
                "type": 0,
                "userId": self.UserId
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_09_SubInStep(self):
        """保存基本信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/SubInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "cooperlayOutId": "1f54a3eb-5121-4003-931a-64d112f5266d",
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "modelList": [{
                    "modelCode": "se_baseinfo_companyname",
                    "modelValue": "白兔咖啡有限责任公司"
                }, {
                    "modelCode": "se_baseinfo_name",
                    "modelValue": "白兔咖啡"
                }, {
                    "modelCode": "se_baseinfo_state",
                    "modelValue": "{\"key\":\"0\",\"value\":\"\"}"
                }, {
                    "modelCode": "se_baseinfo_storeimg",
                    "modelValue": "https:\/\/upfileserver.iuoooo.com\/Jinher.JAP.BaseApp.FileServer.UI\/FileManage\/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661%2F2022092209%2Fe17a61337fed4cc3a6d88f12ad9380b2_3d2-44e2-a876-8bfd8b1057a1.jpg"
                }, {
                    "modelCode": "se_baseinfo_operone",
                    "modelValue": "{\"opertypepid\":\"00000000-0000-0000-0000-000000000000\",\"opertypeid\":\"7d6815f0-09cb-47a0-aa08-6be84d138a80\",\"opertypename\":\"食品-餐饮\",\"isonelevel\":\"1\",\"operchange\":0,\"operchangenum\":0}"
                }, {
                    "modelCode": "se_baseinfo_opertwo",
                    "modelValue": "{\"opertypepid\":\"7d6815f0-09cb-47a0-aa08-6be84d138a80\",\"opertypeid\":\"4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc\",\"opertypename\":\"中型餐饮\",\"isonelevel\":null,\"operchange\":1,\"operchangenum\":4}"
                }, {
                    "modelCode": "se_baseinfo_label",
                    "modelValue": "[{\"check\":1,\"id\":\"ba945857-7002-4252-8143-ff0ecfccb11e\",\"level\":2,\"name\":\"电梯\",\"pid\":\"92a7951f-101b-4c2b-bb3d-a0581e3a7240\"},{\"check\":1,\"id\":\"ea7a8695-2806-4729-9c44-5fcfed5e73b8\",\"level\":2,\"name\":\"重点消防企业\",\"pid\":\"a5bb75a3-5fd6-44bf-9c4a-a884fc1916df\"}]"
                }, {
                    "modelCode": "se_baseinfo_area",
                    "modelValue": "{\"address\":\"青海省海北藏族自治州刚察县伊克乌兰乡尕曲村\",\"city\":\"海北藏族自治州\",\"citycode\":\"632200\",\"community\":\"青海湖农场社区居民委员会\",\"communitycode\":\"aec48c31-2edc-11eb-a1b1-7cd30ae45db0\",\"district\":\"刚察县\",\"districtcode\":\"632224\",\"latitude\":\"37.319169\",\"locataddress\":\"青海省海北藏族自治州刚察县伊克乌兰乡尕曲村\",\"longitude\":\"100.098095\",\"province\":\"青海省\",\"provincecode\":\"630000\",\"street\":\"伊克乌兰乡\",\"streetcode\":\"348eb972-2e13-11eb-a1b1-7cd30ae45db0\"}"
                }, {
                    "modelCode": "se_baseinfo_linkname",
                    "modelValue": "lemon"
                }, {
                    "modelCode": "se_baseinfo_linktel",
                    "modelValue": "18612608626"
                }],
                "moduleCode": "se_baseinfo",
                "moduleId": "8243766d-75df-45fd-8d0d-97937c8c85a9",
                "placeId": placeId,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","保存成功")

    def test_10_GetInStep(self):
        """营业执照信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/GetInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "isOneLevel": 0,
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "moduleCode": "se_licence",
                "placeId": placeId,
                "readOnly": 0,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "clientInfo": {
                            "device": "android",
                            "version": "6.309.797",
                            "versionNum": "180",
                            "appid": self.AppId
                        }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_11_SubInStep(self):
        """保存营业执照信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/SubInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "cooperlayOutId": "1f54a3eb-5121-4003-931a-64d112f5266d",
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "modelList": [{
                    "modelCode": "se_licence_licimg",
                    "modelValue": "{\"key\":\"0\",\"value\":\"https:\/\/upfileserver.iuoooo.com\/Jinher.JAP.BaseApp.FileServer.UI\/FileManage\/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d%2F2022092209%2F5ea7efce809d46b2a92726016f64860c_342-4a41-a179-577a78c7e8ad.jpg\"}"
                }, {
                    "modelCode": "se_licence_creditcode",
                    "modelValue": "678943211024894512"
                }, {
                    "modelCode": "se_licence_legalname",
                    "modelValue": "lemon"
                }, {
                    "modelCode": "se_licence_legaltel",
                    "modelValue": "11888888606,18800000064,15501026282,13019238080,18100010001,"
                }, {
                    "modelCode": "se_licence_creditnum",
                    "modelValue": "110101199001010314"
                }, {
                    "modelCode": "se_licence_abode",
                    "modelValue": "白兔123"
                }],
                "moduleCode": "se_licence",
                "moduleId": "8aef6d7b-bd69-4a73-93af-51ccf90969ed",
                "placeId": placeId,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","保存成功")

    def test_12_GetInStep(self):
        """许可证信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/GetInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "isOneLevel": 0,
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "moduleCode": "se_aptitude",
                "placeId": placeId,
                "readOnly": 0,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "clientInfo": {
                    "device": "android",
                    "version": "6.309.797",
                    "versionNum": "180",
                    "appid": self.AppId
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_13_SubInStep(self):
        """保存许可证信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/SubInStep'
        data_ = {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "cooperlayOutId": "1f54a3eb-5121-4003-931a-64d112f5266d",
                    "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                    "modelList": [{
                        "modelCode": "se_aptitude_foodimg",
                        "modelValue": "{\"key\":\"0\",\"value\":\"https:\/\/fileserver.iuoooo.com\/Jinher.JAP.BaseApp.FileServer.UI\/FileManage\/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661%2F2022042014%2F19d4b734-f341-4c40-97d6-0b36fe6a1372_Img_2c06d08d-c9d6-4d39-b73b-4d56d19b9081.jpg\"}"
                    }, {
                        "modelCode": "se_aptitude_liccode",
                        "modelValue": "JHCY000010"
                    }, {
                        "modelCode": "se_aptitude_licexpire",
                        "modelValue": "2023-09-06"
                    }, {
                        "modelCode": "se_aptitude_proposer",
                        "modelValue": "白兔"
                    }, {
                        "modelCode": "se_aptitude_signer",
                        "modelValue": "白兔"
                    }, {
                        "modelCode": "se_aptitude_signdate",
                        "modelValue": "2021-07-22"
                    }, {
                        "modelCode": "se_aptitude_supervisor",
                        "modelValue": "白兔"
                    }, {
                        "modelCode": "se_aptitude_watchdog",
                        "modelValue": "白兔"
                    }, {
                        "modelCode": "se_aptitude_registauth",
                        "modelValue": "白兔"
                    }],
                    "moduleCode": "se_aptitude",
                    "moduleId": "54a12ac3-f6b7-4117-b16a-e92b4c1092bc",
                    "placeId": placeId,
                    "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                    "storeStatus": 1,
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
                }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","保存成功")

    def test_14_GetStoreRateListByStoreId(self):
        """风险等级信息"""
        url = 'https://patrol.iuoooo.com/api/Store/GetStoreRateListByStoreId'
        data_ = {
                "newStoreInfoId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "pIndex": 1,
                "pSize": 100,
                "versionNum": 1
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess",True)
        State = self.jsonpath('$..State')
        if len(State) < 0:
            raise AssertionError

    def test_15_GetStoreRateDetail(self):
        """获取风险平级信息"""
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = 'https://patrol-ui.iuoooo.com/NewStoreManage/GetStoreRateDetail'
        data_ = {"storerateId":"5fb0ee41-8f9c-4991-8af6-9904de82603f"}
        self.post(url,data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess",True)

    def test_16_GetInStep(self):
        """经营信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/GetInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "isOneLevel": 0,
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "moduleCode": "se_storetype",
                "placeId": placeId,
                "readOnly": 0,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "clientInfo": {
                    "device": "android",
                    "version": "6.309.797",
                    "versionNum": "180",
                    "appid": self.AppId
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_17_GetEntrustStoreList(self):
        """获取委托单位门店列表"""
        url = 'https://patrol.iuoooo.com/api/NewStoreManage/GetEntrustStoreList'
        data_ = {
                "param": {
                    "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "Name": "",
                    "PageIndex": 1,
                    "PageSize": 20,
                    "StoreId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_18_GetStoreOperList(self):
        """获取集配单位门店列表"""
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/GetStoreOperList'
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "CompanyName": "",
                "PageIndex": 0,
                "PageSize": 0,
                "StoreId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_19_SubInStep(self):
        """保存经营信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/SubInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "cooperlayOutId": "1f54a3eb-5121-4003-931a-64d112f5266d",
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "modelList": [{
                    "modelCode": "se_storetype_mealmodel",
                    "modelValue": "{\"distrlist\":[],\"distrmode\":\"3\",\"distrnum\":\"0\",\"imgurl\":\"\",\"inname\":\"\"}"
                }, {
                    "modelCode": "se_storetype_mealtime",
                    "modelValue": "[\"09:00-22:00\"]"
                }, {
                    "modelCode": "se_storetype_mealtel",
                    "modelValue": "13681181315"
                }, {
                    "modelCode": "se_storetype_mealdesc",
                    "modelValue": "白兔咖啡用于上好的巴西咖啡豆现场打磨，为你制作一份美味的美式咖啡☕️23"
                }, {
                    "modelCode": "se_storetype_mealsize",
                    "modelValue": "[{\"key\":\"6\",\"value\":\"＜50㎡或＜25座\",\"check\":0},{\"key\":\"5\",\"value\":\"50～150㎡或25～75座\",\"check\":0},{\"key\":\"1\",\"value\":\"＜150㎡或＜75座\",\"check\":0},{\"key\":\"2\",\"value\":\"150～500㎡或75～250座\",\"check\":0},{\"key\":\"3\",\"value\":\"500～3000㎡或250～1000座\",\"check\":1},{\"key\":\"4\",\"value\":\">3000㎡或＞1000座\",\"check\":0}]"
                }, {
                    "modelCode": "se_storetype_mealitem",
                    "modelValue": "咖啡"
                }, {
                    "modelCode": "se_storetype_mealcate",
                    "modelValue": "[{\"check\":1,\"key\":\"c1543ff4-23c6-4440-88c9-ebd44da0043a\",\"value\":\"咖啡店\"}]"
                }, {
                    "modelCode": "se_storetype_meallive",
                    "modelValue": "0"
                }, {
                    "modelCode": "se_storetype_mealtake",
                    "modelValue": "0"
                }, {
                    "modelCode": "se_storetype_mealcoll",
                    "modelValue": "1"
                }, {
                    "modelCode": "se_storetype_mealconsum",
                    "modelValue": "120"
                }, {
                    "modelCode": "se_storetype_mealchain",
                    "modelValue": "{\"key\":\"\",\"value\":\"直营加盟\"}"
                }],
                "moduleCode": "se_storetype",
                "moduleId": "df1175a0-f95c-4318-bd4f-daa800a291d5",
                "placeId": placeId,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","保存成功")

    def test_20_getCooperateLiveInfoOne(self):
        """直播信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/getCooperateLiveInfoOne'
        data_ = {
                "appId": placeId,
                "isOneLevel": 0,
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "moduleCode": "se_equipment",
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess",True)

    def test_21_getBusLiveListsTwo(self):
        """获取直播列表"""
        url = 'https://patrol.iuoooo.com/api/BusinessEnterQuery/getBusLiveListsTwo'
        data_ = {
                "flag": 1,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_22_deleteBusLive(self):
        """删除设备"""
        live_id = self.jsonpath(f'$..[?(@.liveCode=="021b57e2f9")].liveId')
        url = 'https://patrol.iuoooo.com/api/BusinessEnterQuery/deleteBusLive'
        data_ = {
                    "liveId": live_id[0],
                    "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                    "storeStatus": 1,
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
                }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","操作成功")

    def test_23_GetEquipmentModuleInfo(self):
        """获取添加设备类型"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/Release/GetEquipmentModuleInfo'
        data_ = {
                "appId": placeId,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess",True)

    def test_24_getCooperateStoreBasicInfoOne(self):
        """获取门店信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/getCooperateStoreBasicInfoOne'
        data_ = {
                "appId": placeId,
                "cooperlayOutId": "1f54a3eb-5121-4003-931a-64d112f5266d",
                "flag": 1,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess",True)

    def test_25_getLiveTitleInfo(self):
        """获取直播标题"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessEnterQuery/getLiveTitleInfo'
        data_ = {
                "appId": placeId,
                "operTypeId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_26_submitBusLiveJHTwo(self):
        """添加直播"""
        url = 'https://patrol.iuoooo.com/api/BusinessEnterQuery/submitBusLiveJHTwo'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "appName": "查安康",
                "cooperlayOutId": "1f54a3eb-5121-4003-931a-64d112f5266d",
                "isOldLibrary": True,
                "liveTitle": "动物粗加工间",
                "moduleId": "bce613e1-936d-4aa8-8e58-d7951f74d528",
                "sn": "021b57e2f9",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","添加设备成功")

    def test_27_SetAuth(self):
        """修改企业密码"""
        url = 'https://patrol.iuoooo.com/api/Simple/SetAuth'
        data_ = {
                "account": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "passWord": "111111",
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","设置成功")

    def test_28_getsp_data(self):
        """我的组织"""
        url = 'https://ripx-ui.iuoooo.com/api/InspectEnforce/getsp_data'
        data_ = {
                "StoreId": "ff223c14-aacb-4a3d-be72-548000c617d6"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success","true")

    def test_29_GetEnterChainListV2(self):
        """获取父级门店"""
        url = 'https://patrol.iuoooo.com/api/Simple/GetEnterChainListV2'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "pageIndex": 1,
                "pageSize": 20,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess",True)
        count = self.jsonpath('$..bindId')
        if len(count)<0:
            raise AssertionError

    def test_30_DelFirmChain(self):
        """删除父级门店"""
        chainId = self.jsonpath('$..chainId')
        url = 'https://patrol.iuoooo.com/api/Simple/DelFirmChain'
        data_ = {
                "chainId": chainId[0],
                "state": 2,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","操作成功")

    def test_31_GetFirmChainList(self):
        """获取门店列表"""
        url = 'https://patrol.iuoooo.com/api/Simple/GetFirmChainList'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "condition": "小飞生产供货商吉林分公司",
                "pageIndex": 1,
                "pageSize": 20
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_32_AddEnterChainV2(self):
        """添加父级门店"""
        url = 'https://patrol.iuoooo.com/api/Simple/AddEnterChainV2'
        data_ = {
                "account": "18800000064",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "bindStoreList": [{
                    "bindId": "80da7640-c3af-48aa-856b-c35606adf0dc",
                    "companyName": "小飞生产供货商吉林分公司"
                }],
                "state": 2,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","操作成功")

    def test_33_GetEnterChainStatV2(self):
        """获取子级门店"""
        url = 'https://patrol.iuoooo.com/api/Simple/GetEnterChainStatV2'
        data_ = {
                "pageIndex": 1,
                "pageSize": 20,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "clientInfo": {
                    "device": "android",
                    "version": "6.309.797",
                    "versionNum": "180",
                    "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
                }
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess",True)
        count = self.jsonpath('$..storeId')
        if len(count)<0:
            raise AssertionError

    def test_34_DelFirmChain(self):
        """删除子级门店"""
        chainId = self.jsonpath('$..chainId')
        url = 'https://patrol.iuoooo.com/api/Simple/DelFirmChain'
        data_ = {
                "chainId": chainId[0],
                "state": 1,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","操作成功")

    def test_35_AddEnterChainV2(self):
        """添加子级门店"""
        url = 'https://patrol.iuoooo.com/api/Simple/AddEnterChainV2'
        data_ = {
                "account": "18800000064",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "bindStoreList": [{
                    "bindId": "ff223c14-aacb-4a3d-be72-548000c617d6",
                    "companyName": "金玉食府"
                }],
                "state": 1,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","操作成功")

    def test_36_ModifyFirmChainV2(self):
        """更换父级门店"""
        url = 'https://patrol.iuoooo.com/api/Simple/ModifyFirmChainV2'
        data_ = {
                "account": "18800000064",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "bindId": "80da7640-c3af-48aa-856b-c35606adf0dc",
                "chainId": "4137aa19-9fc2-465f-a6d2-52420111d9fe",
                "companyName": "小飞生产供货商吉林分公司",
                "state": 2,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)

    def test_37_GetInStep(self):
        """宣传展示信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/GetInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "isOneLevel": 0,
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "moduleCode": "se_adver",
                "placeId": placeId,
                "readOnly": 0,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "clientInfo": {
                    "device": "android",
                    "version": "6.309.797",
                    "versionNum": "180",
                    "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
                }
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message','获取成功')

    def test_38_SubInStep(self):
        """保存展示信息"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/SubInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "cooperlayOutId": "1f54a3eb-5121-4003-931a-64d112f5266d",
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "modelList": [{
                    "modelCode": "se_adver_vr",
                    "modelValue": "https:\/\/baidu.com"
                }, {
                    "modelCode": "se_adver_homeimg",
                    "modelValue": "https:\/\/fileserver.iuoooo.com\/Jinher.JAP.BaseApp.FileServer.UI\/FileManage\/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661%2F2022042914%2F155e9c37-08a1-4036-bf55-a368ac4c255e_Img_c3f6606d-5f7e-46a2-8864-e366b2bad035.jpg"
                }, {
                    "modelCode": "se_adver_homelogo",
                    "modelValue": ""
                }, {
                    "modelCode": "se_adver_homeaddr",
                    "modelValue": ""
                }],
                "moduleCode": "se_adver",
                "moduleId": "d3de8e16-acaa-11ec-904e-02004c4f4f50",
                "placeId": placeId,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message','保存成功')

    def test_39_GetInStep(self):
        """特种设备类型"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/GetInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "isOneLevel": 0,
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "moduleCode": "se_spec",
                "placeId": placeId,
                "readOnly": 0,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "clientInfo": {
                    "device": "android",
                    "version": "6.309.797",
                    "versionNum": "180",
                    "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
                }
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message','获取成功')

    def test_40_SubInStep(self):
        """保存特种设备"""
        placeId = cache.get("placeId")
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/SubInStep'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "cooperlayOutId": "1f54a3eb-5121-4003-931a-64d112f5266d",
                "levelId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                "modelList": [{
                    "modelCode": "se_spec_spectype",
                    "modelValue": "[{\"check\":1,\"key\":\"dc7b7ec3-be19-43dc-b285-f517edeff37f\",\"value\":\"专用车辆\"}]"
                }],
                "moduleCode": "se_spec",
                "moduleId": "81b7a049-bbc6-11ec-a593-02004c4f4f50",
                "placeId": placeId,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "storeStatus": 1,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message','保存成功')