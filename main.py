from tkinter import *
import networkx as nx
import pylab as plt
from tkinter.messagebox import *

class Main:
    def __init__(self):
        self.window_3_adjacency = Tk()
        self.window_3_adjacency.geometry("+500+250")
        self.list = Listbox(self.window_3_adjacency, height=18)

        self.frame_3_adjacency = Frame(self.window_3_adjacency)

        self.lable_aj_2 = Label(self.frame_3_adjacency, text="введіть кількість вершин")
        self.lable_aj_2.pack()
        self.E_1_aj = Entry(self.frame_3_adjacency, width=5)
        self.E_1_aj.pack()
        self.frame_3_adjacency.pack()

        self.number_of_vertex = 0

        self.botton_1_adjacency = Button(self.frame_3_adjacency, text="задати кількість ребр",
                                         command=self.set_power_of_aj)
        self.botton_1_adjacency.pack()
        self.botton_2_adjacency = Button(self.frame_3_adjacency, text="створити матрицю",
                                         command=self.make_matrix_adjacency)
        self.botton_2_adjacency.pack()

        self.frame_for_matrix_aj = Frame(self.window_3_adjacency)
        self.frame_for_matrix_aj.pack()

        self.window_3_adjacency.mainloop()

    def set_power_of_aj(self):
        try:
            self.number_of_vertex = int(self.E_1_aj.get())
        except:
            showerror("Помилка !",
                      "Тип данних не є прийнятним та містить недопустимі символи для задання кількості ребр, або данні є відсутніми.")


    def make_matrix_adjacency(self):
        self.A_aj = [[0 for i in range(self.number_of_vertex)] for i in range(self.number_of_vertex)]

        for i in range(self.number_of_vertex):
            a = Label(self.frame_for_matrix_aj, text=i + 1)
            a.grid(row=i + 1, column=0)

        for i in range(self.number_of_vertex):
            a = Label(self.frame_for_matrix_aj, text=i + 1)
            a.grid(row=0, column=i + 1)

        for i in range(self.number_of_vertex):
            for j in range(self.number_of_vertex):
                self.A_aj[i][j] = Entry(self.frame_for_matrix_aj, width=5)
                self.A_aj[i][j].grid(row=i + 1, column=j + 1)

        d = Button(self.window_3_adjacency, command=self.graph_aj, text="створити граф")
        d.pack()

    def graph_aj(self):
        self.A_2_adj=[]
        for i in range(self.number_of_vertex):
            for j in range(self.number_of_vertex):
                if self.A_aj[i][j].get()=="1":
                    self.A_2_adj.append([i+1,j+1])


        G = nx.DiGraph()
        G.add_edges_from(self.A_2_adj, color='b')
        nx.draw(G, with_labels=True)
        plt.show()

a=Main()