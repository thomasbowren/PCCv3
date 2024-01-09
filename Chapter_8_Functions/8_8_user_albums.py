def main():

    albums = make_album_list()
        
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

def make_album_list():
    albums = []
    while True:
        albums_list = []
        print("\n")
        a_name = input('Artist: ')
        albums_list.append(a_name)
        a_title = input('Album Title: ')
        albums_list.append(a_title)
        n_songs = input('How many songs: ')
        albums_list.append(n_songs)
        album = make_album(albums_list[0], albums_list[1], albums_list[2])
        albums.append(album)
        if input("Press 'q' to quit, or any other key to continue: ") == 'q':
            return albums



if __name__ == "__main__":
    main()