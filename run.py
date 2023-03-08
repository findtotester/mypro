import seldom
from seldom import ChromeConfig
from seldom.utils import cache


if __name__ == '__main__':
    cache.clear()
    ChromeConfig.headless = True  # WEB浏览器无界面模式运行
    seldom.main(path="./test_dir/API/chaankang/",
            #    browser="chrome",  # WEB自动化测试（浏览器：chrome）
                base_url="Online",  # API接口测试（正式环境：Online 测试环境：Test）
                app_info=None,  # app自动化测试（appium，opium）
                app_server=None,   # APP自动化测试服务
                report=None,
                title="自动化测试",
                tester="lm",
                description="正式环境查安康测试",
                debug=False,
                rerun=0,
                save_last_run=False,
                language="en",
                timeout=10,
                whitelist=[],
                blacklist=[],  # "slow"
                open=True
    )
