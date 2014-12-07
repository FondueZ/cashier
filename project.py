from Tkinter import *

home = Tk()
home.geometry("1300x700")
####  SLIPT ZONE ########################################
        #Slipt Frame#
sliptframe = LabelFrame(home, text="This is a SliptFrame")
sliptframe.grid(row=0,column=0,sticky=W)
scrollbar = Scrollbar(sliptframe)
scrollbar.grid(ipadx = 140,ipady=150)

####  NUMPAD ZONE ########################################
        #Numpad Frame#
numpad = LabelFrame(home, text="This is a Numpad Frame")
numpad.grid()
numvar = IntVar()
        #Numpad Radiobutton#
n1 = Radiobutton(numpad,text = "1",indicatoron=0,value = 1,variable=numvar)
n1.grid(row=1,column=1,ipadx=40,ipady=40)
n2 = Radiobutton(numpad,text = "2",indicatoron=0,value = 2,variable=numvar)
n2.grid(row=1,column=2,ipadx=40,ipady=40)
n3 = Radiobutton(numpad,text = "3",indicatoron=0,value = 3,variable=numvar)
n3.grid(row=1,column=3,ipadx=40,ipady=40)
n4 = Radiobutton(numpad,text = "4",indicatoron=0,value = 4,variable=numvar)
n4.grid(row=2,column=1,ipadx=40,ipady=40)
n5 = Radiobutton(numpad,text = "5",indicatoron=0,value = 5,variable=numvar)
n5.grid(row=2,column=2,ipadx=40,ipady=40)
n6 = Radiobutton(numpad,text = "6",indicatoron=0,value = 6,variable=numvar)
n6.grid(row=2,column=3,ipadx=40,ipady=40)
n7 = Radiobutton(numpad,text = "7",indicatoron=0,value = 7,variable=numvar)
n7.grid(row=3,column=1,ipadx=40,ipady=40)
n8 = Radiobutton(numpad,text = "8",indicatoron=0,value = 8,variable=numvar)
n8.grid(row=3,column=2,ipadx=40,ipady=40)
n9 = Radiobutton(numpad,text = "9",indicatoron=0,value = 9,variable=numvar)
n9.grid(row=3,column=3,ipadx=40,ipady=40)
####Coffe Selection Zone ###############################
        #Selection Frame= size+type+coffee#
select = LabelFrame(home,text = "Coffe Selection")
select.grid(row=0,column=1,sticky=N)
####  TYPE ZONE ######################################## 
typepad = LabelFrame(select, text="This is a Typepad Frame")#Type Frame
typepad.grid(row=0,column=0,sticky=NW)
typevar = StringVar()

hot = Radiobutton(typepad,text = "Hot",indicatoron=0,value = "hot",variable=typevar)
hot.grid(row=0,column=0,ipadx=50,ipady=20)
iced = Radiobutton(typepad,text = "Iced",indicatoron=0,value = "iced",variable=typevar)
iced.grid(row=0,column=1,ipadx=50,ipady=20)
frappe = Radiobutton(typepad,text = "Frappe",indicatoron=0,value = "frappe",variable=typevar)
frappe.grid(row=0,column=2,ipadx=50,ipady=20)
hot.select()#-->default select = hot
####  SIZE ZONE ########################################
        #Size Frame#
sizepad = LabelFrame(select, text="This is a Sizepad Frame")
sizepad.grid(row=1,column=0,sticky=W)
sizevar = StringVar()
        #Size RadioButtonZone#
short = Radiobutton(sizepad,text = "Short (8.Oz)",indicatoron=0,value = "short",variable=sizevar)
short.grid(row=0,column=0,ipadx=50,ipady=20)
tall = Radiobutton(sizepad,text = "Tall (12.Oz)",indicatoron=0,value = "tall",variable=sizevar)
tall.grid(row=0,column=1,ipadx=50,ipady=20)
grande = Radiobutton(sizepad,text = "Grande (16.Oz)",indicatoron=0,value = "grande",variable=sizevar)
grande.grid(row=0,column=2,ipadx=50,ipady=20)
venti = Radiobutton(sizepad,text = "Venti (20.Oz)",indicatoron=0,value = "venti",variable=sizevar)
venti.grid(row=0,column=3,ipadx=50,ipady=20)
trenta = Radiobutton(sizepad,text = "Trenta (24.Oz)",indicatoron=0,value = "trenta",variable=sizevar)
trenta.grid(row=0,column=4,ipadx=50,ipady=20)
short.select()#-->default select = tall

####  CAFE ZONE ########################################
        #Cafe Frame#

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=950,height=200)


