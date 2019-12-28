import scrapy
import csv


class GetReviewData(scrapy.Spider):
    name = 'get_review_data'
    authors = []
    body = []
    start_urls = ['http://localhost/html/markup.html']

    # this key will be changed every time
    product_handle = "pfotenherzen®-personalisiertes-hundegeschirr"

    status = "published"
    rating = "5"

    def parse(self, response):
        data = response.xpath(
            "//div[@class='main']/div[@class='box']")
        for d in data:
            self.authors.append(
                d.xpath(".//div[@class='block title']/text()").get())
            self.body.append(d.xpath(
                ".//div[@class='block']/div[@class='pre-wrap main-text action']/text()").get())

        with open(self.product_handle + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["product_handle", "state", "rating", "title", "author",
                             "email", "location", "body", "reply", "created_at", "replied_at"])
            for n in range(len(self.authors) + 1):
                fakeEmail = "%s@email.com" % (
                    self.authors[n].lower().replace(" ", ""))
                writer.writerow([self.product_handle, self.status, self.rating, self.authors[n], self.authors[n], fakeEmail, "",
                                 self.body[n], "", "2017-01-09 16:40:12 -0400", ""])
