import json

import os


class JsonWriterPipeline(object):

    def process_item(self, item, spider):
        path = 'result'
        if not os.path.exists(path):
            os.makedirs(path)
        file_name = spider.name + '.txt'
        with open(os.path.join(path, file_name), 'w') as f:
            json.dump(item, f)
