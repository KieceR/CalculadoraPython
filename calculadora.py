#======import=============
import tkinter as tk

#=======global var========
operator = ''
operation = ''
nop = ['/', '*', '+', '-']
nops = ['/', '*']

#=======define============
def click(number):
    global operator
    if len(operator) == 19:
        return
    operator += str(number)
    if len(operator) == 1:
        if operator[0] in nops:
            operator = ''
    if len(operator) > 2:
        if operator[-3] in nop and operator[-2] in nop and operator[-1] in nop:
            operator = operator[:-1]
    if len(operator) > 1:
        if operator[-2] in nop and operator[-1] in nops:
            operator = operator[:-2] + operator[-1]
    visor['text'] = operator
   
def Clear():
    global operator
    operator = ''
    visor['text'] = operator

def delete():
    global operator
    operator = operator[:-1]
    visor['text'] = operator
    pass
    
def Igual():
    global operator
    if operator[-1] == '.':
        operator += '0'
    visor['text'] = eval(operator)
    operator = str(eval(operator))
    pass

def MM():
    global operator
    operator = str(-(float(operator)))
    visor['text'] = operator

#========root=============
root = tk.Tk()
root.title('Caculadora')

#=======widgets===========
visor = tk.Label(root, text = '', fg = 'white', font = 'Consolas 20 bold', width = 20, height = 3, bg = '#333333', anchor = 'e')
visor.grid(column = 0, row = 0, columnspan = 4, sticky = 'snew')

b1 = tk.Button(root, text = "CLEAR",font = 'Consolas 14 bold', command = Clear, width = 5, height = 2, bg = '#CCCCCC',
               bd = 1)
b1.grid(column = 0, row = 1, sticky = 'snew')

bdelete = tk.Button(root, text = "DEL",font = 'Consolas 14 bold', command = delete, width = 5, height = 2, bg = '#CCCCCC',
                    bd = 1)
bdelete.grid(column = 1, row = 1, sticky = 'snew')

bMM = tk.Button(root, text = "+/-",font = 'Consolas 14 bold', command = MM, width = 5, height = 2, bg = '#CCCCCC',
                    bd = 1)
bMM.grid(column = 2, row = 1, sticky = 'snew')

b2 = tk.Button(root, text = "÷", font = 'Consolas 14 bold', command = lambda: click('/'), width = 5, height = 2, bg = '#83D4C0',
               bd = 1)
b2.grid(column = 3, row = 1, sticky = 'snew')

b3 = tk.Button(root, text = "7", font = 'Consolas 14 bold', command = lambda: click(7), width = 5, height = 2, bg = '#E0E0E0',
               bd = 1)
b3.grid(column = 0, row = 2, sticky = 'snew')

b4 = tk.Button(root, text = "8", font = 'Consolas 14 bold', command = lambda: click(8), width = 5, height = 2, bg = '#E0E0E0',
               bd = 1)
b4.grid(column = 1, row = 2, sticky = 'snew')

b5 = tk.Button(root, text = "9", font = 'Consolas 14 bold', command = lambda: click(9), width = 5, height = 2, bg = '#E0E0E0',
               bd = 1)
b5.grid(column = 2, row = 2, sticky = 'snew')

b6 = tk.Button(root, text = "×", font = 'Consolas 14 bold', command = lambda: click('*'), width = 5, height = 2, bg = '#83D4C0',
               bd = 1)
b6.grid(column = 3, row = 2, sticky = 'snew')

b7 = tk.Button(root, text = "4", font = 'Consolas 14 bold', command = lambda: click(4), width = 5, height = 2, bg = '#E0E0E0',
               bd = 1)
b7.grid(column = 0, row = 3, sticky = 'snew')

b8 = tk.Button(root, text = "5", font = 'Consolas 14 bold', command = lambda: click(5), width = 5, height = 2, bg = '#E0E0E0',
               bd = 1)
b8.grid(column = 1, row = 3, sticky = 'snew')

b9 = tk.Button(root, text = "6", font = 'Consolas 14 bold', command = lambda: click(6), width = 5, height = 2, bg = '#E0E0E0',
               bd = 1)
b9.grid(column = 2, row = 3, sticky = 'snew')

b10 = tk.Button(root, text = "-", font = 'Consolas 14 bold', command = lambda: click('-'), width = 5, height = 2, bg = '#83D4C0',
                bd = 1)
b10.grid(column = 3, row = 3, sticky = 'snew')

b11 = tk.Button(root, text = "1", font = 'Consolas 14 bold', command = lambda: click(1), width = 5, height = 2, bg = '#E0E0E0',
                bd = 1)
b11.grid(column = 0, row = 4, sticky = 'snew')

b12 =  tk.Button(root, text = "2", font = 'Consolas 14 bold', command = lambda: click(2), width = 5, height = 2, bg = '#E0E0E0',
                 bd = 1)
b12.grid(column = 1, row = 4, sticky = 'snew')

b13 = tk.Button(root, text = "3", font = 'Consolas 14 bold', command = lambda: click(3), width = 5, height = 2, bg = '#E0E0E0',
                bd = 1)
b13.grid(column = 2, row = 4, sticky = 'snew')

b14 = tk.Button(root, text = "+", font = 'Consolas 14 bold', command = lambda: click('+'), width = 5, height = 2, bg = '#83D4C0',
                bd = 1)
b14.grid(column = 3, row = 4, sticky = 'snew')

b15 = tk.Button(root, text = "0", font = 'Consolas 14 bold', command = lambda: click(0), width = 5, height = 2, bg = '#E0E0E0', bd = 1)
b15.grid(column = 0, row = 5, columnspan = 2, sticky = 'snew')

b16 = tk.Button(root, text = ",", font = 'Consolas 14 bold', command = lambda: click('.'), width = 5, height = 2, bg = '#E0E0E0', bd = 1)
b16.grid(column = 2, row = 5, sticky = 'snew')

b17 = tk.Button(root, text = "=", font = 'Consolas 14 bold', command = Igual, width = 5, height = 2, bg = '#83D4C0', bd = 1)
b17.grid(column = 3, row = 5, sticky = 'snew')

#=======mainloop==========
root.resizable(width=False, height=False)
root.mainloop()
