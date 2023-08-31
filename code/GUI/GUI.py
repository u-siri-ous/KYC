import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

'''
def start():
    a_notebook.tab(card_depiction_frame, state="normal")
    a_notebook.select(card_depiction_frame)
'''
    
#Nicola's command that ChatGPT cancelled but it doesn't run yet so we don't know if it works
def kyc(cen, cor, edg, sur):
        a_notebook.tab(card_depiction_frame, state="normal")
        a_notebook.select(card_depiction_frame)
        card = Image.open("code/card.jpg")
        resized=card.resize((300,375))
        card_pic=ImageTk.PhotoImage(resized)
        image_label=tk.Label(card_frame,image=card_pic)
        image_label.image=card_pic #Very important to display the photo correctly
        image_label.place(relx=0.5,rely=0.5,anchor='center')
        centering_label=tk.Label(centering_frame,text="Centering  {}  ".format(cen)) #to be filled by the output of the grading
        centering_label.place(relx=0.1,rely=0.5,anchor="w")
        edges_label=tk.Label(edges_frame,text="Edges  {}  ".format(edg))  #to be filled by the output of the grading
        edges_label.place(relx=0.1,rely=0.5,anchor="w")
        corners_label=tk.Label(corners_frame,text="Corners  {}  ".format(cor))  #to be filled by the output of the grading
        corners_label.place(relx=0.1,rely=0.5,anchor="w")
        surface_label=tk.Label(surface_frame,text="Surface  {}  ".format(sur))  #to be filled by the output of the grading
        surface_label.place(relx=0.1,rely=0.5,anchor="w")
        mean=(cen+cor+edg+sur)//4
        mean_label=tk.Label(mean_frame,text="{}".format(mean),font="60")  #to be filled by the output of the grading
        mean_label.place(relx=0.5,rely=0.5,anchor='center')
        pass
    
def home():
    a_notebook.select(starting_frame)
    a_notebook.tab(card_depiction_frame, state="hidden")

def set_base_toggle():
     set_base_checkbox.toggle()
     fossil_checkbox.deselect()
     jungle_checkbox.deselect()
     if var1.get()==1 or var2.get()==1 or var3.get()==1:
        logo_button.configure(state="normal")
     else:
         logo_button.configure(state='disabled')
     
     
          

    
def fossil_toggle():
     fossil_checkbox.toggle()
     jungle_checkbox.deselect()
     set_base_checkbox.deselect()
     if var1.get()==1 or var2.get()==1 or var3.get()==1:
        logo_button.configure(state="normal")
     else:
         logo_button.configure(state='disabled')
     

def jungle_toggle():
     jungle_checkbox.toggle()
     fossil_checkbox.deselect()
     set_base_checkbox.deselect()
     if var1.get()==1 or var2.get()==1 or var3.get()==1:
        logo_button.configure(state="normal")
     else:
         logo_button.configure(state='disabled')
     
          
# Initialize the main application
root = tk.Tk()
root.title("KYC")
root.geometry("850x700")
root.iconbitmap("images\GUI\Logo_wind.ico")

# Notebook initialization
a_notebook = ttk.Notebook(root)
a_notebook.pack(fill="both", expand=1)

# Frame initialization
starting_frame = tk.Frame(a_notebook, width=850, height=700)
card_depiction_frame = tk.Frame(a_notebook, width=850, height=700)
starting_frame.pack(fill="both", expand=1)
card_depiction_frame.pack(fill="both", expand=1)

# Adding frames to the notebook
a_notebook.add(starting_frame, text="Start")
a_notebook.add(card_depiction_frame, text="Card")
a_notebook.tab(card_depiction_frame, state="hidden")

# Structure of the input form
upper_frame = tk.LabelFrame(card_depiction_frame, border=0,background="red")
upper_frame.place(relx=0, rely=0,relwidth=1, relheight=0.2)
here_it_is=tk.PhotoImage(file="images/GUI/Logo.png") #da sostituire con scritta here's your card! con font bellini che riprendono il logo 
Heres_your_card=tk.Label(upper_frame,image=here_it_is)
Heres_your_card.image=here_it_is
Heres_your_card.place(relx=0.5,rely=0.5,anchor="center")
home_button = tk.Button(card_depiction_frame, text='HOME', command=home)
home_button.place(relx=0.003, rely=0.997, anchor="sw")

# Structure of the frames in the card depiction page
card_frame = tk.LabelFrame(card_depiction_frame, border=0,background='#2a75bb')
card_frame.place(relx=0, rely=0.3, relwidth=0.35,relheight=0.65, anchor="nw")
vote_frame = tk.LabelFrame(card_depiction_frame, height=50, width=300, border=2)
vote_frame.place(relx=0, rely=0.2, relwidth=0.35,relheight=0.1, anchor="nw")
name_frame=tk.LabelFrame(card_depiction_frame,background='yellow')
name_frame.place(relx=0.35,rely=0.2, relheight=0.1,relwidth=0.65,anchor='nw')
description_frame = tk.LabelFrame(card_depiction_frame, border=1,background='purple')
description_frame.place(relx=0.35, rely=0.3, relheight=0.65,relwidth=0.65, anchor="nw")

