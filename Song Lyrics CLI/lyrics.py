import sys
import re
import urllib.request
from bs4 import BeautifulSoup

user_artist = ""
user_song_title = ""


def get_lyrics(artist, song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub("[^A-Za-z0-9]+", "", artist)
    song_title = re.sub("[^A-Za-z0-9]+", "", song_title)
    if artist.startswith(
        "the"
    ):  # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/" + artist + "/" + song_title + ".html"

    try:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, "html.parser")
        lyrics = str(soup)
        # lyrics lies between up_partition and down_partition
        up_partition = "<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->"
        down_partition = "<!-- MxM banner -->"
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        return (
            lyrics.replace("<br/>", "")
            .replace("<i>", "")
            .replace("</i>", "")
            .replace("</div>", "")
            .strip()
        )
    except Exception:
        return "Song not found, maybe you have misspelled it."


if __name__ == "__main__":
    try:
        try:
            user_song_title = sys.argv[1]
        except IndexError:
            user_song_title = input("Enter Song Title: ")
        try:
            user_artist = sys.argv[2]
        except IndexError:
            user_artist = input("Enter Artist Name: ")
        if sys.argv[3] == "-s" or sys.argv[3] == "--save":
            with open("C:/Users/Avaneesh/Desktop/lyrics.txt", "w") as file:
                file.write(get_lyrics(user_artist, user_song_title))
            print("Lyrics saved successfully")
        else:
            # print(get_lyrics(user_artist, user_song_title))
            print(get_lyrics(user_artist, user_song_title))
    except KeyboardInterrupt:
        exit(0)
