from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

        self.addresses = {}
        for country in self.__data:
            self.bfs_with_memory(country)

    def _apply_geocoding(self, area_id: str) -> str:
        return self.addresses[str(area_id)]

    # Перебор дерева в ширину с запоминанием вершин
    def bfs_with_memory(self, tree):

        if tree.parent_id is not None:
            self.addresses[tree.id] = "{}, {}".format(self.addresses[tree.parent_id],
                                                      tree.name)
        else:
            self.addresses[tree.id] = tree.name

        for child in tree.areas:
            self.addresses[child.id] = "{}, {}".format(self.addresses[child.parent_id],
                                                       child.name)
            if len(child.areas) != 0:
                self.bfs_with_memory(child)
