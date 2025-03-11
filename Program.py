class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Lagu '{song}' telah ditambahkan ke playlist.")

    def remove_song(self, song):
        current = self.head
        previous = None
        while current:
            if current.song == song:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"Lagu '{song}' telah dihapus dari playlist.")
                return
            previous = current
            current = current.next
        print(f"Lagu '{song}' tidak ditemukan dalam playlist.")

    def play_song(self, song):
        current = self.head
        while current:
            if current.song == song:
                print(f"Memutar lagu: '{song}'")
                return
            current = current.next
        print(f"Lagu '{song}' tidak ditemukan dalam playlist.")

    def add_to_queue(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Lagu '{song}' telah ditambahkan ke antrian putar.")

    def display_playlist(self):
        current = self.head
        if not current:
            print("Playlist kosong.")
            return
        print("Playlist:")
        while current:
            print(f"- {current.song}")
            current = current.next

# Contoh penggunaan
if __name__ == "__main__":
    playlist = Playlist()
    
    # Menambahkan lagu
    playlist.add_song("Lagu 1")
    playlist.add_song("Lagu 2")
    playlist.add_song("Lagu 3")
    
    # Menampilkan playlist
    playlist.display_playlist()
    
    # Memutar lagu
    playlist.play_song("Lagu 2")
    
    # Menghapus lagu
    playlist.remove_song("Lagu 1")
    
    # Menampilkan playlist setelah penghapusan
    playlist.display_playlist()
    
    # Menambahkan lagu ke antrian
    playlist.add_to_queue("Lagu 4")
    
    # Menampilkan playlist setelah menambahkan antrian
    playlist.display_playlist()