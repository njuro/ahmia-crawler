# -*- coding: utf-8 -*-
"""
In this module, you can find the OnionSpider class.
It's a spider to crawl the tor network.
"""
import requests
from scrapy.linkextractors import LinkExtractor

from .base import WebSpider


class OnionSpider(WebSpider):

    """
    Crawls the tor network.
    """
    name = "ahmia-tor"
    es_index = "tor"
    custom_settings = {
        'ITEM_PIPELINES': {
            'ahmia.pipelines.OnionPipeline': 200
        },
        'ELASTICSEARCH_INDEX': "tor"
    }

    default_start_url = \
        ['http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page',
         'http://tt3j2x4k5ycaa5zt.onion/',
         'http://msydqstlz2kzerdg.onion/address/',
         'http://msydqstlz2kzerdg.onion/add/onionsadded/',
         'https://blockchainbdgpzk.onion/',
         'http://7cbqhjnlkivmigxf.onion/',
         'http://3bbaaaccczcbdddz.onion/discover',
         'http://cb3rob5vwac2dtyc.onion/darknet/']

    url = "http://zlal32teyptf4tvi.onion/?search=&rep=n%2Fa&page="
    for i in range(1, 100):
        default_start_url.append(url + str(i))

    def get_link_extractor(self):
        FAKE_DOMAINS = []
        response = requests.get('https://ahmia.fi/static/fakelist.txt')
        for onion in response.text.split("\n"):
            onion = onion.strip().replace(" ", "")
            if len(onion) is 16:
                FAKE_DOMAINS.append('%s.onion' % onion)

        return LinkExtractor(allow=[r'^http://[a-z2-7]{16}.onion', r'^http://[a-z2-7]{56}.onion'],
                             deny=[r'^https://blockchainbdgpzk.onion/address/',
                                   r'^https://blockchainbdgpzk.onion/tx/'],
                             deny_domains=FAKE_DOMAINS)
