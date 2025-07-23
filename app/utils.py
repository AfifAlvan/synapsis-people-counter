from shapely.geometry import Point, Polygon

def is_inside_polygon(x, y, polygon_coords):
    polygon = Polygon(polygon_coords)
    return polygon.contains(Point(x, y))
