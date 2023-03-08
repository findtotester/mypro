import seldom
from seldom import  data
import re
from seldom.utils import cache
from seldom import depend
import json


class Testyunyingjiashicang(seldom.TestCase):
    # 驾驶舱首页
    def test_01_cockpit_html(self):
        url = "https://dss.iuoooo.com/Html/Hamster/cockpit/cockpit.html?curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&jhWebView=1&orgId=ab9d121e-0145-41d8-b787-460480290d42&shopOrgId=&isLogin=1&hidjhnavigation=1&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&roleName=%E5%B7%A1%E6%9F%A5%E5%91%98&account=18800000064&relationOId=ab9d121e-0145-41d8-b787-460480290d42"
        self.get(url)
        self.assertStatusCode(200)

    @depend("test_01_cockpit_html")
    def test_02_MobileView(self):
        data = self.response
        id = self.re_findall('protamplateId: \'(.*?)\' // 正式环境', str(data))
        for templateId in id:
            url = f"https://dss.iuoooo.com/html/Hamster/MobileView/#/?templateId={templateId}&userId=3c73f483-0a2f-4838-b04b-58a2eb64ebd0&sessionId=9f900416-882b-4996-9956-d944e3c6f74c&orgId=ab9d121e-0145-41d8-b787-460480290d42&appId=2fd5f092-d360-4783-b95c-6d47ee5cac44&changeOrg=ab9d121e-0145-41d8-b787-460480290d42&curChangeOrg=ab9d121e-0145-41d8-b787-460480290d42&account=18800000064&hidjhnavigation=1&jhWebView=1&newpage=1&cockpit=1"
            self.get(url)
            self.assertStatusCode(200)


    def test_03_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id": "3a01cdd4-a700-474b-a6d1-5950c6b2a67a"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "运营驾驶舱-用户分析")

    def test_04_Getsp_Layout_GetUpdateTime(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_Layout_GetUpdateTime?id=17&prc_name=sp_rpt_app_insert_guozh_20200224&PrjName=%E8%BF%90%E8%90%A5%E9%A9%BE%E9%A9%B6%E8%88%B1"
        data_ = {"Code": "", "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.detail[0].PrjName", "运营驾驶舱")

    def test_05_UserAnalysis_DAU(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_YY_ChaAnKang_UserAnalysis_DAU"
        data_ = {"Code": "", "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_06_DAU_Last30days(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_YY_ChaAnKang_UserAnalysis_DAU_Last30days"
        data_ = {"Code": "", "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_07_DAU_ByProvince(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_YY_ChaAnKang_UserAnalysis_DAU_ByProvince"
        data_ = {"Code": "", "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_07_DAU_ByCity(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_YY_ChaAnKang_UserAnalysis_DAU_ByCity"
        data_ = {"Code": "", "AppId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 主体情况

    def test_09_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id": "b428e813-6e58-4bf5-aa66-370840dd0820"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "运营驾驶舱-主体情况")

    def test_10_GetHamsterArea(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterArea"
        data_ = {"appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44", "areaCode": None}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_11_GetHamsterArea(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterArea"
        data_ = {"appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44", "areaCode": "0-000000"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_12_AnKangReport_StoreNum(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_Layout_AnKangReport_StoreNum?cockpit=1"
        data_ = {"appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44", "Code": "0-000000"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.r1[0].Name", "主体总数")

    def test_13_AnKangReport_EnterStoreLine30d(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_Layout_AnKangReport_EnterStoreLine30d"
        data_ = {"appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44", "Code": "0-000000"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_14_AnKangReport_AreaStoreRank(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_Layout_AnKangReport_AreaStoreRank"
        data_ = {"appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44", "Code": "0-000000"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)
    # 自查情况


    def test_16_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id": "9c54fe0a-001e-4670-9f8e-8c31e09be370"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "运营驾驶舱-自查情况")


    def test_18_AnKangReport_TaskStoreNum(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_Layout_AnKangReport_TaskStoreNum?cockpit=1"
        data_ = {"Code": "", "appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.r1[0].Name","自查主体数")

    def test_19_AnKangReport_FinishStoreLine30d(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_Layout_AnKangReport_FinishStoreLine30d"
        data_ = {"Code": "", "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_20_AnKangReport_FinishUserLine30d(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_Layout_AnKangReport_FinishUserLine30d"
        data_ = {"Code": "", "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_21_AnKangReport_FinishTaskLine30d(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_Layout_AnKangReport_FinishTaskLine30d"
        data_ = {"Code": "", "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_22_AnKangReport_AreaFinishTaskRank(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_AreaFinishTaskRank"
        data_ = {"Code": "", "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_23_AnKangReport_AreaFinishRateRank(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_Layout_AnKangReport_AreaFinishRateRank"
        data_ = {"Code": "", "appId": "2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 合伙人情况
    def test_25_GetHamsterReportManageById(self):
        url = "https://hamster.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id": "67789130-2acc-47ea-a0cc-1d96a737b938"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)
        # Show = re.findall('"shapeType":(.*?),', str(self.response))
        # id = re.findall('true,"Id":"(.*?)","isShow"', str(self.response))

    def test_25_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"tableName":"mp.original_app_partner_stats","x":{},"y":[{"columnName":"ytd_performance_amount","calcType":"1","whereData":[{"columnName":"","columnVal":"","operator":""}]},{"columnName":"total_performance_amount","calcType":"1","whereData":[{"columnName":"","columnVal":"","operator":""}]}],"shapeType":1,"whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"id":"4b235462-2e6e-4295-bc29-a47e00f27ff9"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    def test_26_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"tableName":"mp.original_app_partner_stats","x":{},"y":[{"columnName":"ytd_commission_amount","calcType":"1","whereData":[{"columnName":"","columnVal":"","operator":""}]},{"columnName":"total_commission_amount","calcType":"1","whereData":[{"columnName":"","columnVal":"","operator":""}]}],"shapeType":1,"whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"id":"8458f81f-ece8-4254-8286-5aba27b8e564"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    def test_27_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"tableName":"mp.original_app_partner_stats","x":{},"y":[{"columnName":"ytd_increase_partner_count","calcType":"1","whereData":[{"columnName":"","columnVal":"","operator":""}]},{"columnName":"total_partner_count","calcType":"1","whereData":[{"columnName":"","columnVal":"","operator":""}]}],"shapeType":1,"whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"id":"509986ac-3b3d-417d-9668-ee8d727ce8aa"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    def test_28_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"tableName":"mp.original_app_partner_stats","x":{},"y":[{"columnName":"ytd_order_count","calcType":"1","whereData":[{"columnName":"","columnVal":"","operator":""}]},{"columnName":"total_order_count","calcType":"1","whereData":[{"columnName":"","columnVal":"","operator":""}]}],"shapeType":1,"whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"id":"b6eb47c3-2e3b-4ef9-af6b-8b9054993760"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    def test_29_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"id":"f0e6b989-ded0-482c-b0ad-db8227051ebf","whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"StoreIsolation":{"enabled":False,"appIdVal":"","appIdColumn":""},"tableName":"mp.original_app_partner_tendency_30d","shapeType":4,"xArr":[{"columnName":"day_id","order":"asc","fieldType":"string"}],"y":[{"columnName":"today_performance_amount","calcType":"1","whereData":[],"order":""}]}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    def test_30_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"id":"63c853bf-d146-4fff-aec2-a4dd52bb0ae3","whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"StoreIsolation":{"enabled":False,"appIdVal":"","appIdColumn":""},"tableName":"mp.original_app_partner_tendency_30d","shapeType":4,"xArr":[{"columnName":"day_id","order":"asc","fieldType":"string"}],"y":[{"columnName":"today_increase_partner_count","calcType":"1","whereData":[],"order":""}]}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    def test_31_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"id":"eeea3fc0-62c0-4c86-92cf-2694ec399862","whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"StoreIsolation":{"enabled":False,"appIdVal":"","appIdColumn":""},"tableName":"mp.original_app_partner_tendency_30d","shapeType":4,"xArr":[{"columnName":"day_id","order":"asc","fieldType":"string"}],"y":[{"columnName":"today_order_count","calcType":"1","whereData":[],"order":""}]}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    def test_32_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"id":"d2e8ea9b-8036-45e2-a0f7-9ec7984e2117","whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"StoreIsolation":{"enabled":False,"appIdVal":"","appIdColumn":""},"code":"","tableName":"mp.original_app_partner_rank","shapeType":2,"x":{"columnName":"partner_name","order":"","fieldType":"string","hiddenColumnName":""},"y":[{"columnName":"subordinate_partner_count","calcType":"1","whereData":[],"order":"desc"}]}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    def test_33_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"id":"d2e8ea9b-8036-45e2-a0f7-9ec7984e2117","whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"StoreIsolation":{"enabled":False,"appIdVal":"","appIdColumn":""},"code":"","tableName":"mp.original_app_partner_rank","shapeType":2,"x":{"columnName":"partner_name","order":"","fieldType":"string","hiddenColumnName":""},"y":[{"columnName":"performance_amount","calcType":"1","whereData":[],"order":"desc"}]}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    def test_34_CalcLine(self):
        url = "https://hamster.iuoooo.com/CockpitPc/CalcLine"
        data_ = {"id":"d2e8ea9b-8036-45e2-a0f7-9ec7984e2117","whereData":[],"app":{"enabled":False,"appIdColumn":"","appIdVal":""},"StoreIsolation":{"enabled":False,"appIdVal":"","appIdColumn":""},"code":"","tableName":"mp.original_app_partner_rank","shapeType":2,"x":{"columnName":"partner_name","order":"","fieldType":"string","hiddenColumnName":""},"y":[{"columnName":"commission_amount","calcType":"1","whereData":[],"order":"desc"}]}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Msg", None)

    # 冷链情况
    def test_35_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"a20e66ae-eb34-43a1-ad11-ecd3344be599"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "运营驾驶舱-冷链情况")


    def test_37_AnKangReport_XJColdChainInfo(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_XJColdChainInfo?cockpit=3"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.r1[0].Name", "冷链表单提交总数")

    def test_38_AnKangReport_XJColdChainStore30d(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_XJColdChainStore30d"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_39_AnKangReport_XJColdChainSubmit30d(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_XJColdChainSubmit30d"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 培训情况
    def test_40_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"16b6d9ed-5633-477f-b154-a4e8350fba98"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "运营驾驶舱-培训情况")


    def test_42_AnKangReport_TrainingLearningPlan(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_TrainingLearningPlan?type=1&cockpit=5"
        data_ = {"Code":"","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.r1[0].Name", "课程数")

    def test_43_AnKangReport_TrainingLearning(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_TrainingLearningPlan?type=2"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","type":"2"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_44_AnKangReport_TrainingLearningPlan(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_TrainingLearningPlan?type=3"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","type":"3"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 考试情况
    def test_45_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"96b67425-09ff-4a1e-9698-0005ecac3c40"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "运营驾驶舱-考试情况")


    def test_47_AnKangReport_ExamUserNum(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_ExamUserNum?cockpit=4"
        data_ = {"Code":"","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.r1[0].Name", "考题数")

    def test_48_AnKangReport_ExamUserLine30d(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_ExamUserLine30d"
        data_ = {"Code":"","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_49_AnKangReport_ExamAreaUserRank(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Layout_AnKangReport_ExamAreaUserRank"
        data_ = {"Code":"","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 考试情况
    def test_50_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"1f45e8da-1ce9-4696-952e-eac5a5070682"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "运营驾驶舱-发烧药登记")


    def test_52_AnKangReport_Index(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Medicine_AnKangReport_Index?cockpit=1"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.r1[0].Name", "药品登记门店数")

    def test_53_AnKangReport_Rank(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_Medicine_AnKangReport_Rank"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 智能硬件销售
    def test_54_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"25ac56f5-6fc5-4760-8fca-1b18955b16a3"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "智能硬件销售0917-01")


    def test_56_Getsp_em_intelligentDevice_Index(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_em_intelligentDevice_Index?cockpit=6"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.r0[0].Name", "本年交易总金额")

    def test_57_Getsp_em_intelligentDevice_orderPrice_byday(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_em_intelligentDevice_orderPrice_byday"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_58_Getsp_em_intelligentDevice_orderCount_byday(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_em_intelligentDevice_orderCount_byday"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_59_Getsp_em_intelligentDevice_platformSale_byYear(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_em_intelligentDevice_platformSale_byYear"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_60_Getsp_em_intelligentDevice_platformSale_byDay(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_em_intelligentDevice_platformSale_byDay"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_61_Getsp_em_intelligentDevice_commoditySalePrice_byYear(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_em_intelligentDevice_commoditySalePrice_byYear"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 安康汇情况
    def test_62_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"5066d613-bcdc-4438-a74e-785ba9ff2d79"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "运营驾驶舱-安康汇情况")


    def test_64_AnKangHui_Index(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_YY_ChaAnKang_AnKangHui_Index?cockpit=2"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_65_AnKangHui_orderCount_byday(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_YY_ChaAnKang_AnKangHui_orderCount_byday"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_66_AnKangHui_commoditySalePrice(self):
        url = "https://dss.iuoooo.com/Cockpitmobile/Getsp_YY_ChaAnKang_AnKangHui_commoditySalePrice"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_67_AnKangHui_commodityPV(self):
        url = "https://tdss.iuoooo.com/Cockpitmobile/Getsp_YY_ChaAnKang_AnKangHui_commodityPV"
        data_ = {"Code":"","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 地方馆DAU
    def test_68_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"4b127ca1-293e-41f0-9345-a4932b53e49f"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "按DAU排名")


    def test_72_sp_Layout_DauRank_ByApp_TopIndex(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_DauRank_ByApp_TopIndex&GroupType=0"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_DauRank_ByApp_TopIndex","GroupType":"0"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.r0[0].Name", "DAU总数")
        Diff = self.jsonpath('$..Diff')
        Num = self.jsonpath('$..Num')
        print(Diff, Num)

    def test_73_sp_Layout_DauRank_ByApp_Tendency(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_DauRank_ByApp_Tendency&GroupType=0"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_DauRank_ByApp_Tendency","GroupType":"0"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_74_sp_Layout_DauRank_BelowIndex(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_DauRank_BelowIndex"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_DauRank_BelowIndex"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 摄像头数量分析
    def test_75_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"d083fef8-3690-43d2-b5c1-de596aa37984"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "设备数量分析")

    def test_79_sp_Layout_CameraAnalysis_TopIndex(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_CameraAnalysis_TopIndex"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_CameraAnalysis_TopIndex"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)
        Diff = self.jsonpath('$..Diff')
        Num = self.jsonpath('$..Num')
        print(Diff, Num)

    def test_80_sp_Layout_CameraAnalysis_Tendency(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_CameraAnalysis_Tendency"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_CameraAnalysis_Tendency"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_81_sp_Layout_CameraAnalysis_Tendency(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_CameraAnalysis_BelowIndex"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_CameraAnalysis_BelowIndex"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 特种设备分析
    def test_82_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"1a903fd9-1d77-4b39-b683-bae98b037212"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "特种设备数量分析")

    def test_86_sp_Layout_SpecEquipReport_Top(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_SpecEquipReport_Top"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_SpecEquipReport_Top"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_87_sp_Layout_SpecEquipReport_Line(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_SpecEquipReport_Line"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_SpecEquipReport_Line"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_88_sp_Layout_SpecEquipReport_AreaRank(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_SpecEquipReport_AreaRank"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_SpecEquipReport_AreaRank"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_89_sp_Layout_SpecEquipReport_Rank(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_SpecEquipReport_Rank"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_SpecEquipReport_Rank"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 消防数量分析
    def test_90_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"5e7a53e9-fdad-460f-b839-9222236477a1"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "消防数量分析1")

    def test_91_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"5e7a53e9-fdad-460f-b839-9222236477a1"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "消防数量分析1")

    def test_91_sp_Layout_FireControl_Top(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_FireControl_Top"
        data_ = {"id":"5e7a53e9-fdad-460f-b839-9222236477a1"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_92_sp_Layout_FireControl_Line(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_FireControl_Line"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_FireControl_Line"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_93_sp_Layout_FireControl_AreaRank(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_FireControl_AreaRank"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_FireControl_AreaRank"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_94_sp_Layout_FireControl_LabelRank(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_FireControl_LabelRank"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_FireControl_LabelRank"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 农贸市场分析
    def test_95_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"e0fd8f75-f122-4f92-96ee-44f1f6fd8a57"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "农贸市场分析1")

    def test_96_sp_Layout_FarmMarket_Top(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_FarmMarket_Top"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_FarmMarket_Top"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_97_sp_Layout_FarmMarket_Line(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_FarmMarket_Line"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_FarmMarket_Line"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_98_sp_Layout_FarmMarket_AreaRank(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_FarmMarket_AreaRank"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_FarmMarket_AreaRank"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 物联设备统计
    def test_99_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"725fe27a-7774-4c19-8ff3-d44fa370beb7"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "物联设备统计1")

    def test_100_sp_Layout_IntelligentDevice_TopIndex(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_IntelligentDevice_TopIndex"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_IntelligentDevice_TopIndex"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_101_sp_Layout_IntelligentDevice_TopIndex(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_IntelligentDevice_Tendency"
        data_ = {"Code":"0-000000","AppId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_IntelligentDevice_Tendency"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_102_sp_Layout_IntelligentDevice_TypeIndex(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_IntelligentDevice_TypeIndex"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_IntelligentDevice_TypeIndex"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_103_sp_Layout_IntelligentDevice_RegionIndex(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_IntelligentDevice_RegionIndex"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_IntelligentDevice_RegionIndex"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_104_sp_sp_Layout_IntelligentDevice_OperateIndex(self):
        url = "https://dss.iuoooo.com/CockpitMobile/getsp_data?SpName=sp_Layout_IntelligentDevice_OperateIndex"
        data_ = {"Code":"0-000000","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44","SpName":"sp_Layout_IntelligentDevice_OperateIndex"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    # 物联设备统计
    def test_105_GetHamsterReportManageById(self):
        url = "https://dss.iuoooo.com/CockpitPc/GetHamsterReportManageById"
        data_ = {"id":"67e01821-7c58-4ae5-bfb9-f67fd300c4e6"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Data.Name", "运营驾驶舱-正能量情况")

    def test_104_Getsp_YY_ChaAnKang_EnergyAnalysis_Money(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_YY_ChaAnKang_EnergyAnalysis_Money?cockpit=1"
        data_ = {"Code":"","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)

    def test_104_Getsp_YY_ChaAnKang_EnergyAnalysis_ConsumptionMoney_ByDay(self):
        url = "https://dss.iuoooo.com/CockpitMobile/Getsp_YY_ChaAnKang_EnergyAnalysis_ConsumptionMoney_ByDay"
        data_ = {"Code":"","appId":"2fd5f092-d360-4783-b95c-6d47ee5cac44"}
        self.post(url, json=data_)
        self.assertStatusCode(200)
        self.assertPath("Success", True)