myframe=LabelFrame(select,relief=GROOVE,width=200,height=100,bd=1)
myframe.grid(sticky=W)
canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
cafevar = StringVar()
affogato =  Radiobutton(frame,text = "Affogato",indicatoron=0,value = "affogato",variable=cafevar)
affogato.grid(row=0,column=0,ipadx=50,ipady=20)
americano =  Radiobutton(frame,text = "Americano",indicatoron=0,value = "americano",variable=cafevar)
americano.grid(row=0,column=1,ipadx=50,ipady=20)
blackeye =  Radiobutton(frame,text = "Black eye",indicatoron=0,value = "blackeye",variable=cafevar)
blackeye.grid(row=0,column=2,ipadx=50,ipady=20)
borgia =  Radiobutton(frame,text = "Borgia",indicatoron=0,value = "borgia",variable=cafevar)
borgia.grid(row=0,column=3,ipadx=50,ipady=20)
breve =  Radiobutton(frame,text = "Breve",indicatoron=0,value = "breve",variable=cafevar)
breve.grid(row=0,column=4,ipadx=50,ipady=20)
cafecrema =  Radiobutton(frame,text = "Cafe Crema",indicatoron=0,value = "cafecrema",variable=cafevar)
cafecrema.grid(row=1,column=0,ipadx=50,ipady=20)
cafecubano =  Radiobutton(frame,text = "Cafe Cubano",indicatoron=0,value = "cafecubano",variable=cafevar)
cafecubano.grid(row=1,column=1,ipadx=50,ipady=20)
cafeaulait =  Radiobutton(frame,text = "Cafe au lait",indicatoron=0,value = "cafeaulait",variable=cafevar)
cafeaulait.grid(row=1,column=2,ipadx=50,ipady=20)
cafeconhielo =  Radiobutton(frame,text = "Cafe con Hielo",indicatoron=0,value = "cafeconhielo",variable=cafevar)
cafeconhielo.grid(row=1,column=3,ipadx=50,ipady=20)
cafeconleche =  Radiobutton(frame,text = "Cafe con Leche",indicatoron=0,value = "cafeconleche",variable=cafevar)
cafeconleche.grid(row=1,column=4,ipadx=50,ipady=20)
cafedeltiempo =  Radiobutton(frame,text = "Cafe del Tiempo",indicatoron=0,value = "cafedeltiempo",variable=cafevar)
cafedeltiempo.grid(row=2,column=0,ipadx=50,ipady=20)
caffelatte =  Radiobutton(frame,text = "Caffe Latte",indicatoron=0,value = "caffelatte",variable=cafevar)
caffelatte.grid(row=2,column=1,ipadx=50,ipady=20)
cappucino =  Radiobutton(frame,text = "Cappucino",indicatoron=0,value = "cappucino",variable=cafevar)
cappucino.grid(row=2,column=2,ipadx=50,ipady=20)
flatwhite =  Radiobutton(frame,text = "Flat white",indicatoron=0,value = "flatwhite",variable=cafevar)
flatwhite.grid(row=2,column=3,ipadx=50,ipady=20)
cortadocortadito =  Radiobutton(frame,text = "CortadoCortadito",indicatoron=0,value = "cortadocortadito",variable=cafevar)
cortadocortadito.grid(row=2,column=4,ipadx=50,ipady=20)
deadeye =  Radiobutton(frame,text = "Dead eye",indicatoron=0,value = "dead eye",variable=cafevar)
deadeye.grid(row=3,column=0,ipadx=50,ipady=20)
dirtychailatte =  Radiobutton(frame,text = "Dirty chai latte",indicatoron=0,value = "dirtychailatte",variable=cafevar)
dirtychailatte.grid(row=3,column=1,ipadx=50,ipady=20)
doppio =  Radiobutton(frame,text = "Doppio",indicatoron=0,value = "doppio",variable=cafevar)
doppio.grid(row=3,column=2,ipadx=50,ipady=20)
espressino =  Radiobutton(frame,text = "Espressino",indicatoron=0,value = "espressino",variable=cafevar)
espressino.grid(row=3,column=3,ipadx=50,ipady=20)
espresso =  Radiobutton(frame,text = "Espresso",indicatoron=0,value = "espresso",variable=cafevar)
espresso.grid(row=3,column=4,ipadx=50,ipady=20)
espressoromano =  Radiobutton(frame,text = "Espresso Romano",indicatoron=0,value = "espressoromano",variable=cafevar)
espressoromano.grid(row=4,column=0,ipadx=50,ipady=20)
galao =  Radiobutton(frame,text = "Galao",indicatoron=0,value = "galao",variable=cafevar)
galao.grid(row=4,column=1,ipadx=50,ipady=20)
irishcoffee =  Radiobutton(frame,text = "Irish Coffee",indicatoron=0,value = "irishcoffee",variable=cafevar)
irishcoffee.grid(row=4,column=2,ipadx=50,ipady=20)
lazyeye =  Radiobutton(frame,text = "Lazy eye",indicatoron=0,value = "lazyeye",variable=cafevar)
lazyeye.grid(row=4,column=3,ipadx=50,ipady=20)
longblack =  Radiobutton(frame,text = "Long Black",indicatoron=0,value = "longblack",variable=cafevar)
longblack.grid(row=4,column=4,ipadx=50,ipady=20)
lungo =  Radiobutton(frame,text = "Lungo",indicatoron=0,value = "lungo",variable=cafevar)
lungo.grid(row=5,column=0,ipadx=50,ipady=20)
macchiato =  Radiobutton(frame,text = "Macchiato",indicatoron=0,value = "macchiato",variable=cafevar)
macchiato.grid(row=5,column=1,ipadx=50,ipady=20)
mocha =  Radiobutton(frame,text = "Mocha",indicatoron=0,value = "mocha",variable=cafevar)
mocha.grid(row=5,column=2,ipadx=50,ipady=20)
piccololatte =  Radiobutton(frame,text = "Piccolo latte",indicatoron=0,value = "piccololatte",variable=cafevar)
piccololatte.grid(row=5,column=3,ipadx=50,ipady=20)
redeye =  Radiobutton(frame,text = "Red eye",indicatoron=0,value = "redeye",variable=cafevar)
redeye.grid(row=5,column=4,ipadx=50,ipady=20)
ristretto =  Radiobutton(frame,text = "Ristretto",indicatoron=0,value = "ristretto",variable=cafevar)
ristretto.grid(row=6,column=0,ipadx=50,ipady=20)
turkishcoffe =  Radiobutton(frame,text = "Turkish coffe",indicatoron=0,value = "turkishcoffe",variable=cafevar)
turkishcoffe.grid(row=6,column=1,ipadx=50,ipady=20)
vienna =  Radiobutton(frame,text = "Vienna",indicatoron=0,value = "vienna",variable=cafevar)
vienna.grid(row=6,column=2,ipadx=50,ipady=20)



        #Cafe RadioButtonZone#
