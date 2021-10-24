from tkinter import *
global b,o,d,h,pocet,kod,j,f,button21,button23,dolezite,t
h = 0
root = Tk()
root.configure(bg='white')
root.attributes('-fullscreen', True)
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
button_font, label_font = width // 100, width // 300
canvas = Canvas(root, width=width, height=height, bg='lightgrey')
canvas.place(x=0, y=0)
changings = {}

canvas.create_rectangle((width / 20)*6,(height / 20)*2,(width / 20)*18,(height / 20)*18,fill  = 'white')
canvas.create_rectangle(0,(height / 20)*2,(width/20)*4.5,(height / 20)*20,fill  = 'white',outline = 'white')
canvas.create_rectangle(0,0,(width/20)*4.5,(height / 20)*3,fill  = '#679222',outline = '#679222')
canvas.create_rectangle((width / 20)*6,(height / 20)*2,(width / 20)*18,(height / 20)*4,fill  = 'silver')

canvas.create_line((width / 20)*12,(height / 20)*4,(width / 20)*12,(height / 20)*18,fill  = 'black')
#Label(root, bg='#679222',
     # width=width//35,
      #height=11).place(x=-3.5, y=-8.5)

Label(root, text='SKLAD',
      font='Roboto {}'.format(button_font + 10),
      bg='#679222',).place(x=width / 13, y=height / 20 * 1.6)
Label(root, text='Kód:',
      font='Roboto {}'.format(button_font + 10),
      bg='silver',).place(x=(width / 20)*8.5, y=(height / 20) * 2.5)
Label(root, text='Počet na sklade:',
      font='Roboto {}'.format(button_font + 10),
      bg='silver',).place(x=(width / 20)*13, y=(height / 20) * 2.5)
f = 0

#####
def vyhladavanie():
    canvas.create_rectangle(width/20*9,height/20*0.5,width/20*17,height/20*1.5,fill = 'white',outline = 'white')
    canvas.create_text(width/20*7.5,height/20*1,text = 'Vyhladavanie:',font='Roboto {}'.format(button_font + 5))
vyhladavanie()

####
def objednavka():
    global f,entry
    f = 0
    for i in range(8):
        entry = Entry(canvas, textvariable='daco')
        
        entry.place(x=width/20*16, y=height/20*4.5 + f)
        
        f = f+height/20
        entry.delete(0, 'end')
    potvrdenieman()
    



def polo():
    canvas.create_rectangle(width/20*8,height/20*6,width/20*16,height/20*14,fill='grey',tags = 'spat')
    canvas.create_text(width/20*12,height/20*7,text='Z kazdeho produktu bude',font='Roboto {}'.format(button_font + 3),tags = 'spat')
    canvas.create_rectangle(width/20*11.5,height/20*8,width/20*12.5,height/20*8.5,fill='white',tags = 'spat')
    potvrdenie()

def auto():
    canvas.create_rectangle(width/20*8,height/20*6,width/20*16,height/20*14,fill='grey',tags = 'spat')
    canvas.create_text(width/20*12,height/20*7,text='Tovary sa automaticky doplnia na hodnotu 20',font='Roboto {}'.format(button_font + 3),tags = 'spat')
    potvrdenie()

def potvrdenie():
    global button21,button23
    button23 = Button(root, text='Potvrdiť',
                    
                font='Roboto {}'.format(button_font),
                width=10,
                bg='#98C151',
                relief=RAISED,
                bd=3,
                activebackground='#98C151',
                command=reset)
    button23.place(x=width / 20*13.5, y=height / 20 * 11)
    button21 = Button(root, text='Zrušiť',
                    
                font='Roboto {}'.format(button_font),
                width=10,
                bg='#98C151',
                relief=RAISED,
                bd=3,
                activebackground='#98C151',
                command=reset)
    button21.place(x=width /20*8.5, y=height / 20 * 11)

def potvrdenieman():
    global button24
    button24 = Button(root, text='Potvrdiť',
                    
                font='Roboto {}'.format(button_font),
                width=8,
                bg='#98C151',
                relief=RAISED,
                bd=3,
                activebackground='#98C151',
                command=reset)
    button24.place(x=width / 20*18.15, y=height / 20 * 3)
    
    
