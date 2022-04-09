from bs4 import BeautifulSoup as soup
import requests
import lxml


class AmzPriceChecker:
    """
    This class checks for price on Amazon.co.uk from a provided link and gets the product price.
    """
    __headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip,deflate",
        "Accept": "text/plain",
        "Charset": "utf-8"
    }

    def __init__(self, product_url):
        """
        :param product_url: Insert URL from Amazon.co.uk website
        """
        self.product_url = product_url
        response = requests.request(method="get", url=self.product_url, headers=self.__headers)
        self.html_text = response.text

    def get_price_from_url(self):
        """
        The method extracts a price in British pounds
        from a given Amazon product URL.
        :return: float type value
        """
        html_data = soup(self.html_text, features="lxml", parser=lxml)
        price = html_data.findAll(class_="a-price-whole") #id="mbc-price-2")
        price = [p.text.strip(" ").strip("£").replace(",", "") for p in price]
        price = float(price[0])
        return price


if __name__ == "__main__":
    link = "https://www.amazon.co.uk/dp/B09JR213KZ/ref=uk_a_macbook_2"
    am = AmzPriceChecker(link)
    print(am.get_price_from_url())