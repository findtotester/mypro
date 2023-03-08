import seldom
from seldom.utils import cache
import re
from seldom import file_data
import time
import jsonpath



class TestNMG(seldom.TestCase):
    def start(self):
        print()

    def test_01_login(self):
        self.url = f"http://aup.iuoooo.com/Jinher.AMP.App.SV.UserAppSV.svc/UserLoginNew"
        data_ = {
            "dto": {
                "AppId": "26fbfe8c-af1b-49fe-b9c2-0fd4da828680",
                "Account": "18800000064",
                "Password": "jhtest",
                "AccountType": "0"
            }
        }
        self.post(self.url, json=data_)
        try:
            self.assertStatusCode(200)
            UID = self.response["ContextDTO"]["LoginUserID"]
            SID = self.response["ContextDTO"]["SessionID"]
            cache.set({"UID": UID})
            cache.set({"SID": SID})
            return True
        except AssertionError as e:
            print('执行结果:Failed')
            raise e

    def test_02_NewStoreManage(self):
        fiddler_proxies = {'http': '127.0.0.1:8888'}
        UID = cache.get("UID")
        SID = cache.get("SID")
        self.url = f"http://iustore-ui.iuoooo.com/NewStoreManage/List?userId={UID}&sessionId={SID}&isEncrypt=False&curChangeOrg=e395cc5e-4d87-4923-9e87-21dcb03c5e42&isHD=false&limitDate=&mpage=CanTingGuanLi_26fbfe8c-af1b-49fe-b9c2-0fd4da828680&changeOrg=47f92693-ca6b-4541-9cd4-e811d56aef1c&appId=8151f186-e6f8-4c98-bb73-08163279c740"
        r = self.get(self.url, allow_redirects=False)
        d = re.findall('<a href="/Login/(.*?)">here', str(self.response))
        SSOIndex = str(d[0]).replace('amp;', '')
        ASP_NET_SessionId = re.findall('ASP.NET_SessionId=(.*?) path=/; HttpOnly', str(r.headers.get('Set-Cookie')))
        cache.set({"SSOIndex": SSOIndex})
        cache.set({"ASP_NET_SessionId": ASP_NET_SessionId})

    def test_03_SSOIndex(self):
        fiddler_proxies = {'http': '127.0.0.1:8888'}  # 设置代理地址和端口
        SSOIndex = cache.get("SSOIndex")
        ASP_NET_SessionId = cache.get("ASP_NET_SessionId")
        cookies = {'ASP_NET_SessionId': ASP_NET_SessionId[0]}
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Cookie": "ASP.NET_SessionId="+ASP_NET_SessionId[0]}
        self.url = f"http://iustore-ui.iuoooo.com/Login/{SSOIndex}"
        # 代理抓包
        # self.get(self.url, cookies=cookies, proxies=fiddler_proxies, allow_redirects=False)  # allow_redirects 请求重定向设置
        self.get(self.url, cookies=cookies, headers=headers, allow_redirects=False)
        d = re.findall('<a href="/NewStoreManage/(.*?)">here', str(self.response))
        NewStoreManage = str(d[0]).replace('amp;', '')
        cache.set({"NewStoreManage": NewStoreManage})

    @file_data("test_data/city.json", key="City")
    def test_04_BusinessStoreManage(self, _, req):
        ASP_NET_SessionId = cache.get("ASP_NET_SessionId")
        cookies = {'ASP_NET_SessionId': ASP_NET_SessionId[0]}
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Cookie": "ASP.NET_SessionId="+ASP_NET_SessionId[0]}
        data = {
                "OperateType": "[\"7d6815f0-09cb-47a0-aa08-6be84d138a80\",\"c120779d-cb4f-4d89-ae1a-6dd346cb5c34\",\"4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc\",\"e0ec80e1-2e05-4d11-bef8-188eb7ea4378\",\"ff135c54-0722-4e91-8608-452c1ab44700\",\"c26e0efc-5c3d-4309-94fd-fb844ebe7287\",\"938a550f-1538-46d2-8256-f5f5f3ae8ffa\",\"71610555-ebeb-444d-ad72-d073da8dd35e\",\"a51022b1-63e4-4d37-b4fe-ff3694bb93cb\",\"ca85a5a6-60c0-4013-abbc-80562edc7158\",\"2e8f4040-2616-445c-bddd-75ea56e37482\",\"d37988cb-9921-4f71-a873-ac32b9b1c5b4\",\"38040440-3fb6-41ca-aafb-3da10d61e3f4\",\"ec1e71df-1de8-4e80-9639-21e6b4b6c0fd\",\"caca1930-f8ba-4cf2-9ce3-013c1a6c2054\",\"1390823a-7ec0-4f13-9621-4e009df3c51f\",\"f759e3d3-f81d-4553-8906-3341c3edf124\",\"c6403ff5-64a7-4ceb-892c-75be5006c012\",\"24d630f9-cb22-4403-8baf-bc3567d46b94\",\"3264b42c-058e-4fe6-84d6-eed0846584f3\",\"8d27e56e-c161-4058-b943-7308a4eea7fb\",\"45406181-2297-46c9-9a48-a8b7759275ea\",\"66742d19-8b89-4735-9bf6-492256c2898c\",\"c6d7b442-30ec-42df-9f3f-aeb4364bbdf6\",\"aac1bfb8-eac2-40b2-807d-612222966b71\",\"2f4c5bb3-822d-4b9d-aabd-6211a5c68809\",\"6546ed24-b6af-483b-a843-82668471f846\",\"8b22fbd1-b4a4-42b2-b943-c9f48a13327a\",\"adcb6995-3db0-4b53-9bde-fa49adea9841\",\"d0649fe6-485e-49c5-9b33-e7463faa215d\",\"39c618db-5954-4ca0-bd0e-9a44a3e907fb\",\"09bffc62-32d2-464e-97e7-bea62f13d4fb\",\"1008e75b-aa97-4f35-892a-ceb9dc0c61b3\",\"25f2de34-5905-454a-8912-f4e755609498\",\"fe52e7fb-21ca-4d82-a5d7-125b55839aa9\",\"e06e26c7-0c5e-4f26-a51d-421467e12992\",\"541267fb-41f9-4900-a07b-fa43c058759f\",\"dc9a3e98-7f2f-4bc0-ae2f-f2c364ff8840\",\"44ff5903-e162-42a1-b531-5865e97eb0a2\",\"c0d4d1da-95e9-454e-8739-420398d7cc7c\",\"b031e741-0caa-45cc-b4f5-063299702af1\",\"e42b89e0-32e6-4f17-af26-10ab1676ad54\",\"899f03f9-c2c8-44e0-9561-7acfc76ea2d1\",\"0cfa3b3b-94c4-407c-b95d-1b99a54caef2\",\"9c098ae9-f7e9-4433-8f90-b19b3d13cd20\",\"0521f26f-76b8-40c2-8a27-a68b2e62db13\",\"d36a86e4-5579-44c5-8eaa-68196edb2899\",\"295d267e-d7bb-4cdd-bcaa-2a70c42f04ab\",\"dd81fa26-0620-4899-8463-9ddcca135d3f\",\"b1d907f1-9e7a-437f-bbed-9d3d8703f4ac\",\"51aadf05-f33f-45cd-ad77-d718739a792c\",\"63430017-600d-4f5b-89fa-de8e84c580dc\",\"26eb8866-0a2f-4661-b1c0-0420e235538c\",\"06f50e36-24fc-4920-8cfa-5c77b2203c23\",\"19362b99-61ff-4ebb-97fd-b629a0eee2d1\",\"9b1e32f0-2a79-482e-8413-69b12a8a69a2\",\"43ea621c-650f-48f5-9504-5db5c3551f7d\",\"fdf02602-ec7f-4c48-8256-4a4eac585fe2\",\"546f3a95-2f40-4edd-8028-c11b55a006fd\",\"6038bc3b-834e-43ad-a668-e8112946b270\",\"4d357bf0-906b-4714-90a0-c480e7135bfa\",\"201ba1b6-335c-4b9a-b25c-c0669fe2e29f\",\"f498b5dc-fbc5-4d8e-926b-9c56b2f26222\",\"9db5cb67-9309-4277-8fce-4191d52a1c7c\",\"79cb789a-6f2e-4b02-b9f7-de7067f77dd5\",\"b7001140-a26c-4269-b9a1-8aed5a57e0af\",\"deb73fa7-bfa4-40b2-9946-c152dbe9a413\",\"4328e3fa-3346-4d10-ba4c-43bee52739a8\",\"b43e2c16-f44a-478d-9838-213cb052657d\",\"a7fa4d13-22c4-4d58-9294-017e009fddf7\",\"c92b317a-d8aa-457f-8181-385560ae04e2\",\"51e61c9c-c946-47f2-bab7-bb17ba07f176\",\"a4421504-77c8-4c83-b358-18a1678408b8\",\"9b6e2407-509d-4ec3-b7a7-65cb1926b93c\",\"0bf07a61-5204-4458-b3a3-9d133602313d\",\"a19bb492-482e-4e40-a204-f029b3e6b143\",\"219cc73e-a522-46be-b457-01122d853771\",\"20225b06-bc60-4592-b60e-ee99615c1e88\",\"9200ff75-a091-43cc-86fc-cada25fe5ec1\",\"55e2c08d-4aa0-4075-ab9c-6f16639dd19b\",\"cf4eb285-f7a1-488a-9352-45df0cf0873c\",\"49eea3e7-f898-4326-8083-1c99f8e76f63\",\"d7aa6c50-9899-4451-ad38-20550105d142\",\"f15b2f06-0b35-49c7-bbc5-7f0d5b774a24\",\"02d08bd5-1287-4b33-b124-d2c1f00e08b9\",\"158f1057-23dc-4b0c-b8bf-ad38a241fd8a\",\"372d9d26-1659-488d-9fb5-960301077f97\",\"21d06b2c-4f45-4eed-bf0a-f8614005d0b1\",\"7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7\",\"ece6a8a5-d6d3-4253-85d2-9ad3a141312a\",\"251b05ad-846f-11ea-8a1a-7cd30aeb142a\",\"5c76e7b1-5da3-42a5-b449-a895a262ccaa\",\"82144a37-cfe5-4972-92fb-fb35ae452702\",\"9cd3921a-4e00-4fc8-972f-9e6e4cee52cb\",\"4af55cca-e762-4df0-b463-37b85502fabb\",\"ab4814af-cd64-424f-8ec1-64afc56f067e\",\"7ad0841d-843b-4d91-83a4-8927b8764c9f\",\"e0ee8a9b-42c3-4291-aef7-c2351963297e\",\"575d4f4e-563a-456f-a4ab-5e3ab8f41b51\",\"6021a4bd-0cc0-422b-b0ad-4c6f7f59967d\",\"63587879-0275-40bb-a7a9-decc15a9d2cd\",\"b6b93af9-e3fc-479d-b857-9561c1b26316\",\"a9e344ce-678e-43d4-9f0a-d712428fb010\",\"39f08565-38d5-4cbb-b205-5cb233990bfe\",\"3953eebf-846e-11ea-8a1a-7cd30aeb142a\",\"2ce8fc14-9ad2-45c7-b875-a61c02441ed8\",\"8cf1bb42-10ed-4833-a385-2881aa6da26e\",\"0dd81fbf-c463-4614-82d1-c7de5016caa5\",\"13551abc-e926-462c-888e-fa68d27062a1\",\"54a50f7e-477c-4581-97d5-6aa9e9fbaca6\",\"b6ac8500-f3b4-43a1-8926-a42497eccb3c\",\"af862012-681b-4dea-97a6-de49594ddefb\",\"548bf6c1-2001-43a1-9f00-d22a95238bd3\",\"b42bd2f4-8580-4374-bf39-d1edb91535ca\",\"670bde3e-ec1a-46a9-9d5f-ac476ee47cd7\",\"0429b032-0caa-459a-9cc1-bdada63f672f\",\"b8df94ff-71a8-4b2b-88b8-8a86b04a948f\",\"534833eb-c005-4318-8a9f-dd9f67eef11a\",\"cae2a9f0-e27c-48b8-ba65-956f3be4bf52\",\"52ad72a4-24e1-4817-94d0-e3ba58ceec61\",\"61732579-e5fe-45fa-9461-a802a14b2a93\",\"a2dcdba8-b01b-4fb4-9532-7c163fdc5e3e\",\"95089bdc-522f-459b-9d36-0135d0c0020f\",\"3ab2902e-f6e6-4d69-831c-b9c5abb34e86\",\"614c8659-7621-4238-9c97-c964cc2d3fab\",\"9cd6379f-a069-4496-9798-931b81a4f497\",\"c04c1104-07c7-432c-bdce-267176e7cbb8\",\"123df428-1b13-4237-8a1a-a8d0ec5f9655\",\"9fa4d726-93c5-498f-ba82-e72b4e7e5ada\",\"397fea91-c1b0-416e-a79d-ad39e4ed0ec5\",\"f90d394e-0c0c-4604-8ea5-cae34b2beead\",\"9fe28e04-b2b7-47d1-a79d-6b35ca7a935e\",\"6feb4540-5e36-41d1-b14a-3512684aae35\",\"3d5228ad-b4c6-4166-884b-fca3adf90489\",\"fee089c4-2d3f-432e-9705-17dc518c4e0a\",\"9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb\",\"54babb89-27cd-4979-bdb2-bb70a70747af\",\"e7f2f508-c07c-4a47-86f8-cdee1d7942c7\",\"d031b370-26ee-4996-8f5c-d7536d4fbd1c\",\"ea9a9b89-bd2d-48c5-b838-b2d29a078d7d\",\"f70a135a-fdb2-4d12-bbf9-aa6eba941bef\",\"2f0a287d-8f03-40f7-a474-c26f47ca8a36\",\"28f5b615-c63e-4974-8569-34cc9271a9e4\",\"6bcb3398-0e18-4371-a173-d66e43cfb457\",\"2d1afbaa-fa13-4407-93fd-64a32269529e\",\"09d60d64-afce-4b89-8162-ec71c4309c0d\",\"3725e3dd-4d1d-4d71-bd12-c477ee611880\",\"2d06fd86-013d-49a5-9951-dfb3bf25d36b\",\"8068eaa1-0269-47f8-b2ab-02047096a6d4\",\"683a901c-0c80-485f-b940-6fe9fb13a47b\"]",
                "Name": "",
                "CompanyName": "",
                "AppId": "8151f186-e6f8-4c98-bb73-08163279c740",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "OrgId": "53cb543e-ca41-4036-8da6-5b892ccc1ab3",
                "Community": "",
                "Location": "00000000-0000-0000-0000-000000000000",
                "LicenceCode": "",
                "LicenseStatus": "",
                "ProvinceCode": "1-150000",
                "CityCode": req["code1"],
                "DistrictCode": "",
                "Status": "0",
                "CreditCode": "",
                "MainLabelIds": "",
                "page": "1",
                "rows": "20",
                "Address": "",
                "BusNet": "0",
                "CollDistr": "0",
                "Fuel": "0",
                "LiveRestIds": "[]",
                "CategoryIds": "",
                "RateState": ""
              }
        self.url = f"http://iustore-ui.iuoooo.com/NewStoreManage/GetFormalStoreList"
        self.post(self.url, data=data, cookies=cookies, headers=headers, allow_redirects=False)
        records = self.response["records"]
        f = open(r"D:\test001.csv", "a", encoding="UTF-8")
        f.write("门店管理_正常营业"+","+req["city"]+","+str(records)+'\n')
        f.close()
        self.assertStatusCode(200)

    @file_data("test_data/city.json", key="City")
    def test_05_StopStoreManage(self, _, req):
        ASP_NET_SessionId = cache.get("ASP_NET_SessionId")
        cookies = {'ASP_NET_SessionId': ASP_NET_SessionId[0]}
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Cookie": "ASP.NET_SessionId="+ASP_NET_SessionId[0]}
        data = {
                "OperateType": "[\"7d6815f0-09cb-47a0-aa08-6be84d138a80\",\"c120779d-cb4f-4d89-ae1a-6dd346cb5c34\",\"4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc\",\"e0ec80e1-2e05-4d11-bef8-188eb7ea4378\",\"ff135c54-0722-4e91-8608-452c1ab44700\",\"c26e0efc-5c3d-4309-94fd-fb844ebe7287\",\"938a550f-1538-46d2-8256-f5f5f3ae8ffa\",\"71610555-ebeb-444d-ad72-d073da8dd35e\",\"a51022b1-63e4-4d37-b4fe-ff3694bb93cb\",\"ca85a5a6-60c0-4013-abbc-80562edc7158\",\"2e8f4040-2616-445c-bddd-75ea56e37482\",\"d37988cb-9921-4f71-a873-ac32b9b1c5b4\",\"38040440-3fb6-41ca-aafb-3da10d61e3f4\",\"ec1e71df-1de8-4e80-9639-21e6b4b6c0fd\",\"caca1930-f8ba-4cf2-9ce3-013c1a6c2054\",\"1390823a-7ec0-4f13-9621-4e009df3c51f\",\"f759e3d3-f81d-4553-8906-3341c3edf124\",\"c6403ff5-64a7-4ceb-892c-75be5006c012\",\"24d630f9-cb22-4403-8baf-bc3567d46b94\",\"3264b42c-058e-4fe6-84d6-eed0846584f3\",\"8d27e56e-c161-4058-b943-7308a4eea7fb\",\"45406181-2297-46c9-9a48-a8b7759275ea\",\"66742d19-8b89-4735-9bf6-492256c2898c\",\"c6d7b442-30ec-42df-9f3f-aeb4364bbdf6\",\"aac1bfb8-eac2-40b2-807d-612222966b71\",\"2f4c5bb3-822d-4b9d-aabd-6211a5c68809\",\"6546ed24-b6af-483b-a843-82668471f846\",\"8b22fbd1-b4a4-42b2-b943-c9f48a13327a\",\"adcb6995-3db0-4b53-9bde-fa49adea9841\",\"d0649fe6-485e-49c5-9b33-e7463faa215d\",\"39c618db-5954-4ca0-bd0e-9a44a3e907fb\",\"09bffc62-32d2-464e-97e7-bea62f13d4fb\",\"1008e75b-aa97-4f35-892a-ceb9dc0c61b3\",\"25f2de34-5905-454a-8912-f4e755609498\",\"fe52e7fb-21ca-4d82-a5d7-125b55839aa9\",\"e06e26c7-0c5e-4f26-a51d-421467e12992\",\"541267fb-41f9-4900-a07b-fa43c058759f\",\"dc9a3e98-7f2f-4bc0-ae2f-f2c364ff8840\",\"44ff5903-e162-42a1-b531-5865e97eb0a2\",\"c0d4d1da-95e9-454e-8739-420398d7cc7c\",\"b031e741-0caa-45cc-b4f5-063299702af1\",\"e42b89e0-32e6-4f17-af26-10ab1676ad54\",\"899f03f9-c2c8-44e0-9561-7acfc76ea2d1\",\"0cfa3b3b-94c4-407c-b95d-1b99a54caef2\",\"9c098ae9-f7e9-4433-8f90-b19b3d13cd20\",\"0521f26f-76b8-40c2-8a27-a68b2e62db13\",\"d36a86e4-5579-44c5-8eaa-68196edb2899\",\"295d267e-d7bb-4cdd-bcaa-2a70c42f04ab\",\"dd81fa26-0620-4899-8463-9ddcca135d3f\",\"b1d907f1-9e7a-437f-bbed-9d3d8703f4ac\",\"51aadf05-f33f-45cd-ad77-d718739a792c\",\"63430017-600d-4f5b-89fa-de8e84c580dc\",\"26eb8866-0a2f-4661-b1c0-0420e235538c\",\"06f50e36-24fc-4920-8cfa-5c77b2203c23\",\"19362b99-61ff-4ebb-97fd-b629a0eee2d1\",\"9b1e32f0-2a79-482e-8413-69b12a8a69a2\",\"43ea621c-650f-48f5-9504-5db5c3551f7d\",\"fdf02602-ec7f-4c48-8256-4a4eac585fe2\",\"546f3a95-2f40-4edd-8028-c11b55a006fd\",\"6038bc3b-834e-43ad-a668-e8112946b270\",\"4d357bf0-906b-4714-90a0-c480e7135bfa\",\"201ba1b6-335c-4b9a-b25c-c0669fe2e29f\",\"f498b5dc-fbc5-4d8e-926b-9c56b2f26222\",\"9db5cb67-9309-4277-8fce-4191d52a1c7c\",\"79cb789a-6f2e-4b02-b9f7-de7067f77dd5\",\"b7001140-a26c-4269-b9a1-8aed5a57e0af\",\"deb73fa7-bfa4-40b2-9946-c152dbe9a413\",\"4328e3fa-3346-4d10-ba4c-43bee52739a8\",\"b43e2c16-f44a-478d-9838-213cb052657d\",\"a7fa4d13-22c4-4d58-9294-017e009fddf7\",\"c92b317a-d8aa-457f-8181-385560ae04e2\",\"51e61c9c-c946-47f2-bab7-bb17ba07f176\",\"a4421504-77c8-4c83-b358-18a1678408b8\",\"9b6e2407-509d-4ec3-b7a7-65cb1926b93c\",\"0bf07a61-5204-4458-b3a3-9d133602313d\",\"a19bb492-482e-4e40-a204-f029b3e6b143\",\"219cc73e-a522-46be-b457-01122d853771\",\"20225b06-bc60-4592-b60e-ee99615c1e88\",\"9200ff75-a091-43cc-86fc-cada25fe5ec1\",\"55e2c08d-4aa0-4075-ab9c-6f16639dd19b\",\"cf4eb285-f7a1-488a-9352-45df0cf0873c\",\"49eea3e7-f898-4326-8083-1c99f8e76f63\",\"d7aa6c50-9899-4451-ad38-20550105d142\",\"f15b2f06-0b35-49c7-bbc5-7f0d5b774a24\",\"02d08bd5-1287-4b33-b124-d2c1f00e08b9\",\"158f1057-23dc-4b0c-b8bf-ad38a241fd8a\",\"372d9d26-1659-488d-9fb5-960301077f97\",\"21d06b2c-4f45-4eed-bf0a-f8614005d0b1\",\"7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7\",\"ece6a8a5-d6d3-4253-85d2-9ad3a141312a\",\"251b05ad-846f-11ea-8a1a-7cd30aeb142a\",\"5c76e7b1-5da3-42a5-b449-a895a262ccaa\",\"82144a37-cfe5-4972-92fb-fb35ae452702\",\"9cd3921a-4e00-4fc8-972f-9e6e4cee52cb\",\"4af55cca-e762-4df0-b463-37b85502fabb\",\"ab4814af-cd64-424f-8ec1-64afc56f067e\",\"7ad0841d-843b-4d91-83a4-8927b8764c9f\",\"e0ee8a9b-42c3-4291-aef7-c2351963297e\",\"575d4f4e-563a-456f-a4ab-5e3ab8f41b51\",\"6021a4bd-0cc0-422b-b0ad-4c6f7f59967d\",\"63587879-0275-40bb-a7a9-decc15a9d2cd\",\"b6b93af9-e3fc-479d-b857-9561c1b26316\",\"a9e344ce-678e-43d4-9f0a-d712428fb010\",\"39f08565-38d5-4cbb-b205-5cb233990bfe\",\"3953eebf-846e-11ea-8a1a-7cd30aeb142a\",\"2ce8fc14-9ad2-45c7-b875-a61c02441ed8\",\"8cf1bb42-10ed-4833-a385-2881aa6da26e\",\"0dd81fbf-c463-4614-82d1-c7de5016caa5\",\"13551abc-e926-462c-888e-fa68d27062a1\",\"54a50f7e-477c-4581-97d5-6aa9e9fbaca6\",\"b6ac8500-f3b4-43a1-8926-a42497eccb3c\",\"af862012-681b-4dea-97a6-de49594ddefb\",\"548bf6c1-2001-43a1-9f00-d22a95238bd3\",\"b42bd2f4-8580-4374-bf39-d1edb91535ca\",\"670bde3e-ec1a-46a9-9d5f-ac476ee47cd7\",\"0429b032-0caa-459a-9cc1-bdada63f672f\",\"b8df94ff-71a8-4b2b-88b8-8a86b04a948f\",\"534833eb-c005-4318-8a9f-dd9f67eef11a\",\"cae2a9f0-e27c-48b8-ba65-956f3be4bf52\",\"52ad72a4-24e1-4817-94d0-e3ba58ceec61\",\"61732579-e5fe-45fa-9461-a802a14b2a93\",\"a2dcdba8-b01b-4fb4-9532-7c163fdc5e3e\",\"95089bdc-522f-459b-9d36-0135d0c0020f\",\"3ab2902e-f6e6-4d69-831c-b9c5abb34e86\",\"614c8659-7621-4238-9c97-c964cc2d3fab\",\"9cd6379f-a069-4496-9798-931b81a4f497\",\"c04c1104-07c7-432c-bdce-267176e7cbb8\",\"123df428-1b13-4237-8a1a-a8d0ec5f9655\",\"9fa4d726-93c5-498f-ba82-e72b4e7e5ada\",\"397fea91-c1b0-416e-a79d-ad39e4ed0ec5\",\"f90d394e-0c0c-4604-8ea5-cae34b2beead\",\"9fe28e04-b2b7-47d1-a79d-6b35ca7a935e\",\"6feb4540-5e36-41d1-b14a-3512684aae35\",\"3d5228ad-b4c6-4166-884b-fca3adf90489\",\"fee089c4-2d3f-432e-9705-17dc518c4e0a\",\"9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb\",\"54babb89-27cd-4979-bdb2-bb70a70747af\",\"e7f2f508-c07c-4a47-86f8-cdee1d7942c7\",\"d031b370-26ee-4996-8f5c-d7536d4fbd1c\",\"ea9a9b89-bd2d-48c5-b838-b2d29a078d7d\",\"f70a135a-fdb2-4d12-bbf9-aa6eba941bef\",\"2f0a287d-8f03-40f7-a474-c26f47ca8a36\",\"28f5b615-c63e-4974-8569-34cc9271a9e4\",\"6bcb3398-0e18-4371-a173-d66e43cfb457\",\"2d1afbaa-fa13-4407-93fd-64a32269529e\",\"09d60d64-afce-4b89-8162-ec71c4309c0d\",\"3725e3dd-4d1d-4d71-bd12-c477ee611880\",\"2d06fd86-013d-49a5-9951-dfb3bf25d36b\",\"8068eaa1-0269-47f8-b2ab-02047096a6d4\",\"683a901c-0c80-485f-b940-6fe9fb13a47b\"]",
                "Name": "",
                "CompanyName": "",
                "AppId": "8151f186-e6f8-4c98-bb73-08163279c740",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "OrgId": "53cb543e-ca41-4036-8da6-5b892ccc1ab3",
                "Community": "",
                "Location": "00000000-0000-0000-0000-000000000000",
                "LicenceCode": "",
                "LicenseStatus": "",
                "ProvinceCode": "1-150000",
                "CityCode": req["code1"],
                "DistrictCode": "",
                "Status": "5",
                "CreditCode": "",
                "MainLabelIds": "",
                "page": "1",
                "rows": "20",
                "Address": "",
                "BusNet": "0",
                "CollDistr": "0",
                "Fuel": "0",
                "LiveRestIds": "[]",
                "CategoryIds": "",
                "RateState": ""
              }
        self.url = f"http://iustore-ui.iuoooo.com/NewStoreManage/GetFormalStoreList"
        self.post(self.url, data=data, cookies=cookies, headers=headers, allow_redirects=False)
        records = self.response["records"]
        f = open(r"D:\test001.csv", "a", encoding="UTF-8")
        f.write("门店管理_暂停营业"+","+req["city"]+","+str(records)+'\n')
        f.close()
        self.assertStatusCode(200)

    @file_data("test_data/city.json", key="City")
    def test_06_ClosedStoreManage(self, _, req):
        ASP_NET_SessionId = cache.get("ASP_NET_SessionId")
        cookies = {'ASP_NET_SessionId': ASP_NET_SessionId[0]}
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Cookie": "ASP.NET_SessionId="+ASP_NET_SessionId[0]}
        data = {
                "OperateType": "[\"7d6815f0-09cb-47a0-aa08-6be84d138a80\",\"c120779d-cb4f-4d89-ae1a-6dd346cb5c34\",\"4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc\",\"e0ec80e1-2e05-4d11-bef8-188eb7ea4378\",\"ff135c54-0722-4e91-8608-452c1ab44700\",\"c26e0efc-5c3d-4309-94fd-fb844ebe7287\",\"938a550f-1538-46d2-8256-f5f5f3ae8ffa\",\"71610555-ebeb-444d-ad72-d073da8dd35e\",\"a51022b1-63e4-4d37-b4fe-ff3694bb93cb\",\"ca85a5a6-60c0-4013-abbc-80562edc7158\",\"2e8f4040-2616-445c-bddd-75ea56e37482\",\"d37988cb-9921-4f71-a873-ac32b9b1c5b4\",\"38040440-3fb6-41ca-aafb-3da10d61e3f4\",\"ec1e71df-1de8-4e80-9639-21e6b4b6c0fd\",\"caca1930-f8ba-4cf2-9ce3-013c1a6c2054\",\"1390823a-7ec0-4f13-9621-4e009df3c51f\",\"f759e3d3-f81d-4553-8906-3341c3edf124\",\"c6403ff5-64a7-4ceb-892c-75be5006c012\",\"24d630f9-cb22-4403-8baf-bc3567d46b94\",\"3264b42c-058e-4fe6-84d6-eed0846584f3\",\"8d27e56e-c161-4058-b943-7308a4eea7fb\",\"45406181-2297-46c9-9a48-a8b7759275ea\",\"66742d19-8b89-4735-9bf6-492256c2898c\",\"c6d7b442-30ec-42df-9f3f-aeb4364bbdf6\",\"aac1bfb8-eac2-40b2-807d-612222966b71\",\"2f4c5bb3-822d-4b9d-aabd-6211a5c68809\",\"6546ed24-b6af-483b-a843-82668471f846\",\"8b22fbd1-b4a4-42b2-b943-c9f48a13327a\",\"adcb6995-3db0-4b53-9bde-fa49adea9841\",\"d0649fe6-485e-49c5-9b33-e7463faa215d\",\"39c618db-5954-4ca0-bd0e-9a44a3e907fb\",\"09bffc62-32d2-464e-97e7-bea62f13d4fb\",\"1008e75b-aa97-4f35-892a-ceb9dc0c61b3\",\"25f2de34-5905-454a-8912-f4e755609498\",\"fe52e7fb-21ca-4d82-a5d7-125b55839aa9\",\"e06e26c7-0c5e-4f26-a51d-421467e12992\",\"541267fb-41f9-4900-a07b-fa43c058759f\",\"dc9a3e98-7f2f-4bc0-ae2f-f2c364ff8840\",\"44ff5903-e162-42a1-b531-5865e97eb0a2\",\"c0d4d1da-95e9-454e-8739-420398d7cc7c\",\"b031e741-0caa-45cc-b4f5-063299702af1\",\"e42b89e0-32e6-4f17-af26-10ab1676ad54\",\"899f03f9-c2c8-44e0-9561-7acfc76ea2d1\",\"0cfa3b3b-94c4-407c-b95d-1b99a54caef2\",\"9c098ae9-f7e9-4433-8f90-b19b3d13cd20\",\"0521f26f-76b8-40c2-8a27-a68b2e62db13\",\"d36a86e4-5579-44c5-8eaa-68196edb2899\",\"295d267e-d7bb-4cdd-bcaa-2a70c42f04ab\",\"dd81fa26-0620-4899-8463-9ddcca135d3f\",\"b1d907f1-9e7a-437f-bbed-9d3d8703f4ac\",\"51aadf05-f33f-45cd-ad77-d718739a792c\",\"63430017-600d-4f5b-89fa-de8e84c580dc\",\"26eb8866-0a2f-4661-b1c0-0420e235538c\",\"06f50e36-24fc-4920-8cfa-5c77b2203c23\",\"19362b99-61ff-4ebb-97fd-b629a0eee2d1\",\"9b1e32f0-2a79-482e-8413-69b12a8a69a2\",\"43ea621c-650f-48f5-9504-5db5c3551f7d\",\"fdf02602-ec7f-4c48-8256-4a4eac585fe2\",\"546f3a95-2f40-4edd-8028-c11b55a006fd\",\"6038bc3b-834e-43ad-a668-e8112946b270\",\"4d357bf0-906b-4714-90a0-c480e7135bfa\",\"201ba1b6-335c-4b9a-b25c-c0669fe2e29f\",\"f498b5dc-fbc5-4d8e-926b-9c56b2f26222\",\"9db5cb67-9309-4277-8fce-4191d52a1c7c\",\"79cb789a-6f2e-4b02-b9f7-de7067f77dd5\",\"b7001140-a26c-4269-b9a1-8aed5a57e0af\",\"deb73fa7-bfa4-40b2-9946-c152dbe9a413\",\"4328e3fa-3346-4d10-ba4c-43bee52739a8\",\"b43e2c16-f44a-478d-9838-213cb052657d\",\"a7fa4d13-22c4-4d58-9294-017e009fddf7\",\"c92b317a-d8aa-457f-8181-385560ae04e2\",\"51e61c9c-c946-47f2-bab7-bb17ba07f176\",\"a4421504-77c8-4c83-b358-18a1678408b8\",\"9b6e2407-509d-4ec3-b7a7-65cb1926b93c\",\"0bf07a61-5204-4458-b3a3-9d133602313d\",\"a19bb492-482e-4e40-a204-f029b3e6b143\",\"219cc73e-a522-46be-b457-01122d853771\",\"20225b06-bc60-4592-b60e-ee99615c1e88\",\"9200ff75-a091-43cc-86fc-cada25fe5ec1\",\"55e2c08d-4aa0-4075-ab9c-6f16639dd19b\",\"cf4eb285-f7a1-488a-9352-45df0cf0873c\",\"49eea3e7-f898-4326-8083-1c99f8e76f63\",\"d7aa6c50-9899-4451-ad38-20550105d142\",\"f15b2f06-0b35-49c7-bbc5-7f0d5b774a24\",\"02d08bd5-1287-4b33-b124-d2c1f00e08b9\",\"158f1057-23dc-4b0c-b8bf-ad38a241fd8a\",\"372d9d26-1659-488d-9fb5-960301077f97\",\"21d06b2c-4f45-4eed-bf0a-f8614005d0b1\",\"7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7\",\"ece6a8a5-d6d3-4253-85d2-9ad3a141312a\",\"251b05ad-846f-11ea-8a1a-7cd30aeb142a\",\"5c76e7b1-5da3-42a5-b449-a895a262ccaa\",\"82144a37-cfe5-4972-92fb-fb35ae452702\",\"9cd3921a-4e00-4fc8-972f-9e6e4cee52cb\",\"4af55cca-e762-4df0-b463-37b85502fabb\",\"ab4814af-cd64-424f-8ec1-64afc56f067e\",\"7ad0841d-843b-4d91-83a4-8927b8764c9f\",\"e0ee8a9b-42c3-4291-aef7-c2351963297e\",\"575d4f4e-563a-456f-a4ab-5e3ab8f41b51\",\"6021a4bd-0cc0-422b-b0ad-4c6f7f59967d\",\"63587879-0275-40bb-a7a9-decc15a9d2cd\",\"b6b93af9-e3fc-479d-b857-9561c1b26316\",\"a9e344ce-678e-43d4-9f0a-d712428fb010\",\"39f08565-38d5-4cbb-b205-5cb233990bfe\",\"3953eebf-846e-11ea-8a1a-7cd30aeb142a\",\"2ce8fc14-9ad2-45c7-b875-a61c02441ed8\",\"8cf1bb42-10ed-4833-a385-2881aa6da26e\",\"0dd81fbf-c463-4614-82d1-c7de5016caa5\",\"13551abc-e926-462c-888e-fa68d27062a1\",\"54a50f7e-477c-4581-97d5-6aa9e9fbaca6\",\"b6ac8500-f3b4-43a1-8926-a42497eccb3c\",\"af862012-681b-4dea-97a6-de49594ddefb\",\"548bf6c1-2001-43a1-9f00-d22a95238bd3\",\"b42bd2f4-8580-4374-bf39-d1edb91535ca\",\"670bde3e-ec1a-46a9-9d5f-ac476ee47cd7\",\"0429b032-0caa-459a-9cc1-bdada63f672f\",\"b8df94ff-71a8-4b2b-88b8-8a86b04a948f\",\"534833eb-c005-4318-8a9f-dd9f67eef11a\",\"cae2a9f0-e27c-48b8-ba65-956f3be4bf52\",\"52ad72a4-24e1-4817-94d0-e3ba58ceec61\",\"61732579-e5fe-45fa-9461-a802a14b2a93\",\"a2dcdba8-b01b-4fb4-9532-7c163fdc5e3e\",\"95089bdc-522f-459b-9d36-0135d0c0020f\",\"3ab2902e-f6e6-4d69-831c-b9c5abb34e86\",\"614c8659-7621-4238-9c97-c964cc2d3fab\",\"9cd6379f-a069-4496-9798-931b81a4f497\",\"c04c1104-07c7-432c-bdce-267176e7cbb8\",\"123df428-1b13-4237-8a1a-a8d0ec5f9655\",\"9fa4d726-93c5-498f-ba82-e72b4e7e5ada\",\"397fea91-c1b0-416e-a79d-ad39e4ed0ec5\",\"f90d394e-0c0c-4604-8ea5-cae34b2beead\",\"9fe28e04-b2b7-47d1-a79d-6b35ca7a935e\",\"6feb4540-5e36-41d1-b14a-3512684aae35\",\"3d5228ad-b4c6-4166-884b-fca3adf90489\",\"fee089c4-2d3f-432e-9705-17dc518c4e0a\",\"9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb\",\"54babb89-27cd-4979-bdb2-bb70a70747af\",\"e7f2f508-c07c-4a47-86f8-cdee1d7942c7\",\"d031b370-26ee-4996-8f5c-d7536d4fbd1c\",\"ea9a9b89-bd2d-48c5-b838-b2d29a078d7d\",\"f70a135a-fdb2-4d12-bbf9-aa6eba941bef\",\"2f0a287d-8f03-40f7-a474-c26f47ca8a36\",\"28f5b615-c63e-4974-8569-34cc9271a9e4\",\"6bcb3398-0e18-4371-a173-d66e43cfb457\",\"2d1afbaa-fa13-4407-93fd-64a32269529e\",\"09d60d64-afce-4b89-8162-ec71c4309c0d\",\"3725e3dd-4d1d-4d71-bd12-c477ee611880\",\"2d06fd86-013d-49a5-9951-dfb3bf25d36b\",\"8068eaa1-0269-47f8-b2ab-02047096a6d4\",\"683a901c-0c80-485f-b940-6fe9fb13a47b\"]",
                "Name": "",
                "CompanyName": "",
                "AppId": "8151f186-e6f8-4c98-bb73-08163279c740",
                "UserId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                "OrgId": "53cb543e-ca41-4036-8da6-5b892ccc1ab3",
                "Community": "",
                "Location": "00000000-0000-0000-0000-000000000000",
                "LicenceCode": "",
                "LicenseStatus": "",
                "ProvinceCode": "1-150000",
                "CityCode": req["code1"],
                "DistrictCode": "",
                "Status": "1",
                "CreditCode": "",
                "MainLabelIds": "",
                "page": "1",
                "rows": "20",
                "Address": "",
                "BusNet": "0",
                "CollDistr": "0",
                "Fuel": "0",
                "LiveRestIds": "[]",
                "CategoryIds": "",
                "RateState": ""
              }
        self.url = f"http://iustore-ui.iuoooo.com/NewStoreManage/GetFormalStoreList"
        self.post(self.url, data=data, cookies=cookies, headers=headers, allow_redirects=False)
        records = self.response["records"]
        f = open(r"D:\test001.csv", "a", encoding="UTF-8")
        f.write("门店管理_关闭歇业"+","+req["city"]+","+str(records)+'\n')
        f.close()
        self.assertStatusCode(200)

    @file_data("test_data/city.json", key="City")
    def test_07_GetMengGuRiskTotal(self, _, req):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"appId": "8151f186-e6f8-4c98-bb73-08163279c740", "code": "", "type": "all", "labelId": "all"}
        self.url = f"http://dss.iuoooo.com/CockpitMobile/GetMengGuRiskTotal"
        self.post(self.url, data=data, headers=headers, allow_redirects=False)
        cache.set({"body": self.response})
        city = req["city"]
        EnterNum = ''.join(self.jsonpath(f'$..[?(@.AreaName=="{city}")].EnterNum'))
        f = open(r"D:\test001.csv", "a", encoding="UTF-8")
        f.write("风险监管大数据_风险总况"+","+req["city"]+","+str(EnterNum)+'\n')
        f.close()
        self.assertStatusCode(200)

    def test_07_GetMengGuRiskTotal(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"appId": "8151f186-e6f8-4c98-bb73-08163279c740", "code": "", "type": "all", "labelId": "all"}
        self.url = f"http://dss.iuoooo.com/CockpitMobile/GetMengGuRiskTotal"
        self.post(self.url, data=data, headers=headers, allow_redirects=False)
        cache.set({"body": self.response})

    @file_data("test_data/city.json", key="City")
    def test_08_writeRiskTotal(self, _, req):
        data = cache.get("body")
        city = req["city"]
        if city != '内蒙古':
            EnterNum = jsonpath.jsonpath(data, f'$..[?(@.AreaName=="{city}")].EnterNum')
            f = open(r"D:\test001.csv", "a", encoding="UTF-8")
            if EnterNum is not None:
                f.write("风险监管大数据_风险总况"+","+req["city"]+","+''.join(EnterNum)+'\n')
            else:
                f.write("风险监管大数据_风险总况" + "," + req["city"] + "," + "0" + '\n')
            f.close()

    def test_09_GetResetDate(self):
        self.url = f"http://dss.iuoooo.com/SunshineCater/GetResetDate"
        headers = {"Connection": "keep-alive", "Cookie": "CookieContextDTO=%7B%22userId%22%3A%223c73f483-0a2f-4838-b04b-58a2eb64ebd0%22%2C%22sessionId%22%3A%2245c54837-0b18-49d0-b7a9-312b757db229%22%2C%22changeOrg%22%3A%2253cb543e-ca41-4036-8da6-5b892ccc1ab3%22%2C%22originalUserId%22%3A%22%22%7D; CookieOrgContextDTO=%7B%22userId%22%3A%223c73f483-0a2f-4838-b04b-58a2eb64ebd0%22%2C%22sessionId%22%3A%2245c54837-0b18-49d0-b7a9-312b757db229%22%2C%22changeOrg%22%3A%2253cb543e-ca41-4036-8da6-5b892ccc1ab3%22%2C%22orgId%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22originalUserId%22%3A%22%22%7D; Label=00000000-0000-0000-0000-000000000000; LabelId=; OperateTypeId=; ParentLabelId=; ParentOperateTypeId=7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7%2Caac1bfb8-eac2-40b2-807d-612222966b71%2Ca9e344ce-678e-43d4-9f0a-d712428fb010%2C1008e75b-aa97-4f35-892a-ceb9dc0c61b3%2C39c618db-5954-4ca0-bd0e-9a44a3e907fb%2C52ad72a4-24e1-4817-94d0-e3ba58ceec61%2C0bf07a61-5204-4458-b3a3-9d133602313d%2C683a901c-0c80-485f-b940-6fe9fb13a47b%2Ced8e25c8-5b9a-434b-aac6-c8c2a18f5021%2C7d6815f0-09cb-47a0-aa08-6be84d138a80%2C219cc73e-a522-46be-b457-01122d853771%2C6feb4540-5e36-41d1-b14a-3512684aae35%2Cfdf02602-ec7f-4c48-8256-4a4eac585fe2%2C9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb%2C3264b42c-058e-4fe6-84d6-eed0846584f3%2C548bf6c1-2001-43a1-9f00-d22a95238bd3%2Cdd81fa26-0620-4899-8463-9ddcca135d3f%2C2d1afbaa-fa13-4407-93fd-64a32269529e%2Cdf514ffe-6890-4f10-a1c4-e43900b61668%2C7ad0841d-843b-4d91-83a4-8927b8764c9f%2Cf759e3d3-f81d-4553-8906-3341c3edf124%2C5c76e7b1-5da3-42a5-b449-a895a262ccaa%2C36fc0bac-1830-42c5-a227-1fb14de96647%2C; operateType=7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7%2Caac1bfb8-eac2-40b2-807d-612222966b71%2Ca9e344ce-678e-43d4-9f0a-d712428fb010%2C1008e75b-aa97-4f35-892a-ceb9dc0c61b3%2C39c618db-5954-4ca0-bd0e-9a44a3e907fb%2C52ad72a4-24e1-4817-94d0-e3ba58ceec61%2C0bf07a61-5204-4458-b3a3-9d133602313d%2C683a901c-0c80-485f-b940-6fe9fb13a47b%2Ced8e25c8-5b9a-434b-aac6-c8c2a18f5021%2C7d6815f0-09cb-47a0-aa08-6be84d138a80%2C219cc73e-a522-46be-b457-01122d853771%2C6feb4540-5e36-41d1-b14a-3512684aae35%2Cfdf02602-ec7f-4c48-8256-4a4eac585fe2%2C9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb%2C3264b42c-058e-4fe6-84d6-eed0846584f3%2C548bf6c1-2001-43a1-9f00-d22a95238bd3%2Cdd81fa26-0620-4899-8463-9ddcca135d3f%2C2d1afbaa-fa13-4407-93fd-64a32269529e%2Cdf514ffe-6890-4f10-a1c4-e43900b61668%2C7ad0841d-843b-4d91-83a4-8927b8764c9f%2Cf759e3d3-f81d-4553-8906-3341c3edf124%2C5c76e7b1-5da3-42a5-b449-a895a262ccaa%2C36fc0bac-1830-42c5-a227-1fb14de96647%2C", "Content-Length": "0", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Host": "dss.iuoooo.com", "User-Agent": "Apache-HttpClient/4.5.6 (Java/1.8.0_291)"}
        cookies = {"CookieContextDTO": "%7B%22userId%22%3A%223c73f483-0a2f-4838-b04b-58a2eb64ebd0%22%2C%22sessionId%22%3A%2245c54837-0b18-49d0-b7a9-312b757db229%22%2C%22changeOrg%22%3A%2253cb543e-ca41-4036-8da6-5b892ccc1ab3%22%2C%22originalUserId%22%3A%22%22%7D", "CookieOrgContextDTO": "%7B%22userId%22%3A%223c73f483-0a2f-4838-b04b-58a2eb64ebd0%22%2C%22sessionId%22%3A%2245c54837-0b18-49d0-b7a9-312b757db229%22%2C%22changeOrg%22%3A%2253cb543e-ca41-4036-8da6-5b892ccc1ab3%22%2C%22orgId%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22originalUserId%22%3A%22%22%7D", "Label": "00000000-0000-0000-0000-000000000000", "LabelId": "", "OperateTypeId": "", "ParentLabelId": "", "ParentOperateTypeId": "7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7%2Caac1bfb8-eac2-40b2-807d-612222966b71%2Ca9e344ce-678e-43d4-9f0a-d712428fb010%2C1008e75b-aa97-4f35-892a-ceb9dc0c61b3%2C39c618db-5954-4ca0-bd0e-9a44a3e907fb%2C52ad72a4-24e1-4817-94d0-e3ba58ceec61%2C0bf07a61-5204-4458-b3a3-9d133602313d%2C683a901c-0c80-485f-b940-6fe9fb13a47b%2Ced8e25c8-5b9a-434b-aac6-c8c2a18f5021%2C7d6815f0-09cb-47a0-aa08-6be84d138a80%2C219cc73e-a522-46be-b457-01122d853771%2C6feb4540-5e36-41d1-b14a-3512684aae35%2Cfdf02602-ec7f-4c48-8256-4a4eac585fe2%2C9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb%2C3264b42c-058e-4fe6-84d6-eed0846584f3%2C548bf6c1-2001-43a1-9f00-d22a95238bd3%2Cdd81fa26-0620-4899-8463-9ddcca135d3f%2C2d1afbaa-fa13-4407-93fd-64a32269529e%2Cdf514ffe-6890-4f10-a1c4-e43900b61668%2C7ad0841d-843b-4d91-83a4-8927b8764c9f%2Cf759e3d3-f81d-4553-8906-3341c3edf124%2C5c76e7b1-5da3-42a5-b449-a895a262ccaa%2C36fc0bac-1830-42c5-a227-1fb14de96647%2C", "operateType": "7b226b7b-f2a8-48dd-a8c5-50ff8bf782c7%2Caac1bfb8-eac2-40b2-807d-612222966b71%2Ca9e344ce-678e-43d4-9f0a-d712428fb010%2C1008e75b-aa97-4f35-892a-ceb9dc0c61b3%2C39c618db-5954-4ca0-bd0e-9a44a3e907fb%2C52ad72a4-24e1-4817-94d0-e3ba58ceec61%2C0bf07a61-5204-4458-b3a3-9d133602313d%2C683a901c-0c80-485f-b940-6fe9fb13a47b%2Ced8e25c8-5b9a-434b-aac6-c8c2a18f5021%2C7d6815f0-09cb-47a0-aa08-6be84d138a80%2C219cc73e-a522-46be-b457-01122d853771%2C6feb4540-5e36-41d1-b14a-3512684aae35%2Cfdf02602-ec7f-4c48-8256-4a4eac585fe2%2C9f3b10fa-bdd2-4f43-8b2d-9a49747b93cb%2C3264b42c-058e-4fe6-84d6-eed0846584f3%2C548bf6c1-2001-43a1-9f00-d22a95238bd3%2Cdd81fa26-0620-4899-8463-9ddcca135d3f%2C2d1afbaa-fa13-4407-93fd-64a32269529e%2Cdf514ffe-6890-4f10-a1c4-e43900b61668%2C7ad0841d-843b-4d91-83a4-8927b8764c9f%2Cf759e3d3-f81d-4553-8906-3341c3edf124%2C5c76e7b1-5da3-42a5-b449-a895a262ccaa%2C36fc0bac-1830-42c5-a227-1fb14de96647%2C"}
        self.post(self.url, headers=headers, cookies=cookies)
        self.assertStatusCode(200)

    @file_data("test_data/city.json", key="City")
    def test_10_CabinEquipmentStatus(self, _, req):
        self.url = "https://dss.iuoooo.com/CockpitPc/CabinEquipmentStatus"
        data = {
                "Code": req["code"],
                "OperateType": "00000000-0000-0000-0000-000000000000",
                "AppId": "8151f186-e6f8-4c98-bb73-08163279c740"
                }
        self.post(self.url, json=data)
        num1 = self.response['SCater']['Data']['CabinEquipmentStatus_A'][1]['Num']
        num2 = self.response['SCater']['Data']['CabinEquipmentStatus_A'][2]['Num']
        f = open(r"D:\test001.csv", "a", encoding="UTF-8")
        if num1 is not None and num2 is not None:
            num = num1+num2
            f.write("智慧大数据_设备在线分析_有设备" + "," + req["city"] + "," + str(num) + '\n')
        else:
            f.write("智慧大数据_设备在线分析_有设备" + "," + req["city"] + "," + '0' + '\n')
        f.close()
        self.assertStatusCode(200)

    @file_data("test_data/city.json", key="City")
    def test_11_CabinStoreRanks(self, _, req):
        self.url = "https://dss.iuoooo.com/CockpitMobile/CabinStoreRanks"
        day = time.strftime("%Y/%m/%d", time.localtime())
        data = {
                "Code": req["code"],
                "OperateType": "00000000-0000-0000-0000-000000000000",
                "ModuleIds": "se_equipment_tv,se_equipment_other,se_equipment_glass,se_equipment_no",
                "AppId": "8151f186-e6f8-4c98-bb73-08163279c740",
                "StartTime": "2012/01/01",
                "endTime": day
                }
        self.post(self.url, json=data)
        num = self.response['SCater']['Data']['CabinStoreRanks_A'][0]['num']
        f = open(r"D:\test001.csv", "a", encoding="UTF-8")
        if num is not None:
            f.write("智慧大数据_设备在线分析_无设备" + "," + req["city"] + "," + str(num) + '\n')
        else:
            f.write("智慧大数据_设备在线分析_无设备" + "," + req["city"] + "," + '0' + '\n')
        f.close()
        self.assertStatusCode(200)
