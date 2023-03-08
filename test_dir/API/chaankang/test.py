import seldom
import re
# import numpy as np



class Test(seldom.TestCase):
    def test_01_(self):
        url = 'https://jianguan.iuoooo.com/jc6/api/JForm/findBusinessData?userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=a77a993e-a158-4cd6-bed8-cfbb8285e964&currentOrgId=7035c461-c80e-49ce-a7c8-5584f0453646&appId=9be42759-9686-4541-b5a4-2be15a5c7d73&mainType=&account=18800000064----------&storeId=a5bac1d7-0c0c-4328-8af1-2df7955a0e74&storeAppId=&storeOrgId=&parentAppId=&parentOrgId='
        data_ = {"formId": "2c91c99879843e2b017988fe69273ca9"}
        self.post(url, json=data_)
        designHtml = ''.join(self.jsonpath('$.designHtml'))
        mblConfig = ''.join(self.re_findall('"mblConfig":(.*?),"JumpSettings"',designHtml))
        id = self.re_findall('([(0-9)|(a-z)|(A-Z)]{32})(!?)', mblConfig)
        # id = re.findall('([(0-9)|(a-z)|(A-Z)]{32})(!?)', mblConfig)
        # id_ = str(id[0]).replace(', \'\'', '')
        # id_1 = id_.replace('(', '')
        # id_2 = id_1.replace(')', '')
        # id_3 = id_2.replace('\'', '')
        print("调试：",  id)


        # mblConfig = ''.join(re.findall('"mblConfig":(.*?),"JumpSettings"', designHtml))

        # data_id = ''.join(self.re_findall('"(.*?)":{"jfType":"paragraph"', designHtml))
        # print("调试2：", data_id)
        # id = self.re_findall('"(.*?)":{"jfType":', str(body))
        # print(f"调试：{id}")