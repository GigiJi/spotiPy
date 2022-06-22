from SpotiPy.album import Album
from SpotiPy.artist import Artist
from SpotiPy.song import Song


class SpotiPy:
    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists

    def addArtists(self, *artists):
        artArr = []
        str1 = ''
        for artist in artists:
            for a in self.__artists:
                str1 += a.getFirstName() + a.getSecondName() + str(a.getBirthYear())
                artArr.append(str1)
                str1 = ''
            if artist.getFirstName() + artist.getSecondName() + str(artist.getBirthYear()) not in artArr:
                self.__artists.append(artist)
        return self.__artists

    def getTopTrendingArtist(self):
        arr = []
        for artist in self.__artists:
            arr.append(artist.totalLikes())
        ind = arr.index(max(arr))
        tpl = (self.__artists[ind].getFirstName(), self.__artists[ind].getSecondName())
        return tpl

    def getTopTrendingAlbum(self):
        arr = []
        for artist in self.__artists:
            for album in artist.getAlbums():
                sum = 0
                for song in album.getSongs():
                    sum += song.getLikes()
                if len(arr) == 0:
                    arr.append(sum)
                    arr.append(album)
                else:
                    if sum > arr[0]:
                        arr[0] = sum
                        arr[1] = album
        return arr[1].getTitle()

    def getTopTrendingSong(self):
        arr = []
        for artist in self.__artists:
            for album in artist.getAlbums():
                reversed = album.sortByPopularity(False)
                popSong = reversed[0]
                if len(arr) == 0:
                    arr.append(popSong)
                else:
                    if popSong.getLikes() > arr[0].getLikes():
                        arr[0] = popSong
            for song in artist.getSingle():
                if len(arr) == 0:
                    arr[0] = song
                else:
                    if song.getLikes() > arr[0].getLikes():
                        arr[0] = song
        return arr[0].getTitle()


# 3 helper functions for LoadFromFile function
def getArtist(str1):
    artistStr = ''
    artNameLst = []
    for char in str1:  # getting the info for the first artist
        if char != '{':
            if char != ',':
                artistStr += char
            else:
                artNameLst.append(artistStr)
                artistStr = ''
        else:
            break
    return artNameLst

def getAlbum(str1):
    albumStr = ''
    albList = []
    for char in str1:  # getting the album info
        if char != '{':
            if char != ',':
                albumStr += char
            else:
                albList.append(albumStr)
                albumStr = ''
        else:
            break
    realList = []
    albName = albList[0]
    albyear = int(albList[1])
    alb = Album(albName,albyear)
    return alb

def getSong(str1):
    ind = str1.index("}")
    songStr = ''
    lstSong = []
    bList = []
    for index in range(ind):
        if str1[index] != "|":
            if str1[index] != ",":
                songStr += str1[index]
            else:
                lstSong.append(songStr)
                songStr = ''
        else:
            lstSong.append(songStr)
            songStr = ''
            bList.append(lstSong)
            lstSong = []

            pass
    lstSong.append(songStr)
    bList.append(lstSong)
    realList =[]
    for lst in bList:
        songName = lst[0]
        songDur = float(lst[1][:3])
        songYear = int(lst[2])
        songLikes = int(lst[3])
        newSong = Song(songName,songYear,songDur, songLikes)
        realList.append(newSong)
    return realList

