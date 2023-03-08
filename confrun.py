"""
seldom confrun.py hooks function
"""


def browser():
    """
    web UI test:
    browser: gc(google chrome)/ff(firefox)/edge/ie/safari
    """
    return "gc"


def base_url():
    """
    http test
    api base url
    """
    return "http://httpbin.org"

def app_info():
    """
    app UI test
    appium app config
    """
    desired_caps = {
        'deviceName': 'Huawei P40',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '10.0',
        'appPackage': 'com.meizu.flyme.flymebbs',
        'appActivity': '.ui.LoadingActivity',
        'noReset': True,
    }
    return desired_caps


def app_server():
    """
    app UI test
    appium server/desktop address
    """
    return "http://127.0.0.1:4723"


def debug():
    """
    debug mod
    """
    return False


def rerun():
    """
    error/failure rerun times
    """
    return 0


def report():
    """
    setting report path
    Used:
    return "d://mypro/result.html"
    return "d://mypro/result.xml"
    """
    return None


def timeout():
    """
    setting timeout
    """
    return 10


def title():
    """
    setting report title
    """
    return "seldom test report"


def tester():
    """
    setting report tester
    """
    return "bugmaster"


def description():
    """
    setting report description
    """
    return ["windows", "jenkins"]


def language():
    """
    setting report language
    return "en"
    return "zh-CN"
    """
    return "en"


def whitelist():
    """test label white list"""
    return []


def blacklist():
    """test label black list"""
    return []
