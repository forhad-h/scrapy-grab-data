import scrapy
import xlsxwriter


class GetReviewData(scrapy.Spider):
    name = 'get_review_data'
    authors = []
    body = []
    review_images = []
    start_urls = ['http://localhost/html/markup.html']

    # Product properties
    product_id = "4467381174358"
    rating = "5"
    approved = "1"
    product_handle = 'fellpflege-handschuh-by-pfotenherzen®'
    product_title = 'FELLPFLEGE HANDSCHUH BY PFOTENLOVER®'
    product_image_url = '//cdn.shopify.com/s/files/1/0278/1685/3590/products/1-Pair-Soft-Efficient-Cleaning-B_300x300.png?v=1576959695'
    columns = ['product_id', 'email', 'rating', 'author', 'title', 'body', 'image',
               'approved', 'created_at', 'product_handle', 'product_title', 'product_image']

    workbook = xlsxwriter.Workbook('product-%s.xlsx' % (product_handle))
    worksheet = workbook.add_worksheet()

    def parse(self, response):

        # grab author name and body text
        box_elms = response.xpath(
            "//div[@class='main']/div[@class='box']")
        for elm in box_elms:
            self.authors.append(
                elm.xpath(".//div[@class='block title']/text()").get())
            self.body.append(elm.xpath(
                ".//div[@class='block']/div[@class='pre-wrap main-text action']/text()").get())

        # grab review image url
        image_elms = response.xpath("//div[@class='grid-item clearfix']")
        for elm in image_elms:
            src = elm.xpath(".//div[@class='item-img box']/img/@src").get()
            url = src if src else ''
            self.review_images.append(url)

        for n in range(len(self.columns)):
            self.worksheet.write(0, n, self.columns[n])

        for n in range(len(self.authors)):
            row = n + 1

            fakeEmail = "%s@email.com" % (
                self.authors[n].lower().replace(" ", ""))
            # Column 1 - Product ID
            self.worksheet.write(row, 0, self.product_id)
            # Column 2 - Email
            self.worksheet.write(row, 1, fakeEmail)
            # Column 3 - Rating
            self.worksheet.write(row, 2, self.rating)
            # Column 4 - Author
            self.worksheet.write(row, 3, self.authors[n])
            # Column 5 - Title
            self.worksheet.write(row, 4, self.authors[n])
            # Column 6 - Body
            self.worksheet.write(row, 5, self.body[n])
            # Column 7 - Image
            self.worksheet.write(row, 6, "https:%s" % self.review_images[n])
            # Column 8 - Approved
            self.worksheet.write(row, 7, self.approved)
            # Column 9 - Created At
            self.worksheet.write(row, 8, "2019-05-18 14:40:43")
            # Column 10 - Product Handle
            self.worksheet.write(row, 9, self.product_handle)
            # Column 11 - Product Title
            self.worksheet.write(row, 10, self.product_title)
            # Column 12 - Product Image URL
            self.worksheet.write(row, 11, self.product_image_url)
        self.workbook.close()
