import introspeqt
from PySide import QtGui, QtCore
import sys
import functools

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        layout = QtGui.QVBoxLayout()

        myText = QtGui.QLineEdit('This is a label')
        myText.setObjectName('My Line Edit')
        btn00 = QtGui.QPushButton('Button00')
        btn00.setObjectName('Btn00')
        btn01 = QtGui.QPushButton('Button01')
        btn01.setObjectName('Btn01')
        btn02 = QtGui.QPushButton('Button02')
        btn02.setObjectName('Btn02')
        btn03 = QtGui.QPushButton('Button03')
        btn03.setObjectName('Btn01')

        layout.addWidget(btn00)
        layout.addWidget(myText)
        layout.addWidget(btn01)
        layout.addWidget(btn02)
        layout.addWidget(btn03)

        self.setLayout(layout)

c = 0

def click(app):
    global c
    mouseState = app.mouseButtons()
    if c ==0:
        if mouseState == QtCore.Qt.LeftButton:
            c= 1
            print 'clicked'
    if mouseState == QtCore.Qt.NoButton:
        c=0

def main():

    timer = QtCore.QTimer()
    timer.setInterval(10)  # 1000/sec

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('My test application')
    ex = Example()
    ex.show()

    check = functools.partial(click,app)

    timer.timeout.connect(check)
    timer.start()


    introspeqt.log_path = 'z:'
    introspeqt.event_list.extend(['PySide.QtCore.QEvent.Type.ContextMenu',
                                  'PySide.QtCore.QEvent.Type.Wheel'])

    handler = introspeqt.log_usage(app)

    screenCaptureWidget(ex,r'z:\wh00t.png')

    sys.exit(app.exec_())

def getRelativeFrameGeometry(widget):
    g = widget.geometry()
    fg = widget.frameGeometry()
    return fg.translated(-g.left(),-g.top())

def screenCaptureWidget(widget, filename, fileformat='png'):
    rfg = getRelativeFrameGeometry(widget)
    pixmap =  QtGui.QPixmap.grabWidget(widget,
                                       rfg.left(), rfg.top(),
                                       rfg.width(), rfg.height())
    pixmap.save(filename, fileformat) 

if __name__ == '__main__':
    main()