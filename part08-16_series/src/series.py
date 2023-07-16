import statistics 

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = ", ".join(genres)
        self.ratings = []

    def info(self):
        if len(self.ratings) > 0:
            return f"{len(self.ratings)} ratings, average {statistics.mean(self.ratings):.1f} points"
        else:
            return 'no ratings'
        
    def rate(self, rating: int):
        if rating >= 0 and rating <= 5:
            self.ratings.append(rating)

    def __str__(self):
        return f"{self.title} ({self.seasons} seasons)\ngenres: {self.genres}\n{self.info()}"

def minimum_grade(rating: float, series_list: list):
    minimum_grade_list = []
    print(f"a minimum grade of {rating}:")
    for serie in series_list:
        if statistics.mean(serie.ratings) > rating:
            minimum_grade_list.append(serie)
    return minimum_grade_list
        
def includes_genre(genre: str, series_list: list):
    this_genre_list = []

    print(f"genre {genre}")
    for serie in series_list:
        if genre in serie.genres:
            this_genre_list.append(serie)
    return this_genre_list
        
if __name__ == "__main__":
    print('test 1')
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)

    print('test 2')
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    print('test 3')
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    series = [s1, s2, s3]

    vastaus = includes_genre("Crime", series)