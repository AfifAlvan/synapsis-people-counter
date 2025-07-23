from app.utils import is_inside_polygon

def count_people(tracked_objects, polygon_coords, previous_positions):
    count_in, count_out = 0, 0
    for obj_id, (x, y) in tracked_objects.items():
        was_inside = is_inside_polygon(*previous_positions.get(obj_id, (x, y)), polygon_coords)
        is_now_inside = is_inside_polygon(x, y, polygon_coords)

        if was_inside and not is_now_inside:
            count_out += 1
        elif not was_inside and is_now_inside:
            count_in += 1

        previous_positions[obj_id] = (x, y)
    return count_in, count_out
