import tkinter as tk
import tkinter.ttk as ttk


class Main:
    def __init__(self):
        self.r = tk.Tk()
        self.r.title('laba3')
        self.r.geometry('280x140')

        self.n = 0
        self.ans = 0

        self.label1 = tk.Label(self.r, text='0')
        self.label1.place(x=140, y=25)
        self.label2 = tk.Label(self.r, text='0')
        self.label2.place(x=140, y=65)
        self.label3 = tk.Label(self.r, text='0')
        self.label3.place(x=0, y=110)
        self.label4 = tk.Label(self.r, text='0')
        self.label4.place(x=140, y=110)

        self.entry1 = tk.Entry(self.r)
        self.entry1.place(x=0, y=25)
        self.entry2 = tk.Entry(self.r)
        self.entry2.place(x=0, y=65)

        self.button1 = tk.Button(self.r, text='2', command=self.calc1)
        self.button1.place(x=140, y=0)
        self.button2 = tk.Button(self.r, text='=', command=self.calc2)
        self.button2.place(x=0, y=85)

        self.box = ttk.Combobox(self.r, values=['+', '-', '*', '/'])
        self.box.place(x=0, y=45)

        self.r.mainloop()

    def calc1(self):
        self.n += 1
        self.n %= 3
        self.button1.config(text=(['2', '8', '16'])[self.n])
        a, b, c = 0, 0, 0
        try:
            a = int(self.entry1.get())
        except:
            pass
        try:
            b = int(self.entry2.get())
        except:
            pass
        if self.n == 0:
            a = bin(a)
            b = bin(b)
            c = bin(self.ans)
        elif self.n == 1:
            a = oct(a)
            b = oct(b)
            c = oct(self.ans)
        else:
            a = hex(a)
            b = hex(b)
            c = hex(self.ans)
        self.label1.config(text=a[2:])
        self.label2.config(text=b[2:])
        self.label4.config(text=c[2:])

    def calc2(self):
        c, a, b = '', 0, 0
        try:
            c = self.box.get()
            a = int(self.entry1.get())
            b = int(self.entry2.get())
        except:
            pass
        if c == '+':
            self.ans = a + b
        elif c == '-':
            self.ans = a - b
        elif c == '*':
            self.ans = a * b
        elif c == '/':
            self.ans = a // b
        self.label3.config(text=str(self.ans))


if __name__ == '__main__':
    Main()
