import sys
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView
import tkFileDialog

import os
sys.path.append( '../meshController/meshControllerWrapper' )

 
html = """
<html>
<body>
   <button id="myInputType1" type="button">Import Model</button>
<script>

document.getElementById("myInputType1").onclick = function(){
   htmlHelper.click();
   
};

</script>


</body>
</html>
"""
 
class HTMLHelper(QObject):
    def __init__(self, parent=None):
        super(HTMLHelper, self).__init__(parent)
 
    @pyqtSlot()
    def click(self):
        print tkFileDialog.askopenfilename()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QWebView()
    frame = view.page().mainFrame()
    helper = HTMLHelper()
    view.setHtml(html)
    frame.addToJavaScriptWindowObject('htmlHelper', helper)
   
    view.show()
    app.exec_()