import pytest
from television import *

class TestTelevision:
    def setup_method(self):
        self.tv = Television()
        self.tv2 = Television()
        self.tv3 = Television()
        self.tv4 = Television()
        self.tv5 = Television()
        self.tv6 = Television()
    def test_init(self):
        assert str(self.tv) == "Power = [False], Channel = [0], Volume = [0]"
        assert str(self.tv2) == "Power = [False], Channel = [0], Volume = [0]"
        assert str(self.tv3) == "Power = [False], Channel = [0], Volume = [0]"
        assert str(self.tv4) == "Power = [False], Channel = [0], Volume = [0]"
        assert str(self.tv5) == "Power = [False], Channel = [0], Volume = [0]"
        assert str(self.tv6) == "Power = [False], Channel = [0], Volume = [0]"
    def test_power(self):
        self.tv.power()
        assert str(self.tv) == "Power = [True], Channel = [0], Volume = [0]"
        self.tv.power()
        assert str(self.tv) == "Power = [False], Channel = [0], Volume = [0]"
    def test_mute(self):
        self.tv2.power()
        self.tv2.volume_up()
        self.tv2.mute()
        assert str(self.tv2) == "Power = [True], Channel = [0], Volume = [0]" # Powered on, volume up by 1, then muted
        self.tv2.mute()
        assert str(self.tv2) == "Power = [True], Channel = [0], Volume = [1]" # Powered on, then unmuted
        self.tv2.power()
        self.tv2.mute()
        assert str(self.tv2) == "Power = [False], Channel = [0], Volume = [1]" # Powered off, then tries to mute
        self.tv2.power()
        self.tv2.mute()
        assert str(self.tv2) == "Power = [True], Channel = [0], Volume = [0]" # Powered on, then muted
        self.tv2.power()
        assert str(self.tv2) == "Power = [False], Channel = [0], Volume = [0]" # Muted and powered off

    def test_channel_up(self):
        self.tv3.channel_up()
        assert str(self.tv3) == "Power = [False], Channel = [0], Volume = [0]" # Powered off, tries to channel up
        self.tv3.power()
        self.tv3.channel_up()
        assert str(self.tv3) == "Power = [True], Channel = [1], Volume = [0]" # Powered on, channels up once
        self.tv3.channel_up()
        self.tv3.channel_up()
        self.tv3.channel_up()
        assert str(self.tv3) == "Power = [True], Channel = [0], Volume = [0]" # Powered on, channels up 1 beyond the max

    def test_channel_down(self):
        self.tv4.channel_down()
        assert str(self.tv4) == "Power = [False], Channel = [0], Volume = [0]" # Powered off, tries to channel down
        self.tv4.power()
        self.tv4.channel_down()
        assert str(self.tv4) == "Power = [True], Channel = [3], Volume = [0]" # Powered on, then channel down 1 below the min

    def test_volume_up(self):
        self.tv5.volume_up()
        assert str(self.tv5) == "Power = [False], Channel = [0], Volume = [0]" # Powered off, tries to up volume
        self.tv5.power()
        self.tv5.volume_up()
        assert str(self.tv5) == "Power = [True], Channel = [0], Volume = [1]" # Powered on, then volume up
        self.tv5.mute()
        self.tv5.volume_up()
        assert str(self.tv5) == "Power = [True], Channel = [0], Volume = [2]" # Powered on, muted, then volume up
        self.tv5.volume_up()
        assert str(self.tv5) == "Power = [True], Channel = [0], Volume = [2]" # Powered on, then volume up 1 beyond the max

    def test_volume_down(self):
        self.tv6.volume_down()
        assert str(self.tv6) == "Power = [False], Channel = [0], Volume = [0]" # Powered off, tries to down volume
        self.tv6.power()
        self.tv6.volume_up()
        self.tv6.volume_up()
        self.tv6.volume_down()
        assert str(self.tv6) == "Power = [True], Channel = [0], Volume = [1]" # Powered on, volume to max, then volume down
        self.tv6.mute()
        self.tv6.volume_down()
        assert str(self.tv6) == "Power = [True], Channel = [0], Volume = [0]" # Powered on, muted, the volume down
        self.tv6.volume_down()
        assert str(self.tv6) == "Power = [True], Channel = [0], Volume = [0]" # Powered on, then volume down 1 below the min


