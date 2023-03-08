import seldom
from seldom import file_data


class SampleTest(seldom.TestCase):

    def case(self):
        """a simple test case """
        self.open("http://www.itest.info")
        self.assertInUrl("itest.info")


class DDTTest(seldom.TestCase):

    @file_data(file="data.json", key="bing")
    def test_data_driver(self, _, key):
        """ data driver case """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text=key, enter=True)
        self.assertInTitle(key)


if __name__ == '__main__':
    seldom.main(debug=True)