# Frames in the vote frame
# Frames for each individual vote
centering_frame = tk.LabelFrame(vote_frame,  border=0)
centering_frame.place(relx=0, rely=0,relheight=0.5,relwidth=0.4, anchor="nw")
edges_frame = tk.LabelFrame(vote_frame,  border=0)
edges_frame.place(relx=0, rely=0.5, relheight=0.5,relwidth=0.4, anchor="nw")
corners_frame = tk.LabelFrame(vote_frame,  border=0)
corners_frame.place(relx=0.4, rely=0, relheight=0.5,relwidth=0.4, anchor="nw")
surface_frame = tk.LabelFrame(vote_frame,   border=0)
surface_frame.place(relx=0.4, rely=0.5, relheight=0.5,relwidth=0.4, anchor="nw")
# Frame for the mean aka final vote
mean_frame = tk.LabelFrame(vote_frame,  border=0 )
mean_frame.place(relx=0.8, rely=0, relheight=1,relwidth=0.2, anchor="nw")

# Structure of the description frame
ability_frame = tk.LabelFrame(description_frame, background='green')
ability_frame.place(relx=0,rely=0,relheight=0.25,relwidth=1,anchor='nw')
move1_frame = tk.LabelFrame(description_frame,background='red')
move1_frame.place(relx=0,rely=0.25,relheight=0.25,relwidth=1,anchor='nw')
move2_frame = tk.LabelFrame(description_frame,background='cyan')
move2_frame.place(relx=0,rely=0.5,relheight=0.25,relwidth=1,anchor='nw')
weakness_frame = tk.LabelFrame(description_frame,background='white')
weakness_frame.place(relx=0,rely=0.75,relheight=0.25,relwidth=1,anchor='nw')

# Structure of the start frame
logo = Image.open("images/GUI/Logo_res.png")
resized_logo=logo.resize((400,400))
new_logo=ImageTk.PhotoImage(resized_logo)
logo_button = tk.Button(starting_frame, image=new_logo, command=kyc(0,0,0,0), borderwidth=0,state="disabled")
logo_button.place(relx=0.5, rely=0.4, anchor="center")
var1=tk.IntVar()
set_base_checkbox=tk.Checkbutton(starting_frame,variable=var1,border=0,state="disabled",relief="flat")
set_base_checkbox.place(relx=0.4,rely=0.85,anchor="center")
setbase_logo = Image.open('images\GUI\setbase.png')
resized_setbase=setbase_logo.resize((25,25))
new_setbase_logo=ImageTk.PhotoImage(resized_setbase)
set_base_button=tk.Button(starting_frame,image=new_setbase_logo,border=1,command=set_base_toggle)
set_base_button.place(relx=0.397,rely=0.8,anchor="center")
var2=tk.IntVar()
fossil_checkbox=tk.Checkbutton(starting_frame,variable=var2,border=0,state="disabled",relief='flat')
fossil_checkbox.place(relx=0.5,rely=0.85,anchor="center")
fossil_logo = Image.open('images\\GUI\\fossil.png')
resized_fossil=fossil_logo.resize((25,25))
new_fossil_logo=ImageTk.PhotoImage(resized_fossil)
fossil_button=tk.Button(starting_frame,image=new_fossil_logo,border=1,command=fossil_toggle)
fossil_button.place(relx=0.497,rely=0.8,anchor="center")
var3=tk.IntVar()
jungle_checkbox=tk.Checkbutton(starting_frame,variable=var3,border=0,state="disabled",relief="flat")
jungle_checkbox.place(relx=0.6,rely=0.85,anchor="center")
jungle_logo = Image.open('images\GUI\jungle.png')
resized_jungle=jungle_logo.resize((25,25))
new_jungle_logo=ImageTk.PhotoImage(resized_jungle)
jungle_button=tk.Button(starting_frame,image=new_jungle_logo,border=1,command=jungle_toggle)
jungle_button.place(relx=0.597,rely=0.8,anchor="center")

# Descriptive label
to_start = tk.Label(starting_frame, text="To get to know your card,select below the expansion it is from and then click the logo")
to_start.place(relx=0.5, rely=0.75, anchor="center")

# Credits label
credits_lbl = tk.Label(text="A project by Bianchi Christian, Mastrorilli Nicola, Ramil Leonard Vincent, Sannino Siria")
credits_lbl.place(relx=0.997, rely=0.997, anchor='se')

# Start the application's main loop
root.mainloop()