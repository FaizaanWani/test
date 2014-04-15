# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from nameparser.parser import HumanName
import re
class FdaPipeline(object):
    def process_item(self, item, spider):
    	for k in item.keys():
    		if isinstance(item[k],list):
    			item[k] = re.sub(r'\s+',' ',' '.join(item[k])) 
    		elif isinstance(item[k],str):
    			item[k] = item[k]
    	name = HumanName(item["name"])
    	print name.first
    	print name.last
    	print name.middle
    	item["name_first"] = name.first 
    	item["name_last"]  =	name.last
    	item["name_middle"] =  name.middle
        return item
