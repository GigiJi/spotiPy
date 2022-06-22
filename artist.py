
class Artist:
    def __init__(self, firstName, lastName, birthYear, albums, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles

    def getFirstName(self):
        return self.__firstName
    def getSecondName(self):
        return self.__lastName
    def getBirthYear(self):
        return self.__birthYear
    def getAlbums(self):
        return self.__albums
    def getSingle(self):
        return self.__singles

    def mostLikedSong(self):
        songsArr = []
        for alb in self.__albums:
            for sng in alb.getSongs():
                if len(songsArr) == 0:
                    songsArr.append(sng)
                else:
                    if sng.getLikes() > songsArr[0].getLikes():
                        songsArr[0] = sng
        for s in self.__singles:
            if s.getLikes() > songsArr[0].getLikes():
                songsArr.clear()
                songsArr.append(s)
        return songsArr[0]

    def leastLikedSong(self):
        songsArr = []
        for alb in self.__albums:
            for sng in alb.getSongs():
                if len(songsArr) == 0:
                    songsArr.append(sng)
                else:
                    if sng.getLikes() < songsArr[0].getLikes():
                        songsArr[0] = sng
        for s in self.__singles:
            if s.getLikes() < songsArr[0].getLikes():
                songsArr.clear()
                songsArr.append(s)
        return songsArr[0]

    def totalLikes(self):
        likesArr = []
        count = 0
        for alb in self.__albums:
            for sng in alb.getSongs():
                likesArr.append(sng.getLikes())
        for s in self.__singles:
            likesArr.append(s.getLikes())
        for likes in likesArr:
            count += likes
        return count

    def __str__(self):
        return f"Name: {self.__firstName} {self.__lastName},Birth year:{self.__birthYear},Total likes:{self.totalLikes()}"