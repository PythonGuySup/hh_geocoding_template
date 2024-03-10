from api import API, TreeNode
from geocoders.geocoder import Geocoder


class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
        result = self.bfs(self.__data, str(area_id))
        return ", ".join([node.name for node in result][::-1])

    # Перебор дерева в ширину
    def bfs(self, root_children, area_id: str) -> list[TreeNode] | None:
        result = []
        for node in root_children:

            if node.id == area_id:
                result.append(node)
                return result
            if len(node.areas) != 0:
                res_return = self.bfs(node.areas, area_id)
                if res_return:
                    result.extend(res_return)
                    result.append(node)
                    return result


