import seldom
from seldom.testdata import *
from seldom.utils import cache
from seldom import depend, if_depend
import uuid


class Testzaixianxunjian(seldom.TestCase):
    def start(self):
        self.appid = "9be42759-9686-4541-b5a4-2be15a5c7d73"
        self.orgid = "7035c461-c80e-49ce-a7c8-5584f0453646"
        self.userid = "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
        self.storeid = "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"


    def test_01_GetUserAreaNew(self):
        url = 'https://ripx.iuoooo.com/api/Area/GetUserAreaNew'
        data_ = {
                "AppId": self.appid,
                "UserId": self.userid
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath('Message', '操作成功')
            Name = self.jsonpath('$..Name')
            if '青海省' not in Name:
                print("获取网格权限失败")
                raise AssertionError
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    def test_02_GetOperateInfo(self):
        url = 'https://ripx.iuoooo.com/api/UserManage/v2/GetOperateInfo'
        data_ = {
                "appId": self.appid,
                "clientType": "1",
                "isShowDisabled": "0",
                "orgId": self.orgid,
                "type": "0",
                "userId": self.userid
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath('Message', '操作成功')
            Name = self.jsonpath('$..Name')
            if '中型餐饮' not in Name:
                print("获取网格权限失败")
                raise AssertionError
        except ArithmeticError as e:
            print('执行结果:Failed')
            raise e

    def test_04_GetAreaByLevel(self):
        url = 'https://ripx.iuoooo.com/api/Area/GetAreaByLevel'
        data_ = {
                "Code": "1-630000",
                "Level": "1"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_05_GetStoreBaseInfoList(self):
        url = 'https://ripx.iuoooo.com/api/Store/GetStoreBaseInfoList'
        data_ = {
            "AppId": self.appid,
            "IsGrid": "1",
            "Name": "白兔咖啡",
            "OrgId": self.orgid,
            "PageIndex": 1,
            "PageSize": 50,
            "UserId": self.userid
        }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    def test_06_GetStoreEquAuditByArea(self):
        url = 'https://patrol.iuoooo.com/api/StoreEquipmentManage/GetStoreEquAuditByArea'
        data_ = {
                "AppId": self.appid,
                "AreaCode": "1-630000",
                "Level": "1",
                "OrgId": self.orgid,
                "PageIndex": 1,
                "PageSize": 10,
                "StoreId": self.storeid,
                "UserId": self.userid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '获取成功')

    def test_07_GetAllStoreCheckAuditPicList(self):
        url = 'https://ripx.iuoooo.com/api/AuditPic/GetAllStoreCheckAuditPicList'
        data_ = {
                "AppId": self.appid,
                "AreaCode": "1-630000",
                "Level": "1",
                "OrgId": self.orgid,
                "PageIndex": 1,
                "PageSize": 10,
                "StoreId": self.storeid,
                "UserId": self.userid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '获取成功')

    def test_08_IsInblacklist(self):
        url = 'https://ripx.iuoooo.com/api/AuditPic/IsInblacklist'
        data_ = {
                "UserId": self.userid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '获取成功')

    def test_09_GetAuditPicIntegralSetInfo(self):
        url = 'https://ripx.iuoooo.com/api/AuditPic/GetAuditPicIntegralSetInfo'
        data_ = {
                "AppId": self.appid,
                "AttrType": "1",
                "OrgId": self.orgid,
                "UserId": self.userid
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath('Message', '获取成功')
            Name = self.jsonpath('$..AttrName')
            if '证照过期' not in Name:
                print("获取图片违规项错误")
                raise AssertionError
        except ArithmeticError as e:
            print('执行结果:Failed')
            raise e

    def test_10_SingleSubmit(self):
        url = 'https://ripx.iuoooo.com/api/ReformAuditPic/SingleSubmit'
        data_ = {
                "AppId": self.appid,
                "AuditOptionList": [{
                    "AttrCode": "expired",
                    "AttrTxt": "证照过期",
                    "Height": 41,
                    "InitHeight": 720,
                    "InitWidth": 720,
                    "Left": 393,
                    "Text": "",
                    "Top": 307,
                    "Width": 41,
                    "imageRealHeight": 720,
                    "imageRealWidth": 720,
                    "leftMark": False,
                    "mark": 0,
                    "markHeight": 90,
                    "markWidth": 327
                }],
                "AuditResult": "2",
                "Id": "f8102de5-802c-4427-8a84-c415e86dda8a",
                "InitHeight": "870",
                "InitWidth": "870",
                "Integral": "0",
                "PicturePath": "https:\/\/upfileserver.iuoooo.com\/Jinher.JAP.BaseApp.FileServer.UI\/FileManage\/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d%2F2022092209%2F5ea7efce809d46b2a92726016f64860c_342-4a41-a179-577a78c7e8ad.jpg",
                "StoreId": self.storeid,
                "SubmitType": "2",
                "TextList": [],
                "UserId": self.userid,
                "picType": "3",
                "showTitle": "营业执照"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', '提交成功！')

    def test_11_GetAllWorkList(self):  # 查安康上做任务
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
        TaskId = self.jsonpath('$..[?(@.Name=="证照过期-证照过期" && @.WorkStatus == 0)].SourceId')
        TaskType = self.jsonpath('$..[?(@.Name=="证照过期-证照过期" && @.WorkStatus == 0)].TaskType')
        BusinessId = self.jsonpath('$..[?(@.Name=="证照过期-证照过期" && @.WorkStatus == 0)].BusinessId')
        WorkId = self.jsonpath('$..[?(@.Name=="证照过期-证照过期" && @.WorkStatus == 0)].WorkId')
        if TaskId is None or TaskId is False:
            Testzaixianxunjian.test_11_GetAllWorkList = False
        else:
            cache.set({"TaskId": TaskId})
            cache.set({"TaskType": TaskType})
            cache.set({"BusinessId": BusinessId})
            cache.set({"WorkId": WorkId})

    @if_depend("test_11_GetAllWorkList")
    def test_12_form_html(self):
        TaskId = cache.get("TaskId")
        BusinessId = cache.get("BusinessId")
        WorkId = cache.get("WorkId")
        url = f'https://jianguan.iuoooo.com/jc6/OAPlus/view/JForm/form.html?TaskId={TaskId}&jhWebView=1&hideShare=1&orgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&isLogin=1&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&checkFormid=&relationOId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&formId={BusinessId}&StoreName=&submitTag=1&curChangeOrg=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&changeOrg=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&WorkId={WorkId}&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&storeId=a5bac1d7-0c0c-4328-8af1-2df7955a0e74&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&shopOrgId=ab9d121e-0145-41d8-b787-460480290d42&shopAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&isX5=1&UserId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&checkBusinessid=&roleName=%E7%AE%A1%E7%90%86%E5%91%98&userType=B&account=18800000064'
        self.get(url)
        self.assertStatusCode(200)

    @depend("test_12_form_html")
    def test_13_findBusinessData(self):
        url = 'https://jianguan.iuoooo.com/jc6/api/JForm/findBusinessData?userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&currentOrgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&mainType=&account=18800000064///&storeId=a5bac1d7-0c0c-4328-8af1-2df7955a0e74&storeAppId=&storeOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&parentAppId=2fd5f092-d360-4783-b95c-6d47ee5cac44&parentOrgId=6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b&roleName=%E7%AE%A1%E7%90%86%E5%91%98'
        data_ = {"formId": "2c9889c9822049b0018244513e8b606a"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        design_id = self.jsonpath('$..designId')
        designHtml = ''.join(self.jsonpath('$.designHtml'))
        data_id = ''.join(self.re_findall('"data":{"(.*?)"', designHtml))
        # data_id = ''.join(re.findall('"data":{"(.*?)"', designHtml))
        cache.set({"design_id": design_id})
        cache.set({"data_id": data_id})

    @depend("test_13_findBusinessData")
    def test_14_saveBusiness2point0(self):  # 表单整改提交
        TaskId = cache.get("TaskId")
        data_id = cache.get("data_id")
        design_id = cache.get("design_id")
        BusinessId = cache.get("BusinessId")
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
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "orgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "formId": BusinessId[0],
                "taskId": TaskId[0],
                "storeOrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "userType": "B"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    @depend("test_14_saveBusiness2point0")
    def test_15_InspectWorkSubmit(self):   # 同步千人千面整改状态
        TaskId = cache.get("TaskId")
        BusinessId = cache.get("BusinessId")
        TaskType = cache.get("TaskType")
        WorkId = cache.get("WorkId")
        result_business_id = cache.get("result_business_id")
        url = "https://layouts-task.iuoooo.com/api/Work/InspectWorkSubmit"
        body = {
                "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "BusinessId": BusinessId[0],
                "OrgId": "ab9d121e-0145-41d8-b787-460480290d42",
                "ResultBusinessId": result_business_id,
                "RrtNumber": 1,
                "StoreId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "TaskId": TaskId[0],
                "TaskType": TaskType[0],
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "UserName": "API",
                "WorkId": WorkId[0],
            }
        self.post(url, json=body)
        self.assertStatusCode(200)
        self.assertPath('Message', '操作成功')

    """整改审核"""
    @depend("test_15_InspectWorkSubmit")
    def test_16_Search_daishenhe(self):    # 整改待审核页面
            result_business_id = cache.get("result_business_id")
            url = "https://ripx.iuoooo.com/api/TaskRectification/Search"
            body = {
                "state": 1,
                "search": {
                    "BeginDate": "",
                    "StoreSecTypeId": "",
                    "StoreId": "",
                    "BusinessType": "",
                    "ParentCode": "",
                    "appId": self.appid,
                    "StoreTypeId": "",
                    "appeal": False,
                    "userId": self.userid,
                    "EndDate": "",
                    "PageIndex": 1,
                    "Expiration": "0",
                    "Level": "",
                    "PageSize": 20,
                    "IsAboutUser": False
                }
            }
            self.post(url, json=body)
            self.assertStatusCode(200)
            self.assertPath('Message', '操作成功')
            self.assertPath('Content.Contents[0].BusinessId', result_business_id)

    @depend("test_16_Search_daishenhe")
    def test_17_saveBusiness2point0(self):  # 审核通过
        TaskId = cache.get("TaskId")
        data_id = cache.get("data_id")
        design_id = cache.get("design_id")
        BusinessId = cache.get("BusinessId")
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
                "formId": BusinessId[0],
                "taskId": TaskId[0],
                "userType": "G",
                "businessFrom": "ReformAudit"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        cache.clear("BusinessId")
        cache.clear("WorkId")
        cache.clear("TaskType")
        cache.clear("design_id")
        cache.clear("data_id")
        cache.clear("result_business_id")

    @depend("test_17_saveBusiness2point0")
    def test_18_GetByTaskDetailId(self):
        TaskId = cache.get("TaskId")
        url = 'https://ripx-ui.iuoooo.com/api/TaskRectification/GetByTaskDetailId'
        data_ = {
                    "taskDetailId": TaskId[0]
                }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Message', "操作成功")
        cache.clear("TaskId")

    """巡检记录"""
    def test_19_getsp_data(self):
        url = 'https://dss.iuoooo.com/CockpitMobile/getsp_data'
        data_ = {
                "AppId": self.appid,
                "Code": "1-630000",
                "SpName": "sp_guangzhou_online_inspect_home_page",
                "Type": "df514ffe-6890-4f10-a1c4-e43900b61668,6feb4540-5e36-41d1-b14a-3512684aae35,683a901c-0c80-485f-b940-6fe9fb13a47b,1af90198-0f8d-48f8-bc9c-67580852685f,7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7,219cc73e-a522-46be-b457-01122d853771,a9e344ce-678e-43d4-9f0a-d712428fb010,7d6815f0-09cb-47a0-aa08-6be84d138a80,1008e75b-aa97-4f35-892a-ceb9dc0c61b3,9a84958b-f742-497f-950c-e78951aa2c65,9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb,548bf6c1-2001-43a1-9f00-d22a95238bd3,2d1afbaa-fa13-4407-93fd-64a32269529e,b003e1af-f259-445c-86a1-19817c8d4383,e687a7b1-fce8-4383-b4f5-5be46868d2ff,dd81fa26-0620-4899-8463-9ddcca135d3f,aac1bfb8-eac2-40b2-807d-612222966b71,0bf07a61-5204-4458-b3a3-9d133602313d,3264b42c-058e-4fe6-84d6-eed0846584f3,5c76e7b1-5da3-42a5-b449-a895a262ccaa,29d5f31d-2fb2-4765-bdde-6ec4f5325581,fdf02602-ec7f-4c48-8256-4a4eac585fe2,c81a3ccd-71f5-4e5e-9c51-11dab7f89145,5e43eb26-7a27-486a-893d-a09c408f3e30,36fc0bac-1830-42c5-a227-1fb14de96647,31b965c8-0f05-447d-b4ab-506091bd1121,52ad72a4-24e1-4817-94d0-e3ba58ceec61,39c618db-5954-4ca0-bd0e-9a44a3e907fb,ed8e25c8-5b9a-434b-aac6-c8c2a18f5021"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath('Success', True)

    def test_20_GetStoreOnlineAuditRecord(self):
        url = 'https://ripx-ui.iuoooo.com/api/ReformAuditPic/GetStoreOnlineAuditRecord'
        data_ = {
                "EndDate": get_custom_data("d"),
                "PageNo": 1,
                "PageSize": 20,
                "StartDate": get_custom_data("m",-1),
                "StoreId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_21_Getsp_guangzhou_online_inspect_export_out(self):
        url = 'https://dss.iuoooo.com/CockpitMobile/Getsp_guangzhou_online_inspect_export_out'
        data_ = {
                "AppId": self.appid,
                "Code": "1-630000",
                "Type": "9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb,ed8e25c8-5b9a-434b-aac6-c8c2a18f5021,7d6815f0-09cb-47a0-aa08-6be84d138a80,fdf02602-ec7f-4c48-8256-4a4eac585fe2,2d1afbaa-fa13-4407-93fd-64a32269529e,1008e75b-aa97-4f35-892a-ceb9dc0c61b3,",
                "storeName": "白兔咖啡"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        url = self.response["Url"]
        if url is None:
            print("获取数据异常")
            return False

