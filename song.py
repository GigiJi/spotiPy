
class Song:
    def __init__(self, title, releaseYear, duration = 60, likes = 0):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__duration = duration
        self.__likes = likes

    def getTitle(self):
        return self.__title
    def getReleaseYear(self):
        return self.__releaseYear
    def getDuration(self):
        return self.__duration
    def getLikes(self):
        return self.__likes

    def setDuration(self,dur):
        if dur < 0 or dur > 720 or dur == self.__duration:
            return False
        else:
            self.__duration = dur
            return True

    def like(self):
        self.__likes += 1
    def unLike(self):
        self.__likes -= 1

    def __str__(self):
        return f"Title:{self.__title},Duration:{self.__duration / 60} minutes,Release year:{self.__releaseYear},Likes:{self.__likes}"