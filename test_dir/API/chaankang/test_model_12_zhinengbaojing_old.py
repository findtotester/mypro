import seldom
from seldom.testdata import *
from seldom.utils import cache
from seldom import depend

class Testzhinengbaojingold(seldom.TestCase):
    def start(self):
        self.appid = "24830a2b-a6ae-462c-869d-b045ea2300ee"
        self.orgid = "bab76178-ca54-4692-8627-ce262a00597b"
        self.orgid = "bab76178-ca54-4692-8627-ce262a00597b"
        self.userid = "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
        self.code = "330500"
        self.attrCode = "hwoverflow"
        self.month = get_month().replace(f'{get_year()}-', '')
        self.year = get_year()

    """
    智能报警页面
    """
    def test_01_videoAnalyze_html(self):
        url = f'https://ripx-ui.iuoooo.com/ui/videoAnalyze/videoAnalyze.html?userId={self.userid}&AppId={self.appid}&orgId={self.orgid}&jhWebView=1&hideShare=1&IsApp=1&roleName=%E6%A3%80%E6%9F%A5%E7%AE%A1%E7%90%86%E5%91%98&shopOrgId='
        self.get(url)
        self.assertStatusCode(200)

    def test_02_(self):
        url = 'https://ripx-ui.iuoooo.com/api/Area/GetUserAreaNew'
        data_ = {"UserId":self.userid,"AppId":self.appid}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Content[0].Name', '湖州市')

    def test_03_GetEleStatists(self):
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetEleStatists'
        data_ = {
                "Level": "2",
                "AreaCode": self.code,
                "EleDate": self.month,
                "EleYearDate": self.year,
                "OrgId": self.orgid,
                "UserId": self.userid,
                "AppId": self.appid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_04_GetAttrStatists(self):
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetAttrStatists'
        data_ = {
                "EleDate": self.month,
                "EleYearDate": self.year,
                "Level": "2",
                "AreaCode": self.code,
                "OrgId": self.orgid,
                "UserId": self.userid,
                "AppId": self.appid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_05_GetStoreEleDetail(self):
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetStoreEleDetail'
        data_ = {
                "requestDTO": {
                    "EleDate": self.month,
                    "EleYearDate": self.year,
                    "AttrCode": self.attrCode,
                    "PageNo": 1,
                    "PageSize": 10,
                    "Level": "2",
                    "AreaCode": self.code,
                    "OrgId": self.orgid,
                    "UserId": self.userid,
                    "AppId": self.appid
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_06_GetViolatList(self):
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetViolatList'
        data_ = {
                "requestDTO": {
                    "EleDate": self.month,
                    "EleYearDate": self.year,
                    "Level": "2",
                    "AreaCode": self.code,
                    "OrgId": self.orgid,
                    "UserId": self.userid,
                    "AppId": self.appid,
                    "Type": "1"
                }
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            count = len(self.jsonpath('$..No'))
            day = get_date().replace(f'{self.year}-{self.month}-', '')
            if day not in ("01", "02"):
                if count < 0:
                    return AssertionError
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    def test_07_GetIndustryList(self):  # 业态分布
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetIndustryList'
        data_ = {
                "requestDTO": {
                    "EleDate": self.month,
                    "EleYearDate": self.year,
                    "Level": "2",
                    "AreaCode": self.code,
                    "OrgId": self.orgid,
                    "UserId": self.userid,
                    "AppId": self.appid
                }
            }
        self.post(url, json=data_)
        try:
                self.assertStatusCode(200)
                count = len(self.jsonpath('$..operId'))
                day = get_date().replace(f'{self.year}-{self.month}-', '')
                if day not in ("01", "02"):
                    if count < 0:
                       return AssertionError
        except AssertionError as e:
                print('执行结果:Failed')
                raise e

    """
    查看门店
    """
    def test_08_GetEleStoreList(self):  # 查看门店
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetEleStoreList'
        data_ = {"AreaCode":self.code,"Level":"2","SerchName":"","TimeType":0,"PageNo":1,"PageSize":10}
        self.post(url, json=data_)
        try:
                self.assertStatusCode(200)
                id_temp = self.jmespath("Content.StoreData[0].StoreId")
                cache.set({"id_temp": id_temp})
                count = len(self.jsonpath('$..StoreId'))
                if count < 0:
                    return AssertionError
        except AssertionError as e:
                print('执行结果:Failed')
                raise e

    @depend("test_08_GetEleStoreList")
    def test_09_GetAttrStatistsLately(self):
        id_temp = cache.get("id_temp")
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetAttrStatistsLately'
        data_ = {"StoreId":id_temp, "TimeType":0}
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            count = len(self.jsonpath('$..AttrCode'))
            if count < 0:
                return AssertionError
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    @depend("test_09_GetAttrStatistsLately")
    def test_10_GetStoreEleDetail(self):
        id_temp = cache.get("id_temp")
        AttrCode = self.jmespath("Content[0].AttrCode")
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetStoreEleDetail'
        data_ = {
                "AttrCode": AttrCode,
                "Level": 0,
                "StoreId": id_temp,
                "AppId": self.appid,
                "Type": 1,
                "PageNo": 1,
                "PageSize": 10
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            count = len(self.jsonpath('$..EleDate'))
            if count < 0:
                return AssertionError
        except AssertionError as e:
            print('执行结果:Failed')
            raise e
    @depend("test_10_GetStoreEleDetail")
    def test_11_GetEquEleImgInfo(self):
        EleDate = self.jmespath("Content[0].StoreDetail[0].EleDate")
        JhMac = self.jmespath("Content[0].StoreDetail[0].JhMac")
        AttrCode = self.jmespath("Content[0].StoreDetail[0].AttrCode")
        ChannelNo = self.jmespath("Content[0].StoreDetail[0].ChannelNo")
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetEquEleImgInfo'
        data_ = {
                "EleDate": EleDate,
                "JhMac": JhMac,
                "AttrCode": AttrCode,
                "ChannelNo": ChannelNo,
                "PageNo": 1,
                "PageSize": 500
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    @depend("test_08_GetEleStoreList")
    def test_12_GetAttrRateList(self):
        id_temp = cache.get("id_temp")
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetAttrRateList'
        data_ = {"StoreId": id_temp}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")
        cache.clear("id_temp")

    """
    AI记录
    """
    def test_13_GetAreaByLevel(self):
        url = 'https://ripx.iuoooo.com/api/Area/GetAreaByLevel'
        data_ = {
                "AppId": self.appid,
                "Code": f"2-{self.code}",
                "Level": "2"
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            count = len(self.jsonpath('$..Name'))
            if count < 0:
                raise AssertionError
        except AssertionError as e:
            raise e

    def test_14_GetElectronicRecord(self):
        url = 'https://ripx.iuoooo.com/api/Electronic/GetElectronicRecord'
        data_ = {
                "UserId":self.userid,
                "ByDays": 0,
                "IsBackStage": False,
                "PageIndex": 1,
                "IsAuthority": True,
                "PageSize": 10,
                "EleSource": 2,
                "AreaCode": [f"2-{self.code}"],
                "OrgId": self.orgid,
                "AppId": self.appid
                }
        self.post(url, json=data_)
        try:
                self.assertStatusCode(200)
                count = int(self.response["Detail"])
                if count < 0:
                    raise AssertionError
        except AssertionError as e:
                raise e

    @depend("test_14_GetElectronicRecord")
    def test_15_GetElectronicDetail(self):
        EleId = self.jmespath("Content[0].EleId")
        EleSource = self.jmespath("Content[0].EleSource")
        url = 'https://ripx.iuoooo.com/api/Electronic/GetElectronicDetail'
        data_ = {
                "EleId": EleId,
                "EleSource": EleSource
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    @depend("test_15_GetElectronicDetail")
    def test_16_GetReformDetail(self):
        Id = self.jmespath("Data.ResultId")
        url = 'https://ripx.iuoooo.com/api/Reform/GetReformDetail'
        data_ = {
                "UserId": self.userid,
                "AppId": self.appid,
                "OrgId": self.orgid,
                "Id": Id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    """
    整改管理
    """
    def test_17_GetReformNum(self):
        url = 'https://ripx.iuoooo.com/api/Reform/GetReformNum'
        data_ = {
                  "UserId": self.userid,
                  "JustMe": 0,
                  "HandleType": 2,
                  "Area": "",
                  "Street": "",
                  "ClientType": 2,
                  "Province": "",
                  "Community": "",
                  "OrgId": self.orgid,
                  "AppId": self.appid,
                  "City": f"2-{self.code}"
                }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            count = int(self.jmespath('Content.Reformed'))
            if count < 0:
                raise AssertionError
        except AssertionError as e:
            raise e

    def test_18_GetReformList(self):
        url = 'https://ripx.iuoooo.com/api/Reform/GetReformList'
        data_ = {
                "Province": "",
                "ClientType": 2,
                "Street": "",
                "Community": "",
                "UserId": self.userid,
                "HandleType": 2,
                "ReformStateList": [0],
                "PageIndex": 1,
                "AppId": self.appid,
                "Area": "",
                "PageSize": 20,
                "JustMe": 0,
                "OrgId": self.orgid,
                "City": f"2-{self.code}"
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            count = int(self.jmespath('Data'))
            if count < 1:
                raise AssertionError
        except AssertionError as e:
            raise e

    """整改闭环脚本未编写"""