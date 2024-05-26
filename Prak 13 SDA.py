class Graph:
    def __init__(self):
        self.vertices = {}

    def tambah_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
            print(f"Vertex {vertex} ditambahkan.")
        else:
            print(f"Vertex {vertex} sudah ada.")

    def hapus_vertex(self, vertex):
        if vertex in self.vertices:
            self.vertices.pop(vertex)
            for edges in self.vertices.values():
                edges.discard(vertex)
            print(f"Vertex {vertex} dihapus.")
        else:
            print(f"Vertex {vertex} tidak ditemukan.")

    def tambah_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
            print(f"Edge dari {vertex1} ke {vertex2} ditambahkan.")
        else:
            print("Salah satu atau kedua vertex tidak ditemukan.")

    def hapus_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if vertex2 in self.vertices[vertex1]:
                self.vertices[vertex1].remove(vertex2)
                self.vertices[vertex2].remove(vertex1)
                print(f"Edge dihapus antara {vertex1} dan {vertex2}.")
            else:
                print("Edge tidak ditemukan.")
        else:
            print("Salah satu atau kedua vertex tidak ditemukan.")

    def tampilkan_graph(self):
        print("Graph saat ini:")
        for vertex, edges in self.vertices.items():
            print(f"{vertex}: {list(edges)}")

def main():
    graph = Graph()
    while True:
        print("\nMenu Operasi Graph")
        print("1. Tambah Vertex")
        print("2. Hapus Vertex")
        print("3. Tambah Edge")
        print("4. Hapus Edge")
        print("5. Tampilkan Graph")
        print("6. Keluar")
        
        pilihan = input("Pilih operasi: ")
        
        if pilihan == '1':
            vertex = input("Masukkan vertex yang ingin ditambahkan: ")
            graph.tambah_vertex(vertex)
        elif pilihan == '2':
            vertex = input("Masukkan vertex yang ingin dihapus: ")
            graph.hapus_vertex(vertex)
        elif pilihan == '3':
            vertex1 = input("Masukkan vertex pertama dari edge: ")
            vertex2 = input("Masukkan vertex kedua dari edge: ")
            graph.tambah_edge(vertex1, vertex2)
        elif pilihan == '4':
            vertex1 = input("Masukkan vertex pertama dari edge: ")
            vertex2 = input("Masukkan vertex kedua dari edge: ")
            graph.hapus_edge(vertex1, vertex2)
        elif pilihan == '5':
            graph.tampilkan_graph()
        elif pilihan == '6':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()