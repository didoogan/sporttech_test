import json
import os


class Common(object):
    RESULT_DIR = 'result'
    PADDYPOWER_SPIDER_NAME = 'paddypower'
    SKYBET_SPIDER_NAME = 'skybet'
    WILLIAM_HILL_SPIDER_NAME = 'williamhill'

    @classmethod
    def write_result(cls, name, result):
        if not os.path.exists(cls.RESULT_DIR):
            os.makedirs(cls.RESULT_DIR)
        file_name = '{}.json'.format(name)
        with open(os.path.join(cls.RESULT_DIR, file_name), 'w') as f:
            json.dump(result, f)
