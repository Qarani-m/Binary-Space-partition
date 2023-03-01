import random
import time
class BSPNode:
    def __init__(self, plane, front=None, back=None):
        self.plane = plane
        self.front = front
        self.back = back
class BSPTree:
    def __init__(self, polygon_list):
        self.root = None
        self.polygon_list = polygon_list

    def build(self):
        if not self.polygon_list:
            return
        print("Building BSP tree...")
        time.sleep(2)
        self.root = self._build(self.polygon_list)
        print("BSP tree construction complete.")
        time.sleep(2)
    def _build(self, polygon_list):
        if not polygon_list:
            return None

        if len(polygon_list) == 1:
            print("Partitioning polygons...")
            time.sleep(2)

            return BSPNode(polygon_list[0])

        plane = self._choose_plane(polygon_list)
        front_list, back_list = self._partition(plane, polygon_list)

        front = self._build(front_list)
        back = self._build(back_list)

        return BSPNode(plane, front, back)

    def _choose_plane(self, polygon_list):
        # Choose a random polygon from the list as the dividing plane
        return random.choice(polygon_list)

    def _partition(self, plane, polygon_list):
        front_list = []
        back_list = []
        for polygon in polygon_list:
            result = self._classify_polygon(plane, polygon)
            if result == "FRONT":
                front_list.append(polygon)
            elif result == "BACK":
                back_list.append(polygon)
            else:
                front_list.append(polygon)
                back_list.append(polygon)

        return front_list, back_list

    def _classify_polygon(self, plane, polygon):
        # Determine the position of the polygon relative to the plane
        # For simplicity, assume that all polygons are convex and have vertices in clockwise order

        front = 0
        back = 0
        for i in range(len(polygon)):
            a = polygon[i]
            b = polygon[(i + 1) % len(polygon)]

            d1 = (b[0] - a[0]) * (plane[1][1] - a[1]) - (b[1] - a[1]) * (plane[1][0] - a[0])
            d2 = (b[0] - a[0]) * (plane[0][1] - a[1]) - (b[1] - a[1]) * (plane[0][0] - a[0])

            if d1 > 0:
                front = 1
            if d1 < 0:
                back = 1

            if front and back:
                return "SPANNING"

        if front:
            return "FRONT"
        elif back:
            return "BACK"
        else:
            return "COPLANAR"

    def print_tree(self):
        # Traverse the BSP tree and print its contents to the console
        self._print_tree(self.root)

    def _print_tree(self, node, level=0):
        if node:
            print("BSP tree....")
            print("  " * level + str(node.plane))

vertices = [(2,1),(3,1),(4,1),(56,77),(34,21),(24,56)]
tree = BSPTree([vertices])
tree.build()
tree.print_tree()