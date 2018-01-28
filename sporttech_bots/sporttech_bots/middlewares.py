class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://test0:Aexahx2vah7xiegh@35.177.8.95:53128"

