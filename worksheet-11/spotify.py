class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def addSong(self, song):
        self.songs.append(song)

    def removeSong(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def displayPlaylist(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f"- {song}")


class Spotify:
    def __init__(self):
        self.playlists = []

    def createPlaylist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def displayPlaylists(self):
        print("Existing Playlists:")
        for playlist in self.playlists:
            print(f"- {playlist.name}")

    def displayMenu(self):
        print("\nSpotify Playlist Management Menu:")
        print("1. Create Playlist")
        print("2. Display Playlists")
        print("3. Add Song to Playlist")
        print("4. Remove Song from Playlist")
        print("5. View Songs in Playlist")
        print("6. Quit")


def testSpotify():
    spotify = Spotify()

    playlist1 = spotify.createPlaylist("My Favorites")
    playlist2 = spotify.createPlaylist("Chill Vibes")

    song1 = Song("Cut - 1990 Demo", "The Cure")
    song2 = Song("Grace", "Jeff Buckley")
    song3 = Song("It's Oh So Quiet", "Bjork")
    song4 = Song("Sour Times", "Portishead")
    song5 = Song("Beetlebum - 2012 Remaster", "Blur")

    playlist1.addSong(song1)
    playlist1.addSong(song2)
    playlist2.addSong(song3)
    playlist2.addSong(song4)
    playlist2.addSong(song5)

    while True:
        spotify.displayMenu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the name of the new playlist: ")
            new_playlist = spotify.createPlaylist(name)
            print(f"Playlist '{new_playlist.name}' created.")
        elif choice == "2":
            spotify.displayPlaylists()
        elif choice == "3":
            spotify.displayPlaylists()
            playlist_name = input("Enter the name of the playlist: ")
            playlist = next((pl for pl in spotify.playlists if pl.name == playlist_name), None)
            if playlist:
                title = input("Enter the title of the song: ")
                artist = input("Enter the artist of the song: ")
                new_song = Song(title, artist)
                playlist.addSong(new_song)
                print(f"Song '{new_song}' added to the playlist '{playlist_name}'.")
            else:
                print("Playlist not found.")
        elif choice == "4":
            spotify.displayPlaylists()
            playlist_name = input("Enter the name of the playlist: ")
            playlist = next((pl for pl in spotify.playlists if pl.name == playlist_name), None)
            if playlist:
                print("Songs in the playlist:")
                for idx, song in enumerate(playlist.songs):
                    print(f"{idx + 1}. {song}")
                song_idx = int(input("Enter the number of the song to remove: ")) - 1
                if 0 <= song_idx < len(playlist.songs):
                    removed_song = playlist.songs.pop(song_idx)
                    print(f"Song '{removed_song}' removed from the playlist '{playlist_name}'.")
                else:
                    print("Invalid song number.")
            else:
                print("Playlist not found.")
        elif choice == "5":
            spotify.displayPlaylists()
            playlist_name = input("Enter the name of the playlist: ")
            playlist = next((pl for pl in spotify.playlists if pl.name == playlist_name), None)
            if playlist:
                playlist.displayPlaylist()
            else:
                print("Playlist not found.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    testSpotify()
