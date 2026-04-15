class Television:
    """
    A class to represent a television's description.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to set default values for television.
        """

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to return power status of television.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True


    def mute(self) -> None:
        """
        Method to return mute status of television.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Method to increase channel of television.
        """
        if self.__status:

            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        """
        Method to decrease channel of television.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase volume of television.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method to decrease volume of television.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method to return string representation of television.
        :return: Description of television.
        """
        if self.__muted:
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [0]"
        return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"