import seldom
from seldom.utils import cache
from seldom import depend


class TestComment(seldom.TestCase):

    def start(self):
        self.store_id = cache.get("store_id")
        self.store_name = cache.get("store_name")
        self.oper_id = cache.get("oper_id")

    # 获取九宫格中的内容
    def test_01_GetLayFunList(self):
        url = "https://patrol.iuoooo.com/api/ModuleLayOutDetail/GetLayFunList"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "storeId": self.store_id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    # 证照信息
    def test_02_qualificationCertificate(self):
        url = "http://wap.iuoooo.com/Areas/AStroeH5/views/qualificationCertificate.html?shopOrgId=ab9d121e-0145-41d8-b787-460480290d42&isLogin=1&isshowsharebenefitbtn=0&shopAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E7%AE%A1%E7%90%86%E5%91%98&storeId=ff223c14-aacb-4a3d-be72-548000c617d6&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&relationOId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
        self.get(url)
        self.assertStatusCode(200)

    def test_03_getStoreAttrDetail(self):
        url = "http://wap.iuoooo.com/AStore/Store/getStoreAttrDetail"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "storeId": self.store_id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("date.companyName", self.store_name)

    # 量化等级
    def test_04_safetyQualificationDetail(self):
        url = "http://wap.iuoooo.com/Areas/AStroeH5/views/safetyQualificationDetail.html?shopOrgId=ab9d121e-0145-41d8-b787-460480290d42&isLogin=1&isshowsharebenefitbtn=0&shopAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E7%AE%A1%E7%90%86%E5%91%98&storeId=ff223c14-aacb-4a3d-be72-548000c617d6&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&relationOId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
        self.get(url)
        self.assertStatusCode(200)

    def test_05_GetpublicityInfo(self):
        url = "http://wap.iuoooo.com/ARipx/Rips/GetpublicityInfo"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "storeId": self.store_id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取数据成功")

    def test_06_GetScoreLevel(self):
        url = "http://wap.iuoooo.com/ARipx/Rips/GetScoreLevel"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "storeId": self.store_id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "查询成功")

    def test_07_getStoreAttFoodList(self):
        url = "http://wap.iuoooo.com/AStore/Store/getStoreAttFoodList"
        data_ = {
                "type": 0,
                "storeId": self.store_id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("date.Name", "安全信息")

    # 承诺书
    def test_08_GetStoreMapAppId(self):
        url = "https://layouts.iuoooo.com/api/FormWork/GetStoreMapAppId"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "StoreId": self.store_id,
                "OperId": self.oper_id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_09_GetUndertakingList(self):
        url = "https://ripx.iuoooo.com/api/Undertaking/GetUndertakingList"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "StoreId": self.store_id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")
        self.assertPath("Data[0].UndertakingTitle", "食品安全承诺书")

    @depend("test_09_GetUndertakingList")
    def test_10_GetUndertakingById(self):
        id = self.response["Data"][0]["Id"]
        url = "https://ripx.iuoooo.com/api/Undertaking/GetUndertakingById"
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "StoreId": self.store_id,
                "Id": id
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")
        self.assertPath("Data.UndertakingTypeValue", "承诺书")

    # 每日晨检
    def test_11_form_html(self):
        url = "https://jianguan.iuoooo.com/jc6/OAPlus/view/JForm/form.html?hidjhnavigation=1&title=%E6%AF%8F%E6%97%A5%E6%99%A8%E6%A3%80&jhWebView=1&isX5=1&hideShare=1&formId=2c91c82f780215130178163648306f88&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&orgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&account=18800000064&relationOId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&formParams=%5B%5D&searchTag=1&isReadonly=1&storeId=ff223c14-aacb-4a3d-be72-548000c617d6&isLogin=1&shopAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&roleName=%E7%AE%A1%E7%90%86%E5%91%98&shopOrgId=ab9d121e-0145-41d8-b787-460480290d42"
        self.get(url)
        self.assertStatusCode(200)

    def test_12_version_json(self):
        url = "https://jianguan.iuoooo.com/jc6/OAPlus/scripts/JForm/js/version.json?v=1615361288478"
        self.get(url)
        self.assertStatusCode(200)

    def test_13_getWordExportState(self):
        url = "https://jianguan.iuoooo.com/jc6/JForm/j-form-word-template!getWordExportState.action?formId=2c91c82f721cec710172207cd4e2019d"
        self.get(url)
        self.assertStatusCode(200)

    def test_14_enable_get(self):
        url = "https://jianguan.iuoooo.com/jc6/api/advancedExcel/v1/enable/get?formId=2c91c82f721cec710172207cd4e2019d"
        self.get(url)
        self.assertStatusCode(200)

    def test_15_findBusinessData(self):
        url = "https://jianguan.iuoooo.com/jc6/api/JForm/findBusinessData?userId=580d9178-29f3-40c2-bbba-9c98e04eb7c8&sessionId=5c21c7ee-0186-42b0-bf48-f31e654b8315&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=null&account=18800000061&storeId=ff223c14-aacb-4a3d-be72-548000c617d6"
        data_ = {"formId": "2c91c82f721cec710172207cd4e2019d"}
        self.post(url, json=data_,)
        self.assertStatusCode(200)

    def test_16_excuteSqlByFormId(self):
        url = "https://jianguan.iuoooo.com/jc6/api/Statistical/excuteSqlByFormId?formId=2c91c82f721cec710172207cd4e2019d&storeId=ff223c14-aacb-4a3d-be72-548000c617d6&type=1&controlId=838af0dfcf684e9e81b96786e44fb6eb&datasourceId=2c91c82f721cec7101722034a69c005a&userId=580d9178-29f3-40c2-bbba-9c98e04eb7c8&sessionId=5c21c7ee-0186-42b0-bf48-f31e654b8315&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=null&account=18800000061&storeId=ff223c14-aacb-4a3d-be72-548000c617d6"
        data_ = {"filters": [], "searchValue": ""}
        self.post(url, json=data_,)
        self.assertStatusCode(200)

    def test_17_getStyle(self):
        url = "https://jianguan.iuoooo.com/jc6/api/JForm/getStyle?userId=580d9178-29f3-40c2-bbba-9c98e04eb7c8&sessionId=5c21c7ee-0186-42b0-bf48-f31e654b8315&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=null&account=18800000061&storeId=ff223c14-aacb-4a3d-be72-548000c617d6"
        data_ = {"formId":"2c91c82f721cec710172207cd4e2019d"}
        self.post(url, json=data_,)
        self.assertStatusCode(200)

    def test_18_getBusinessData(self):
        url = "https://jianguan.iuoooo.com/jc6/api/JForm/getBusinessData?userId=580d9178-29f3-40c2-bbba-9c98e04eb7c8&sessionId=5c21c7ee-0186-42b0-bf48-f31e654b8315&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=null&account=18800000061&storeId=ff223c14-aacb-4a3d-be72-548000c617d6"
        data_ = {
                "formId": "2c91c82f721cec710172207cd4e2019d",
                "pageNo": 1,
                "searchTag": "1",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "storeId": "ff223c14-aacb-4a3d-be72-548000c617d6",
                "leftJoinFlag": "0",
                "selectFields": "tbl_jh_form_business_D647f4rL.business_id,tbl_jh_form_business_D647f4rL.b3c6a85f7163433eae2cc7969f7fe9e4,`2c91c82f721cec71017220405fb60060`,`e7c943515bc24fcf937dbbd66fc474c1`,`5a62028bf40f46cb8e6d012412dffe41`,`30d3bde82afe4ad3b366ab2b352245cb`,`e088bc925f4845fcb335c9cdde91f59c`,`66b7b060b4654e56a0de77e47d25b41a`"
            }
        self.post(url, json=data_,)
        self.assertStatusCode(200)

    # 食安管理员
    def test_19_employList(self):
        url = "https://patrol.iuoooo.com/api/EmployeeFiles/employList"
        data_ = {
                "storeId": self.store_id,
                "showType": "1",
                "userAccount": "18800000064",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "orgId": "00000000-0000-0000-0000-000000000000"
            }
        self.post(url, json=data_,)
        self.assertStatusCode(200)

    # 自查公示
    def test_20_allTask(self):
        url = "https://tep-ui.iuoooo.com/uiMobile/#/allTask?isshowsharebenefitbtn=0&curChangeOrg=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&changeOrg=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&storeId=ff223c14-aacb-4a3d-be72-548000c617d6&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&hideShare=1&orgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&shopOrgId=ab9d121e-0145-41d8-b787-460480290d42&isLogin=1&hidjhnavigation=1&shopAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E7%AE%A1%E7%90%86%E5%91%98&relationOId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
        self.get(url)
        self.assertStatusCode(200)

    def test_21_StoreAllTask(self):
        url = "https://tep-ui.iuoooo.com/TaskDetail/StoreAllTask"
        data_ = {
                "ObjectId": self.store_id,
                "PageNo": 1,
                "PageSize": 20
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")
        task_id = self.response["Content"][0]["TaskId"]
        cache.set({"task_id": task_id})

    def test_22_StoreTaskSum(self):
        url = "https://tep-ui.iuoooo.com/TaskDetail/StoreTaskSum"
        data_ = {
                "ObjectId": self.store_id,
                "PageNo": 1,
                "PageSize": 20
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    @depend("test_21_StoreAllTask")
    def test_23_GetObjectTaskDetailExecutor(self):   # 查看任务
        task_id = cache.get("task_id")
        url = "https://tep-ui.iuoooo.com/TaskDetailExecutor/GetObjectTaskDetailExecutor"
        data_ = {
                "TaskId": task_id,
                "ObjectId": self.store_id,
                "IsReadOnly": 1,
                "StartTime": "",
                "EndTime": "",
                "PageNo": 1,
                "PageSize": 5
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Content.Id", task_id)
        cache.clear("task_id")
