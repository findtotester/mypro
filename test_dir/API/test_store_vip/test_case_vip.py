import seldom
import random
from test_data import Data, Host
from seldom import Seldom
from seldom.utils import cache


class TestVIP(seldom.TestCase):
    def start(self):
        if Seldom.base_url == "Test":
            self.patrol = Host.Test.get('patrol')
            self.account = Data.Test.get('Account')
            self.userid = Data.Test.get('UserId')
            self.appid = Data.Test.get('AppId')
            self.storeid = Data.Test.get('StoreId_B')
        if Seldom.base_url == "Online":
            self.patrol = Host.Online.get('patrol')
            self.account = Data.Online.get('Account')
            self.userid = Data.Online.get('UserId')
            self.appid = Data.Online.get('AppId')
            self.storeid = Data.Online.get('StoreId_B')

    # 随机生成手机号
    def random_phone(self):
        headlist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "131",
                    "152", "153", "154", "156", "158", "159", "186", "187", "188", "189"]
        return random.choice(headlist) + "".join(random.choice("0123456789") for i in range(8))

    # 注册会员
    def test_01_regmember(self):
        self.url = f"{self.patrol}/api/Member/RegMember"
        phone = self.random_phone()
        cache.set({"phone": phone})
        data_ = {
                "appId": self.appid,
                "storeId": self.storeid,
                "userId": self.userid,
                "phone": phone,
                "birth": "",
                "sex": "1"
                }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            msg = self.response["Message"]
            if msg == "已注册过会员" or msg == "添加成功":
                return True
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    # 获取会员注册信息
    def test_02_getismember(self):
        phone = cache.get("phone")
        self.assertNotEqual(phone, None)
        self.url = f"{self.patrol}/api/Member/GetIsMember"
        data_ = {
                "appId": self.appid,
                "storeId": self.storeid,
                "userId": self.userid,
                "account": phone
                }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            msg = self.response["Message"]
            if msg == "获取成功":
                return True
            elif msg == "未注册会员":
                print(msg)
                return True
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    # 获取会员统计信息
    def test_getmemberstat(self):
        self.url = f"{self.patrol}/api/Member/GetMemberStat"
        data_ = {
                "account": self.account,
                "appId": self.appid,
                "storeId": self.storeid,
                "userId": self.userid
                }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            msg = self.response["Message"]
            if msg == "获取成功":
                return True
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

