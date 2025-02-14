import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json
"""
it's a script to scrap data on https://zara.com
"""
class ZaraDataScrapper:
    def __init__(self,WishListURL):
        self.WishListURL = WishListURL #whishlist url 
       
    
    def RequestFromContent(self) -> list:
        try:
            content = requests.get(self.WishListURL,headers=Headers(browser="chrome",os="win",headers=True).generate()) #fake headers for to not ban 
            return [content.status_code,content.content]
        except:
            return ["404","Error!"]
    
    def GetAllProducts(self):
        ListOfProducts = ZaraDataScrapper.RequestFromContent(self)
        if ListOfProducts[0] == 200:
            product_list = []
            soup = BeautifulSoup(ListOfProducts[1],"html.parser")
            sourceOne = soup.find("article")
            items = sourceOne.find_all("li")
            for item in items:
                # Product Name
                name = item.find("span", {"data-qa-qualifier": "product-detail-secondary-product-info-name"}).text.strip()
                
                # Product Lİnk
                link = item.find("a", class_="product-link link")["href"]
                
                # Old Price (eğer varsa)
                old_price = item.find("span", class_="price-old__amount")
                old_price = old_price.text.strip() if old_price else "Yok"

                # Current Price
                current_price = item.find("span", class_="price-current__amount")
                current_price = current_price.text.strip() if current_price else "Yok"

                # Stock Status 
                stock_status = item.find("button", class_="zds-button--disabled")
                stock_status = stock_status.text.strip() if stock_status else "Stokta var"

                # Verileri yazdır
                product_data = {
                "name": name,
                "link": link,
                "old_price": old_price,
                "current_price": current_price,
                "stock_status": stock_status}

                # Add to list
                product_list.append(product_data)

                # Save data to JSON file
                with open("zara_products.json", "w") as json_file:
                    json.dump(product_list, json_file, indent=4, ensure_ascii=False)
    
        else:
            with open("zara_products.json","w") as json_file:
                json.dump([{"Error":"Connection Error"}],json_file)

