import seldom
from seldom.utils import cache
from seldom.testdata import *
from seldom import depend,if_depend


class Testdianzibiaodanxuncha(seldom.TestCase):
    def start(self):
        self.appid = "9be42759-9686-4541-b5a4-2be15a5c7d73"
        self.storename = '白兔咖啡'
        self.storeid = "a5bac1d7-0c0c-4328-8af1-2df7955a0e74"
        self.storeorgid = "6a0376d0-9196-4792-a2ca-f6b6e2d6fc8b"
        self.operid = "4ffc07ae-4f78-4f73-835f-3d6bdae6b7dc"
        self.userid = "3c73f483-0a2f-4838-b04b-58a2eb64ebd0"
        self.fromid = "2c91c99879843e2b017988fe69273ca9"
        self.designId = "2c91c87479a3f3430179a667fc011530"

    def test_01_getStoreDetailConfig(self):
        url = 'https://patrol.iuoooo.com/api/ModuleLayOutDetail/getStoreDetailConfig'
        data_ = {
                "configPara": {
                    "appId": self.appid,
                    "storeId": self.storeid,
                    "storeState": "170",
                    "versionType": 1,
                    "operId": self.operid
                }
            }
        self.post(url, json=data_)
        try:
            self.assertStatusCode(200)
            alias = self.jsonpath('$..alias')
            if "电子表单巡查" not in alias:
                raise AssertionError
            if "电子巡查" not in alias:
                raise AssertionError
        except AssertionError as e:
            raise e

    def test_02_GetMapStoreBase(self):
        url = 'https://patrol.iuoooo.com/api/StoreDetail/GetMapStoreBase'
        data_ = {
                "storeId": self.storeid,
                "lng": "0",
                "lat": "0",
                "equipmentStatus": "1"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    def test_03_getStoreDetailInfoIncludeCommentsTwo(self):
        url = 'https://patrol.iuoooo.com/api/StoreQuery/getStoreDetailInfoIncludeCommentsTwo'
        data_ = {
                "getStoreDetailInfoSearchDTO": {
                    "appId": self.appid,
                    "storeId": self.storeid,
                    "lng": "101.723320",
                    "lat": "37.379780",
                    "userId": self.userid,
                    "shopAppId": self.storeid
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "获取成功")

    def test_04_getappform(self):
        url = 'https://ripx.iuoooo.com/api/appform/getappform'
        data_ = {
                "appId": self.appid,
                "typeId": "1"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")

    def test_05_findBusinessData(self):
        formid = self.jmespath("Content.FormId")
        if formid is False or formid is None:
            formid = self.fromid
        url = f'https://jianguan.iuoooo.com/jc6/api/JForm/findBusinessData?userId={self.userid}&sessionId=a77a993e-a158-4cd6-bed8-cfbb8285e964&currentOrgId=7035c461-c80e-49ce-a7c8-5584f0453646&appId={self.appid}&mainType=&account=18800000064&storeId={self.storeid}&storeAppId=&storeOrgId={self.storeorgid}&parentAppId={self.appid}&parentOrgId={self.storeorgid}&roleName=%E8%BD%A6%E8%BE%86%E7%AE%A1%E7%90%86%E5%91%98'
        data_ = {"formId": formid}
        self.post(url, json=data_)
        design_id = self.jsonpath('$..designId')
        if design_id is False or design_id is None:
            design_id = self.designId
        cache.set({"design_id": design_id})

    def test_06_getDataSourceFieldListController(self):
        url = f'https://jianguan.iuoooo.com/jc6/api/JForm/getDataSourceFieldListController?userId={self.userid}&sessionId=a77a993e-a158-4cd6-bed8-cfbb8285e964&currentOrgId=7035c461-c80e-49ce-a7c8-5584f0453646&appId={self.appid}&mainType=&account=18800000064&storeId={self.storeid}&storeAppId=&storeOrgId={self.storeorgid}&parentAppId={self.appid}&parentOrgId={self.storeorgid}&userName=%E4%B8%93%E6%A3%80&roleName=%E8%BD%A6%E8%BE%86%E7%AE%A1%E7%90%86%E5%91%98'
        data_ = {
                "datasourceId": "mendianzhuanyongshujuyuan123456"
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    def test_07_saveBusiness2point0(self):
        result_business_id = get_uuid("-").upper()
        cache.set({"result_business_id": result_business_id})
        url = f'https://jianguan.iuoooo.com/jc6/api/JForm/saveBusiness2point0?userId={self.userid}&sessionId=a77a993e-a158-4cd6-bed8-cfbb8285e964&currentOrgId=7035c461-c80e-49ce-a7c8-5584f0453646&appId={self.appid}&mainType=&account=18800000064&storeId={self.storeid}&storeAppId=&storeOrgId=&parentAppId=&parentOrgId=&userName=%E4%B8%93%E6%A3%80'
        data_ = {
                "businessId": result_business_id,
                "designId": "2c91c87479a3f3430179a667fc011530",
                "formData": [{
                    "14a42c7b0cef435a960f1955df528322": [{
                        "title": "白兔咖啡",
                        "businessId": "A5BAC1D7-0C0C-4328-8AF1-2DF7955A0E74",
                        "tradeId": "4FFC07AE-4F78-4F73-835F-3D6BDAE6B7DC"
                    }]
                }, {
                    "1727d0c9468b45239a7568f3faad3cc0": [{
                        "userId": "3c73f483-0a2f-4838-b04b-58a2eb64ebd0",
                        "userName": "专检"
                    }]
                }, {
                    "93e17d43691d4751ad2a00037e479dff": get_strftime(get_now_datetime(True), "%Y-%m-%d %H:%M")
                }, {
                    "879c461fabe44e919d084063a091656e": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用"
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖"
                        }],
                        "curr": {
                            "key": "否",
                            "name": "否",
                            "score": 0
                        }
                    }
                }, {
                    "d57cefff22b14e5488346b70813614d5": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用"
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖"
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "43aeceaf9ab14951ab42b158155ab378": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "42c2f21d4a67410b9cfc62747b9e1bc8": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "37acb7eef04643a7bc000c2a16cb0716": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "3c2668d77eb94bb1b4b28bcf07b2f753": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "63d8636720e84cb3b5057eb1fd6a180c": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "a186fb755747485391371860562b863d": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "1a1e3fbce21f4d3fbffc0f57b4ab13e1": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "7fcbc1a26f4f4c779a218ce77beb4262": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "2a25020bf2e744e1bff94cb21dea1b16": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "e64c03a7aed84a088f2472bc552c58fc": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "ad7d963c8dfe414b9684a65aedea5c98": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "149c57b6fb0d43418791889baf31bfe1": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "34f708f173544e04822be2d108532ad4": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "9f1b9678e75643358e2322fad12420ea": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "54c898b59d6e4e37b30c9e1b399e2544": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "daf3b114a71d4ebaa19cbeb5b649ccbe": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "3cf3d11627ff4aa0b599e4b496929b5f": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "ee7a4994cb374fa09bc8963e9dada86f": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "c3a7b1bef23d401b9d56f3bb8ea19e37": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "322e379dcefd45cdba7f7d1bdd8c916e": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "7fb15b8177f94d788e918b98107fe4dd": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "40df0440aa084fd7ae78d88f94312ca1": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "c62789cd44984f5b8fbca4d57c1bb2a0": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "e0cb81505a854d00a75222afabb319d3": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "2b2914eb4109450c972d93e19214f7d9": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "0a89c34336fd40f682ddeeedc5295e44": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "055598768f5e4c5ca7563bb52ab181fa": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "d34c46a2343d451186cda91bb4d71d44": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "71ee6ccbd076481ca487b2edb317831a": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "6f768a27c0e84ff0ad9d0adc3e43e8e7": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "8ec804f70a634a28bc059f08773ff4be": {
                        "photo": [],
                        "allOps": [{
                            "key": "是",
                            "name": "是",
                            "selected": False
                        }, {
                            "key": "否",
                            "name": "否",
                            "selected": False
                        }, {
                            "key": "不适用",
                            "name": "不适用",
                            "selected": False
                        }, {
                            "key": "视频未覆盖",
                            "name": "视频未覆盖",
                            "selected": False
                        }],
                        "curr": {
                            "key": "",
                            "name": "请选择"
                        }
                    }
                }, {
                    "07da0da7a47e438984172c0e0b85d862": 1
                }, {
                    "076b5c92497f404a98a51af84caea943": 1
                }, {
                    "16d3d32198c94cf1a1a8d068d047de8b": 1
                }, {
                    "40757752fcf54b39b853177584a6e484": {
                        "value": "不符合",
                        "text": "不符合"
                    }
                }, {
                    "8b868a3ed6974f8aac6c4dd03953cb3e": {
                        "value": "限期整改",
                        "text": "限期整改"
                    }
                }, {
                    "292b6b9318d24f24bf2b0ea330f2f32d": {
                        "value": "需要",
                        "text": "需要"
                    }
                }, {
                    "c01169a9e9944b3397afb9b51e1495c9": {
                        "hasImg": True,
                        "imageId": "c01169a9e9944b3397afb9b51e1495c9",
                        "src": "https://fileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d/2023022710/da091f2c3c0143bb940b527d4e6a8044_15cc9943d8af386c429817deb1.png",
                        "realUrl": "https://fileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d/2023022710/da091f2c3c0143bb940b527d4e6a8044_15cc9943d8af386c429817deb1.png",
                        "name": "ea681215cc9943d8af386c429817deb1.png",
                        "username": "专检",
                        "uploadTime": get_custom_data("d")
                    }
                }],
                "uploadIds": ["c01169a9e9944b3397afb9b51e1495c9"],
                "insertFlag": True,
                "storeId": self.storeid,
                "appId": self.appid,
                "userId": self.userid,
                "orgId": "7035c461-c80e-49ce-a7c8-5584f0453646",
                "formId": self.fromid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    """原生代办整改"""
    def test_09_GetAllWorkList(self):  # 查安康上做任务
        self.sleep(5)
        url = 'https://layouts-task.iuoooo.com/api/Work/GetAllWorkList'
        data_ = {
            "AppId": self.appid,
            "OrgId": self.storeorgid,
            "QueryDate": get_date(),
            "RoleName": "管理员",
            "RoleTypeClient": 2,
            "StoreId": self.storeid,
            "StoreOrgId": self.storeorgid,
            "UserId": self.userid
        }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        BusinessId_daiban = self.jsonpath('$..[?(@.Name=="网上巡查整改任务" && @.WorkStatus == 0)].BusinessId')
        taskId_daiban = self.jsonpath('$..[?(@.Name=="网上巡查整改任务" && @.WorkStatus == 0)].SourceId')
        WorkId_daiban = self.jsonpath('$..[?(@.Name=="网上巡查整改任务" && @.WorkStatus == 0)].WorkId')
        print(BusinessId_daiban)
        if BusinessId_daiban is None or BusinessId_daiban is False:
            Testdianzibiaodanxuncha.test_09_GetAllWorkList = False
        else:
            cache.set({"BusinessId_daiban": BusinessId_daiban})
            cache.set({"taskId_daiban": taskId_daiban})
            cache.set({"WorkId_daiban": WorkId_daiban})

    def test_10_getFieldInfo2(self):
        BusinessId_daiban = cache.get("BusinessId_daiban")
        uir = 'https://jianguan.iuoooo.com/jc6/api/Layout/getFieldInfo2'
        data_ = {"formId": BusinessId_daiban[0]}
        self.post(uir, json=data_)
        self.assertStatusCode(200)
        self.assertPath("message", "success")
        id_temp = self.jmespath("data[0].id")
        cache.set({"id_temp": id_temp})

    def test_11_getCheckControl(self):
        result_business_id = cache.get("result_business_id")
        print(f"调试1:{result_business_id}")
        url = 'https://jianguan.iuoooo.com/jc6/api/JForm/getCheckControl'
        data_ = {
                "check": {
                    "businessId":  result_business_id,
                    "fields": ["879c461fabe44e919d084063a091656e", "d57cefff22b14e5488346b70813614d5", "43aeceaf9ab14951ab42b158155ab378", "42c2f21d4a67410b9cfc62747b9e1bc8", "37acb7eef04643a7bc000c2a16cb0716", "63d8636720e84cb3b5057eb1fd6a180c", "a186fb755747485391371860562b863d", "1a1e3fbce21f4d3fbffc0f57b4ab13e1"],
                    "formId": "2c91c99879843e2b017988fe69273ca9"  # 录入表单
                },
                "rectification": {
                    "businessId": "",
                    "fields": ["9b1f28aca7a947c8a40789d0551cad67", "33236ffd5dd04302a13523ce694e060c", "bf3f86f3c20b4601a41ea8d3b416d1b6", "a5a7f20cfb5c4300851cdfd3f93eaada", "6539b9f3535c420ca57ffb77f0dea82f", "7d4dec0d72fe464696d17002b50f72d6", "391be364226e4be9b38a330ccb95cbba", "f11f2b7c0f344ad69b998e0e5d455db5"],
                    "formId": "2c91c99879843e2b017988fe69273cae"   #整改表单
                }
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)

    @depend("test_10_getFieldInfo2")
    def test_12_OperateSubmitFormInfo(self):  # 提交整改
        id_temp = cache.get("id_temp")
        taskId_daiban = cache.get("taskId_daiban")
        WorkId_daiban = cache.get("WorkId_daiban")
        url = 'https://layouts-task.iuoooo.com/api/FormOperate/OperateSubmitFormInfo'
        data_ = {
                "ExecutorName": "API",
                "RrtNumber": 1,
                "appId": self.appid,
                "formData": [{
                    id_temp[0]: {
                        "CheckImgList": [],
                        "Rectification": [{
                            "isImage": True,
                            "isVideo": True,
                            "lat": 40.055239,
                            "lng": 116.303022,
                            "name": "任务图片",
                            "url": "https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d%2F2023022710%2F71c4532a0f794f12a2a9f847200a061b_23f-449b-b916-3907e69b6fd2.png"
                        }],
                        "rectification": [{
                            "isImage": True,
                            "isVideo": True,
                            "lat": 40.055239,
                            "lng": 116.303022,
                            "name": "任务图片",
                            "url": "https://upfileserver.iuoooo.com/Jinher.JAP.BaseApp.FileServer.UI/FileManage/GetFile?fileURL=29e54e46-3e17-4ca4-8f03-db71fb8f967d%2F2023022710%2F71c4532a0f794f12a2a9f847200a061b_23f-449b-b916-3907e69b6fd2.png"
                        }]
                    }
                }],
                "formId": "2c91c99879843e2b017988fe69273cae",
                "insertFlag": True,
                "orgId": self.storeorgid,
                "storeId": self.storeid,
                "taskId": taskId_daiban[0],
                "uploadIds": [],
                "userId": self.userid,
                "userType": "B",
                "workId": WorkId_daiban[0],
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Message", "操作成功")
        # result_business_id = self.response['Data']
        # print("调试3：", result_business_id)
        # cache.set({"result_business_id": result_business_id})

    @depend("test_12_OperateSubmitFormInfo")
    def test_13_GetJinherEnergyAds(self):
        taskId_daiban = cache.get("taskId_daiban")
        url = 'https://dsapi.iuoooo.com/adm/api/AdComponent/GetJinherEnergyAds'
        data_ = {
                "IsAnon": False,
                "UserId": self.userid,
                "AreaCode": "3-110108",
                "PageIndex": 1,
                "ClientType": "android",
                "taskId": taskId_daiban[0],
                "AppVersion": "6.309.1121",
                "Device_Model": "ANA-AN00",
                "StoreId": self.storeid,
                "RoleName": "管理员",
                "AppId": self.appid,
                "Device_Info": "12",
                "PhoneBrand": "HUAWEI",
                "PhoneModel": "ANA-AN00",
                "ProductType": 74,
                "PageSize": 100,
                "FromAppId": self.appid
            }
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("IsAutoPlayAble", True)
        cache.clear("taskId_daiban")
        cache.clear("id_temp")
        cache.clear("WorkId_daiban")
        cache.clear("result_business_id")
        cache.clear("BusinessId_daiban")
        cache.clear("design_id")

