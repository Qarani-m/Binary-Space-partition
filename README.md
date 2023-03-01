# Binary-Space-Partition
The code is an implementation of a Binary Space Partition (BSP) tree, which is a data structure commonly used for rendering 3D graphics in real-time computer graphics. The BSP tree is a hierarchical representation of 3D space that allows for efficient culling of objects that are not visible from the viewpoint.

The code consists of two classes, BSPNode and BSPTree. The BSPNode class represents a node in the tree, which consists of a plane, and pointers to its front and back children. The BSPTree class represents the tree as a whole and provides methods for building the tree and partitioning polygons.

The input to the BSPTree class is a list of polygons represented as lists of vertices, where each vertex is represented as a tuple of (x, y) coordinates. The polygons are assumed to be convex and ordered in clockwise direction.

The build method is used to construct the BSP tree. It starts by checking if the input list of polygons is empty. If it is, the build process returns immediately. Otherwise, the method calls the _build helper method to create the tree recursively.

The _build method is responsible for dividing the input polyggon list into two parts and creating a BSPNode for each division. It starts by checking if the input list of polygons is empty. If it is, the method returns None. If the list has only one polygon, a BSPNode is created for that polygon with no children and returned.

If the input list has more than one polygon, a plane is chosen by calling the _choose_plane method, which randomly selects one of the polygons from the list. The partition method is then called to separate the polygons into two lists, front and back, based on their position relative to the dividing plane. The _build method is then called recursively on each of the front and back lists to create the subtrees. Finally, a BSPNode is created for the current division with the front and back lists as its children, and the BSPNode is returned.

The _partition method separates the polygons into front and back lists based on their position relative to the dividing plane. It does this by calling the _classify_polygon method on each polygon in the input list. The _classify_polygon method uses the Winding number algorithm to determine the position of each polygon relative to the dividing plane. If a polygon is in front of the plane, it is added to the front list, if it is behind the plane, it is added to the back list, and if it spans the plane, it is added to both lists.

The output of the code is a binary tree structure where each node represents a dividing plane, and its children represent either front or back polygons. The root of the tree is the starting node that represents the entire 3D space. The tree can be used for rendering 3D graphics by traversing the tree from the root to the leaves and only drawing polygons that are visible from the viewpoint.

In summary, the code is an implementation of a Binary Space Partition (BSP) tree data structure, which is used for efficiently rendering 3D graphics. The code takes as input a list of polyggon vertices, builds a binary tree, and outputs the root node of the tree, which represents the entire 3D space.


#To execute the Code
Python3 file.py





The following assumptions are made in the code:

1:The input to the BSPTree class is a list of polyggon lists.

2:The polygon lists consist of vertices represented as tuples of (x, y) coordinates.

3:The vertices of each polygon are ordered in clockwise direction.

4:The polyggon lists are convex and non-intersecting.

5:The classify_polygon method uses the Winding number algorithm to classify the position of each polygon relative to the dividing plane.

6:The choose_plane method randomly selects one of the polygons from the list as the dividing plane.

7:The partition method separates the polygons into front and back lists based on their position relative to the dividing plane.

8:The build method creates a binary tree structure where each node is a dividing plane, and the children are either front or back polyggon lists.
