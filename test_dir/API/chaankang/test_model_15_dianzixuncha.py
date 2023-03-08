import seldom
from seldom.testdata import *
from seldom.utils import cache


class Testdianzixuncha(seldom.TestCase):
    def start(self):
        self.storeid = 'a5bac1d7-0c0c-4328-8af1-2df7955a0e74'
        self.appid = '9be42759-9686-4541-b5a4-2be15a5c7d73'
        self.userid = '3c73f483-0a2f-4838-b04b-58a2eb64ebd0'
        self.day = get_custom_data("m", 1).replace('-', '.')
        self.storename = '白兔咖啡'


    def test_01_GetMapStoreBase(self):
        url = 'https://patrol.iuoooo.com/api/StoreDetail/GetMapStoreBase'
        data_ = {
                "equipmentStatus": "0",
                "lat": "0",
                "lng": "0",
                "storeId": self.storeid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    def test_02_GetInspectDictionaryBaseData(self):
        url = 'https://ripx.iuoooo.com/api/Inspect/GetInspectDictionaryBaseData'
        data_ = {
                "AppId": self.appid,
                "GetDicType": "1",
                "StoreId": self.storeid,
                "UserId": self.userid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_03_GetInspectOptionList(self):
        url = 'https://ripx.iuoooo.com/api/Reform/GetInspectOptionList'
        data_ = {
                "AppId": self.appid,
                "OrgId": "7035c461-c80e-49ce-a7c8-5584f0453646",
                "ProcessType": 0,
                "StoreId": self.storeid,
                "Type": 6,
                "UserId": self.userid,
                "clientType": 1,
                "roleType": 0,
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_04_SubEleTask(self):
        url = 'https://ripx.iuoooo.com/api/Electronic/SubEleTask'
        data_ = {
                    "AppId": self.appid,
                    "EnforceUserId": self.userid,
                    "EnforceUserName": "188****0064",
                    "InspectOptionLst": [{
                        "ClassificationId": "b8aff244-6f31-4924-94cb-fcd41d36b9e4",
                        "ImgLst": ["https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d%2F2023022713%2F6b810efb91704811a54d8153e4e4eccb_37f-45e7-a9d0-80bc159cde9d.jpg"],
                        "InspectOptionId": "238d49a5-376e-4ed9-835c-1929c8c6050a",
                        "InspectOptionRemark": "111",
                        "InspectOptionRemarkImg": "http://fileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661/2021052819/f9526ef5-3aa3-4368-8fe4-626b5418742c_f.png",
                        "InspectOptionText": "未带帽子",
                        "Status": 0,
                        "StatusText": "不合格"
                    }],
                    "InspectResult": "基本符合",
                    "InspectResultId": "08b30180-c9e7-4542-9e88-f286e8069a51",
                    "Latitude": "37.379779",
                    "Longitude": "101.723321",
                    "ProcessResult": "现场整改",
                    "ProcessResultId": "45fcb890-c72c-4d36-b91b-e375053fd9f3",
                    "StoreId": self.storeid
                }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_05_AddReform(self):
        SourceId = self.response['Detail']
        url = 'https://ripx.iuoooo.com/api/Reform/AddReform'
        data_ = {
                "AppId": self.appid,
                "ExamineUserId": self.userid,
                "ExamineUserName": "188****0064",
                "OrgId": "7035c461-c80e-49ce-a7c8-5584f0453646",
                "ReformEndTime": self.day,
                "ReformId": "",
                "ReformModelList": [{
                    "ReformOptionList": [{
                        "InspectOptionId": "238d49a5-376e-4ed9-835c-1929c8c6050a",
                        "InspectOptionName": "未带帽子",
                        "ViolationPicIds": ["a413ce7f-4eef-4c02-ae45-987fcca2e9b0"],
                        "ViolationPics": ["https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d%2F2023022713%2F6b810efb91704811a54d8153e4e4eccb_37f-45e7-a9d0-80bc159cde9d.jpg"]
                    }],
                    "ReformText": "整改",
                    "StoreId": self.storeid,
                    "StoreName": self.storename
                }],
                "ReformSource": "1",
                "ReformStartTime": get_strftime(get_now_datetime(True), "%Y.%m.%d %H:%M"),
                "SourceId": SourceId,
                "UserId": self.userid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")
        Id = self.response['Data']  # d9ac6007-5b2b-4e1e-9112-1feed5394e8d
        cache.set({"Id": Id})

    def test_06_GetReformList(self):
        Id = cache.get("Id")
        url = 'https://ripx.iuoooo.com/api/Reform/GetReformList'
        data_ = {
                "AppId": self.appid,
                "ClientType": "1",
                "OrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "PageIndex": "1",
                "PageSize": "20",
                "ReformStateList": [],
                "StoreIdList": [self.storeid],
                "UserId": self.userid,
                "handleType": ""
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Content[0].Id", Id)

    def test_07_GetReformDetail(self):
        Id = cache.get("Id")
        url = 'https://ripx.iuoooo.com/api/Reform/GetReformDetail'
        data_ = {
                "AppId": self.appid,
                "Id": Id,
                "OrgId": "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b",
                "UserId": self.userid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_08_EditReform(self):
        Id = cache.get("Id")
        ReformOptinId = self.jmespath("Content.OptionList[0].ReformOptionId")
        url = 'https://ripx.iuoooo.com/api/Reform/EditReform'
        data_ = {
                "Id": Id,
                "ReformOptionList": [{
                    "ReformOptinId": ReformOptinId,
                    "ReformPicInfo": [{
                        "OriginalPic": "https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d%2F2023022713%2F38ac774a746d45838d16656785a555d6_ef1-4958-9861-1d3d77af9edc.jpg",
                        "Pic": "https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661%2F2023022713%2F5d0ce4ceed6241b58e93af33f1273c68_e25-4c0b-8136-76fc5e66e1f0.jpg"
                    }],
                    "ReformPics": "https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661%2F2023022713%2F5d0ce4ceed6241b58e93af33f1273c68_e25-4c0b-8136-76fc5e66e1f0.jpg"
                }]
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        cache.clear("Id")

