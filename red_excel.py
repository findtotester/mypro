import seldom
from seldom import file_data


class YouTest(seldom.TestCase):

    #  数据驱动：excle
    @file_data("C:/Users/limm.JINHER/Desktop/data.xlsx", sheet="Sheet1", line=2)
    def test_login(self, city, code):
        """a simple test case """
        print(city)
        print(code)

    #  数据驱动：csv
    @file_data("C:/Users/limm.JINHER/Desktop/data.csv", line=2)
    def test_login2(self, city, code):
        """a simple test case """
        print(city)
        print(code)



