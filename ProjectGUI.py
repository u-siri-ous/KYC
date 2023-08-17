import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
root = tk.Tk()
root.title("KYC")
root.geometry("800x600")
#root.iconbitmap("icona") Quando avremo un'icona inserirla qui

def start():
    a_notebook.add(card_depiction_frame,text="Card", state="normal")
    a_notebook.select(1)

def kyc():
    if input_form.get().endswith('.jpg'):
        kyc_button.config(state="disabled")
        new_pokemon=Image.open(input_form.get())
        resized=new_pokemon.resize((300,375),Image.ANTIALIAS)
        card_pic=ImageTk.PhotoImage(resized)
        image_label=tk.Label(card_frame,image=card_pic)
        image_label.image=card_pic #Very important to display the photo correctly
        image_label.pack()
        centering_label=tk.Label(centering_frame,text="Centering    ") #to be filled by the output of the grading
        centering_label.place(relx=0.1,rely=0.5,anchor="w")
        edges_label=tk.Label(edges_frame,text="Edges    ")  #to be filled by the output of the grading
        edges_label.place(relx=0.1,rely=0.5,anchor="w")
        corners_label=tk.Label(corners_frame,text="Corners    ")  #to be filled by the output of the grading
        corners_label.place(relx=0.1,rely=0.5,anchor="w")
        surface_label=tk.Label(surface_frame,text="Surface    ")  #to be filled by the output of the grading
        surface_label.place(relx=0.1,rely=0.5,anchor="w")
        mean_label=tk.Label(mean_frame,text="X",font="60")  #to be filled by the output of the grading
        mean_label.place(relx=0.5,rely=0.5,anchor='center')
        input_form.delete(0,'end')
        instructions.place_forget()
        input_form.place_forget()
        kyc_button.place_forget()
        here_it_is=tk.PhotoImage(file="images\Logo_placeholder.png") #da sostituire con scritta here's your card! con font bellini che riprendono il logo 
        Heres_your_card=tk.Label(upper_frame,image=here_it_is)
        Heres_your_card.image=here_it_is
        Heres_your_card.place(relx=0.5,rely=0.5,anchor="center")
    else:
        pass


    


def home():
    a_notebook.select(0)
    a_notebook.hide(1)


#Creates the notebook to switch between frames
a_notebook=ttk.Notebook(root)
a_notebook.pack()

#Generate and pack said frames
starting_frame=tk.Frame(a_notebook,width=800,height=600)
card_depiction_frame=tk.Frame(a_notebook,width=800,height=600)
starting_frame.pack(fill="both",expand=1)
card_depiction_frame.pack(fill="both",expand=1)

#Adding the frames to the notebook:the card depiction one is there but hidden
a_notebook.add(starting_frame,text="Start")
a_notebook.add(card_depiction_frame,text="Card", state="hidden")

#Structure of the input form
upper_frame=tk.LabelFrame(card_depiction_frame,height=115,width=800,border=0)
upper_frame.place(relx=0,rely=0)
instructions=tk.Label(upper_frame, text="Insert the path to the image of the card you want to analyze and then click the button below")
instructions.place(relx=0.5,rely=0.2,anchor="center")
input_form=tk.Entry(upper_frame,width=100)
input_form.place(relx=0.5,rely=0.45,anchor="center")
kyc_button=tk.Button(upper_frame,text="KYC",command=kyc,padx=5,pady=5)
kyc_button.place(relx=0.5,rely=0.8,anchor="center")
home_button=tk.Button(card_depiction_frame,text='HOME',command=home)
home_button.place(relx=0.003,rely=0.997,anchor="sw")

#Structure of the frames in the card depiction page
card_frame=tk.LabelFrame(card_depiction_frame,height=400,width=300,border=0)
card_frame.place(relx=0.003,rely=0.95,anchor="sw")
vote_frame=tk.LabelFrame(card_depiction_frame,height=50,width=300,border=2)
vote_frame.place(relx=0.003,rely=0.2,anchor="nw")
description_frame=tk.LabelFrame(card_depiction_frame,height=430,width=495,border=1)
description_frame.place(relx=0.378,rely=0.2,anchor="nw")

#Frames in the vote frame
#Frames for each individual vote
centering_frame=tk.LabelFrame(vote_frame,width=125,height=25,border=0)
centering_frame.place(relx=0,rely=0,anchor="nw")
edges_frame=tk.LabelFrame(vote_frame,width=125,height=25,border=0)
edges_frame.place(relx=0,rely=1,anchor="sw")
corners_frame=tk.LabelFrame(vote_frame,width=125,height=25,border=0)
corners_frame.place(relx=0.4166,rely=0,anchor="nw")
surface_frame=tk.LabelFrame(vote_frame,width=125,height=25,border=0)
surface_frame.place(relx=0.4166,rely=1,anchor="sw")
#Frame for the mean aka final vote
mean_frame=tk.LabelFrame(vote_frame,width=50,height=45,border=0)
mean_frame.place(relx=0.8332,rely=0,anchor="nw")

#Structure of the description frame
name_frame=tk.LabelFrame(description_frame,height=50,width=495)
name_frame.pack()
ability_frame=tk.LabelFrame(description_frame,height=129,width=300)
ability_frame.pack()
moves_frame=tk.LabelFrame(description_frame,height=129,width=300)
moves_frame.pack()
weakness_frame=tk.LabelFrame(description_frame,height=129,width=495)
weakness_frame.pack()
another_frame=tk.LabelFrame(description_frame,height=258,width=195)
another_frame.pack()
#PROBLEMA DA RISOLVERE: se lo metto nella grid mi sfancula tutto


#Structure of the start frame
#Structure of the logo button
logo=tk.PhotoImage(file="images\Logo_placeholder.png")
logo_button=tk.Button(starting_frame,image=logo ,command=start, borderwidth=0)
logo_button.place(relx=0.5,rely=0.5, anchor="center")

#Descriptive label
to_start=tk.Label(starting_frame,text="To get to know your card click the logo above")
to_start.place(relx=0.5,rely=0.65,anchor="center")

#Credits label
credits_lbl=tk.Label(text="A project by Bianchi Christian, Mastrorilli Nicola, Ramil Leonard Vincent, Sannino Siria")
credits_lbl.place(relx=0.997,rely=0.997, anchor='se')
root.mainloop()

