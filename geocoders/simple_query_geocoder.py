from geocoders.geocoder import Geocoder
from api import API


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        node = API.get_area(area_id)
        full_address = "" + node.name

        while node.parent_id:
            node = API.get_area(node.parent_id)
            full_address = node.name + ", " + full_address

        return full_address