dolezite = 0  
kod = []
pocet = []
kod1 = []
pocet1 = []
o = 0
d = 1
medzi = height/20
def kon():
    global o,d,b,dolezite
    d = 1
    canvas.delete('aah')
    with open('Sklad.txt') as file:
        cele = file.readline()
        
        cele = file.readline()
        while cele !='':
        #file = file.read().rstrip().split('\n')[1:]
            for i in cele:
                o=o+1
                
                if i==';':
                    b = o
                    #print(b)
            kod = cele[:b-1]
            pocet = cele[b:]
            kod1.append(kod)
            pocet1.append(int(pocet))
            
            o  =0
            cele = file.readline()
        for i in range(13):
            if dolezite <= len(kod1):
            
                #print(kod1,pocet1)
                canvas.create_text((width/20)*15,(height/20)*4+(medzi*d),text = pocet1[i+dolezite],font  ='Roboto {}'.format(button_font + 10),tags = 'aah',)
                canvas.create_text((width/20)*9,(height/20)*4+(medzi*d),text = kod1[i+dolezite],font  ='Roboto {}'.format(button_font + 10),tags = 'aah' )
                d += 1
            
            
kon()
def pes():
    
    global pocet1,kod1,d
    pocet1, kod1 = (list(t) for t in zip(*sorted(zip(pocet1, kod1))))
    #sort(pocet1)#sooooooort
    #print(kod1,pocet1)
    canvas.delete('aah')
    d=0
    for i in pocet1:
        canvas.create_text((width/20)*15,(height/20)*4+(medzi*(d+1)),text = pocet1[d],font  ='Roboto {}'.format(button_font + 10),tags = 'aah' )
        canvas.create_text((width/20)*9,(height/20)*4+(medzi*(d+1)),text = kod1[d],font  ='Roboto {}'.format(button_font + 10),tags = 'aah' )
        d += 1
        o  =0
    kod1=[]
    pocet1=[]
j=0
t =1
def dog():
    global j
    if j == 1:
        kon()
        j=0
    else:
        pes()
        j=1
def test():
    pass

canvas.create_rectangle(width/20*11.5,height/20*16.5,width/20*12.5,height/20*17.5,fill = 'white',outline  = 'white')
canvas.create_text(width/20*12,height/20*17,text = t,font  ='Roboto {}'.format(button_font + 10),tags = 'strana',)
def bruh():
    global dolezite,t
    canvas.delete('strana')
    dolezite +=12
    t = t+1
    canvas.create_text(width/20*12,height/20*17,text = t,font  ='Roboto {}'.format(button_font + 10),tags = 'strana',)
    kon()
    
def bruh1():
    global dolezite,t
    canvas.delete('strana')
    if dolezite >=12:
        dolezite -=12
        t = t-1
        canvas.create_text(width/20*12,height/20*17,text = t,font  ='Roboto {}'.format(button_font + 10),tags = 'strana',)
        
    kon()
def reset():
    global button21,button23,entry,button24
    canvas.delete('spat')
    button21.destroy()
    button23.destroy()
    button24.destroy()
    entry.destroy()

button = Button(root, text='Manuálna objednávka',
                font='Roboto {}'.format(button_font),
                width=23,
                bg='#98C151',
                relief=RAISED,
                bd=3,
                activebackground='#98C151',
                command=objednavka)
button.place(x=width / 400, y=height / 20 * 4)


button1 = Button(root, text='Poloautomatická objednávka',
                 font='Roboto {}'.format(button_font),
                 width=23,
                 bg='#98C151',
                 relief=RAISED,
                 bd=3,
                 
                 activebackground='#98C151',
                 command=polo)
button1.place(x=width / 400, y=height / 20 * 6)

button2 = Button(root, text='Automatická objednávka',
                 font='Roboto {}'.format(button_font),
                 width=23,
                 bg='#98C151',
                 relief=RAISED,
                 bd=3,
                 activebackground='#98C151',
                 command=auto)
button2.place(x=width / 400, y=height / 20 * 8)

button25 = Button(root, text='<',
                    
                font='Roboto {}'.format(button_font),
                width=5,
                bg='silver',
                relief=RAISED,
                bd=3,
                activebackground='silver',
                command=bruh1)
button25.place(x=width / 20*6, y=height / 20 * 16.75)
button26 = Button(root, text='>',
                    
                font='Roboto {}'.format(button_font),
                width=5,
                bg='silver',
                relief=RAISED,
                bd=3,
                activebackground='silver',
                command=bruh)
button26.place(x=width / 20*17, y=height / 20 * 16.75)


button5 = Button(root, text='Späť',
                 font='Roboto {}'.format(button_font),
                 width=15,
                 bg='#98C151',
                 relief=RAISED,
                 bd=3,
                 activebackground='#98C151',
                 command=reset)
button5.place(x=width / 20, y=height / 20 * 14)

button6 = Button(root, text='Zoradiť/Všetko',
                 font='Roboto {}'.format(button_font),
                 width=15,
                 bg='#98C151',
                 relief=RAISED,
                 bd=3,
                 activebackground='#98C151',
                 command=dog)
button6.place(x=width / 20, y=height / 20 * 16)


previous = button














root.bind('<Escape>', lambda event: root.destroy())
if __name__ == '__main__':
    root.mainloop()
