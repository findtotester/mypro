import seldom
from seldom.utils import cache
from  seldom import data


class Testzhenggaiguanli(seldom.TestCase):

    def test_01_GetUserAreaNew(self):
        url = 'https://ripx.iuoooo.com/api/Area/GetUserAreaNew'
        data_ = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    @data([
        ("First case", 0),
        ("Second case", 1),
        ("Third case", 2),
    ])
    def test_02_SearchCount(self, name, state):
        url = 'https://ripx.iuoooo.com/api/TaskRectification/SearchCount'
        data_ = {
                "state": state,
                "search": {
                    "BeginDate": "",
                    "StoreSecTypeId": "",
                    "StoreId": "",
                    "BusinessType": "",
                    "ParentCode": "",
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "StoreTypeId": "",
                    "appeal": False,
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                    "EndDate": "",
                    "Expiration": "0",
                    "Level": "",
                    "IsAboutUser": False
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    @data([
        ("First case", 0),
        ("Second case", 1),
        ("Third case", 2),
    ])
    def test_03_Search(self, name, state):
        url = 'https://ripx.iuoooo.com/api/TaskRectification/Search'
        data_ = {
                "state": state,
                "search": {
                    "BeginDate": "",
                    "StoreSecTypeId": "",
                    "StoreId": "",
                    "BusinessType": "",
                    "ParentCode": "",
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
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
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')
        if state == 2:
            taskDetailId = self.response['Content']['Contents'][0]['TaskDetailId']
            StoreId = self.response['Content']['Contents'][0]['StoreId']
            cache.set({"taskDetailId": taskDetailId})
            cache.set({"StoreId": StoreId})

    def test_04_GetOperateInfo(self):
        url = 'https://ripx.iuoooo.com/api/UserManage/v2/GetOperateInfo'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "orgId": "ab9d121e-0145-41d8-b787-460480290d42"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_05_GetByTaskDetailId(self):
        taskDetailId = cache.get("taskDetailId")
        url = 'https://ripx-ui.iuoooo.com/api/TaskRectification/GetByTaskDetailId'
        data_ = {"taskDetailId": taskDetailId}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')
        businessId = self.response['Content']['BusinessId']
        formId = self.response['Content']['FormId']
        cache.set({"businessId": businessId})
        cache.set({"formId": formId})

    def test_06_form_html(self):
        StoreId = cache.get("StoreId")
        formId = cache.get("formId")
        businessId = cache.get("businessId")
        taskDetailId = cache.get("taskDetailId")
        url = f'https://jianguan.iuoooo.com/jc6/OAPlus/view/JForm/form.html?jhWebView=1&hidjhnavigation=1&isRectificationDetails=true&isX5=1&hideShare=1&storeId={StoreId}&StoreName=&formId={formId}&businessId={businessId}&isReadonly=true&checkFormid=00000000000000000000000000000000&checkBusinessid=00000000000000000000000000000000&taskId={taskDetailId}4&userType=G&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=a77a993e-a158-4cd6-bed8-cfbb8285e964&orgId==ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42&isLogin=1'
        self.get(url)

    def test_07_get_formId(self):
        formId = cache.get("formId")
        url = f'https://jianguan.iuoooo.com/jc6/api/advancedExcel/v1/enable/get?formId={formId}'
        self.get(url)
        self.assertStatusCode(200)
        self.assertPath('message', '成功')

    def test_08_findBusinessData(self):
        StoreId = cache.get("StoreId")
        formId = cache.get("formId")
        businessId = cache.get("businessId")
        url = f'https://jianguan.iuoooo.com/jc6/api/JForm/findBusinessData?userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=a77a993e-a158-4cd6-bed8-cfbb8285e964&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=&account=18800000064&storeId={StoreId}&storeAppId=&storeOrgId=&parentAppId=&parentOrgId='
        data_ = {
                "businessId": businessId,
                "formId": formId
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("code", "200")

    def test_09_GetAreaByLevel(self):
        url = 'https://ripx.iuoooo.com/api/Area/GetAreaByLevel'
        data_ = {
                "Level": "1",
                "Code": "1-110000"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_10_GetStoreStatisticalStateCount(self):
        url = "https://ripx.iuoooo.com/api/TaskRectification/GetStoreStatisticalStateCount"
        data_ = {
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "StoreId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_11_Search_baitu(self):
        url = "https://ripx.iuoooo.com/api/TaskRectification/Search"
        data = {
                "state": 0,
                "search": {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "PageSize": 20,
                    "StoreId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                    "BusinessType": "",
                    "PageIndex": 1
                }
            }
        self.post(url, json=data)
        self.assertStatusCode(200)

    def test_12_Notice(self):
        taskDetailId = self.response['Content']['Contents'][0]['TaskDetailId']
        url = "https://ripx.iuoooo.com/api/TaskRectification/Notice"
        data = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "taskDetailId": taskDetailId
            }
        self.post(url, json=data)
        self.assertStatusCode(200)
        self.assertPath('Message', "操作成功")

