path_admin_schedules = '/schedules?grade=10&school=true&'


def __init__(self, token=None):
    self.token = token


def get_token(self):
    headers_user = {
        "Authorization": self.access_token,
    }
    return headers_user
