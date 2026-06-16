from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView


class MapWindow(QMainWindow):

    
    def __init__(self, html_content: str):
        super().__init__()
        self.setWindowTitle("Map Viewer")
        self.resize(1024, 768)
        self.browser = QWebEngineView()
        self.browser.setHtml(html_content)
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(self.browser)
        self.setCentralWidget(container)
