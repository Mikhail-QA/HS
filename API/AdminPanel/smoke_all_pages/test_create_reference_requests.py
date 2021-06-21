import requests
import allure
from API.setting_tests import LogInfoApi
from API.AdminPanel.smoke_all_pages.credentials import *


# Запрос справки о готовности школы принять ученика
@allure.step
def test_check_status_ok(url, admin):
    check_status_ok = requests.get(
        url + path_admin_schedules,
        headers=admin,
        allow_redirects=False)

    LogInfoApi.log_info(log=check_status_ok)
    assert check_status_ok.status_code == 204
