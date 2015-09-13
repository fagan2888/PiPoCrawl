# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PipocrawlPipeline(object):

    def process_item(self, item, spider):
        replaceable = {u"\r": u"", u"\n": u" ", u"\t": u"", u"\xa0": u""}
        for i, j in replaceable.items():
            item['date'] = item['date'].replace(i, j)
            item['description'][0] = item['description'][0].replace(i, j)
            item['title'][0] = item['title'][0].replace(i, j)
        return item
