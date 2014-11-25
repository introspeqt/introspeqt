from PySide import QtGui
from PySide import QtCore
import getpass
import os

objects_dict = {}
log_path = None


class Handler(QtCore.QObject):
    def __init__(self, app):
        super(Handler, self).__init__()
        self.app = app

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            widget_type = type(obj).__name__
            event_type = str(event.type())
            obj_name = obj.objectName()

            objects_dict[widget_type][obj_name].setdefault(event_type, 0)
            objects_dict[widget_type][obj_name][event_type] += 1

            save_file(objects_dict, self.app)

        return super(Handler, self).eventFilter(obj, event)


def log_usage(app):
    handler = Handler(app)
    for widget in QtGui.QApplication.allWidgets():
        widget_type = str(type(widget).__name__)
        objects_dict.setdefault(str(widget_type), {})
        objectName = widget.objectName()
        if not objectName:
            objectName = '<Unknown objectName>'
        objects_dict[widget_type].setdefault(objectName, {})

        #if isinstance(widget, QtGui.QPushButton):
        #print "Installing in %s" % widget.text()
        widget.installEventFilter(handler)

    return handler


def pretty_dict(d, indent=0):
    content = ''

    for key, value in d.iteritems():
        content += '\t' * indent + str(key)+'\n'
        if isinstance(value, dict):
            content += pretty_dict(value, indent+1)
        else:
            content += '\t' * (indent+1) + str(value)+'\n'
    return content


def save_file(data, app):
    try:
        with open((log_path + os.sep + "introspeqt.txt"), 'w') as file:
            app_name = app.applicationName()

            if not app_name:
                app_name = '<Unknown>'

            file.write('App name: ' + app_name + '\n')
            file.write('Username: ' + getpass.getuser() + '\n\n')
            file.write(pretty_dict(data))

    except Exception, e:
        print "ERROR: Unable to create introspeqt's log file"
        print e
