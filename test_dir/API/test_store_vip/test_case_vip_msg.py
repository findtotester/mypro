import seldom
from seldom import Seldom , label
from test_data import Data, Host
from seldom.utils import cache
import re
from seldom import depend
import json


class TestVIPmsg(seldom.TestCase):
    def start(self):
        if Seldom.base_url == "Test":
            self.patrol = Host.Test.get('patrol')
            self.account = Data.Test.get('Account')
            self.userid = Data.Test.get('UserId')
            self.appid = Data.Test.get('AppId')
            self.storeid = Data.Test.get('StoreId_B')
            self.storename = Data.Test.get('StoreName_B')
        if Seldom.base_url == "Online":
            self.patrol = Host.Online.get('patrol')
            self.account = Data.Online.get('Account')
            self.userid = Data.Online.get('UserId')
            self.appid = Data.Online.get('AppId')
            self.storeid = Data.Online.get('StoreId_B')
            self.storename = Data.Test.get('StoreName_B')

    # 发送消息
    @seldom.label("slow")
    def test_01_sendmember(self):
        self.url = f"{self.patrol}/api/Member/SendMember"
        data_ = {
                "appId": self.appid,
                "content": "会员消息测试",
                "storeId": self.storeid,
                "storeName": self.storename,
                "title": "会员通知栏消息",
                "userAccount": self.account,
                "userId": self.appid,
                "userImg": "https://fileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f9661%2F2022061613%2F748f485b-bff0-44d6-ade9-b48864365f37_Img_7565ca8d-3d6d-48bb-887e-d9c8e59d694d.jpg",
                "userName": "API"
                }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath("Message", "发布成功")
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    # 获取消息列表
    def test_02_Getmemberlist(self):
        ship_id = cache.get("ship_id")
        if ship_id is not None:
            return True
        self.url = f"{self.patrol}/api/Member/GetMemberList"
        data_ = {
                "appId": self.appid,
                "storeId": self.storeid,
                "userId": self.userid,
                "account": self.account,
                "pageIndex": "1",
                "pageSize": "20"
                }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            ship_id = self.response["Data"][0]["shipId"]
            cache.set({"ship_id": ship_id})
            print("调试信息", ship_id)
            return True
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    # 查看消息详情
    @depend("test_02_Getmemberlist")     # 依赖的用例成功后才会执行此用例否则跳过
    def test_03_getmemberdetail(self):
        # self.getmemberlist()
        shipid = cache.get("ship_id")
        self.assertNotEqual(shipid, None)
        self.url = f"{self.patrol}/api/Member/GetMemberDetail"
        data_ = {
                "appId": self.appid,
                "storeId": self.storeid,
                "userId": self.userid,
                "shipId": shipid
                }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath("Message", "获取成功")
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    # 删除消息
    @seldom.label("slow")
    @depend("test_02_Getmemberlist")
    def test_04_delmemberlist(self):
        # self.getmemberlist()
        shipid = cache.get("ship_id")
        self.assertNotEqual(shipid, None)
        self.url = f"{self.patrol}/api/Member/DelMemberList"
        data_ = {
            "appId": self.appid,
            "storeId": self.storeid,
            "userId": self.userid,
            "shipId": shipid
        }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            self.assertPath("Message", "删除成功")
            cache.clear("ship_id")
        except AssertionError as e:
            print('执行结果:Failed')
            cache.clear("ship_id")
            raise e

    # 消息列表验证
    @seldom.label("slow")
    def test_05_getmemberlist(self):
        for i in range(1, 20):
            self.url = f"{self.patrol}/api/Member/GetMemberList"
            data_ = {
                "appId": self.appid,
                "storeId": self.storeid,
                "userId": self.userid,
                "account": self.account,
                "pageIndex": i,
                "pageSize": "20"
            }

            self.post(self.url, json=data_)
            try:
                self.assertStatusCode(200)
                self.assertPath("Message", "获取成功")
            except AssertionError as e:
                print('执行结果:Failed')
                raise e
            body = self.jsonpath('$.Data')
            ship_list = re.findall('\'shipId\': \'(.*?)\'', str(body))  # 正则获取指定数据
            count = len(ship_list)
            if count < 20 and i == 1:
                print("只有一页数据：", i)
            if 'shipId' not in str(body):  # 判断某个字段是否存在
                print("当前页数无数据:", i)
                print("总页数：", i-1)
                break
            print("页数:", i)

