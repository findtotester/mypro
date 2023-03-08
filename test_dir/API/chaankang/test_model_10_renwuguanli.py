import seldom


class Testrenwuguanli(seldom.TestCase):

    def start(self):
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def test_01_TaskManage(self):
        url = 'https://dss.iuoooo.com/HMView/TaskManage?fixIOSUrl=1&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=a77a993e-a158-4cd6-bed8-cfbb8285e964&curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&orgId=ab9d121e-0145-41d8-b787-460480290d42&account=18800000064&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&relationOId=ab9d121e-0145-41d8-b787-460480290d42&jhWebView=1&needLogin=1&hidjhnavigation=1&isLogin=1&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98'
        self.get(url)
        self.assertStatusCode(200)

    def test_02_GetTaskManageList(self):
        url = 'http://dss.iuoooo.com/taskengine/GetTaskManageList'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "pageIndex": 1,
                "pageSize": 20,
                "CategoryIds": ""
            }
        self.post(url, data=data_, headers=self.headers)

    def test_03_GetAreaInfoListByParentCode(self):
        url = 'http://dss.iuoooo.com/CockpitMobile/GetAreaInfoListByParentCode'
        data_ = {
                "orgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_04_GetOperateByUser(self):
        url = 'http://dss.iuoooo.com/CockpitMobile/GetOperateByUser'
        data_ = {
                "OrgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('data.Message', '获取成功')

    def test_05_GetLabelByUser(self):
        url = 'http://dss.iuoooo.com/CockpitMobile/GetLabelByUser'
        data_ = {
                "OrgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('data.Message', '获取成功')

    def test_06_TaskEngineCountSearch(self):
        url = 'http://dss.iuoooo.com/taskengine/TaskEngineCountSearch'
        data_ = {
                "AreaCode": "630000",
                "AreaLevel": "1",
                "LabelId": "",
                "LabelPId": "",
                "OperateTypeId": "",
                "ParentOperateTypeId": "df514ffe-6890-4f10-a1c4-e43900b61668,6feb4540-5e36-41d1-b14a-3512684aae35,683a901c-0c80-485f-b940-6fe9fb13a47b,1af90198-0f8d-48f8-bc9c-67580852685f,7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7,219cc73e-a522-46be-b457-01122d853771,a9e344ce-678e-43d4-9f0a-d712428fb010,7d6815f0-09cb-47a0-aa08-6be84d138a80,1008e75b-aa97-4f35-892a-ceb9dc0c61b3,9a84958b-f742-497f-950c-e78951aa2c65,9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb,548bf6c1-2001-43a1-9f00-d22a95238bd3,2d1afbaa-fa13-4407-93fd-64a32269529e,b003e1af-f259-445c-86a1-19817c8d4383,e687a7b1-fce8-4383-b4f5-5be46868d2ff,dd81fa26-0620-4899-8463-9ddcca135d3f,aac1bfb8-eac2-40b2-807d-612222966b71,0bf07a61-5204-4458-b3a3-9d133602313d,3264b42c-058e-4fe6-84d6-eed0846584f3,5c76e7b1-5da3-42a5-b449-a895a262ccaa,29d5f31d-2fb2-4765-bdde-6ec4f5325581,fdf02602-ec7f-4c48-8256-4a4eac585fe2,c81a3ccd-71f5-4e5e-9c51-11dab7f89145,5e43eb26-7a27-486a-893d-a09c408f3e30,36fc0bac-1830-42c5-a227-1fb14de96647,31b965c8-0f05-447d-b4ab-506091bd1121,52ad72a4-24e1-4817-94d0-e3ba58ceec61,39c618db-5954-4ca0-bd0e-9a44a3e907fb,ed8e25c8-5b9a-434b-aac6-c8c2a18f5021,"
            }
        self.post(url, data=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath('IsSuccess', True)

    def test_07_GetTaskEngineStoreAdmin(self):
        url = 'http://dss.iuoooo.com/taskengine/GetTaskEngineStoreAdmin'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "LabelId": "00000000-0000-0000-0000-000000000000",
                "operateType": "df514ffe-6890-4f10-a1c4-e43900b61668,6feb4540-5e36-41d1-b14a-3512684aae35,683a901c-0c80-485f-b940-6fe9fb13a47b,1af90198-0f8d-48f8-bc9c-67580852685f,7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7,219cc73e-a522-46be-b457-01122d853771,a9e344ce-678e-43d4-9f0a-d712428fb010,7d6815f0-09cb-47a0-aa08-6be84d138a80,1008e75b-aa97-4f35-892a-ceb9dc0c61b3,9a84958b-f742-497f-950c-e78951aa2c65,9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb,548bf6c1-2001-43a1-9f00-d22a95238bd3,2d1afbaa-fa13-4407-93fd-64a32269529e,b003e1af-f259-445c-86a1-19817c8d4383,e687a7b1-fce8-4383-b4f5-5be46868d2ff,dd81fa26-0620-4899-8463-9ddcca135d3f,aac1bfb8-eac2-40b2-807d-612222966b71,0bf07a61-5204-4458-b3a3-9d133602313d,3264b42c-058e-4fe6-84d6-eed0846584f3,5c76e7b1-5da3-42a5-b449-a895a262ccaa,29d5f31d-2fb2-4765-bdde-6ec4f5325581,fdf02602-ec7f-4c48-8256-4a4eac585fe2,c81a3ccd-71f5-4e5e-9c51-11dab7f89145,5e43eb26-7a27-486a-893d-a09c408f3e30,36fc0bac-1830-42c5-a227-1fb14de96647,31b965c8-0f05-447d-b4ab-506091bd1121,52ad72a4-24e1-4817-94d0-e3ba58ceec61,39c618db-5954-4ca0-bd0e-9a44a3e907fb,ed8e25c8-5b9a-434b-aac6-c8c2a18f5021,",
                "code": "1-310000"
            }
        self.post(url, data=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath('IsSuccess', True)

    def test_08_TaskEngineSearch(self):
        url = 'http://dss.iuoooo.com/taskengine/TaskEngineSearch'
        data_ = {
                "AreaCode": "630000",
                "AreaLevel": "1",
                "LabelId": "",
                "LabelPId": "",
                "OperateTypeId": "",
                "ParentOperateTypeId": "df514ffe-6890-4f10-a1c4-e43900b61668,6feb4540-5e36-41d1-b14a-3512684aae35,683a901c-0c80-485f-b940-6fe9fb13a47b,1af90198-0f8d-48f8-bc9c-67580852685f,7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7,219cc73e-a522-46be-b457-01122d853771,a9e344ce-678e-43d4-9f0a-d712428fb010,7d6815f0-09cb-47a0-aa08-6be84d138a80,1008e75b-aa97-4f35-892a-ceb9dc0c61b3,9a84958b-f742-497f-950c-e78951aa2c65,9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb,548bf6c1-2001-43a1-9f00-d22a95238bd3,2d1afbaa-fa13-4407-93fd-64a32269529e,b003e1af-f259-445c-86a1-19817c8d4383,e687a7b1-fce8-4383-b4f5-5be46868d2ff,dd81fa26-0620-4899-8463-9ddcca135d3f,aac1bfb8-eac2-40b2-807d-612222966b71,0bf07a61-5204-4458-b3a3-9d133602313d,3264b42c-058e-4fe6-84d6-eed0846584f3,5c76e7b1-5da3-42a5-b449-a895a262ccaa,29d5f31d-2fb2-4765-bdde-6ec4f5325581,fdf02602-ec7f-4c48-8256-4a4eac585fe2,c81a3ccd-71f5-4e5e-9c51-11dab7f89145,5e43eb26-7a27-486a-893d-a09c408f3e30,36fc0bac-1830-42c5-a227-1fb14de96647,31b965c8-0f05-447d-b4ab-506091bd1121,52ad72a4-24e1-4817-94d0-e3ba58ceec61,39c618db-5954-4ca0-bd0e-9a44a3e907fb,ed8e25c8-5b9a-434b-aac6-c8c2a18f5021,",
                "FinishedStatus": "",
                "StoreName": "",
                "MaxFinishedRate": 100,
                "MinFinishedRate": 0,
                "Sort": [{
                    "Key": "FinishedNum",
                    "Value": "desc"
                }],
                "PageIndex": 1,
                "PageSize": 20
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('IsSuccess', True)


    #  未完待续 后期固定青海区域，使用固定的门店