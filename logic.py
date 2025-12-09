from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_TV_window):
    MIN_VOLUME = 0
    MAX_VOLUME = 100
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self)->None:
        """
        sets up default tv - off - 0 volume - channel 0
        """
        super().__init__()
        self.__status__ = False
        self.__muted__ = False
        self.__volume__ = Logic.MIN_VOLUME
        self.__channel__ = Logic.MIN_CHANNEL
        self.setupUi(self)
        self.label_volumeimage.hide()
        self.progress_bar.hide()
        self.button_power.clicked.connect(lambda: self.power())
        self.button_volume_up.clicked.connect(lambda: self.volume_up())
        self.button_volume_down.clicked.connect(lambda: self.volume_down())
        self.button_channel_up.clicked.connect(lambda: self.channel_up())
        self.button_channel_down.clicked.connect(lambda: self.channel_down())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_channel0.clicked.connect(lambda: self.channel_0())
        self.button_channel1.clicked.connect(lambda: self.channel_1())
        self.button_channel2.clicked.connect(lambda: self.channel_2())
        self.button_channel3.clicked.connect(lambda: self.channel_3())

    def channel_0(self) -> None:
        """
        Method to set channel to 0
        """
        if self.__status__:
            self.__channel__ = 0
            self.set_channel()

    def channel_1(self) -> None:
        """
        Method to set channel to 1
        """
        if self.__status__:
            self.__channel__ = 1
            self.set_channel()

    def channel_2(self) -> None:
        """
        Method to set channel to 2
        """
        if self.__status__:
            self.__channel__ = 2
            self.set_channel()

    def channel_3(self) -> None:
        """
        Method to set channel to 3
        """
        if self.__status__:
            self.__channel__ = 3
            self.set_channel()

    def power(self)->None:
        """
        Method to turn the television on and off
        """
        self.__status__ = not self.__status__ #changes status to on or off
        if self.__status__:# if on sets channel
            self.label_volumeimage.show()
            self.progress_bar.show()
            self.set_channel()
        else:# if off, turns off tv
            self.label_volumeimage.hide()
            self.progress_bar.hide()
            self.label_image.setPixmap(QtGui.QPixmap(""))
            self.label_channel_text.setText("")

    def set_channel(self)->None:
        """
        Method to set the television channel picture and title
        """
        if self.__channel__ == 0:
            self.label_image.setPixmap(QtGui.QPixmap("images/BTS.jpg"))
            self.label_channel_text.setText("0 - BTS")
        elif self.__channel__ == 1:
            self.label_image.setPixmap(QtGui.QPixmap("images/chococat.jpg"))
            self.label_channel_text.setText("1 - Chococat")
        elif self.__channel__ == 2:
            self.label_image.setPixmap(QtGui.QPixmap("images/miku.jpg"))
            self.label_channel_text.setText("2 - Hatsune Miku")
        elif self.__channel__ == 3:
            self.label_image.setPixmap(QtGui.QPixmap("images/my_melody&kuromi.png"))
            self.label_channel_text.setText("3 - My Melody & Kuromi")

    def set_volume(self)->None:
        if self.__muted__:
            self.label_volumeimage.setPixmap(QtGui.QPixmap("images/mute-speaker-icon.jpg"))
            self.progress_bar.setProperty("value", 0)
        else:
            self.label_volumeimage.setPixmap(QtGui.QPixmap("images/sound-speaker-icon.jpg"))
            self.progress_bar.setProperty("value", self.__volume__)

    def mute(self)->None:
        """
        Method to mute television volume
        """
        if self.__status__:
            self.__muted__ = not self.__muted__
            self.set_volume()

    def channel_up(self)->None:
        """
        Method to increase television channel by one
        """
        if self.__status__:
            if self.__channel__ == Logic.MAX_CHANNEL:
                self.__channel__ = Logic.MIN_CHANNEL
                self.set_channel()
            else:
                self.__channel__ += 1
                self.set_channel()

    def channel_down(self)->None:
        """
        Method to decrease television channel by one
        """
        if self.__status__:
            if self.__channel__ == Logic.MIN_CHANNEL:
                self.__channel__ = Logic.MAX_CHANNEL
                self.set_channel()
            else:
                self.__channel__ -= 1
                self.set_channel()

    def volume_up(self)->None:
        """
        Method to increase television volume by one
        """
        if self.__status__:
            if self.__muted__:
                Logic.mute(self)
            if self.__volume__ < Logic.MAX_VOLUME:
                self.__volume__ += 5
                self.set_volume()

    def volume_down(self)->None:
        """
        Method to decrease television volume by one
        """
        if self.__status__:
            if self.__muted__:#if muted, unmutes
                Logic.mute(self)
            if self.__volume__ > Logic.MIN_VOLUME: # if greater than min, decreases by 1
                self.__volume__ -= 5
                self.set_volume()