
class Album:

    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def getTitle(self):
        return self.__title
    def getReleaseYear(self):
        return self.__releaseYear
    def getSongs(self):
        return self.__songs

    def addSongs(self, *songs):
        count = 0
        str1 = ''
        strArr = []
        for s in songs:
            for sng in self.__songs:
                str1 += sng.getTitle() + str(sng.getReleaseYear()) + str(sng.getDuration())
                strArr.append(str1)
                str1 = ''
            if (s.getTitle() + str(s.getReleaseYear()) + str(s.getDuration())) not in strArr:
                self.__songs.append(s)
                count += 1
        return count

    def sortBy(self, byKey, reverse):
        if reverse:
            return sorted(self.__songs, key=byKey)
        else:
            return sorted(self.__songs, key=byKey)[::-1]

    def sortByName(self, reverse):
        return self.sortBy(lambda x : x.getTitle(), reverse)
    def sortByPopularity(self, reverse):
        return self.sortBy(lambda x : x.getLikes(), reverse)
    def sortByDuration(self,reverse):
        return self.sortBy(lambda x : x.getDuration(), reverse)
    def sortByReleaseYear(self, reverse):
        return self.sortBy(lambda x : x.getReleaseYear(), reverse)

    def __str__(self):
        str1 = ""
        for s in self.__songs:
            str1 += s.__str__() + '|'
        str1 = str1[:len(str1)-1]
        return f"Title:{self.__title},Release year:{self.__releaseYear},songs:{'{' + str1 + '}'}"