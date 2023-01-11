import tkinter as tk

class interfaz():
    def __init__(self):
        
        self.ventana = tk.Tk()
        self.ventana.title('Algoritmo Genetico Canonico')
        self.ventana.geometry('530x500')
        self.ventana.config(background="#026793")
        self.ventana.resizable(0,0)

        # self.label_Rango = tk.Label(self.ventana, text='RANGO ')
        # self.label_Rango.place(x=40, y=50)
        # self.label_Rango.config(background="#026793", foreground='white', font=('Helveica',14,'bold'))

        self.label_Vmaximo = tk.Label(self.ventana, text='Xmin : ')
        self.label_Vmaximo.place(x=40, y=90)
        self.label_Vmaximo.config(background="#026793", foreground='white', font=('Helveica',13,'bold'))

        self.label_Vminimo = tk.Label(self.ventana, text='Xmax : ')
        self.label_Vminimo.place(x=280, y=90)
        self.label_Vminimo.config(background="#026793", foreground='white', font=('Helveica',13,'bold'))

        self.label_Intervalo = tk.Label(self.ventana, text='Intervalo : ')
        self.label_Intervalo.place(x=40, y=150)
        self.label_Intervalo.config(background="#026793", foreground='white', font=('Helveica',13,'bold'))

        self.label_PoblacionInicial = tk.Label(self.ventana, text='| Po | : ')
        self.label_PoblacionInicial.place(x=40, y=210)
        self.label_PoblacionInicial.config(background="#026793", foreground='white', font=('Helveica',13,'bold'))

        self.label_PoblacionMaxima = tk.Label(self.ventana, text='Pmax : ')
        self.label_PoblacionMaxima.place(x=280, y=210)
        self.label_PoblacionMaxima.config(background="#026793", foreground='white', font=('Helveica',13,'bold'))

        self.label_PoblabilidadCruza = tk.Label(self.ventana, text='Pcruza : ')
        self.label_PoblabilidadCruza.place(x=40, y=270)
        self.label_PoblabilidadCruza.config(background="#026793", foreground='white', font=('Helveica',13,'bold'))

        self.label_PmutacionIndividual = tk.Label(self.ventana, text='Pm_Indv : ')
        self.label_PmutacionIndividual.place(x=40, y=330)
        self.label_PmutacionIndividual.config(background="#026793", foreground='white', font=('Helveica',13,'bold'))

        self.label_PmutacionGen = tk.Label(self.ventana, text='Pm_Gen : ')
        self.label_PmutacionGen.place(x=280, y=330)
        self.label_PmutacionGen.config(background="#026793", foreground='white', font=('Helveica',13,'bold'))

        # entrada de datos

        self.valor_Minimo = tk.Entry(self.ventana, font=('Helveica',13))
        self.valor_Minimo.place(x=120, y=90, width=120)
        
        self.valor_Maximo = tk.Entry(self.ventana, font=('Helveica',13))
        self.valor_Maximo.place(x=360, y=90, width=120)
        
        self.valor_Intervalo = tk.Entry(self.ventana, font=('Helveica',13))
        self.valor_Intervalo.place(x=140, y=150, width=100)

        self.valor_PoblacionInicial = tk.Entry(self.ventana, font=('Helveica',13))
        self.valor_PoblacionInicial.place(x=120, y=210, width=120)

        self.valor_PoblacionMaxima = tk.Entry(self.ventana, font=('Helveica',13))
        self.valor_PoblacionMaxima.place(x=360, y=210, width=120)

        self.valor_ProbabilidadCruza = tk.Entry(self.ventana, font=('Helveica',13))
        self.valor_ProbabilidadCruza.place(x=124, y=270, width=120)

        self.valor_MutacionIndividual = tk.Entry(self.ventana, font=('Helveica',13))
        self.valor_MutacionIndividual.place(x=130, y=330, width=120)

        self.valor_MutacionGen = tk.Entry(self.ventana, font=('Helveica',13))
        self.valor_MutacionGen.place(x=370, y=330, width=110)

        self.btn_GraficaFormula = tk.Button(self.ventana, text='Grafica Formula', width=15, height=1, font=('Helveica',11), command=lambda:"")
        self.btn_GraficaFormula.place(x=50, y=415)

        self.btn_IniciarProceso = tk.Button(self.ventana, text='Grafica Formula', width=15, height=1, font=('Helveica',11), command=lambda:"")
        self.btn_IniciarProceso.place(x=50, y=415)
        
        self.ventana.mainloop()

ven_Principal = interfaz()
        