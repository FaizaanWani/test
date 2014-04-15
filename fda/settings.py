# Scrapy settings for fda project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fda'

SPIDER_MODULES = ['fda.spiders']
NEWSPIDER_MODULE = 'fda.spiders'
ITEM_PIPELINES = {
    'fda.pipelines.FdaPipeline': 300,
    
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fda (+http://www.yourdomain.com)'
