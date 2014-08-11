import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__data__ = [
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ]

def get_html_box(text):
    return '''<table border="0" width="100%"><tr width="100%" valign="top">
        <td width="1%"><img src="softwarecenter.png"/></td>
        <td><table border="0" width="100%" height="100%">
        <tr><td><b><a href="http://www.google.com">titolo</a></b></td></tr>
        <tr><td>{0}</td></tr><tr><td align="right">88/88/8888, 88:88</td></tr>
        </table></td></tr></table>'''.format(text)

class HTMLDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):
        model = index.model()
        record = model.listdata[index.row()]
        doc = QTextDocument(self)
        doc.setHtml(get_html_box(record))
        doc.setTextWidth(option.rect.width())
        ctx = QAbstractTextDocumentLayout.PaintContext()

        painter.save()
        painter.translate(option.rect.topLeft());
        painter.setClipRect(option.rect.translated(-option.rect.topLeft()))
        dl = doc.documentLayout()
        dl.draw(painter, ctx)
        painter.restore()

    def sizeHint(self, option, index):
        model = index.model()
        record = model.listdata[index.row()]
        doc = QTextDocument(self)
        doc.setHtml(get_html_box(record))
        doc.setTextWidth(option.rect.width())
        return QSize(doc.idealWidth(), doc.size().height())

class MyListModel(QAbstractListModel):

    def __init__(self, parent=None, *args):
        super(MyListModel, self).__init__(parent, *args)
        self.listdata = __data__

    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)

    def data(self, index, role=Qt.DisplayRole):
        return index.isValid() and QVariant(self.listdata[index.row()]) or QVariant()

class MyWindow(QWidget):

    def __init__(self, *args):
        super(MyWindow, self).__init__(*args)
        # listview
        self.lv = QListView()
        self.lv.setModel(MyListModel(self))
        self.lv.setItemDelegate(HTMLDelegate(self))
        self.lv.setResizeMode(QListView.Adjust)
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.lv)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())