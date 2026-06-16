import sys
import folium
import io
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView

from program_settings import ProgramSettings

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

# TODO: move this to a separate persistence layer
def get_bounding_box_coordinates(file_path: str) -> list:
    with open(file_path) as f:
        polygon_coords = json.load(f)
    return polygon_coords

bounding_box_file = ProgramSettings.get_setting("COORDINATES_FILE")

polygon_coords = get_bounding_box_coordinates(bounding_box_file)

# Build the Folium map
m = folium.Map()
folium.Polygon(locations=polygon_coords, color="blue", fill=True, fill_opacity=0.2).add_to(m)
m.fit_bounds(polygon_coords)

# Add title
map_title = f"A Simple Map Example using python {get_python_version()}"

title_html = f"""
    <div style="position: fixed; 
                top: 10px; left: 50%; transform: translateX(-50%);
                z-index: 1000; background-color: white;
                padding: 8px 16px; border-radius: 6px;
                box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
                font-size: 18px; font-weight: bold; font-family: Arial;">
        {map_title}
    </div>
"""
m.get_root().html.add_child(folium.Element(title_html))

# Convert to HTML in memory (no temp file needed)
html_bytes = io.BytesIO()
m.save(html_bytes, close_file=False)
html_content = html_bytes.getvalue().decode()

# Display in Qt window
class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map Viewer")
        self.resize(1024, 768)
        self.browser = QWebEngineView()
        self.browser.setHtml(html_content)
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(self.browser)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MapWindow()
window.show()
sys.exit(app.exec())
