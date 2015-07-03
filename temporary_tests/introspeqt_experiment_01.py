from PySide import QtGui, QtCore
import sys


class Handler(QtCore.QObject, object):
    def __init__(self, overlay):
        super(Handler, self).__init__()
        self.app = QtGui.QApplication.instance()
        self.overlay = overlay

    def eventFilter(self, obj, event):

        if event.type() == QtCore.QEvent.MouseButtonPress:
            widget = widget_at_position(self.overlay)
            print widget
            print event.type()
            mySignal = QtCore.pyqtSignal()
            self.closeApp.connect(widget.clicked)
            return widget.event(event.type())
        return True


def create_overlay(widget):
    '''Creates an invisible QWidget with an event filter.
    It also propagates the events to the widgets below the cursor.

    '''
    geo = widget.geometry()
    overlay = QtGui.QWidget(parent=widget)
    overlay.setObjectName('overlay')
    overlay.setGeometry(geo)
    return overlay


def widget_at_position(overlay):
    overlay.lower()
    cursor = QtGui.QCursor()
    app = QtGui.QApplication.instance()
    toBeReturned = app.widgetAt(cursor.pos())
    overlay.raise_()
    return toBeReturned


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        layout = QtGui.QVBoxLayout()
        btn01 = QtGui.QPushButton('Blah')
        btn01.clicked.connect(self.greet)
        layout.addWidget(btn01)
        self.setLayout(layout)

    def greet(self):
        print 'Hello there!'


def main():

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('My test application')
    ex = Example()
    #overlay = create_overlay(ex)
    #handler = Handler(overlay)
    #overlay.installEventFilter(handler)
    #overlay.raise_()

    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()