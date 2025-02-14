import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem,QLineEdit
import appFeature.zaraReq
import json
import os 
if(os.path.isfile("zara_products.json")):
    os.remove("zara_products.json")
class ZaraScraperApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zara Wishlist Scraper")
        self.setGeometry(300, 300, 500, 400) 

        layout = QVBoxLayout()

        # URL Input Field
        self.label = QLabel("Enter Zara Wishlist URL:")
        layout.addWidget(self.label)

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Paste your Zara wishlist URL here...")
        layout.addWidget(self.url_input)

        # Fetch Button
        self.fetch_button = QPushButton("Fetch Products")
        self.fetch_button.clicked.connect(self.fetch_products)  # Burada fetch_products fonksiyonuna bağlandık
        layout.addWidget(self.fetch_button)

        # Product List
        self.product_list = QListWidget()
        layout.addWidget(self.product_list)
        self.setLayout(layout)

    def fetch_products(self):
        # Burada, URL'yi alıp verileri işleyen kodu yazabilirsin.
        url = self.url_input.text()
        # Örneğin, ZaraDataScrapper'dan veriyi almak gibi bir işlem olabilir.
        appFeature.zaraReq.ZaraDataScrapper(url).GetAllProducts()
        with open("zara_products.json",'r',encoding='utf-8') as file :
            data=json.load(file)
           

            for product in data:
                link = product.get("link")
                status = product.get("stock_status")
                name = product.get("name", "Unknown Product")
                current_price = product.get("current_price", "Price not available")
                old_price = product.get("old_price", "Old price not available")
                                # Ürün metnini oluştur
                display_text = f"{name} - {current_price} (Old: {old_price})\n \nStatus: {status}"

                # Liste öğesini oluştur ve renk değişikliği ekle
                item = QListWidgetItem(display_text)

         
                link_label = QLabel(f'<a href="{link}">{link}</a>')  # HTML linki oluştur
                link_label.setOpenExternalLinks(True)

                # Stok durumunu renkli yapmak
                if status.lower() == "in stock":
                    item.setBackground(QColor(0, 255, 0))  # Yeşil arka plan
                elif status.lower() == "out of stock":
                    item.setBackground(QColor(255, 0, 0))  # Kırmızı arka plan

                # Listeye öğeyi ekle
                self.product_list.addItem(item)
                self.product_list.setItemWidget(item, link_label) 
  
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ZaraScraperApp()
    window.show()
    sys.exit(app.exec())