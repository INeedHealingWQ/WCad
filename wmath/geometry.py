from sympy import Line, Point, Symbol, tan, cos, sin, pi, atan, Segment, oo
from PyQt5.QtCore import QPointF
from math import tan as mtan
from math import atan as matan
from math import degrees
from PyQt5.QtGui import QPainter, QPixmap

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

# def subs_point(l: Line, val):
#     """Take an arbitrary point and make it a fixed point."""
#     t = Symbol('t', real=True)
#     ap = l.arbitrary_point()
#     return Point(ap.x.subs(t, val), ap.y.subs(t, val))

def calc_end(p1: QPointF, ang: float, line_len: float, flag: bool):
    """ b = y - kx """
    k = tan(ang)
    b = p1.y() - k * p1.x()
    abs_ang = abs(ang)
    if 0 <= abs_ang < pi / 2:
        a = abs_ang
        delta_l = cos(a) * line_len
        x = p1.x() + delta_l
        y = k * x + b
    elif abs_ang - pi / 2 == 0:
        if ang > 0:
            x = p1.x()
            y = p1.y() + line_len
        else:
            x = p1.x()
            y = p1.y() - line_len
    else:
        a = pi - abs_ang
        delta_l = cos(a) * line_len
        x = p1.x() - delta_l
        y = k * x + b
    if flag is True:
        return QPointF(x, y)
    else:
        return Point(x, y)

def calc_line_angle(a0: QPointF, a1: QPointF):
    p1 = point_q_to_s(a0)
    p2 = point_q_to_s(a1)
    line = Line(p1, p2)
    slope = line.slope
    if slope == oo:
        if a0.y() > a1.y():
            return 90
        else:
            return -90
    elif slope == 0:

    if p1.x() == p2.x():
        ang_deg = 90
    elif p1.y() == p2.y():
        ang_deg = 0
    else:
        k = (p2.y() - p1.y()) / (p2.x() - p1.x())
        ang = matan(k)
        ang_deg = degrees(ang)
    return ang_deg

def calc_y_at_x(p1: QPointF, p2: QPointF, x: float):
    if p1.x() == p2.x():
        return None
    elif p1.y() == p2.y():
        return p1.y()
    else:
        k = (p2.y() - p1.y()) / (p2.x() - p1.x())
        b = p1.y() - k * p1.x()
        return k * x + b


def calc_baseline(p1: QPointF, p2: QPointF, p_mouse: QPointF):
    if p1 == p2:
        return p1, p2
    p1 = Point(p1.x(), p1.y())
    p2 = Point(p2.x(), p2.y())
    p_m = Point(p_mouse.x(), p_mouse.y())
    line = Line(p1, p2)
    if line.contains(p_m):
        return p1, p2
    perpendicular_1 = line.perpendicular_line(p1)
    perpendicular_2 = line.perpendicular_line(p2)
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

def test_line():
    l = Line(Point(5, 5), Point(9, 9))

def calc_line_side_arrow_points(p1: QPointF, p2: QPointF, p_mouse: QPointF):
    p1_sym = Point(p1.x(), p1.y())
    p2_sym = Point(p2.x(), p2.y())
    p_mouse_sym = Point(p_mouse.x(), p_mouse.y())
    line_sym = Line(p1_sym, p2_sym)
    if line_sym.contains(p_mouse_sym):
        return None
    parallel1 = line_sym.parallel_line(p_mouse_sym)
    perpendicular_1 = parallel1.perpendicular_segment(p1_sym)
    ang_per = calc_line_angle_s(perpendicular_1.points[0], perpendicular_1.points[1])
    ang_line = calc_line_angle_q(p1, p2)
    a1 = calc_end(p1, ang_per, 5, True)
    b1 = calc_end(p1, ang_line, 5, True)
    b2 = calc_end(p2, ang_line + 180, 5, True)
    para = line_sym.parallel_line(a1)
    per1 = line_sym.perpendicular_line(b1)
    per2 = line_sym.perpendicular_line(b2)
    arrow_1_p = para.intersection(per1)
    arrow_2_p = para.intersection(per2)
    qp1 = QPointF(arrow_1_p.x, arrow_1_p.y)
    qp2 = QPointF(arrow_2_p.x, arrow_2_p.y)
    return qp1, qp2
