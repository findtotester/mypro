import seldom
from seldom.testdata import *
from seldom.utils import cache
from  seldom import depend,if_depend


class Testzhinengbaojingnew(seldom.TestCase):
    def start(self):
        self.appid = "9be42759-9686-4541-b5a4-2be15a5c7d73"
        self.orgid = "7035c461-c80e-49ce-a7c8-5584f0453646"
        self.userid = "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
        self.storeid = "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
        self.StoreOrgId = "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
        self.code = "630000"
        self.attrCode = "headwear"
        self.attrTxt = "未戴工作帽"
        self.month = get_month().replace(f'{get_year()}-', '')
        self.year = get_year()
        self.storename = "白兔咖啡"

    """AI运营并审核"""
    def test_01_GetStoreByCompanySearch(self):
        url = 'https://aix-ui.iuoooo.com/api/Basic/GetStoreByCompanySearch'
        data_ = {
            "systemPrivateId": "00000000-0000-0000-0000-000000000000",
            "CompanyName": self.storename,
            "ProvinceCode": "",
            "CityCode": "",
            "DistrictCode": "",
            "LocationId": "00000000-0000-0000-0000-000000000000",
            "CommunityId": "00000000-0000-0000-0000-000000000000"
        }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    def test_02_GetAiPhotoSearch(self):
        id = self.jsonpath('$..StoreId')
        if id is False:
            id  = self.storeid
        url = 'https://aix-ui.iuoooo.com/api/AiAttrRelat/GetAiPhotoSearch'
        data_ = {
                "ProvinceCode": "",
                "CityCode": "",
                "DistrictCode": "",
                "LocationId": "00000000-0000-0000-0000-000000000000",
                "CommunityId": "00000000-0000-0000-0000-000000000000",
                "StoreIds": id,
                "IsRule": "",
                "AuditState": 0,
                "StartTime": f"{get_custom_data('d')} 00:00:00",
                "EndTime": "",
                "AuditUserName": "",
                "PageNo": 1,
                "PageSize": 20,
                "ProjectId": "00000000-0000-0000-0000-000000000000",
                "OrderId": "00000000-0000-0000-0000-000000000000",
                "SN": "",
                "jhmac": "",
                "RuleId": "00000000-0000-0000-0000-000000000000"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "查询成功")

    def test_03_EditAuditInfoV2(self):
        id  = self.jmespath("Content[0].Id")
        img = self.jmespath("Content[0].ImgUrl")
        ChannelNo = self.jmespath("Content[0].ChannelNo")
        Jhmac = self.jmespath("Content[0].Jhmac")
        SubTime = self.jmespath("Content[0].SubTime")
        OperationTypeId = self.jmespath("Content[0].OperationTypeId")
        if id is None or id is False:
            id = "219969fd-c74b-41fd-b300-06844ceff559"
            img = "https://video10.iuoooo.com/pic-video10/openlive/1b57e2f9_1/1677110822792.jpg"
            ChannelNo = "1"
            Jhmac = "1b57e2f9"
            SubTime = "2023-02-23 08:07:04"
            OperationTypeId = "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc"
        cache.set({"day": SubTime})
        url = 'https://aix-ui.iuoooo.com/api/AiAttrRelat/EditAuditInfoV2'
        data_ = {
                "Id": id,
                "State": 1,
                "StoreId": self.storeid,
                "AuditState": "1",
                "AuditUserId": self.userid,
                "AuditUserName": "",
                "OrgId": "d2d8e6ac-b838-4d4b-b177-147b38eeec6b",
                "ResultList": [{
                    "StoreId": self.storeid,
                    "ImgUrl": img,
                    "State": 1,
                    "InitHeight": 360,
                    "InitWidth": 640,
                    "SubTime": SubTime,
                    "PicRectList": [{
                        "AttrCode": self.attrCode,
                        "AttrTxt": self.attrTxt,
                        "Height": 102,
                        "Width": 183,
                        "Left": 277,
                        "Top": 94
                    }]
                }],
                "OperationTypeId": OperationTypeId,
                "Jhmac": Jhmac,
                "ChannelNo": ChannelNo,
                "IsJhSet": False,
                "SystemPrivateId": "00000000-0000-0000-0000-000000000000"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '审核成功')

    """智能报警政府端"""
    def test_04_GetAiAppSetting(self):
        url = 'https://ripx.iuoooo.com/api/AiPC/GetAiAppSetting'
        data_ = {
                "PageSize": 0,
                "AppId": self.appid,
                "PageNo": 0,
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Content[0].AppId", self.appid)

    def test_05_videoAnalyze01_html(self):
        url = f'https://ripx-ui.iuoooo.com/ui/videoAnalyze01/videoAnalyze.html?userId={self.userid}&IsApp=1&orgId={self.orgid}&AppId={self.appid}&jhWebView=1&hideShare=1&IsApp=1&Code=undefined&Name=undefined&Level=undefined&StoreTypeId=undefined&StoreName=undefined'
        self.get(url)
        self.assertStatusCode(200)

    def test_06GetOperateInfo(self):
        url = 'https://ripx-ui.iuoooo.com/api/UserManage/v2/GetOperateInfo'
        data_ = {
                "ParentId": 0,
                "orgId": self.orgid,
                "userId": self.userid,
                "appId": self.appid
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            count = len(self.jsonpath('$..Id'))
            if count < 1:
                raise AssertionError
        except AssertionError as e:
            raise e

    def test_07_GetUserAreaNew(self):
        url = 'https://ripx-ui.iuoooo.com/api/Area/GetUserAreaNew'
        data_ = {
                "UserId": self.userid,
                "AppId": self.appid
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath("Message", "操作成功")
            count = len(self.jsonpath('$..Name'))
            if count < 1:
                raise AssertionError
        except AssertionError as e:
            raise e

    def test_08_GetEleStatists(self):
        day = cache.get("day")
        print(day)
        now_day = get_custom_data("d")
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetEleStatists'
        data_ = {
                "Level": "1",
                "AreaCode": self.code,
                "IsChain": 0,
                "EleDate": self.month,
                "EleYearDate": self.year,
                "OrgId": self.orgid,
                "UserId": self.userid,
                "AppId": self.appid,
                "StoreTypeIds": ["9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb", "ed8e25c8-5b9a-434b-aac6-c8c2a18f5021", "7d6815f0-09cb-47a0-aa08-6be84d138a80", "fdf02602-ec7f-4c48-8256-4a4eac585fe2", "2d1afbaa-fa13-4407-93fd-64a32269529e", "1008e75b-aa97-4f35-892a-ceb9dc0c61b3"]
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath('Message', '操作成功')
            if now_day == get_strftime(day,"%Y-%m-%d"):
                day = get_strftime(day, "%d")
                count = self.jsonpath(f'$..[?(@.EleDate=="{day}")].EleStoreNum')
                if count[0]<=0:
                    print("获取违规趋势图数据失败")
                    raise AssertionError
        except AssertionError as e:
            return e

    def test_09_GetAttrStatists(self):
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetAttrStatists'
        data_ = {
                "EleDate": self.month,
                "EleYearDate": self.year,
                "Level": "1",
                "Name": "青海省",
                "AreaCode": self.code,
                "OrgId": self.orgid,
                "UserId": self.userid,
                "AppId": self.appid,
                "IsChain": 0,
                "StoreTypeIds": ["9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb", "ed8e25c8-5b9a-434b-aac6-c8c2a18f5021", "7d6815f0-09cb-47a0-aa08-6be84d138a80", "fdf02602-ec7f-4c48-8256-4a4eac585fe2", "2d1afbaa-fa13-4407-93fd-64a32269529e", "1008e75b-aa97-4f35-892a-ceb9dc0c61b3"]
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath('Message', '操作成功')
            count = self.jsonpath(f'$..[?(@.AttrCode=="{self.attrCode}")].AttrNum')
            if count[0] <= 0:
                print("获取违规项数据失败")
                raise AssertionError
        except AssertionError as e:
            raise e

    def test_10_GetStoreEleDetail(self):
        day = cache.get("day")
        now_day = get_custom_data("d")
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetStoreEleDetail'
        data_ = {
                "requestDTO": {
                    "EleDate": self.month,
                    "EleYearDate": self.year,
                    "AttrCode": self.attrCode,
                    "PageNo": 1,
                    "PageSize": 10,
                    "Level": "1",
                    "AreaCode": self.code,
                    "OrgId": self.orgid,
                    "UserId": self.userid,
                    "AppId": self.appid,
                    "IsChain": 0,
                    "StoreTypeIds": ["9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb", "ed8e25c8-5b9a-434b-aac6-c8c2a18f5021",
                                     "7d6815f0-09cb-47a0-aa08-6be84d138a80", "fdf02602-ec7f-4c48-8256-4a4eac585fe2",
                                     "2d1afbaa-fa13-4407-93fd-64a32269529e", "1008e75b-aa97-4f35-892a-ceb9dc0c61b3"]
                }
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath('Message', '操作成功')
            if now_day == get_strftime(day,"%Y-%m-%d"):
                self.assertPath("Content[0].EleDate", "今天")
        except AssertionError as e:
            raise e

    def test_11_GetViolatList(self):
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
        self.post(url,json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_12_GetIndustryList(self):  # 业态分布
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetIndustryList'
        data_ = {
                "requestDTO": {
                    "EleDate": self.month,
                    "EleYearDate": self.year,
                    "Level": "1",
                    "AreaCode": self.code,
                    "OrgId": self.orgid,
                    "UserId": self.userid,
                    "AppId": self.appid,
                    "IsChain": 0,
                    "StoreTypeIds": ["9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb", "ed8e25c8-5b9a-434b-aac6-c8c2a18f5021", "7d6815f0-09cb-47a0-aa08-6be84d138a80", "fdf02602-ec7f-4c48-8256-4a4eac585fe2", "2d1afbaa-fa13-4407-93fd-64a32269529e", "1008e75b-aa97-4f35-892a-ceb9dc0c61b3"]
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    """查看门店"""
    def test_13_GetViolatCount(self):
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetViolatCount'
        data_ = {
                "IsChain": 0,
                "AreaCode": self.code,
                "Level": "1",
                "SearchName": "",
                "TimeType": 0,
                "PageIndex": 0,
                "PageSize": 200,
                "AppId": self.appid,
                "OrgId": self.orgid,
                "UserId": self.userid,
                "EleDate": self.month,
                "EleYearDate": self.year,
                "StoreTypeIds": ["9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb", "ed8e25c8-5b9a-434b-aac6-c8c2a18f5021", "7d6815f0-09cb-47a0-aa08-6be84d138a80", "fdf02602-ec7f-4c48-8256-4a4eac585fe2", "2d1afbaa-fa13-4407-93fd-64a32269529e", "1008e75b-aa97-4f35-892a-ceb9dc0c61b3"]
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_14_GetAttrs(self):
        url = 'https://ripx-ui.iuoooo.com/api/AppCustomization/GetAttrs'
        self.post(url)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_15_GetViolatList(self):
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetViolatList'
        data_ = {
                "requestDTO": {
                    "Type": "1",
                    "AreaCode": self.code,
                    "AttrCode": "",
                    "Level": "1",
                    "SearchName": "",
                    "TimeType": 0,
                    "PageIndex": 1,
                    "PageSize": 200,
                    "AppId": self.appid,
                    "OrgId": self.orgid,
                    "UserId": self.userid,
                    "IsChain": 0,
                    "EleDate": self.month,
                    "EleYearDate": self.year,
                    "StoreTypeIds": ["9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb", "ed8e25c8-5b9a-434b-aac6-c8c2a18f5021", "7d6815f0-09cb-47a0-aa08-6be84d138a80", "fdf02602-ec7f-4c48-8256-4a4eac585fe2", "2d1afbaa-fa13-4407-93fd-64a32269529e", "1008e75b-aa97-4f35-892a-ceb9dc0c61b3"]
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")
        id_temp = self.jmespath("Content.rankList[0].StoreId")
        cache.set({"id_temp": id_temp})

    def test_16_Details_html(self):
        id = cache.get("id_temp")
        if id is None:
            id = self.storeid
            cache.set({"id_temp": id})
        url = f'https://ripx-ui.iuoooo.com/ui/videoAnalyze01/Details.html?StoreId={id}&IsChain=0&orgId={self.orgid}&userId={self.userid}&AppId={self.appid}&Type=0&Level=1&AreaCode={self.code}&Code{self.code}&hidjhnavigation=1&storeName=%25E7%2599%25BD%25E5%2585%2594%25E5%2592%2596%25E5%2595%25A1%25E6%259C%2589%25E9%2599%2590%25E8%25B4%25A3%25E4%25BB%25BB%25E5%2585%25AC%25E5%258F%25B8'
        self.get(url)
        self.assertStatusCode(200)

    def test_17_GetAttrStatistsLately(self):
        id = cache.get("id_temp")
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetAttrStatistsLately'
        data_ = {
            "StoreId": id,
            "TimeType": 0,
            "appId": self.appid
        }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","操作成功")

    def test_18_GetStoreEleDetail(self):
        id = cache.get("id_temp")
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetStoreEleDetail'
        data_ = {
                "AttrCode": self.attrCode,
                "Level": 0,
                "StoreId": id,
                "appId": self.appid,
                "Type": 1,
                "PageNo": 1,
                "PageSize": 10
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","操作成功")

    def test_19_GetAttrRateList(self):
        id = cache.get("id_temp")
        url = 'https://ripx-ui.iuoooo.com/api/EleTrend/GetAttrRateList'
        data_ = {"StoreId":id}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message","操作成功")
        cache.clear("id_temp")
        cache.clear("day")

    """AI整改-待整改"""
    def test_20_SearchCountByBusinessType(self):
        url = 'https://ripx.iuoooo.com/api/TaskRectification/SearchCountByBusinessType'
        data_ ={
                "state": 0,
                "businessType": "2",
                "search": {
                    "UserId": self.userid,
                    "Expiration": "0",
                    "ParentCode": "",
                    "StoreTypeId": "",
                    "StoreSecTypeId": "",
                    "StoreId": "",
                    "appeal": False,
                    "EndDate": "",
                    "Level": "",
                    "AppId": self.appid,
                    "BeginDate": ""
                }
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath("Message", "操作成功")
            count = self.jmespath("Content[0].Count")
            if count < 1:
                raise AssertionError
        except AssertionError as e:
            raise e

    def test_21_Search(self):
        url = 'https://ripx.iuoooo.com/api/TaskRectification/Search'
        data_ ={
                "state": 1,
                "search": {
                    "BeginDate": "",
                    "StoreSecTypeId": "",
                    "StoreId": "",
                    "BusinessType": "2",
                    "ParentCode": "",
                    "appId": "9be42759-9686-4541-b5a4-2be15a5c7d73",
                    "StoreTypeId": "",
                    "appeal": False,
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                    "EndDate": "",
                    "PageIndex": 1,
                    "Expiration": "0",
                    "Level": "",
                    "PageSize": 20,
                    "IsAboutUser": False
                }
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath("Message", "操作成功")
            count = len(self.jsonpath('$..TaskDetailId'))
            if count < 1:
                raise AssertionError
        except AssertionError as e:
            raise e

    """千人千面进行表单整改"""
    def test_22_GetAllWorkList(self):  # 查安康上做任务
        self.sleep(3)
        url = 'https://layouts-task.iuoooo.com/api/Work/GetAllWorkList'
        data_ = {
                "AppId": self.appid,
                "OrgId": self.orgid,
                "QueryDate": get_date(),
                "RoleName": "管理员",
                "RoleTypeClient": 2,
                "StoreId": self.storeid,
                "StoreOrgId": self.StoreOrgId,
                "UserId": self.userid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        TaskId_form = self.jsonpath('$..[?(@.Name=="未戴工作帽-未戴工作帽3" && @.WorkStatus == 0)].SourceId')
        TaskType_form = self.jsonpath('$..[?(@.Name=="未戴工作帽-未戴工作帽3" && @.WorkStatus == 0)].TaskType')
        BusinessId_form = self.jsonpath('$..[?(@.Name=="未戴工作帽-未戴工作帽3" && @.WorkStatus == 0)].BusinessId')
        WorkId_form = self.jsonpath('$..[?(@.Name=="未戴工作帽-未戴工作帽3" && @.WorkStatus == 0)].WorkId')
        BusinessId_daiban = self.jsonpath('$..[?(@.Name=="未戴工作帽-未戴帽子" && @.WorkStatus == 0)].BusinessId')
        print(BusinessId_daiban)
        if TaskId_form is False:
            Testzhinengbaojingnew.test_22_GetAllWorkList = False
        else:
            cache.set({"TaskId_form": TaskId_form})
            cache.set({"TaskType_form": TaskType_form})
            cache.set({"BusinessId_form": BusinessId_form})
            cache.set({"WorkId_form": WorkId_form})

    @if_depend("test_22_GetAllWorkList")
    def test_23_findBusinessData(self):
        BusinessId_form = cache.get("BusinessId_form")
        url = 'https://jianguan.iuoooo.com/jc6/api/JForm/findBusinessData?userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=&account=18800000064///&storeId=a5bac1d7-0c0c-4328-8af1-2df7955a0e74&storeAppId=&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&parentAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&parentOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&roleName=%E7%AE%A1%E7%90%86%E5%91%98'
        data_ = {"formId": BusinessId_form[0]}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        design_id = self.jsonpath('$..designId')
        designHtml = ''.join(self.jsonpath('$.designHtml'))
        data_id = ''.join(re.findall('"data":{"(.*?)"', designHtml))
        cache.set({"design_id": design_id})
        cache.set({"data_id": data_id})

    @depend("test_23_findBusinessDat")
    def test_24_saveBusiness2point0(self):  # 表单整改提交
        TaskId_form = cache.get("TaskId_form")
        data_id = cache.get("data_id")
        design_id = cache.get("design_id")
        BusinessId_form = cache.get("BusinessId_form")
        result_business_id = get_uuid("-")
        cache.set({"result_business_id": result_business_id})
        url = 'https://jianguan.iuoooo.com/jc6/api/JForm/saveBusiness2point0?userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=&account=18800000064///&storeId=a5bac1d7-0c0c-4328-8af1-2df7955a0e74&storeAppId=&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&parentAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&parentOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&userName=%E4%B8%93%E6%A3%80&roleName=%E7%AE%A1%E7%90%86%E5%91%98'
        data_ = {
                "businessId": result_business_id,
                "designId": design_id[0],
                "formData": [{
                    data_id: {
                        "rectification": [],
                        "Rectification": [],
                        "CheckImgList": [],
                        "allOps": [{
                            "key": 0,
                            "name": "合格",
                            "selected": False,
                            "score": 0
                        }, {
                            "key": 1,
                            "name": "不合格",
                            "selected": False,
                            "score": 0
                        }],
                        "curr": {
                            "key": "0",
                            "name": "合格",
                            "score": 0
                        },
                        "CheckRemarkVal": ""
                    }
                }],
                "uploadIds": [],
                "insertFlag": True,
                "storeId": self.storeid,
                "appId": self.appid,
                "userId": self.userid,
                "orgId": self.orgid,
                "formId": BusinessId_form[0],
                "taskId": TaskId_form[0],
                "storeOrgId": self.StoreOrgId,
                "userType": "B"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    @depend("test_24_saveBusiness2point0")
    def test_25_InspectWorkSubmit(self):   # 同步千人千面整改状态
        TaskId_form = cache.get("TaskId_form")
        BusinessId_form = cache.get("BusinessId_form")
        TaskType_form = cache.get("TaskType_form")
        WorkId_form = cache.get("WorkId_form")
        result_business_id = cache.get("result_business_id")
        url = "https://layouts-task.iuoooo.com/api/Work/InspectWorkSubmit"
        body = {
                "AppId": self.appid,
                "BusinessId": BusinessId_form[0],
                "OrgId": self.orgid,
                "ResultBusinessId": result_business_id,
                "RrtNumber": 1,
                "StoreId": self.storeid,
                "TaskId": TaskId_form[0],
                "TaskType": TaskType_form[0],
                "UserId": self.userid,
                "UserName": "API",
                "WorkId": WorkId_form[0],
            }
        self.post(url, json=body)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    @depend("test_25_InspectWorkSubmit")
    def test_26_saveBusiness2point0(self):  # 审核通过
        TaskId_form = cache.get("TaskId_form")
        data_id = cache.get("data_id")
        design_id = cache.get("design_id")
        BusinessId_form = cache.get("BusinessId_form")
        result_business_id = cache.get("result_business_id")
        print("调试数据：", design_id[0])
        url = 'https://jianguan.iuoooo.com/jc6/api/JForm/saveBusiness2point0?userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=&account=18800000064///&storeId=a5bac1d7-0c0c-4328-8af1-2df7955a0e74&storeAppId=&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&parentAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&parentOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&userName=%E4%B8%93%E6%A3%80&roleName=%E7%AE%A1%E7%90%86%E5%91%98'
        data_ = {
            "businessId": result_business_id,
            "designId": design_id[0],
            "formData": [{
                data_id: {
                    "rectification": [],
                    "Rectification": [],
                    "CheckImgList": [],
                    "allOps": [{
                        "key": 0,
                        "name": "合格",
                        "selected": False,
                        "score": 0
                    }, {
                        "key": 1,
                        "name": "不合格",
                        "selected": False,
                        "score": 0
                    }],
                    "curr": {
                        "key": "0",
                        "name": "合格",
                        "score": 0
                    },
                    "CheckRemarkVal": ""
                }
            }],
            "uploadIds": [],
            "insertFlag": False,
            "storeId": self.storeid,
            "appId": self.appid,
            "userId": self.userid,
            "orgId": self.orgid,
            "formId": BusinessId_form[0],
            "taskId": TaskId_form[0],
            "userType": "G",
            "businessFrom": "ReformAudit"
        }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        cache.clear("BusinessId_form")
        cache.clear("WorkId_form")
        cache.clear("TaskType_form")
        cache.clear("TaskId_form")
        cache.clear("design_id")
        cache.clear("data_id")
        cache.clear("result_business_id")


    """原生代办整改"""
    def test_27_GetAllWorkList(self):  # 查安康上做任务
        self.sleep(3)
        url = 'https://layouts-task.iuoooo.com/api/Work/GetAllWorkList'
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "OrgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "QueryDate": get_date(),
                "RoleName": "管理员",
                "RoleTypeClient": 2,
                "StoreId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "StoreOrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        BusinessId_daiban = self.jsonpath('$..[?(@.Name=="未戴工作帽-未戴帽子" && @.WorkStatus == 0)].BusinessId')
        AiImgUrl_daiban = self.jsonpath('$..[?(@.Name=="未戴工作帽-未戴帽子" && @.WorkStatus == 0)].AiImgUrl')
        taskId_daiban = self.jsonpath('$..[?(@.Name=="未戴工作帽-未戴帽子" && @.WorkStatus == 0)].SourceId')
        WorkId_daiban = self.jsonpath('$..[?(@.Name=="未戴工作帽-未戴帽子" && @.WorkStatus == 0)].WorkId')
        if BusinessId_daiban is False:
            Testzhinengbaojingnew.test_27_GetAllWorkList = False
            print("调试信息：", cache.get("BusinessId_daiban"))
        else:
            cache.set({"BusinessId_daiban": BusinessId_daiban})
            cache.set({"AiImgUrl_daiban": AiImgUrl_daiban})
            cache.set({"taskId_daiban": taskId_daiban})
            cache.set({"WorkId_daiban": WorkId_daiban})

    @if_depend("test_27_GetAllWorkList")
    def test_28_getFieldInfo2(self):
        BusinessId_daiban = cache.get("BusinessId_daiban")
        uir = 'https://jianguan.iuoooo.com/jc6/api/Layout/getFieldInfo2'
        data_ = {"formId": BusinessId_daiban[0]}
        self.post(uir, json=data_)
        self.assertStatusCode(200)
        self.assertPath("message", "success")
        id_temp = self.jmespath("data[0].id")
        cache.set({"id_temp": id_temp})

    @depend("test_28_getFieldInfo2")
    def test_29_OperateSubmitFormInfo(self):  # 提交整改
        id_temp = cache.get("id_temp")
        BusinessId_daiban = cache.get("BusinessId_daiban")
        AiImgUrl_daiban = cache.get("AiImgUrl_daiban")
        taskId_daiban = cache.get("taskId_daiban")
        WorkId_daiban = cache.get("WorkId_daiban")
        url = 'https://layouts-task.iuoooo.com/api/FormOperate/OperateSubmitFormInfo'
        data_ = {
                "ExecutorName": "API",
                "RrtNumber": 1,
                "appId": self.appid,
                "formData": [{
                    id_temp: {
                        "CheckImgList": [{
                            "isImage": True,
                            "isVideo": False,
                            "name": "整改图片",
                            "url": "http://fileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d\/2023022316\/7841e5c026a34accb56cd9fa728a562c_2e39a4765669_1677111420848.jpg"
                        }],
                        "Rectification": [{
                            "isImage": True,
                            "isVideo": False,
                            "name": "整改图片",
                            "url": "http://fileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d\/2023022316\/7841e5c026a34accb56cd9fa728a562c_2e39a4765669_1677111420848.jpg"
                        }, {
                            "isImage": True,
                            "isVideo": False,
                            "lat": 40.055223,
                            "lng": 116.30305,
                            "name": "任务图片",
                            "url": AiImgUrl_daiban[0]
                        }],
                        "allOps": [{
                            "key": "0",
                            "name": "合格",
                            "selected": False
                        }, {
                            "key": "1",
                            "name": "不合格",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择",
                            "selected": False
                        },
                        "rectification": [{
                            "isImage": True,
                            "isVideo": False,
                            "lat": 40.055223,
                            "lng": 116.30305,
                            "name": "任务图片",
                            "url": AiImgUrl_daiban[0]
                        }]
                    }
                }],
                "formId": BusinessId_daiban[0],
                "insertFlag": True,
                "orgId": self.orgid,
                "storeId": self.storeid,
                "taskId": taskId_daiban[0],
                "uploadIds": [],
                "userId": self.userid,
                "userType": "B",
                "workId": WorkId_daiban[0]
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        result_business_id = self.response['Data']
        cache.set({"result_business_id": result_business_id})

    @depend("test_29_OperateSubmitFormInfo")
    def test_30_findBusinessData(self):
        BusinessId_daiban = cache.get("BusinessId_daiban")
        result_business_id = cache.get("result_business_id")
        url = 'https://jianguan.iuoooo.com/jc6/api/JForm/findBusinessData?userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=&account=18800000064///&storeId=a5bac1d7-0c0c-4328-8af1-2df7955a0e74&storeAppId=&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&parentAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&parentOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&roleName=%E7%AE%A1%E7%90%86%E5%91%98'
        data_ = {"businessId":result_business_id,"formId":BusinessId_daiban[0]}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        design_id = self.jsonpath('$..designId')
        cache.set({"design_id": design_id})

    @depend("test_30_findBusinessData")
    def test_31_saveBusiness2point0(self):  # 审核通过
        taskId_daiban = cache.get("TaskId_form")
        result_business_id = cache.get("result_business_id")
        design_id = cache.get("design_id")
        BusinessId_daiban = cache.get("BusinessId_daiban")
        AiImgUrl_daiban = cache.get("AiImgUrl_daiban")
        id_temp = cache.get("id_temp")
        url = 'https://jianguan.iuoooo.com/jc6/api/JForm/saveBusiness2point0?userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=&account=18800000064///&storeId=a5bac1d7-0c0c-4328-8af1-2df7955a0e74&storeAppId=&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&parentAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&parentOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&userName=%E4%B8%93%E6%A3%80&roleName=%E7%AE%A1%E7%90%86%E5%91%98'
        data_ = {
                "businessId": result_business_id,
                "designId": design_id[0],
                "formData": [{
                    id_temp: {
                        "rectification": [{
                            "isImage": True,
                            "isVideo": False,
                            "lat": 40.055223,
                            "lng": 116.30305,
                            "name": "任务图片",
                            "url": AiImgUrl_daiban[0],
                            "_url": AiImgUrl_daiban[0]
                        }],
                        "Rectification": [{
                            "isImage": True,
                            "isVideo": False,
                            "name": "整改图片",
                            "url": "http://fileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d/2023022316/7841e5c026a34accb56cd9fa728a562c_2e39a4765669_1677111420848.jpg"
                        }, {
                            "isImage": True,
                            "isVideo": False,
                            "lat": 40.055223,
                            "lng": 116.30305,
                            "name": "任务图片",
                            "url": AiImgUrl_daiban[0]
                        }],
                        "CheckImgList": [{
                            "isImage": True,
                            "isVideo": False,
                            "name": "整改图片",
                            "url": "http://fileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d/2023022316/7841e5c026a34accb56cd9fa728a562c_2e39a4765669_1677111420848.jpg"
                        }],
                        "allOps": [{
                            "key": 0,
                            "name": "合格",
                            "selected": False,
                            "score": 0
                        }, {
                            "key": 1,
                            "name": "不合格",
                            "selected": False,
                            "score": 0
                        }],
                        "curr": {
                            "key": "",
                            "name": "合格",
                            "score": 0
                        },
                        "CheckRemarkVal": ""
                    }
                }],
                "uploadIds": [],
                "insertFlag": False,
                "storeId": self.storeid,
                "appId": self.appid,
                "userId": self.userid,
                "orgId": self.orgid,
                "formId": BusinessId_daiban[0],
                "taskId": taskId_daiban[0],
                "userType": "G",
                "businessFrom": "ReformAudit"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        cache.clear("taskId_daiban")
        cache.clear("id_temp")
        cache.clear("design_id")
        cache.clear("BusinessId_daiban")
        cache.clear("AiImgUrl_daiban")
        cache.clear("result_business_id")
        cache.clear("WorkId_daiban")
