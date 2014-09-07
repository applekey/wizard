from PyQt4 import QtCore, QtGui
from PyQt4 import phonon
from PyQt4.QtGui import QSizePolicy
from componentConfirguration import *
from awsomeSeekSlider import awsomeSeekSlider
import time

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



class awsomePlayer( QtGui.QWidget):
    def __init__(self, parentForm):
        super( awsomePlayer, self ).__init__(parentForm)        
        self.videoSource = None
        self.state = 0 
        self.mute = False

        ## god dam python doesn't have enums, 
        #0 means stop, 1 means paused and 2 means playing

        self.shortcutFull = QtGui.QShortcut(self)
        self.shortcutFull.setKey(QtGui.QKeySequence('ESC'))
        self.shortcutFull.setContext(QtCore.Qt.ApplicationShortcut)
        self.shortcutFull.activated.connect(self.handleFullScreen)

        self.__setupUi(self)
        
    def sizeHint(self):
        return QtCore.QSize(0,300)
    def startStopChangeIcon(self,playing):
        if playing:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap( (configureStopSVGLocation)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.playButton.setIcon(icon)

        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap( (configPlaySVGLocation)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.playButton.setIcon(icon)
    def handleMute(self):
        if self.mute:
            self.mute=False
            self.volumeSlider.setMaximumVolume(1.0) 
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap( (volumeSliderIcon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.muteButton.setIcon(icon)

        else:
            self.mute = True
            self.volumeSlider.setMaximumVolume(0.0) 
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap( (volumeSliderMuteIcon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.muteButton.setIcon(icon)

    def  pauseStart(self):
        if self.videoSource is  None:
            return
        if self.state is 0 or self.state is 1:
            self.videoPlayer.play()
            self.videoPlayer.show()
            self.state = 2
            self.startStopChangeIcon(True)
        else:
             self.videoPlayer.pause()
             self.startStopChangeIcon(False)
             
             self.state = 1
    def pause(self):
        self.videoPlayer.pause()
        self.state = 1
        self.startStopChangeIcon(False)

    def setSource(self,source):
        self.videoSource = source
        media = phonon.Phonon.MediaSource(source)
        self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())

        self.videoPlayer.load(media)
        self.videoPlayer.show()
        self.videoPlayer.play()
        time.sleep(0.0001)
        self.videoPlayer.pause()
        
       
    
    def handleFullScreen(self):
        videoWidget = self.videoPlayer.videoWidget()
        if videoWidget.isFullScreen():
            videoWidget.exitFullScreen()
        else: 
            videoWidget.enterFullScreen()
  

       # self.player.mediaObject().stateChanged.connect(self.stateChanged)
    #def stateChanged(self, new, old):
    #    if new == Phonon.PlayingState:
    #        self.play_pause.setIcon(QtGui.QIcon(':/icons/player_pause.svg'))
    #    else:
    #        self.play_pause.setIcon(QtGui.QIcon(':/icons/player_play.svg'))

    def __setupUi(self, parentForm):
        self.setStyleSheet("background: white;")
        # create the verticle layout, everthing lives in this verticle layout
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName( ("verticalLayout"))
        # self.verticalLayout.setContentsMargins(33, 0, 33, 0)
        # create the video player
        self.videoPlayer = phonon.Phonon.VideoPlayer(self)



        self.videoPlayer.setObjectName( ("videoPlayer"))
        policy = QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        self.videoPlayer.setSizePolicy(policy)

        self.verticalLayout.addWidget(self.videoPlayer)
        # this is the space between the controls and the actual player
        #spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        #self.verticalLayout.addItem(spacerItem)
        
        #below are the horizontal box that will contain the actual controls of the player
        self.horizontalLayout = QtGui.QHBoxLayout(self)
        self.horizontalLayout.setObjectName( ("horizontalLayout"))
        self.horizontalLayout.setContentsMargins(11, 0, 11, 5)
        self.playButton = QtGui.QPushButton(self)
        self.playButton.setObjectName(_fromUtf8("pushButton"))
        self.playButton.setStyleSheet("border: none;");
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(configPlaySVGLocation)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.playButton.setIcon(icon)
        self.playButton.setIconSize(self.playButton.size())
        self.horizontalLayout.addWidget(self.playButton)

        ## -----------horizontal space
        #spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        #self.horizontalLayout.addItem(spacerItem1)

        self.seekSlider = awsomeSeekSlider(self)
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.seekSlider.setStyleSheet(qSliderStyle)
        self.seekSlider.setMinimumSize(QtCore.QSize(30, 24))
        self.horizontalLayout.addWidget(self.seekSlider)     
        ## -----------horizontal spacer
         
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        self.horizontalLayout.addItem(spacerItem2)

        self.muteButton = QtGui.QPushButton(self)
        self.muteButton.setStyleSheet("border: none;");
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(volumeSliderIcon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.muteButton.setIcon(icon)
        self.horizontalLayout.addWidget( self.muteButton)

        self.volumeSlider = phonon.Phonon.VolumeSlider(self)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.volumeSlider.setAudioOutput( self.videoPlayer.audioOutput())
        self.volumeSlider.setStyleSheet(qSliderStyle)
        self.volumeSlider.setMaximumSize(QtCore.QSize(100,10000))

     
        self.volumeSlider.setMuteVisible(False)
        # -----------horizontal spacer
        self.horizontalLayout.addWidget(self.volumeSlider)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        
        self.horizontalLayout.addItem(spacerItem3)
        
        self.fullScreenButton = QtGui.QPushButton(self)
        self.fullScreenButton.setObjectName(_fromUtf8("pushButton_2"))
        self.fullScreenButton.setStyleSheet("border: none;");
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(configFullScreenSVGLocation)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.fullScreenButton.setIcon(icon)
        self.fullScreenButton.setIconSize(self.fullScreenButton.size())
        
        self.horizontalLayout.addWidget(self.fullScreenButton)
        self.verticalLayout.addLayout(self.horizontalLayout) 

        minsize = QtCore.QSize(0,400)
        abc = self.verticalLayout.minimumSize()
        # link together singlas
        QtCore.QObject.connect(self.playButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pauseStart)
        QtCore.QObject.connect(self.fullScreenButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleFullScreen)
        QtCore.QObject.connect(self.muteButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.handleMute)