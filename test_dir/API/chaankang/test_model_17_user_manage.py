import seldom
from  seldom import depend,if_depend


class TestUserManage(seldom.TestCase):
    """人员管理"""
    def start(self):
        self.headers = {"ApplicationContext": "eyJFbXBsb3llZUlkIjoiNjc1NGYwNWItOGQ3YS00ZTYxLWEwOGEtMTMxMjFjMWQ5MmU4IiwiTG9naW5DdXJyZW50Q3VsdHVyZSI6MCwiTG9naW5EZXBhcnRtZW50IjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwiTG9naW5PcmciOiJhYjlkMTIxZS0wMTQ1LTQxZDgtYjc4Ny00NjA0ODAyOTBkNDIiLCJMb2dpbk9yZ05hbWUiOiLmn6Xlronlurfnp5HmioDvvIjmt7HlnLPvvInogqHku73mnInpmZDlhazlj7giLCJMb2dpblRlbmFudElkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwiTG9naW5UaW1lIjoiL0RhdGUoMTY3ODQxMjYxMjE0MCswODAwKS8iLCJMb2dpblVzZXJDb2RlIjoiMTg4MDAwMDAwNjQiLCJMb2dpblVzZXJJRCI6IjNjNzNmNDgzLTBhMmYtNDgzOC1iMDRiLTU4YTJlYjY0ZWJkMCIsIkxvZ2luVXNlck5hbWUiOiLmtYvor5U0IiwiU2Vzc2lvbklEIjoiYTc3YTk5M2UtYTE1OC00Y2Q2LWJlZDgtY2ZiYjgyODVlOTY0In0="}

    def GetDepartmentAndEmployeeListV2(self):
        """获取部门信息"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.BP.DepartmentBP.svc/GetDepartmentAndEmployeeListV2'
        data_ = {
                    "departmentSearchDTO": {
                        "OrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                        "StoreId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
                    }
                }
        self.post(url,json=data_,headers=self.headers)
        self.assertStatusCode(200)
        count = self.jsonpath('$..DepId')
        if len(count)< 2:
            raise AssertionError

    def test_02_GetDeptInfo(self):
        """获取部门信息"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.BP.DepartmentBP.svc/GetDeptInfo'
        data_ = {"OrgId":"6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"}
        self.post(url,json=data_,headers=self.headers)
        self.assertStatusCode(200)
        name = self.jsonpath('$..DepName')
        self.assertEqual(name[0],"白兔咖啡")

    def test_03_IsAdminById(self):
        """获取管理员的身份"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.SV.OrganizationInfoSV.svc/IsAdminById'
        data_ = {"code":"Admin","orgId":"6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b","userId":"3c73f483-0a2f-4838-b04b-58a2eb64ebd0"}
        self.post(url,json=data_,headers=self.headers)
        self.assertStatusCode(200)
        self.assertEqual(self.response,True)

    def test_04_GetDepartmentAndEmployeeListV2(self):
        """获取部门下的人员"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.BP.DepartmentBP.svc/GetDepartmentAndEmployeeListV2'
        data_ = {"departmentSearchDTO":{"DeptId":"9dc4d023-7da0-466c-ac72-4e5f9c8c07f5","OrgId":"6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"}}
        self.post(url,json=data_,headers=self.headers)
        self.assertStatusCode(200)
        count = self.jsonpath('$..UserId')
        if len(count) < 0:
            raise AssertionError

    def test_05_GetHsDetectInfo(self):
        url = 'http://arcx.iuoooo.com/api/Heal/GetHsDetectInfo'
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "orgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "type": "1",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url,json=data_,headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_06_GetEmployeeCertificateList(self):
        """获取证件信息"""
        url = 'https://patrol.iuoooo.com/api/EmployeeFiles/GetEmployeeCertificateList'
        data_ = {
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功！")

    def test_07_employeeFilesDetails(self):
        """获取员工信息"""
        url = 'https://patrol.iuoooo.com/api/EmployeeFiles/employeeFilesDetails'
        data_ = {
                "orgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message","获取成功")

    def test_08_GetEmployeeInfoById(self):
        """获取员工信息"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.SV.OrganizationInfoSV.svc/GetEmployeeInfoById'
        data_ = {
                "EmployeeId": "a4471d33-2e8d-4aa9-bd86-2378769b527c"
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("DeptName", "白兔咖啡")

    def test_09_GetCustomAndAminRoleByOrgId(self):
        """获取角色信息"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.BP.RoleBP.svc/GetCustomAndAminRoleByOrgId'
        data_ = {
                "OrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "成功")

    def test_10_UpdateEmployeesInfoByMobile(self):
        """更新员工信息"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.BP.EmployeeBP.svc/UpdateEmployeesInfoByMobile'
        data_ = {
                "employeeDTO": {
                    "DepartmentId": "9dc4d023-7da0-466c-ac72-4e5f9c8c07f5",
                    "EmpRelationCode": "34532543",
                    "HeaderIcon": "https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661/2021112615/166a52c9-5570-47a5-ac9d-9386c7b72506_Img_19039f68-7e08-438d-a98c-9fce8062312f.jpg",
                    "Id": "a4471d33-2e8d-4aa9-bd86-2378769b527c",
                    "IsAdmin": False,
                    "IsEnable": True,
                    "IsLeaders": False,
                    "LoginAccount": "18800000064",
                    "Name": "专检",
                    "OrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                    "PositionId": "5de115ee-2042-4499-abc6-484492e50d9f",
                    "Role": "dfe1016b-6f51-4031-9f33-995d8d946d48,6ff01823-cfc8-4c25-ae1f-d329ce60bac2,a48d904a-5ac6-4964-b583-e203c8d7f50d",
                    "SubId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                    "isSelect": False
                }
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "修改成功！")

    def test_11_CreateOrUpdateHeal(self):
        """更新健康证信息"""
        url = 'http://arcx.iuoooo.com/api/Heal/CreateOrUpdateHeal'
        data_ = {
                "claimTel": "18800000064",
                "examDate": "2022.10.01",
                "examImg": "https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d%2F2023022107%2Ff4b410c4b40c4c78b99b82d4d85800f4_72b-4a16-b138-aad315ff146f.jpg",
                "examOrg": "海淀",
                "examValid": "2024.10.01",
                "healNum": "929737",
                "idyNum": "110",
                "isCanDownLoad": False,
                "isShowHealthCard": True,
                "sourceType": 2,
                "storeId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "whereFrom": 3
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "保存成功")

    def test_12_InsertHsDetectInfo(self):
        url = 'http://arcx.iuoooo.com/api/Heal/InsertHsDetectInfo'
        data_ = {
                "requestDto": {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "btime": "",
                    "detectId": "6c167419-7df7-487d-a943-328ccb71b3b7",
                    "etime": "",
                    "imgurl": "",
                    "orgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                    "type": "1",
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
                }
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "修改成功")

    def test_13_SubmitEmployeeCertificate(self):
        """保存员工信息"""
        url = 'https://patrol.iuoooo.com/api/EmployeeFiles/SubmitEmployeeCertificate'
        data_ = {
                "certificate": {
                    "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "CertExpire": "2022-10-11",
                    "CertificateCode": "018828272",
                    "CertificateType": "特种设备作业人员证",
                    "CertificateTypeId": "f61d0bbe-258a-40a7-8b71-a817efd54625",
                    "Id": "16115561-a480-4584-9e33-a7408239cc89",
                    "IssueDate": "2021-10-11",
                    "Picture": "https://fileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661/TempDirectory/d894dcba22894d8aa094c54e3dfbd764_headIcon.png",
                    "SubId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                    "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                    "UserName": "专检"
                }
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "保存成功！")

    def test_14_AddDepartmentbyMobile(self):
        """添加部门"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.BP.DepartmentBP.svc/AddDepartmentbyMobile'
        data_ = {
                "departmentDTO": {
                    "EBCOrganizationId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                    "Name": "API",
                    "ParentId": "9dc4d023-7da0-466c-ac72-4e5f9c8c07f5",
                    "SubId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
                }
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "添加部门成功")

    @depend("test_14_AddDepartmentbyMobile")
    def test_15_DelDepartmentbyMobile(self):
        """删除部门"""
        TestUserManage.GetDepartmentAndEmployeeListV2(self)
        ID = self.jsonpath('$..[?(@.Name=="API")].DepId')
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.BP.DepartmentBP.svc/DelDepartmentbyMobile'
        data_ = {"Ids":[ID[0]]}
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "删除成功")

    def test_16_AddEmployeesInfoByMobile(self):
        """添加员工"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.BP.EmployeeBP.svc/AddEmployeesInfoByMobile'
        data_ = {
                "ListAddEmployeesInfoDTO": [{
                    "DepartmentId": "5f91294c-ad64-41f1-ada7-73b48f44b815",
                    "EmpRelationCode": "",
                    "HeadImg": "",
                    "HeaderIcon": "",
                    "IsAdmin": False,
                    "IsEnable": False,
                    "IsLeaders": False,
                    "LoginAccount": "13910098600",
                    "Name": "api",
                    "OrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                    "RoleInfo": "d7dae606-2853-4fab-9062-f307182b93f3",
                    "isSelect": False
                }]
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "添加成功!")

    @depend("test_16_AddEmployeesInfoByMobile")
    def test_17_SearchEmployeV2(self):
        """搜索员工"""
        url = 'https://ebc.iuoooo.com/Jinher.AMP.EBC.SV.EmployeeQuerySV.svc/SearchEmployeV2'
        data_ = {"Name":"api","OrgId":"6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"}
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    @depend("test_17_SearchEmployeV2")
    def test_18_DeleteLinkTel(self):
        """删除员工"""
        id = self.jsonpath('$..EmployeeId')
        url = 'https://patrol.iuoooo.com/api/BusinessLayOutDiode/DeleteLinkTel'
        data_ = {
                "OrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "StoreId": "a5bac1d7-0c0c-4328-8af1-2df7955a0e74",
                "UserInfos": [{
                    "Phone": "13910098600",
                    "UserId": id[0]
                }]
            }
        self.post(url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("Message", "删除成功")
