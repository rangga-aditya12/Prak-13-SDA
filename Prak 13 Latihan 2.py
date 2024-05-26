class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = [chr(ord('A') + i) for i in range(num_vertices)]
    
    def tambah_edge(self, start, end):
        if start < 0 or start >= self.num_vertices or end < 0 or end >= self.num_vertices:
            print("Index vertex tidak valid.")
        else:
            self.adj_matrix[start][end] = 1
            self.adj_matrix[end][start] = 1
            print(f"Edge ditambahkan antara {self.vertices[start]} dan {self.vertices[end]}.")

    def hapus_edge(self, start, end):
        if start < 0 or start >= self.num_vertices or end < 0 or end >= self.num_vertices:
            print("Index vertex tidak valid.")
        else:
            self.adj_matrix[start][end] = 0
            self.adj_matrix[end][start] = 0
            print(f"Edge dihapus antara {self.vertices[start]} dan {self.vertices[end]}.")

    def display(self):
        print(" ", " ".join(self.vertices))
        for i, row in enumerate(self.adj_matrix):
            print(self.vertices[i], " ".join(map(str, row)))

if __name__ == "__main__":
    num_vertices = int(input("Masukkan jumlah vertex: "))
    graph = Graph(num_vertices)

    while True:
        print("\nMenu Operasi Graph (Adjacency Matrix)")
        print("1. Tambah Edge")
        print("2. Hapus Edge")
        print("3. Tampilkan Graph")
        print("4. Keluar")
        pilihan = int(input("Pilih operasi: "))

        if pilihan == 1:
            start = int(input("Masukkan index vertex pertama: "))
            end = int(input("Masukkan index vertex kedua: "))
            graph.tambah_edge(start, end)
        elif pilihan == 2:
            start = int(input("Masukkan index vertex pertama: "))
            end = int(input("Masukkan index vertex kedua: "))
            graph.hapus_edge(start, end)
        elif pilihan == 3:
            graph.display()
        elif pilihan == 4:
            break
        else:
            print("Pilihan tidak valid.")
