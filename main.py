import sys
import folium
import io
import json
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView

from map_window import MapWindow
from custom_types import BoundingBoxPolygon
from program_settings import ProgramSettings


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_bounding_box_coordinates(file_path: str) -> BoundingBoxPolygon:
    with open(file_path) as f:
        polygon_coords: BoundingBoxPolygon = json.load(f)
    return polygon_coords


def build_map_html(polygon_coords: BoundingBoxPolygon) -> str:
    """Builds the Folium map and returns HTML as a string."""
    m = folium.Map()

    bounding_box_polygon = folium.Polygon(
        locations=polygon_coords,
        color="blue",
        fill=True,
        fill_opacity=0.2
    )
    bounding_box_polygon.add_to(m)
    m.fit_bounds(polygon_coords)

    # Add title
    map_title = f"A Simple Map Example using python {get_python_version()}"
    map_template = Path("map.html").read_text()
    title_html = map_template.format(map_title=map_title)
    m.get_root().html.add_child(folium.Element(title_html))

    # Convert to HTML in memory
    html_bytes = io.BytesIO()
    m.save(html_bytes, close_file=False)
    return html_bytes.getvalue().decode()


def run_user_interface(html_content: str) -> None:
    """Starts the Qt application and displays the map window."""
    app = QApplication(sys.argv)
    window = MapWindow(html_content)
    window.show()
    sys.exit(app.exec())


def main() -> None:
    bounding_box_file = ProgramSettings.get_setting("COORDINATES_FILE")
    polygon_coords = get_bounding_box_coordinates(bounding_box_file)

    html_content = build_map_html(polygon_coords)

    run_user_interface(html_content)


if __name__ == '__main__':
    main()
