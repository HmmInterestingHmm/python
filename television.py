class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

        return self.__status

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

        return self.__muted

    def channel_up(self):
        if not self.__status:
            return self.__channel

        self.__channel += 1
        if self.__channel > Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL

        return self.__channel

    def channel_down(self):
        if not self.__status:
            return self.__channel

        self.__channel -= 1
        if self.__channel < Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL

        return self.__channel

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME


        return self.__volume

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME


        return self.__volume

    def __str__(self):
        if self.__muted:
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [0]"
        else:
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"