##affogato =  Radiobutton(cafeframe,text = "Affogato",indicatoron=0,value = "affogato",variable=cafevar)
##affogato.grid(row=0,column=0,ipadx=50,ipady=20)
##americano =  Radiobutton(cafepad,text = "Americano",indicatoron=0,value = "americano",variable=cafevar)
##americano.grid(row=0,column=1,ipadx=50,ipady=20)
##blackeye =  Radiobutton(cafepad,text = "Black eye",indicatoron=0,value = "blackeye",variable=cafevar)
##blackeye.grid(row=0,column=2,ipadx=50,ipady=20)
##borgia =  Radiobutton(cafepad,text = "Borgia",indicatoron=0,value = "borgia",variable=cafevar)
##borgia.grid(row=0,column=3,ipadx=50,ipady=20)
##breve =  Radiobutton(cafepad,text = "Breve",indicatoron=0,value = "breve",variable=cafevar)
##breve.grid(row=0,column=4,ipadx=50,ipady=20)
##cafecrema =  Radiobutton(cafepad,text = "Cafe Crema",indicatoron=0,value = "cafecrema",variable=cafevar)
##cafecrema.grid(row=1,column=0,ipadx=50,ipady=20)
##cafecubano =  Radiobutton(cafepad,text = "Cafe Cubano",indicatoron=0,value = "cafecubano",variable=cafevar)
##cafecubano.grid(row=1,column=1,ipadx=50,ipady=20)
##cafeaulait =  Radiobutton(cafepad,text = "Cafe au lait",indicatoron=0,value = "cafeaulait",variable=cafevar)
##cafeaulait.grid(row=1,column=2,ipadx=50,ipady=20)
##cafeconhielo =  Radiobutton(cafepad,text = "Cafe con Hielo",indicatoron=0,value = "cafeconhielo",variable=cafevar)
##cafeconhielo.grid(row=1,column=3,ipadx=50,ipady=20)
##cafeconleche =  Radiobutton(cafepad,text = "Cafe con Leche",indicatoron=0,value = "cafeconleche",variable=cafevar)
##cafeconleche.grid(row=1,column=4,ipadx=50,ipady=20)
##cafedeltiempo =  Radiobutton(cafepad,text = "Cafe del Tiempo",indicatoron=0,value = "cafedeltiempo",variable=cafevar)
##cafedeltiempo.grid(row=2,column=0,ipadx=50,ipady=20)
##caffelatte =  Radiobutton(cafepad,text = "Caffe Latte",indicatoron=0,value = "caffelatte",variable=cafevar)
##caffelatte.grid(row=2,column=1,ipadx=50,ipady=20)
##cappucino =  Radiobutton(cafepad,text = "Cappucino",indicatoron=0,value = "cappucino",variable=cafevar)
##cappucino.grid(row=2,column=2,ipadx=50,ipady=20)
##flatwhite =  Radiobutton(cafepad,text = "Flat white",indicatoron=0,value = "flatwhite",variable=cafevar)
##flatwhite.grid(row=2,column=3,ipadx=50,ipady=20)
##cortadocortadito =  Radiobutton(cafepad,text = "CortadoCortadito",indicatoron=0,value = "cortadocortadito",variable=cafevar)
##cortadocortadito.grid(row=2,column=4,ipadx=50,ipady=20)
##deadeye =  Radiobutton(cafepad,text = "Dead eye",indicatoron=0,value = "dead eye",variable=cafevar)
##deadeye.grid(row=3,column=0,ipadx=50,ipady=20)
##dirtychailatte =  Radiobutton(cafepad,text = "Dirty chai latte",indicatoron=0,value = "dirtychailatte",variable=cafevar)
##dirtychailatte.grid(row=3,column=1,ipadx=50,ipady=20)
##doppio =  Radiobutton(cafepad,text = "Doppio",indicatoron=0,value = "doppio",variable=cafevar)
##doppio.grid(row=3,column=2,ipadx=50,ipady=20)
##espressino =  Radiobutton(cafepad,text = "Espressino",indicatoron=0,value = "espressino",variable=cafevar)
##espressino.grid(row=3,column=3,ipadx=50,ipady=20)
##espresso =  Radiobutton(cafepad,text = "Espresso",indicatoron=0,value = "espresso",variable=cafevar)
##espresso.grid(row=3,column=4,ipadx=50,ipady=20)
##espressoromano =  Radiobutton(cafepad,text = "Espresso Romano",indicatoron=0,value = "espressoromano",variable=cafevar)
##espressoromano.grid(row=4,column=0,ipadx=50,ipady=20)
##galao =  Radiobutton(cafepad,text = "Galao",indicatoron=0,value = "galao",variable=cafevar)
##galao.grid(row=4,column=1,ipadx=50,ipady=20)
##irishcoffee =  Radiobutton(cafepad,text = "Irish Coffee",indicatoron=0,value = "irishcoffee",variable=cafevar)
##irishcoffee.grid(row=4,column=2,ipadx=50,ipady=20)
##lazyeye =  Radiobutton(cafepad,text = "Lazy eye",indicatoron=0,value = "lazyeye",variable=cafevar)
##lazyeye.grid(row=4,column=3,ipadx=50,ipady=20)
##longblack =  Radiobutton(cafepad,text = "Long Black",indicatoron=0,value = "longblack",variable=cafevar)
##longblack.grid(row=4,column=4,ipadx=50,ipady=20)
##lungo =  Radiobutton(cafepad,text = "Lungo",indicatoron=0,value = "lungo",variable=cafevar)
##lungo.grid(row=5,column=0,ipadx=50,ipady=20)
##macchiato =  Radiobutton(cafepad,text = "Macchiato",indicatoron=0,value = "macchiato",variable=cafevar)
##macchiato.grid(row=5,column=1,ipadx=50,ipady=20)
##mocha =  Radiobutton(cafepad,text = "Mocha",indicatoron=0,value = "mocha",variable=cafevar)
##mocha.grid(row=5,column=2,ipadx=50,ipady=20)
##piccololatte =  Radiobutton(cafepad,text = "Piccolo latte",indicatoron=0,value = "piccololatte",variable=cafevar)
##piccololatte.grid(row=5,column=3,ipadx=50,ipady=20)
##redeye =  Radiobutton(cafepad,text = "Red eye",indicatoron=0,value = "redeye",variable=cafevar)
##redeye.grid(row=5,column=4,ipadx=50,ipady=20)
##ristretto =  Radiobutton(cafepad,text = "Ristretto",indicatoron=0,value = "ristretto",variable=cafevar)
##ristretto.grid(row=6,column=0,ipadx=50,ipady=20)
##turkishcoffe =  Radiobutton(cafepad,text = "Turkish coffe",indicatoron=0,value = "turkishcoffe",variable=cafevar)
##turkishcoffe.grid(row=6,column=1,ipadx=50,ipady=20)
##vienna =  Radiobutton(cafepad,text = "Vienna",indicatoron=0,value = "vienna",variable=cafevar)
##vienna.grid(row=6,column=2,ipadx=50,ipady=20)

####  ACTION ZONE ########################################
        #Action Frame#
actionpad = LabelFrame(home, text="This is a Action Frame")
actionpad.grid(row=1,column=1,sticky = NW)
action = Label(actionpad, text="actionpad Here")
action.grid()
        #Action ButtonZone#
addcart = Button(actionpad, text="Add to Cart").grid()
cash = Button(actionpad, text="Cash").grid()
ingredient = Button(actionpad, text = "Ingredient").grid()
##########################################################

home.mainloop()
