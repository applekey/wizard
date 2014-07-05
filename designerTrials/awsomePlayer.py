from PyQt4 import QtCore, QtGui
from PyQt4 import phonon
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class awsomePlayer( QtGui.QFrame):
    def __init__(self, parentForm):
        super( awsomePlayer, self ).__init__()        
        self.videoSource = None
        self.state = 0 

        ## god dam python doesn't have enums, 
        #0 means stop, 1 means paused and 2 means playing

        self.shortcutFull = QtGui.QShortcut(self)
        self.shortcutFull.setKey(QtGui.QKeySequence('F11'))
        self.shortcutFull.setContext(QtCore.Qt.ApplicationShortcut)
        self.shortcutFull.activated.connect(self.handleFullScreen)

        self.__setupUi(self)

    def  pauseStart(self):
        if self.videoSource is  None:
            return
        if self.state is 0 or self.state is 1:
            self.videoPlayer.play()
            self.videoPlayer.show()
            self.state = 2
        else:
             self.videoPlayer.pause()
             self.state = 1

    def setSource(self,source):
        self.videoSource = source
        media = phonon.Phonon.MediaSource(source)
        self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())

        self.videoPlayer.load(media)
        self.videoPlayer.show()
    
    def handleFullScreen(self):
        videoWidget = self.videoPlayer.videoWidget()
        #if videoWidget.isFullScreen():
        #    videoWidget.exitFullScreen()
        #else: 
        #    videoWidget.enterFullScreen()
  

       # self.player.mediaObject().stateChanged.connect(self.stateChanged)
    #def stateChanged(self, new, old):
    #    if new == Phonon.PlayingState:
    #        self.play_pause.setIcon(QtGui.QIcon(':/icons/player_pause.svg'))
    #    else:
    #        self.play_pause.setIcon(QtGui.QIcon(':/icons/player_play.svg'))

    def __setupUi(self, parentForm): 
       
        self.setStyleSheet("background:#27ae60")
        # create the verticle layout, everthing lives in this verticle layout
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout.setContentsMargins(33, 0, 33, 0)
        # create the video player
        self.videoPlayer = phonon.Phonon.VideoPlayer(self)
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.verticalLayout.addWidget(self.videoPlayer)
        # this is the space between the controls and the actual player
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        
        #below are the horizontal box that will contain the actual controls of the player
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.playButton = QtGui.QPushButton(self)
        self.playButton.setObjectName(_fromUtf8("pushButton"))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("play.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.playButton.setIcon(icon)
        self.horizontalLayout.addWidget(self.playButton)

        # -----------horizontal space
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.seekSlider = phonon.Phonon.SeekSlider(self)
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        
        # -----------horizontal spacer
        self.horizontalLayout.addWidget(self.seekSlider)      
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem2)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.volumeSlider.setAudioOutput( self.videoPlayer.audioOutput())
        # -----------horizontal spacer
        self.horizontalLayout.addWidget(self.volumeSlider)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        
        self.horizontalLayout.addItem(spacerItem3)
        
        self.fullScreenButton = QtGui.QPushButton(self)
        self.fullScreenButton.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.fullScreenButton)
        self.verticalLayout.addLayout(self.horizontalLayout) 

        # link together singlas
        QtCore.QObject.connect(self.playButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pauseStart)
        QtCore.QObject.connect(self.fullScreenButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleFullScreen)