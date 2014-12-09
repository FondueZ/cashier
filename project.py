from Tkinter import *
import time
home = Tk()
home.title("The Unsleepable")
home.geometry("1300x700")
####  SLIPT ZONE ########################################
        #Slipt Frame#

sliptframe = LabelFrame(home, text="Order")
sliptframe.grid()


#### Time Date Zone ##########################################
def updatetime():
    current = time.strftime("%H:%M:%S"+"\n"+"%d:%a:%b:%Y")
    timetext.configure(text=current)
    home.after(1000,updatetime)
    
##tdframe = LabelFrame(home,text="Current Time")
##tdframe.grid(row = 1,column = 0,ipadx=55,ipady=100,sticky=N)
timetext = Label(home,text="", font=("Helvetica", 35))
timetext.grid(row = 1, column = 0,ipady=70)

updatetime()

####  NUMPAD ZONE ########################################
        #Numpad Frame#
numpad = LabelFrame(home, text="Amount of Coffee")
numpad.grid(row=1,column=1,sticky=E)
numvar = StringVar()
 

    
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

n1.select()
####Coffe Selection Zone ###############################
        #Selection Frame= size+type+coffee#
select = LabelFrame(home,text = "Coffee Selection")
select.grid(row=0,column=1,sticky=N)
####  TYPE ZONE ########################################
        #Type Frame#
typepad = LabelFrame(select, text="Select Type")
typepad.grid(row=0,column=0,sticky=NW)
typevar = StringVar()
        #Type radiobutton#
hot = Radiobutton(typepad,text = "Hot",indicatoron=0,value = "hot",variable=typevar)
hot.grid(row=0,column=0,ipadx=60,ipady=20)
iced = Radiobutton(typepad,text = "Iced",indicatoron=0,value = "iced",variable=typevar)
iced.grid(row=0,column=1,ipadx=60,ipady=20)
frappe = Radiobutton(typepad,text = "Frappe",indicatoron=0,value = "frappe",variable=typevar)
frappe.grid(row=0,column=2,ipadx=50,ipady=20)
hot.select()#-->default select = hot
####  SIZE ZONE ########################################
        #Size Frame#
sizepad = LabelFrame(select, text="Select Size")
sizepad.grid(row=1,column=0,sticky=W)
sizevar = StringVar()
        #Size RadioButtonZone#
short = Radiobutton(sizepad,text = "Short (8.Oz)",indicatoron=0,value = "short",variable=sizevar)
short.grid(row=0,column=0,ipadx=40,ipady=20)
tall = Radiobutton(sizepad,text = "Tall (12.Oz)",indicatoron=0,value = "tall",variable=sizevar)
tall.grid(row=0,column=1,ipadx=40,ipady=20)
grande = Radiobutton(sizepad,text = "Grande (16.Oz)",indicatoron=0,value = "grande",variable=sizevar)
grande.grid(row=0,column=2,ipadx=30,ipady=20)
venti = Radiobutton(sizepad,text = "Venti (20.Oz)",indicatoron=0,value = "venti",variable=sizevar)
venti.grid(row=0,column=3,ipadx=35,ipady=20)
trenta = Radiobutton(sizepad,text = "Trenta (24.Oz)",indicatoron=0,value = "trenta",variable=sizevar)
trenta.grid(row=0,column=4,ipadx=30,ipady=20)
short.select()#-->default select = tall

####  CAFE ZONE ########################################
        #Cafe Frame#

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=850,height=150)


cafepad=LabelFrame(select,relief=GROOVE,width=200,height=100,bd=1,text = "Select Coffee",)
cafepad.grid(sticky=W)
canvas=Canvas(cafepad)
cafeframe=Frame(canvas)
myscrollbar=Scrollbar(cafepad,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=cafeframe,anchor='nw')
cafeframe.bind("<Configure>",myfunction)
cafevar = StringVar()
      #Cafe RadioButtonZone#
affogato =  Radiobutton(cafeframe,text = "Affogato",indicatoron=0,value = "Affogato",variable=cafevar)
affogato.grid(row=0,column=0,ipadx=75,ipady=20,sticky=W)
americano =  Radiobutton(cafeframe,text = "Americano",indicatoron=0,value = "Americano",variable=cafevar)
americano.grid(row=0,column=1,ipadx=72,ipady=20,sticky=W)
blackeye =  Radiobutton(cafeframe,text = "Black Eye",indicatoron=0,value = "Black Eye",variable=cafevar)
blackeye.grid(row=0,column=2,ipadx=75,ipady=20,sticky=W)
borgia =  Radiobutton(cafeframe,text = "Borgia",indicatoron=0,value = "Borgia",variable=cafevar)
borgia.grid(row=0,column=3,ipadx=85,ipady=20,sticky=W)
breve =  Radiobutton(cafeframe,text = "Breve",indicatoron=0,value = "Breve",variable=cafevar)
breve.grid(row=1,column=0,ipadx=80,ipady=20,sticky=W)
cafecrema =  Radiobutton(cafeframe,text = "Cafe Crema",indicatoron=0,value = "Cafe Crema",variable=cafevar)
cafecrema.grid(row=1,column=1,ipadx=70,ipady=20,sticky=W)
cafecubano =  Radiobutton(cafeframe,text = "Cafe Cubano",indicatoron=0,value = "Cafe Cubano",variable=cafevar)
cafecubano.grid(row=1,column=2,ipadx=60,ipady=20,sticky=W)
cafeaulait =  Radiobutton(cafeframe,text = "Cafe Au Lait",indicatoron=0,value = "Cafe Au Lait",variable=cafevar)
cafeaulait.grid(row=1,column=3,ipadx=70,ipady=20,sticky=W)
cafeconhielo =  Radiobutton(cafeframe,text = "Cafe Con Hielo",indicatoron=0,value = "Cafe Con Hielo",variable=cafevar)
cafeconhielo.grid(row=2,column=0,ipadx=50,ipady=20,sticky=W)
cafeconleche =  Radiobutton(cafeframe,text = "Cafe Con Leche",indicatoron=0,value = "Cafe Con Leche",variable=cafevar)
cafeconleche.grid(row=2,column=1,ipadx=50,ipady=20,sticky=W)
cafedeltiempo =  Radiobutton(cafeframe,text = "Cafe Del Tiempo",indicatoron=0,value = "Cafe Del Tiempo",variable=cafevar)
cafedeltiempo.grid(row=2,column=2,ipadx=50,ipady=20,sticky=W)
caffelatte =  Radiobutton(cafeframe,text = "Caffe Latte",indicatoron=0,value = "Caffe Latte",variable=cafevar)
caffelatte.grid(row=2,column=3,ipadx=50,ipady=20,sticky=W)
cappucino =  Radiobutton(cafeframe,text = "Cappucino",indicatoron=0,value = "Cappucino",variable=cafevar)
cappucino.grid(row=3,column=0,ipadx=50,ipady=20,sticky=W)
flatwhite =  Radiobutton(cafeframe,text = "Flat White",indicatoron=0,value = "Flat White",variable=cafevar)
flatwhite.grid(row=3,column=1,ipadx=50,ipady=20,sticky=W)
cortado =  Radiobutton(cafeframe,text = "Cortado",indicatoron=0,value = "Cortado",variable=cafevar)
cortado.grid(row=3,column=2,ipadx=50,ipady=20,sticky=W)
cortadito =  Radiobutton(cafeframe,text = "Cortadito",indicatoron=0,value = "Cortadito",variable=cafevar)
cortadito.grid(row=3,column=3,ipadx=50,ipady=20,sticky=W)
deadeye =  Radiobutton(cafeframe,text = "Dead Eye",indicatoron=0,value = "Dead Eye",variable=cafevar)
deadeye.grid(row=4,column=0,ipadx=50,ipady=20,sticky=W)
dirtychailatte =  Radiobutton(cafeframe,text = "Dirty Chai Latte",indicatoron=0,value = "Dirty Chai Latte",variable=cafevar)
dirtychailatte.grid(row=4,column=1,ipadx=50,ipady=20,sticky=W)
doppio =  Radiobutton(cafeframe,text = "Doppio",indicatoron=0,value = "Doppio",variable=cafevar)
doppio.grid(row=4,column=2,ipadx=50,ipady=20,sticky=W)
espressino =  Radiobutton(cafeframe,text = "Espressino",indicatoron=0,value = "Espressino",variable=cafevar)
espressino.grid(row=4,column=3,ipadx=50,ipady=20,sticky=W)
espresso =  Radiobutton(cafeframe,text = "Espresso",indicatoron=0,value = "Espresso",variable=cafevar)
espresso.grid(row=5,column=0,ipadx=50,ipady=20,sticky=W)
espressoromano =  Radiobutton(cafeframe,text = "Espresso Romano",indicatoron=0,value = "Espresso Romano",variable=cafevar)
espressoromano.grid(row=5,column=1,ipadx=50,ipady=20,sticky=W)
galao =  Radiobutton(cafeframe,text = "Galao",indicatoron=0,value = "Galao",variable=cafevar)
galao.grid(row=5,column=2,ipadx=50,ipady=20,sticky=W)
irishcoffee =  Radiobutton(cafeframe,text = "Irish Coffee",indicatoron=0,value = "Irish Coffee",variable=cafevar)
irishcoffee.grid(row=5,column=3,ipadx=50,ipady=20,sticky=W)
lazyeye =  Radiobutton(cafeframe,text = "Lazy Eye",indicatoron=0,value = "Lazy Eye",variable=cafevar)
lazyeye.grid(row=6,column=0,ipadx=50,ipady=20,sticky=W)
longblack =  Radiobutton(cafeframe,text = "Long Black",indicatoron=0,value = "Long Black",variable=cafevar)
longblack.grid(row=6,column=1,ipadx=50,ipady=20,sticky=W)
lungo =  Radiobutton(cafeframe,text = "Lungo",indicatoron=0,value = "Lungo",variable=cafevar)
lungo.grid(row=6,column=2,ipadx=50,ipady=20,sticky=W)
macchiato =  Radiobutton(cafeframe,text = "Macchiato",indicatoron=0,value = "Macchiato",variable=cafevar)
macchiato.grid(row=6,column=3,ipadx=50,ipady=20,sticky=W)
mocha =  Radiobutton(cafeframe,text = "Mocha",indicatoron=0,value = "Mocha",variable=cafevar)
mocha.grid(row=7,column=0,ipadx=50,ipady=20,sticky=W)
piccololatte =  Radiobutton(cafeframe,text = "Piccolo Latte",indicatoron=0,value = "Piccolo Latte",variable=cafevar)
piccololatte.grid(row=7,column=1,ipadx=50,ipady=20,sticky=W)
redeye =  Radiobutton(cafeframe,text = "Red Eye",indicatoron=0,value = "Red Eye",variable=cafevar)
redeye.grid(row=7,column=2,ipadx=50,ipady=20,sticky=W)
ristretto =  Radiobutton(cafeframe,text = "Ristretto",indicatoron=0,value = "Ristretto",variable=cafevar)
ristretto.grid(row=7,column=3,ipadx=50,ipady=20,sticky=W)
turkishcoffe =  Radiobutton(cafeframe,text = "Turkish Coffe",indicatoron=0,value = "Turkish Coffe",variable=cafevar)
turkishcoffe.grid(row=8,column=0,ipadx=50,ipady=20,sticky=W)
vienna =  Radiobutton(cafeframe,text = "Vienna",indicatoron=0,value = "Vienna",variable=cafevar)
vienna.grid(row=8,column=1,ipadx=50,ipady=20,sticky=W)
affogato.select()

      


####  ACTION ZONE ########################################
        #command for action button#
drink = []
subtotal = 0
def addcartcommand():
    global drink,subtotal
    thing = sizevar.get().capitalize() + " " + typevar.get().capitalize() + " " + cafevar.get()
    thingprice = str(cafeinfo[cafevar.get()][1] + sizeinfo[sizevar.get()] + typeinfo[typevar.get()])+" B"
    amount = numvar.get()
    drink.append(thing + (" "*20) + thingprice + (" "*20) + amount )
    subtotal += (cafeinfo[cafevar.get()][1] + sizeinfo[sizevar.get()] + typeinfo[typevar.get()])*int(amount)
    #print cafeinfo[cafevar.get()][1]
    print drink,subtotal

    
def removecommand():
    global drink,subtotal
    thing = sizevar.get().capitalize() + " " + typevar.get().capitalize() + " " + cafevar.get()
    thingprice = str(cafeinfo[cafevar.get()][1] + sizeinfo[sizevar.get()] + typeinfo[typevar.get()])+" B"
    amount = numvar.get()
    drink.remove(thing + (" "*20) + thingprice + (" "*20) + amount )
    subtotal -= (cafeinfo[cafevar.get()][1] + sizeinfo[sizevar.get()] + typeinfo[typevar.get()])*int(amount)
    print drink,subtotal


    
