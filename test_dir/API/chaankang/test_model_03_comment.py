import seldom
from seldom.utils import cache
from seldom import depend

class TestComment(seldom.TestCase):
    def start(self):
        self.store_id = "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
        self.store_name = "白兔咖啡"
        self.oper_id = "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc"

    def test_01_GetStoreCommentInfo(self):   # 获取评价信息
        url = "https://comment.iuoooo.com/api/CommentQuery/GetStoreCommentInfo"
        data_ = {
                "equipmentStatus": 0,
                "rtcType": 0,
                "storeId": self.store_id,
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    def test_02_GetCommentPermissions(self):  # 获取评价权限
        url = "https://iustore.iuoooo.com/Jinher.AMP.Store.SV.CommentQuerySV.svc/GetCommentPermissions"
        data_ = {
                "param": {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "storeId": self.store_id,
                    "userId": "b60159e2-f116-4d6e-8bff-a64987c69022",
                    "orgId": "ab9d121e-0145-41d8-b787-460480290d42"
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    def test_03_GetStoreComments(self):  # 获取用户评价
        url = "https://comment.iuoooo.com/api/CommentQuery/GetStoreComments"
        data_ = {
                "getCommentListDTO": {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "commentType": "all",
                    "isManageList": "0",
                    "pageIndex": "1",
                    "pageSize": "10",
                    "shopAppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "storeId": self.store_id,
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_04_InitCreateStoreComment(self):  # 获取评级标签
        url = "https://comment.iuoooo.com/api/CommentQuery/InitCreateStoreComment"
        data_ = {
                "initCommentDTO": {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "authId": self.oper_id,
                    "operId":  self.oper_id,
                    "shopAppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "storeId": self.store_id,
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("commentModel.placeHolderTxt", "说出你的看法，帮助大家更好的选择")

    @depend("test_04_InitCreateStoreComment")
    def test_05_CreateStoreComment(self):  # 获取发布评价
        star_type_01 = self.response["commentModel"]["starModels"][0]["starType"]
        star_name_01 = self.response["commentModel"]["starModels"][0]["starName"]
        tag_type_01 = self.response["commentModel"]["starModels"][0]["goodTags"][0]["tagType"]
        star_type_02 = self.response["commentModel"]["starModels"][1]["starType"]
        star_name_02 = self.response["commentModel"]["starModels"][1]["starName"]
        tag_type_02 = self.response["commentModel"]["starModels"][1]["goodTags"][0]["tagType"]
        star_type_03 = self.response["commentModel"]["starModels"][2]["starType"]
        star_name_03 = self.response["commentModel"]["starModels"][2]["starName"]
        tag_type_03 = self.response["commentModel"]["starModels"][2]["goodTags"][0]["tagType"]
        url = "https://comment.iuoooo.com/api/CommentQuery/CreateStoreComment"
        data_ = {
                "commentDTO": {
                    "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "authId": "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc",
                    "contentTxt": "API test",
                    "images": ["https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661%2F2023021415%2Fad66f2047fe243369f88bac63a7f4c05_581-407c-9ddd-f3e1e2089e68.jpg"],
                    "operId": self.oper_id,
                    "shopAppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                    "starModels": [{
                        "selectdTagsId": [tag_type_01],
                        "starName": star_name_01,
                        "starType": star_type_01,
                        "starValue": "5.0"
                    }, {
                        "selectdTagsId": [tag_type_02],
                        "starName": star_name_02,
                        "starType": star_type_02,
                        "starValue": "5.0"
                    }, {
                        "selectdTagsId": [tag_type_03],
                        "starName": star_name_03,
                        "starType": star_type_03,
                        "starValue": "5.0"
                    }],
                    "storeId": self.store_id,
                    "userIcon": "https:\/\/fileserver.iuoooo.com\/Jinher.JAP.BaseApp.FileServer.UI\/FileManage\/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661\/TempDirectory\/3890c11b649f4b3c860b07ad54e7e5c8_E76B5020-1290-4D3E-9CDC-B3DB01072713.png",
                    "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                    "userName": "测试4"
                },
                "clientInfo": {
                    "device": "android",
                    "version": "6.309.795",
                    "versionNum": "180",
                    "appid": "2fd5f092-d360-4783-b95c-6d47ee5cac44"
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    @depend("test_05_CreateStoreComment")
    def test_06_DelUserCommentById(self):   # 删除评价
        comment_id = self.response["commentId"]
        url = "https://comment.iuoooo.com/api/CommentQuery/DelUserCommentById"
        data_ = {
                "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44",
                "authId": self.oper_id,
                "commentId": comment_id,
                "operId": self.oper_id,
                "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")


