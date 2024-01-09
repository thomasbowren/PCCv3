def main():

    albums = []

    for _ in range(3):
        print()
        a_name = input('Artist: ')
        a_title = input('Album Title: ')
        n_songs = input('How many songs: ')
        album = make_album(a_name, a_title, n_songs)
        albums.append(album)

    for album in albums:
        print_album(album)
        print()    

def make_album(name, title, songs=None):
    new_album = {'artist': name, 'album': title}
    if songs:
        new_album['songs'] = songs
    return new_album

def print_album(raw_album):
    for album_stat, value in raw_album.items():
        print(f"\n{album_stat.title()}: {value.title()}")

if __name__ == "__main__":
    main()