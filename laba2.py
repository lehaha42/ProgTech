import tkinter as tk


class Main:
    def __init__(self):
        self.r = tk.Tk()
        self.r.title('laba2')
        self.r.geometry('200x150')

        self.label = tk.Label(self.r, text='ax^2 + bx + c = 0')
        self.label.place(x=0, y=0)
        self.label1 = tk.Label(self.r, text='a =')
        self.label1.place(x=0, y=20)
        self.label2 = tk.Label(self.r, text='b =')
        self.label2.place(x=0, y=40)
        self.label3 = tk.Label(self.r, text='c =')
        self.label3.place(x=0, y=60)
        self.label4 = tk.Label(self.r)
        self.label4.place(x=0, y=105)

        self.entry1 = tk.Entry(self.r)
        self.entry1.place(x=25, y=20)
        self.entry2 = tk.Entry(self.r)
        self.entry2.place(x=25, y=40)
        self.entry3 = tk.Entry(self.r)
        self.entry3.place(x=25, y=60)

        self.button = tk.Button(self.r, text='вычислить', command=self.calc)
        self.button.place(x=0, y=80)

        self.r.mainloop()

    def calc(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            c = float(self.entry3.get())
            d = b*b - 4*a*c
            if d < 0:
                self.label4.config(text=f'нет корней')
            else:
                self.label4.config(text=f'x1 = {(-b+d**0.5)/(2*a)}\nx2 = {(-b-d**0.5)/(2*a)}')
        except:
            self.label4.config(text=f'неправильный ввод')


if __name__ == '__main__':
    Main()
