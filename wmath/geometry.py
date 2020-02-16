from sympy import Line, Point
from PyQt5.QtCore import QPointF, QLineF, QRectF
from math import tan, atan, sin, asin, cos, acos, degrees, atan2, pi, sqrt


def point_s_to_q(p: Point):
    return QPointF(p.x, p.y)


def point_s_to_q_l(*points: Point):
    plist = []
    for p in points:
        plist.append(QPointF(p.x, p.y))
    return plist


def point_q_to_s(p: QPointF):
    return Point(p.x(), p.y())


def point_q_to_s_l(*points: QPointF):
    plist = []
    for p in points:
        plist.append(Point(p.x(), p.y()))
    return plist


def line_q_to_s(line: QLineF):
    return Line(Point(line.x1(), line.y1()), Point(line.x2(), line.y2()))


def calc_angle_from_p1_to_p2(a0: QPointF, a1: QPointF, degree: bool):
    """ Return the angle from a0 to a1 in radians or degrees(degree = True)
        Return range: -pi ~ pi / -180°~ 180°"""
    dx = a1.x() - a0.x()
    dy = a1.y() - a0.y()
    angle = atan2(dy, dx)
    if degree is True:
        return degrees(angle)
    else:
        return angle


def calc_angle_from_l1_to_l2(a0: QLineF, a1: QLineF, degree: bool):
    """ Return the angle vector line a0 needs rotated from current pos to a1,
        Rotate direction: clockwise
        Return value unit: in radians or degrees(degree = True) """
    angle_a0 = calc_angle_from_p1_to_p2(a0.p1(), a0.p2(), False)
    angle_a1 = calc_angle_from_p1_to_p2(a1.p1(), a1.p2(), False)
    angle = angle_a1 - angle_a0
    if degree is True:
        return degrees(angle)
    return angle


def calc_p2_from_p1(a0: QPointF, angle: float, length: float):
    """ Return the point calculated from p1 which length far from p1 at the angle of angle
        angle: represented in radians
        Return value type: QPointF"""
    return QPointF(length * cos(angle) + a0.x(), length * sin(angle) + a0.y())


def calc_baseline(p1: QPointF, p2: QPointF, p_mouse: QPointF):
    if p1 == p2:
        return p1, p2
    p1_s = Point(p1.x(), p1.y())
    p2_s = Point(p2.x(), p2.y())
    p_m = Point(p_mouse.x(), p_mouse.y())
    line = Line(p1_s, p2_s)
    if line.contains(p_m):
        return p1, p2
    perpendicular_1 = line.perpendicular_line(p1_s)
    perpendicular_2 = line.perpendicular_line(p2_s)
    para = line.parallel_line(p_m)
    prompt_p_1 = para.intersection(perpendicular_1)
    prompt_p_2 = para.intersection(perpendicular_2)
    q_p_1 = QPointF(prompt_p_1[0].x, prompt_p_1[0].y)
    q_p_2 = QPointF(prompt_p_2[0].x, prompt_p_2[0].y)
    return q_p_1, q_p_2


def calc_prompt_perpendicular_line(p_1: QPointF, p_2: QPointF, p_mouse: QPointF):
    if p_1 == p_2:
        return None, None
    mouse = Point(p_mouse.x(), p_mouse.y())
    p_1 = Point(p_1.x(), p_1.y())
    p_2 = Point(p_2.x(), p_2.y())
    line = Line(p_1, p_2)
    para_line = line.parallel_line(mouse)
    perp_line_1 = line.perpendicular_line(p_1)
    perp_line_2 = line.perpendicular_line(p_2)
    conj_p1 = para_line.intersection(perp_line_1)
    conj_p2 = para_line.intersection(perp_line_2)
    qp1 = QPointF(conj_p1[0].x, conj_p1[0].y)
    qp2 = QPointF(conj_p2[0].x, conj_p2[0].y)
    return qp1, qp2


def calc_line_side_arrow_points(p1: QPointF, p2: QPointF, pm: QPointF):
    line = QLineF(p1, p2)
    angle_p12 = calc_angle_from_p1_to_p2(p1, p2, False)
    angle_p21 = calc_angle_from_p1_to_p2(p2, p1, False)
    line_p1m = QLineF(p1, pm)
    angle_line_p1m = calc_angle_from_l1_to_l2(line, line_p1m, False)
    if angle_line_p1m < 0:
        angle_line_p1m += 2 * pi
    if angle_line_p1m <= pi:
        angle_arrow_1 = angle_p12 + pi / 4
        angle_arrow_2 = angle_p21 - pi / 4
    else:
        angle_arrow_1 = angle_p12 - pi / 4
        angle_arrow_2 = angle_p21 + pi / 4
    return calc_p2_from_p1(p1, angle_arrow_1, 5), calc_p2_from_p1(p2, angle_arrow_2, 5)