def clearcommand():
    global drink,subtotal
    drink = []
    subtotal = 0
    print drink,subtotal
def cashcommand():
    global drink,subtotal
    
    drink.append(("Subtotal     "+ str(subtotal)))
    vat = "VAT 7%" + " "*20 + str(subtotal*0.07)
    drink.append(vat)
    total = "Total              " + str(subtotal+(subtotal*0.07))
    drink.append(total)
    
    print drink
def ingredientcommand():
    showing = Tk()
    showing.title(cafevar.get())
    inglabel = Label(showing,text=cafeinfo[cafevar.get()][0])
    inglabel.grid(ipadx = 100)
        #Action Frame#
actionpad = LabelFrame(home, text="Command Set")
actionpad.grid(row=1,column=1,sticky = NW)

        #Action ButtonZone#
addcart = Button(actionpad, text="Add to Order",font =("helvetica",16),command = addcartcommand)
addcart.grid(row=0,column=0,stick=W)
removecart = Button(actionpad, text="Remove from Order",font =("helvetica",16),command = removecommand)
removecart.grid(row=0,column=1,stick=W)
clear = Button(actionpad, text="Clear Order",font =("helvetica",16),command = clearcommand)
clear.grid(row=1,column=0,stick=W)
cash = Button(actionpad, text="Cash",font =("helvetica",16),command = cashcommand)
cash.grid(row=2,column=0,stick=W)
ingredient = Button(actionpad, text = "Ingredient",font =("helvetica",16),command = ingredientcommand)
ingredient.grid(row=2,column=1,stick=W)
##### function for button Zone ###########################

cafeinfo = {
            'Affogato':["crema,espresso,ice cream",20]
            , 'Americano':["hot water,espresso",20]
            , 'Blackeye':["dripped coffee,espresso",20]
            , 'Borgia':["cinnamon,orange peel,whipped cream,hot chocolate,espresso",20]
            , 'Breve':["milk foam steamed half and half,espresso",20]
            , 'Cafe Crema':["crema,much longer brewed espresso",20]
            , 'Cafe Cubano':["crema,brewed with brown sugar espresso",20]
            , 'Cafe Au Lait':["scalded milk,Frech press coffee",20]
            , 'Cafe Con Hielo':["crema,espresso,ice cubes",20]
            , 'Cafe Con Leche':["espresso,serve with hot milk",20]
            , 'Cafe Del Tiempo':["espresso,serve with ice cubes and lemon slice",20]
            , 'Caffe Latte':["milk foam,steamed milk,espresso",20]
            , 'Cappucino':["milk foam,steamed milk,espresso",20]
            , 'Flat White':["steamed milk,espresso",20]
            , 'Cortado':["milk foam,warm milk,espresso",20]
            , 'Cortadito':["milk foam,warm milk,cubano",20]
            , 'Dead Eye':["dripped coffee,espresso",20]
            , 'Dirty Chai Latte':["milk foam,steamed milk,spiced blacktea,espresso",20]
            , 'Doppio':["crema,double espresso",20]
            , 'Espressino':["cocoa powder,steamed milk,espresso",20]
            , 'Espresso':["crema,espresso",20]
            , 'Espresso Romano':["lemon slice,espresso",20]
            , 'Galao':["foamed milk,espresso",20]
            , 'Irish Coffee':["heavy cream,Irish whiskey,French press coffee, brown sugar",20]
            , 'Lazy Eye':["decaffeinated drippd coffee,espresso",20]
            , 'Long Black':["espresso,hot water",20]
            , 'Lungo':["crema,longer brewed espresso",20]
            , 'Macchiato':["dash of foamed milk,espresso",20]
            , 'Mocha':["whipped cream,hot chocolate,espresso",20]
            , 'Piccolo Latte':["milk foam,steamed milk,ristretto",20]
            , 'Red Eye':["dripped coffee,esspresso",20]
            , 'Ristretto':["crema,espresso",20]
            , 'Turkish Coffe':["kopuk,sugar water,ground coffee",20]
            , 'Vienna':["whipped cream,espresso",20]
            }
sizeinfo = {"short":5,"tall":10,"grande":15,"venti":20,"trenta":25}
typeinfo = {"hot":5,"iced":10,"frappe":15}
   
##########################################################

home.mainloop()
