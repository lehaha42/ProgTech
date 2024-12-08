import tkinter as tk


class Main:
    def __init__(self):
        self.r = tk.Tk()
        self.r.title('laba4')
        self.r.geometry('240x280')

        self.arr = [0 for _ in range(9)]
        self.n = 0

        temp = [lambda: self.press(0), lambda: self.press(1), lambda: self.press(2), lambda: self.press(3), lambda: self.press(4), lambda: self.press(5), lambda: self.press(6), lambda: self.press(7), lambda: self.press(8)]
        self.buttonArr = [tk.Button(self.r, command=temp[i]) for i in range(9)]
        for i in range(3):
            for j in range(3):
                self.buttonArr[i+3*j].place(x=i*80, y=j*80, width=80, height=80)

        self.label = tk.Label(self.r, text='')
        self.label.place(x=0, y=250)

        self.r.mainloop()

    def press(self, n):
        if self.arr[n] != 0:
            return
        if self.n % 2 == 0:
            self.arr[n] = 1
            self.buttonArr[n].config(text='X', font=['Calibri', 24])
        else:
            self.arr[n] = -1
            self.buttonArr[n].config(text='0', font=['Calibri', 24])
        self.n += 1
        f = 0
        for i in range(3):
            if self.arr[3*i] + self.arr[3*i+1] + self.arr[3*i+2] == 3:
                f = 1
                break
            if self.arr[3*i] + self.arr[3*i+1] + self.arr[3*i+2] == -3:
                f = -1
                break
            if self.arr[i] + self.arr[i+3] + self.arr[i+6] == 3:
                f = 1
                break
            if self.arr[i] + self.arr[i+3] + self.arr[i+6] == -3:
                f = -1
                break
        if self.arr[0] + self.arr[4] + self.arr[8] == 3:
            f = 1
        if self.arr[0] + self.arr[4] + self.arr[8] == -3:
            f = -1
        if self.arr[2] + self.arr[4] + self.arr[6] == 3:
            f = 1
        if self.arr[2] + self.arr[4] + self.arr[6] == -3:
            f = -1
        self.label.config(text='')
        if f != 0 or self.n > 8:
            s = 'никто'
            if f == 1:
                s = 'X'
            if f == -1:
                s = '0'
            self.label.config(text=f'победил {s}!')
            for i in range(9):
                self.arr[i] = 0
                self.buttonArr[i].config(text='')
                self.n = 0


if __name__ == '__main__':
    Main()
