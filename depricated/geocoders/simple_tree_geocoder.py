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
        result = None
        for country in self.__data:
            if result is None:
                result = self.bfs(country, str(area_id))
        return ", ".join([node.name for node in result][::-1])

    # Перебор дерева в ширину
    def bfs(self, tree, area_id: str) -> list[TreeNode] | None:
        result = []

        if tree.id == area_id:
            result.append(tree)
            return result

        for child in tree.areas:
            if child.id == area_id:
                result.append(child)
                result.append(tree)
                return result
            if len(child.areas) != 0:
                return_res = self.bfs(child, area_id)
                if return_res is not None:
                    result.extend(return_res)
                    result.append(tree)
                    return result
        return None
