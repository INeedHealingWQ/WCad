import typing
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem, QGraphicsItem, QGraphicsSceneMouseEvent, QToolTip
from wpath import WPath
from wtypes import WToolTypes


class WGPathItem(QtWidgets.QGraphicsPathItem):
    def __init__(self):
        super(WGPathItem, self).__init__()

        self._item_type = WToolTypes.WItemTypes.COMMON
        self._default_color = QtCore.Qt.black
        self._current_color = QtCore.Qt.black
        self.__w_g_path_item_init()

    def __w_g_path_item_init(self):
        self.setAcceptHoverEvents(True)

    @property
    def item_type(self):
        return self._item_type

    @property
    def default_color(self):
        return self._default_color

    @property
    def current_color(self):
        return self._current_color

    @current_color.setter
    def current_color(self, color: QtGui.QColor):
        self._current_color = color
        self.update()

    def reset_color(self):
        if self._default_color is not None:
            self._current_color = self._default_color
            self.update()


class WGPromptCircle(WGPathItem):
    def __init__(self, pos: QtCore.QPointF, r, tip: str):
        super(WGPromptCircle, self).__init__()

        self.tip = tip
        self._item_type = WToolTypes.WItemTypes.PROMPT
        self._default_color = QtCore.Qt.red
        self._current_color = QtCore.Qt.red

        self.__pos = pos
        self.__r = r
        self.__w_circle = WPath.WCircle(self.__pos, self.__r)
        self.setPath(self.__w_circle)
        self.setOpacity(0.001)

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem', widget: typing.Optional[QWidget] = ...) -> None:
        painter.setPen(self.current_color)
        painter.drawPath(self.path())

    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        tool = self.scene().current_tool
        if tool is not None and tool.tool_type == WToolTypes.WToolTypes.LINE:
            self.setOpacity(1)
            pos = event.screenPos()
            QToolTip.showText(QtCore.QPoint(int(pos.x()), int(pos.y())), self.tip)
        super(WGPromptCircle, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        self.setOpacity(0.001)
        super(WGPromptCircle, self).hoverLeaveEvent(event)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        if event.button() == QtCore.Qt.LeftButton:
            tool = self.scene().current_tool
            if tool is not None and tool.tool_type == WToolTypes.WToolTypes.LINE:
                tool.prompt_point = self.__pos
        super(WGPromptCircle, self).mousePressEvent(event)


class WGLine(WGPathItem):
    def __init__(self, line: QtCore.QLineF, tmp=False):
        super(WGLine, self).__init__()

        self.__is_tmp = tmp

        self.w_line = WPath.WLineF(line)
        self.setPath(self.w_line)
        self.start_prompt_item = None
        self.end_prompt_item = None
        self.mid_prompt_item = None
        self.prompt_circle_r = 5
        self.__init_attr()

    def dbg_dump_info(self):
        print('start point: ', self.w_line.start_point)
        print('end point: ', self.w_line.end_point)
        print('mid point: ', self.w_line.mid_point)

    def __init_attr(self):
#        self.setFlag(QtWidgets.QGraphicsPathItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsPathItem.ItemSendsGeometryChanges)
        ''' This is needed for the hover would not disturb prompt items' '''
        self.setAcceptHoverEvents(False)
        if self.__is_tmp is False:
            self.add_prompt()

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        return super(WGLine, self).mouseMoveEvent(event)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        if self.__is_tmp is True:
            ''' temp item not receive press event '''
            return event.ignore()
        else:
            return super(WGLine, self).mousePressEvent(event)

    def add_prompt(self):
        start = self.w_line.start_point
        end = self.w_line.end_point
        mid = self.w_line.mid_point
        self.start_prompt_item = WGPromptCircle(start, self.prompt_circle_r, 'End')
        self.end_prompt_item = WGPromptCircle(end, self.prompt_circle_r, 'End')
        self.mid_prompt_item = WGPromptCircle(mid, self.prompt_circle_r, 'Middle')
        self.start_prompt_item.setParentItem(self)
        self.end_prompt_item.setParentItem(self)
        self.mid_prompt_item.setParentItem(self)

    def itemChange(self, change: 'QGraphicsItem.GraphicsItemChange', value: typing.Any) -> typing.Any:
        return super(WGLine, self).itemChange(change, value)
