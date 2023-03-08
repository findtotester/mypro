import seldom
from seldom.testdata import *


class Testjiashicang(seldom.TestCase):
    def start(self):
        self.tomorrow = get_date(1, "/")  # get_date 默认当天的日期

    # 驾驶舱首页
    def test_01_MobileMapIndex(self):
        url = "http://dss.iuoooo.com/CockpitMobile/MobileMapIndex?needLogin=1&curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&shopOrgId=&isLogin=1&hidjhnavigation=1&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42"
        self.get(url)
        self.assertStatusCode(200)

    def test_02_InitReportAppId(self):
        url = "http://dss.iuoooo.com/CockpitMobile/InitReportAppId"
        data_ = {"Appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_03_ReportAppId(self):
        url = "http://dss.iuoooo.com/CockpitMobile/ReportAppId"
        data_ = {"ReportId": "",
                 "operateType": 3,
                 "Appids": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                 "AuthType": 1
                 }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    # 指数分布
    def test_04_FoodSafePro_html(self):
        url = "https://dss.iuoooo.com/Html/FoodSafePro/FoodSafePro.html?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&shopOrgId=&isLogin=1&hidjhnavigation=1&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42"
        self.get(url)
        self.assertStatusCode(200)

    def test_05_GetOverAllInfo(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetOverAllInfo"
        data_ = {"userid": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                 "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                 "cityCode": "all"
                 }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("RM.Code", 200)
        self.assertPath("RM.Data.ltOverAllType[0].countType", "监管主体总数")

    def test_06_GetMapDataInfo(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetMapDataInfo"
        data_ = {"userid": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                 "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                 "curChangeOrg":"ab9d121e-0145-41d8-b787-460480290d42",
                 "cityCode": "all"
                 }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("RM.Code", 200)


    def test_07_GetPermitIndexInfos(self):  # 风险监管
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetPermitIndexInfos"
        data_ = {"userid": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                 "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                 "orgid": "ab9d121e-0145-41d8-b787-460480290d42"
                 }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("Data[0].IndexName", "安康指数")

    def test_08_GetRiskWarningArea(self):  # 风险监管
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetRiskWarningArea"
        data_ = {
                 "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
                 }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_09_GetEmergencyMapData(self):  # 风险监管
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetEmergencyMapData"
        data_ = {
                "Type": "all",
                "userid": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "code": "2-110100",
                "Row": "70",
                "LocationId": "",
                "IndexCode": "4",
                "riskLevel": "0,1,2,3,4",
                "StoreName": "",
                "LeftDown_Longitude": "",
                "LeftDown_Latitude": "",
                "RightUp_Longitude": "",
                "RightUp_Latitude": ""
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_10_OperateFoodSafetyArea(self):  # 风险监管
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/OperateFoodSafetyArea"
        data_ = {
                "Type": "all",
                "userid": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "code": "2-110100",
                "LocationId": "",
                "IndexCode": 4
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_11_GetEmergencyRiskLevel(self):  # 风险监管
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetEmergencyRiskLevel"
        data_ = {
                "Type": "all",
                "userid": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "code": "2-110100",
                "LocationId": "",
                "IndexCode": 4
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    # 设备在线
    def test_12_EquipmentOnlineNew_html(self):
        url = "https://dss.iuoooo.com/html/DriveCabinNew/EquipmentOnlineNew/EquipmentOnlineNew.html?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&shopOrgId=&isLogin=1&hidjhnavigation=1&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42"
        self.get(url)
        self.assertStatusCode(200)

    def test_13_GetResetDate(self):
        url = "https://dss.iuoooo.com/SunshineCater/GetResetDate"
        self.post(url)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_14_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinSelectArea"
        data_ = {"AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_15_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinSelectArea"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "0-000000"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_16_GetStatisticsFormat(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetStatisticsFormat"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "operateId": ""
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess", True)

    def test_17_CabinEquipmentStatus(self):
        url = "https://dss.iuoooo.com/CockpitPc/CabinEquipmentStatus"
        data_ = {
                "Code": "0-000000",
                "OperateType": "00000000-0000-0000-0000-000000000000",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_18_CabinEquipmentStatus(self):  # 在线设备详情
        url = "https://dss.iuoooo.com/CockpitPc/CabinEquipmentDetail"
        data_ = {
                "OperateType": "00000000-0000-0000-0000-000000000000",
                "SearchName": None,
                "Code": "0-000000",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "Page": 1,
                "Rows": 30,
                "IsEquip": "1"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_19_DragonTigerList_html(self):   # 龙虎榜
        url = "https://dss.iuoooo.com/html/DriveCabinNew/DragonTigerList/DragonTigerList.html?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&shopOrgId=&isLogin=1&hidjhnavigation=1&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42"
        self.get(url)
        self.assertStatusCode(200)

    def test_20_GetResetDate(self):
        url = "https://dss.iuoooo.com/SunshineCater/GetResetDate"
        self.post(url)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_21_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinSelectArea"
        data_ = {"AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_22_GetStatisticsFormat(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetStatisticsFormat"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "operateId": ""
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess", True)

    def test_23_GetCooperAreas(self):
        url = "https://dss.iuoooo.com/SunshineCater/GetCooperAreas"
        self.post(url)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 0)

    def test_24_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinSelectArea"
        data_ = {"AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","UserId":"3c73f483-0a2f-4838-b04b-58a2eb64ebd0","Code":"0-000000"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_25_CabinStoreRanks(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinStoreRanks"
        data_ = {
                "Code": "0-000000",
                "opeType": "00000000-0000-0000-0000-000000000000",
                "ModuleIds": "00000000-0000-0000-0000-000000000000",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "StartTime": "2012/01/01",
                "endTime": self.tomorrow
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)
    #
    def test_26_GetDrillStoreSubCount(self):
        url = "https://dss.iuoooo.com/cockpitmobile/GetDrillStoreSubCount"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "areaCodes": ["0-000000"],
                "areaLevel": "0",
                "operateTypeIds": [],
                "operateTypeLevel": 1,
                "newLabelIds": [],
                "businessStatuses": [0, 5],
                "groupBy": "area",
                "sort": "desc",
                "beginSubTime": "2012/01/01",
                "endSubTime": self.tomorrow
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess", True)

    # 入住数据分析
    def test_27_SettlementAnalyseNew_html(self):
        url = "https://dss.iuoooo.com/html/DriveCabinNew/SettlementAnalyseNew/SettlementAnalyseNew.html?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&shopOrgId=&isLogin=1&hidjhnavigation=1&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42#/"
        self.get(url)
        self.assertStatusCode(200)

    def test_28_GetAreaInfoListByParentCode(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetAreaInfoListByParentCode"
        data_ = {
                "orgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_29_GetOperateByUser(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetOperateByUser"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "OrgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "operateId": ""
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("data.Message","获取成功")

    def test_30_GetResetDate(self):
        url = "https://dss.iuoooo.com/SunshineCater/GetResetDate"
        self.post(url)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_31_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinSelectArea"
        data_ = {
                "Code": "1-310000",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_32_GetDrillStoreSubCount(self):
        url = "https://dss.iuoooo.com/cockpitmobile/GetDrillStoreSubCount"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "areaCodes": ["1-310000"],
                "areaLevel": "1",
                "operateTypeIds": ["df514ffe-6890-4f10-a1c4-e43900b61668", "6feb4540-5e36-41d1-b14a-3512684aae35", "683a901c-0c80-485f-b940-6fe9fb13a47b", "1af90198-0f8d-48f8-bc9c-67580852685f", "7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7", "219cc73e-a522-46be-b457-01122d853771", "a9e344ce-678e-43d4-9f0a-d712428fb010", "7d6815f0-09cb-47a0-aa08-6be84d138a80", "1008e75b-aa97-4f35-892a-ceb9dc0c61b3", "9a84958b-f742-497f-950c-e78951aa2c65", "9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb", "548bf6c1-2001-43a1-9f00-d22a95238bd3", "2d1afbaa-fa13-4407-93fd-64a32269529e", "b003e1af-f259-445c-86a1-19817c8d4383", "e687a7b1-fce8-4383-b4f5-5be46868d2ff", "dd81fa26-0620-4899-8463-9ddcca135d3f", "aac1bfb8-eac2-40b2-807d-612222966b71", "0bf07a61-5204-4458-b3a3-9d133602313d", "3264b42c-058e-4fe6-84d6-eed0846584f3", "5c76e7b1-5da3-42a5-b449-a895a262ccaa", "29d5f31d-2fb2-4765-bdde-6ec4f5325581", "fdf02602-ec7f-4c48-8256-4a4eac585fe2", "c81a3ccd-71f5-4e5e-9c51-11dab7f89145", "5e43eb26-7a27-486a-893d-a09c408f3e30", "36fc0bac-1830-42c5-a227-1fb14de96647", "31b965c8-0f05-447d-b4ab-506091bd1121", "52ad72a4-24e1-4817-94d0-e3ba58ceec61", "39c618db-5954-4ca0-bd0e-9a44a3e907fb", "ed8e25c8-5b9a-434b-aac6-c8c2a18f5021"],
                "operateTypeLevel": 1,
                "newLabelIds": [],
                "businessStatuses": [0, 5],
                "groupBy": "area",
                "sort": "desc",
                "beginSubTime": "",
                "endSubTime": ""
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess", True)

    def test_33_GetPanel(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetPanel"
        data_ = {
                "Code": "1-310000",
                "selectShowType": 2,
                "selectLicence": 0,
                "fromTime": "2012/01/01",
                "endTime": "2023/02/17",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "TypeStr": "df514ffe-6890-4f10-a1c4-e43900b61668,6feb4540-5e36-41d1-b14a-3512684aae35,683a901c-0c80-485f-b940-6fe9fb13a47b,1af90198-0f8d-48f8-bc9c-67580852685f,7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7,219cc73e-a522-46be-b457-01122d853771,a9e344ce-678e-43d4-9f0a-d712428fb010,7d6815f0-09cb-47a0-aa08-6be84d138a80,1008e75b-aa97-4f35-892a-ceb9dc0c61b3,9a84958b-f742-497f-950c-e78951aa2c65,9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb,548bf6c1-2001-43a1-9f00-d22a95238bd3,2d1afbaa-fa13-4407-93fd-64a32269529e,b003e1af-f259-445c-86a1-19817c8d4383,e687a7b1-fce8-4383-b4f5-5be46868d2ff,dd81fa26-0620-4899-8463-9ddcca135d3f,aac1bfb8-eac2-40b2-807d-612222966b71,0bf07a61-5204-4458-b3a3-9d133602313d,3264b42c-058e-4fe6-84d6-eed0846584f3,5c76e7b1-5da3-42a5-b449-a895a262ccaa,29d5f31d-2fb2-4765-bdde-6ec4f5325581,fdf02602-ec7f-4c48-8256-4a4eac585fe2,c81a3ccd-71f5-4e5e-9c51-11dab7f89145,5e43eb26-7a27-486a-893d-a09c408f3e30,36fc0bac-1830-42c5-a227-1fb14de96647,31b965c8-0f05-447d-b4ab-506091bd1121,52ad72a4-24e1-4817-94d0-e3ba58ceec61,39c618db-5954-4ca0-bd0e-9a44a3e907fb,ed8e25c8-5b9a-434b-aac6-c8c2a18f5021"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("CockPc.Code", 200)

    #主体浏览情况
    def test_33_StoreLiveVideoViewNew_html(self):
        url = "https://dss.iuoooo.com/html/DriveCabinNew/StoreLiveVideoViewNew/StoreLiveVideoViewNew.html?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&shopOrgId=&isLogin=1&hidjhnavigation=1&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42#/"
        self.get(url)
        self.assertStatusCode(200)

    def test_34_GetResetDate(self):
        url = "https://dss.iuoooo.com/SunshineCater/GetResetDate"
        self.post(url)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_35_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinSelectArea"
        data_ = {"AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_36_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinSelectArea"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "0-000000"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_37_GetStatisticsFormat(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetStatisticsFormat"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "operateId": ""
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsSuccess", True)

    def test_38_CabinLookTimes(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinLookTimes"
        data_ = {
                "Code": "0-000000",
                "OperateType": "00000000-0000-0000-0000-000000000000",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "OrderType": 0
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    # 经营类型分布
    def test_39_StoreOperateTypeNew_html(self):
        url = "https://dss.iuoooo.com/html/DriveCabinNew/StoreOperateTypeNew/StoreOperateTypeNew.html?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&storeOrgId=2658da82-d18b-4b07-bf8e-9f4b81511746&shopOrgId=ab9d121e-0145-41d8-b787-460480290d42&isLogin=1&hidjhnavigation=1&shopAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42#/"
        self.get(url)
        self.assertStatusCode(200)

    def test_40_GetResetDate(self):
        url = "https://dss.iuoooo.com/SunshineCater/GetResetDate"
        self.post(url)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_41_GetAreaInfoListByParentCode(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetAreaInfoListByParentCode"
        data_ = {
                "orgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_42_GetOperateByUser(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetOperateByUser"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "OrgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "operateId": ""
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("data.Message","获取成功")

    def test_43_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinSelectArea"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "1-310000"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_44_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinStoreOperate"
        data_ = {
                "Code": "1-310000",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "TypeStr": "df514ffe-6890-4f10-a1c4-e43900b61668,6feb4540-5e36-41d1-b14a-3512684aae35,683a901c-0c80-485f-b940-6fe9fb13a47b,1af90198-0f8d-48f8-bc9c-67580852685f,7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7,219cc73e-a522-46be-b457-01122d853771,a9e344ce-678e-43d4-9f0a-d712428fb010,7d6815f0-09cb-47a0-aa08-6be84d138a80,1008e75b-aa97-4f35-892a-ceb9dc0c61b3,9a84958b-f742-497f-950c-e78951aa2c65,9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb,548bf6c1-2001-43a1-9f00-d22a95238bd3,2d1afbaa-fa13-4407-93fd-64a32269529e,b003e1af-f259-445c-86a1-19817c8d4383,e687a7b1-fce8-4383-b4f5-5be46868d2ff,dd81fa26-0620-4899-8463-9ddcca135d3f,aac1bfb8-eac2-40b2-807d-612222966b71,0bf07a61-5204-4458-b3a3-9d133602313d,3264b42c-058e-4fe6-84d6-eed0846584f3,5c76e7b1-5da3-42a5-b449-a895a262ccaa,29d5f31d-2fb2-4765-bdde-6ec4f5325581,fdf02602-ec7f-4c48-8256-4a4eac585fe2,c81a3ccd-71f5-4e5e-9c51-11dab7f89145,5e43eb26-7a27-486a-893d-a09c408f3e30,36fc0bac-1830-42c5-a227-1fb14de96647,31b965c8-0f05-447d-b4ab-506091bd1121,52ad72a4-24e1-4817-94d0-e3ba58ceec61,39c618db-5954-4ca0-bd0e-9a44a3e907fb,ed8e25c8-5b9a-434b-aac6-c8c2a18f5021"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_45_CabinStoreOperateDetail(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinStoreOperateDetail"
        data_ = {
                "OperateType": "c120779d-cb4f-4d89-ae1a-6dd346cb5c34",
                "SearchName": None,
                "Code": "1-310000",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "Page": 1,
                "Rows": 30
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    # 指数排行榜
    def test_46_rankList_htm(self):
        url = "https://dss.iuoooo.com/Html/map/rankList/rankList.html?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&storeOrgId=2658da82-d18b-4b07-bf8e-9f4b81511746&shopOrgId=ab9d121e-0145-41d8-b787-460480290d42&isLogin=1&hidjhnavigation=1&shopAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42#/"
        self.get(url)
        self.assertStatusCode(200)

    def test_47_GetPermitIndexInfos(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetPermitIndexInfos"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("Data[0].IndexName", "安康指数")

    def test_48_InitTagInfo(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/InitTagInfo"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_49_OperateTagInfo(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/OperateTagInfo"
        data_ = {
                "operateJsonTest": "",
                "operateType": 1,
                "Appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_50_RankDistrict(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitPc/RankDistrict"
        data_ = {
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "",
                "appIds": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "EBCOrganizationId": "",
                "IndexCode": 4,
                "Page": 1,
                "Type": "all"
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_51_FoodSafetyIndexLocation(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitPc/FoodSafetyIndexLocation"
        data_ = {
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "EBCOrganizationId": "",
                "IndexCode": 4,
                "Page": 1,
                "Type": "all"
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_52_GetFoodSafetyIndexRankCommunity(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetFoodSafetyIndexRankCommunity"
        data_ = {
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "EBCOrganizationId": "",
                "IndexCode": 4,
                "Page": 1,
                "Type": "all"
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_53_GetBusinessCircleScore(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetBusinessCircleScore"
        data_ = {
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "EBCOrganizationId": "",
                "IndexCode": 4,
                "Page": 1,
                "Type": "all"
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_54_GetFoodSafetyIndex(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = "https://dss.iuoooo.com/CockpitMobile/GetFoodSafetyIndex"
        data_ = {
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "all",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "EBCOrganizationId": "",
                "IndexCode": 4,
                "Page": 1,
                "Type": "all",
                "IsExport": 0,
                "OrderCode": "desc",
                "Rows": 20
            }
        self.post(url, data=data_, headers=headers)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    # 监管业务分析
    def test_55_BusinessAnalyzeNew_htm(self):
        url = "https://dss.iuoooo.com/html/DriveCabinNew/BusinessAnalyzeNew/BusinessAnalyzeNew.html?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&storeOrgId=2658da82-d18b-4b07-bf8e-9f4b81511746&shopOrgId=ab9d121e-0145-41d8-b787-460480290d42&isLogin=1&hidjhnavigation=1&shopAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42#/"
        self.get(url)
        self.assertStatusCode(200)

    def test_56_GetAreaInfoListByParentCode(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetAreaInfoListByParentCode"
        data_ = {
                "orgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_57_GetOperateByUser(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetOperateByUser"
        data_ = {
                "orgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("data.Message", "获取成功")

    def test_58_CabinSelectArea(self):
        url = "https://dss.iuoooo.com/CockpitMobile/CabinSelectArea"
        data_ = {
                "Code": "1-310000",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_59_GetTotalInfo(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetTotalInfo"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "1-310000",
                "OrganizationId": "ab9d121e-0145-41d8-b787-460480290d42",
                "type": "df514ffe-6890-4f10-a1c4-e43900b61668,6feb4540-5e36-41d1-b14a-3512684aae35,683a901c-0c80-485f-b940-6fe9fb13a47b,1af90198-0f8d-48f8-bc9c-67580852685f,7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7,219cc73e-a522-46be-b457-01122d853771,a9e344ce-678e-43d4-9f0a-d712428fb010,7d6815f0-09cb-47a0-aa08-6be84d138a80,1008e75b-aa97-4f35-892a-ceb9dc0c61b3,9a84958b-f742-497f-950c-e78951aa2c65,9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb,548bf6c1-2001-43a1-9f00-d22a95238bd3,2d1afbaa-fa13-4407-93fd-64a32269529e,b003e1af-f259-445c-86a1-19817c8d4383,e687a7b1-fce8-4383-b4f5-5be46868d2ff,dd81fa26-0620-4899-8463-9ddcca135d3f,aac1bfb8-eac2-40b2-807d-612222966b71,0bf07a61-5204-4458-b3a3-9d133602313d,3264b42c-058e-4fe6-84d6-eed0846584f3,5c76e7b1-5da3-42a5-b449-a895a262ccaa,29d5f31d-2fb2-4765-bdde-6ec4f5325581,fdf02602-ec7f-4c48-8256-4a4eac585fe2,c81a3ccd-71f5-4e5e-9c51-11dab7f89145,5e43eb26-7a27-486a-893d-a09c408f3e30,36fc0bac-1830-42c5-a227-1fb14de96647,31b965c8-0f05-447d-b4ab-506091bd1121,52ad72a4-24e1-4817-94d0-e3ba58ceec61,39c618db-5954-4ca0-bd0e-9a44a3e907fb,ed8e25c8-5b9a-434b-aac6-c8c2a18f5021"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    def test_60_GetBarChartInfo(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetBarChartInfo"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "Code": "1-310000",
                "OrganizationId": "ab9d121e-0145-41d8-b787-460480290d42",
                "type": "df514ffe-6890-4f10-a1c4-e43900b61668,6feb4540-5e36-41d1-b14a-3512684aae35,683a901c-0c80-485f-b940-6fe9fb13a47b,1af90198-0f8d-48f8-bc9c-67580852685f,7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7,219cc73e-a522-46be-b457-01122d853771,a9e344ce-678e-43d4-9f0a-d712428fb010,7d6815f0-09cb-47a0-aa08-6be84d138a80,1008e75b-aa97-4f35-892a-ceb9dc0c61b3,9a84958b-f742-497f-950c-e78951aa2c65,9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb,548bf6c1-2001-43a1-9f00-d22a95238bd3,2d1afbaa-fa13-4407-93fd-64a32269529e,b003e1af-f259-445c-86a1-19817c8d4383,e687a7b1-fce8-4383-b4f5-5be46868d2ff,dd81fa26-0620-4899-8463-9ddcca135d3f,aac1bfb8-eac2-40b2-807d-612222966b71,0bf07a61-5204-4458-b3a3-9d133602313d,3264b42c-058e-4fe6-84d6-eed0846584f3,5c76e7b1-5da3-42a5-b449-a895a262ccaa,29d5f31d-2fb2-4765-bdde-6ec4f5325581,fdf02602-ec7f-4c48-8256-4a4eac585fe2,c81a3ccd-71f5-4e5e-9c51-11dab7f89145,5e43eb26-7a27-486a-893d-a09c408f3e30,36fc0bac-1830-42c5-a227-1fb14de96647,31b965c8-0f05-447d-b4ab-506091bd1121,52ad72a4-24e1-4817-94d0-e3ba58ceec61,39c618db-5954-4ca0-bd0e-9a44a3e907fb,ed8e25c8-5b9a-434b-aac6-c8c2a18f5021"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("SCater.Code", 200)

    # 区域自查统计
    def test_61_(self):
        url = "https://dss.iuoooo.com/Html/regionCheckStatistic/#/?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&storeOrgId=2658da82-d18b-4b07-bf8e-9f4b81511746&shopOrgId=ab9d121e-0145-41d8-b787-460480290d42&isLogin=1&hidjhnavigation=1&shopAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42"
        self.get(url)
        self.assertStatusCode(200)


    def test_62_GetAreaInfoListByParentCode(self):
        url = "https://dss.iuoooo.com/CockpitMobile/GetAreaInfoListByParentCode"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "orgId": "ab9d121e-0145-41d8-b787-460480290d42"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_63_getsp_data(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "Code": "0-000000",
                "AreaLevel": "0",
                "SpName": "sp_TaskEngine_ReportAdmin"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

