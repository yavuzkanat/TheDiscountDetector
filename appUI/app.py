import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel


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
        layout.addWidget(self.fetch_button)

        # Product List
        self.product_list = QListWidget()
        layout.addWidget(self.product_list)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ZaraScraperApp()
    window.show()
    sys.exit(app.exec())