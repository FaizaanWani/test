from scrapy.spider import Spider
from scrapy.selector import Selector
from fda.items import FdaItem
from time import strftime,localtime
from scrapy.mail import MailSender
mailer = MailSender()

def send_mail(self, message, title):
    print "Sending mail..........."
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    gmailUser = 'faizaan@trialx.com'
    gmailPassword = '***********'
    recipient = 'shahid@trialx.com'

    msg = MIMEMultipart()
    msg['From'] = gmailUser
    msg['To'] = recipient
    msg['Subject'] = title
    msg.attach(MIMEText(message))

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()
    print "Mail sent"

class DmozSpider(Spider):
    name = "fda"
    allowed_domains = ["fda.gov"]
    start_urls = [
        "http://www.fda.gov/ICECI/EnforcementActions/FDADebarmentList/default.htm",
        
    ]

    def parse(self, response):
        sel = Selector(response)
        # print response.body
        trs  = sel.xpath('//*[@id="middle_js"]/table[2]//tr')
        # items = []
        for tr in trs:
            item = FdaItem()
            item['url'] = response.url
            item['name'] = tr.xpath('td[1]//text()').extract()
            item['eff_date'] = tr.xpath('td[2]//text()').extract()
            item['debarment'] = tr.xpath('td[3]//text()').extract()
            item['fr_date'] = tr.xpath('td[4]//text()').extract()
            item['volume_page'] = tr.xpath('td[5]//@href').extract()
            item['time_stamp'] = strftime("%a, %d %b %Y %H:%M:%S ", localtime())
            yield item
        send_mail("self","Crawler Complete", "Scraper Report")
          