import sys
from PyQt4.QtGui import QApplication, QDialog
from mine import Ui_Form

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())