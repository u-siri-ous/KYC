import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import csv


#Nicola's command that ChatGPT cancelled but it doesn't run yet so we don't know if it works
def kyc(p_name, cen, cor, edg, sur, a_notebook, card_depiction_frame, card_frame, centering_frame, edges_frame, corners_frame, surface_frame, mean_frame,inner_name_frame,set_frame,set_base_var,fossil_var,jungle_var,pv_frame,type_frame,ability_name_frame,ability_effect_frame,move1_name_frame,move1_cost_frame,move1_effect_frame,move1_damage_frame,move2_name_frame,move2_cost_frame,move2_effect_frame,move2_damage_frame,weakness_frame,resistance_frame,retreat_frame,rarity_frame):
        
    if set_base_var.get()==1:
        set='Base'
    elif fossil_var.get()==1:
        set='Fossil'
    elif  jungle_var.get()==1:
        set='Jungle'
    
    with open(f'data/datasets/{set}/{set}_ds.CSV', mode='r', encoding='latin-1') as file:
        # Create a CSV reader
        print(file)
        csv_reader = csv.reader(file,delimiter=';')

        # Skip the header row
        next(csv_reader)

        # Perform the query
        for row in csv_reader:
            if row[0] == p_name:
                p_details = row

    a_notebook.tab(card_depiction_frame, state="normal")
    a_notebook.select(card_depiction_frame)
    card = Image.open("code/card.jpg")
    resized=card.resize((300,375))
    card_pic=ImageTk.PhotoImage(resized)
    image_label=tk.Label(card_frame,image=card_pic)
    image_label.image=card_pic #Very important to display the photo correctly
    image_label.place(relx=0.5,rely=0.5,anchor='center')
    centering_label=tk.Label(centering_frame,text="Centering  {}  ".format(cen)) # Centering Value
    centering_label.place(relx=0.1,rely=0.5,anchor="w")
    edges_label=tk.Label(edges_frame,text="Edges         {}  ".format(edg))  # Edges Value
    edges_label.place(relx=0.1,rely=0.5,anchor="w")
    corners_label=tk.Label(corners_frame,text="Corners  {}  ".format(cor))  # Corners Value
    corners_label.place(relx=0.1,rely=0.5,anchor="w")
    surface_label=tk.Label(surface_frame,text="Surface  {}  ".format(sur))  # Surface Value
    surface_label.place(relx=0.1,rely=0.5,anchor="w")
    mean=(cen+cor+edg+sur)//4
    mean_label=tk.Label(mean_frame,text="{}".format(mean),font='80')  # Final Value
    mean_label.place(relx=0.5,rely=0.5,anchor='center')
    pokemon_name_label=tk.Label(inner_name_frame,text=f'{p_details[0]}',font='Helvetica 20',pady=1) # Pokemon name
    pokemon_name_label.place(relx=0.5,rely=0.35,anchor='n')
    set_name_label=tk.Label(set_frame,text='',font='Helvetica 15') #Set the card is from
    set_name_label.place(relx=0.25,rely=0.5,anchor='w')
    set_name_label.configure(text=f'{set}')
    rarity_label=tk.Label(rarity_frame,text=f'{p_details[2]}',font='Helvetica 15') #Rarity
    rarity_label.place(relx=0.25,rely=0.5,anchor='w')
    pv_number_label=tk.Label(pv_frame,text=f'{p_details[4]}',font='Helvetica 10') # Pokemon PV
    pv_number_label.place(relx=0.5,rely=0.5,anchor="center")
    type_name_label=tk.Label(type_frame,text=f'{p_details[1]}',font='Helvetica 10') # Pokemon Type
    type_name_label.place(relx=0.5,rely=0.5,anchor="center")
    ability_name_label=tk.Label(ability_name_frame,text=f'{p_details[5]}',font='Helvetica 15') # Ability Name
    ability_name_label.place(relx=0.5,rely=0.5,anchor='center')
    ability_effect_label=tk.Label(ability_effect_frame,text=f'{p_details[16]}',font='Helvetica 10', justify='left',wraplength=300) # Ability Description MISSING
    ability_effect_label.place(relx=0.5,rely=0.5,anchor='center')
    move1_name_label=tk.Label(move1_name_frame,text=f'{p_details[6]}',font='Helvetica 15') # Move 1 Name
    move1_name_label.place(relx=0.5,rely=0.5,anchor="center")
    move1_cost_label=tk.Label(move1_cost_frame,text=f'{p_details[8]}',font='Helvetica 10') # Move 1 Cost
    move1_cost_label.place(relx=0.5,rely=0.5,anchor="center")
    move1_effect_label=tk.Label(move1_effect_frame,text=f'{p_details[17]}',font='Helvetica 10',justify='left',wraplength=300) # Move 1 Effect MISSING
    move1_effect_label.place(relx=0.5,rely=0.5,anchor="center")
    move1_damage_label=tk.Label(move1_damage_frame,text=f'{p_details[7]}',font='Helvetica 10') # Move 1 Damage
    move1_damage_label.place(relx=0.5,rely=0.5,anchor="center")
    move2_name_label=tk.Label(move2_name_frame,text=f'{p_details[9]}',font='Helvetica 15') # Move 2 Name
    move2_name_label.place(relx=0.5,rely=0.5,anchor="center")
    move2_cost_label=tk.Label(move2_cost_frame,text=f'{p_details[11]}',font='Helvetica 10') # Move 2 Cost
    move2_cost_label.place(relx=0.5,rely=0.5,anchor="center")
    move2_effect_label=tk.Label(move2_effect_frame,text=f'{p_details[18]}',font='Helvetica 10',justify='left',wraplength=300) # Move 2 Effect MISSING
    move2_effect_label.place(relx=0.5,rely=0.5,anchor="center")
    move2_damage_label=tk.Label(move2_damage_frame,text=f'{p_details[10]}',font='Helvetica 10') # Move 2 Damage
    move2_damage_label.place(relx=0.5,rely=0.5,anchor="center")
    weakness_specification_label=tk.Label(weakness_frame,text=f'{p_details[12]}',font='Helvetica 10') # Weakness
    weakness_specification_label.place(relx=0.5,rely=0.5,anchor='center')
    resistance_specification_label=tk.Label(resistance_frame,text=f'{p_details[13]}',font='Helvetica 10') #text to be filled with resistance
    resistance_specification_label.place(relx=0.5,rely=0.5,anchor='center')
    retreat_specification_label=tk.Label(retreat_frame,text=f'{p_details[14]}',font='Helvetica 10') #text to be filled with retreat
    retreat_specification_label.place(relx=0.5,rely=0.5,anchor='center')

def set_base_toggle(set_base_checkbox, fossil_checkbox, jungle_checkbox, set_base_var,fossil_var, jungle_var, logo_button):
    set_base_checkbox.toggle()
    fossil_checkbox.deselect()
    jungle_checkbox.deselect()
    if set_base_var.get()==1 or fossil_var.get()==1 or jungle_var.get()==1:
       logo_button.configure(state="normal")
    else:
        logo_button.configure(state='disabled')
     
    
def fossil_toggle(fossil_checkbox, jungle_checkbox, set_base_checkbox, set_base_var,fossil_var,jungle_var, logo_button):
    fossil_checkbox.toggle()
    jungle_checkbox.deselect()
    set_base_checkbox.deselect()
    if set_base_var.get()==1 or fossil_var.get()==1 or jungle_var.get()==1:
        logo_button.configure(state="normal")
    else:
        logo_button.configure(state='disabled')
     

def jungle_toggle(jungle_checkbox, fossil_checkbox, set_base_checkbox, set_base_var,fossil_var,jungle_var, logo_button):
    jungle_checkbox.toggle()
    fossil_checkbox.deselect()
    set_base_checkbox.deselect()
    if set_base_var.get()==1 or fossil_var.get()==1 or jungle_var.get()==1:
        logo_button.configure(state="normal")
    else:
        logo_button.configure(state='disabled')
     

def GUI(p_name, cen, cor, edg, sur):
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

    a_notebook.add(starting_frame, text="Start")
    a_notebook.add(card_depiction_frame, text="Card")
    a_notebook.tab(card_depiction_frame, state="hidden")

    # Structure of the start frame
    logo = Image.open("images/GUI/Logo_res.png")
    resized_logo=logo.resize((400,400))
    new_logo=ImageTk.PhotoImage(resized_logo)
    logo_button = tk.Button(starting_frame, image=new_logo, command=lambda :kyc(p_name, cen, cor, edg, sur, a_notebook, card_depiction_frame, card_frame, centering_frame, edges_frame, corners_frame, surface_frame, mean_frame,inner_name_frame,set_frame,set_base_var,fossil_var,jungle_var,pv_frame,type_frame,ability_name_frame,ability_effect_frame,move1_name_frame,move1_cost_frame,move1_effect_frame,move1_damage_frame,move2_name_frame,move2_cost_frame,move2_effect_frame,move2_damage_frame,weakness_frame,resistance_frame,retreat_frame,rarity_frame), borderwidth=0,state="disabled")
    logo_button.place(relx=0.5, rely=0.4, anchor="center")
    #Set Base check structure
    set_base_var=tk.IntVar()
    set_base_checkbox=tk.Checkbutton(starting_frame,variable=set_base_var,border=0,state="disabled",relief="flat")
    set_base_checkbox.place(relx=0.4,rely=0.85,anchor="center")
    setbase_logo = Image.open('images/GUI/setbase.png')
    resized_setbase=setbase_logo.resize((25,25))
    new_setbase_logo=ImageTk.PhotoImage(resized_setbase)
    set_base_button=tk.Button(starting_frame,image=new_setbase_logo,border=1,command=lambda: set_base_toggle(set_base_checkbox, fossil_checkbox, jungle_checkbox, set_base_var,fossil_var,jungle_var, logo_button))
    set_base_button.place(relx=0.397,rely=0.8,anchor="center")
    #Fossil check structure
    fossil_var=tk.IntVar()
    fossil_checkbox=tk.Checkbutton(starting_frame,variable=fossil_var,border=0,state="disabled",relief='flat')
    fossil_checkbox.place(relx=0.5,rely=0.85,anchor="center")
    fossil_logo = Image.open('images/GUI/fossil.png')
    resized_fossil=fossil_logo.resize((25,25))
    new_fossil_logo=ImageTk.PhotoImage(resized_fossil)
    fossil_button=tk.Button(starting_frame,image=new_fossil_logo,border=1,command=lambda: fossil_toggle(fossil_checkbox, jungle_checkbox, set_base_checkbox, set_base_var,fossil_var,jungle_var, logo_button))
    fossil_button.place(relx=0.497,rely=0.8,anchor="center")
    #Jungle check structure
    jungle_var=tk.IntVar()
    jungle_checkbox=tk.Checkbutton(starting_frame,variable=jungle_var,border=0,state="disabled",relief="flat")
    jungle_checkbox.place(relx=0.6,rely=0.85,anchor="center")
    jungle_logo = Image.open('images/GUI/jungle.png')
    resized_jungle=jungle_logo.resize((25,25))
    new_jungle_logo=ImageTk.PhotoImage(resized_jungle)
    jungle_button=tk.Button(starting_frame,image=new_jungle_logo,border=1,command=lambda: jungle_toggle(jungle_checkbox, fossil_checkbox, set_base_checkbox, set_base_var,fossil_var,jungle_var, logo_button))
    jungle_button.place(relx=0.597,rely=0.8,anchor="center")

    # Descriptive label
    to_start = tk.Label(starting_frame, text="To get to know your card,select below the expansion it is from and then click the logo")
    to_start.place(relx=0.5, rely=0.75, anchor="center")

    # Credits label
    credits_lbl = tk.Label(text="A project by Bianchi Christian, Mastrorilli Nicola, Ramil Leonard Vincent, Sannino Siria")
    credits_lbl.place(relx=0.997, rely=0.997, anchor='se')
    # Structure of the card depiction frame
    # Structure of the upper frame
    upper_frame = tk.Frame(card_depiction_frame, border=0)
    upper_frame.place(relx=0, rely=0,relwidth=1, relheight=0.2)
    here_it_is=tk.PhotoImage(file="images/GUI/Logo.png") #da sostituire con scritta here's your card! con font bellini che riprendono il logo 
    heres_your_card=tk.Label(upper_frame,image=here_it_is)
    heres_your_card.image=here_it_is
    heres_your_card.place(relx=0.5,rely=0.5,anchor="center")

    card_frame = tk.LabelFrame(card_depiction_frame, border=0)
    card_frame.place(relx=0, rely=0.3, relwidth=0.35,relheight=0.65, anchor="nw")
    vote_frame = tk.LabelFrame(card_depiction_frame, height=50, width=300, border=2)
    vote_frame.place(relx=0, rely=0.2, relwidth=0.35,relheight=0.1, anchor="nw")
     # Frames for each individual vote
    centering_frame = tk.Frame(vote_frame,  border=0)
    centering_frame.place(relx=0, rely=0,relheight=0.5,relwidth=0.4, anchor="nw")
    edges_frame = tk.Frame(vote_frame,  border=0)
    edges_frame.place(relx=0, rely=0.5, relheight=0.5,relwidth=0.4, anchor="nw")
    corners_frame = tk.Frame(vote_frame,  border=0)
    corners_frame.place(relx=0.4, rely=0, relheight=0.5,relwidth=0.4, anchor="nw")
    surface_frame = tk.Frame(vote_frame,   border=0)
    surface_frame.place(relx=0.4, rely=0.5, relheight=0.5,relwidth=0.4, anchor="nw")
    # Frame for the mean aka final vote
    mean_frame = tk.Frame(vote_frame,  border=0 )
    mean_frame.place(relx=0.8, rely=0, relheight=1,relwidth=0.2, anchor="nw")

    #Name frame
    name_frame=tk.LabelFrame(card_depiction_frame)
    name_frame.place(relx=0.35,rely=0.2, relheight=0.1,relwidth=0.65,anchor='nw')
     #Frames in name frame
    inner_name_frame=tk.Frame(name_frame)
    inner_name_frame.place(relx= 0,rely=0,relheight=1,relwidth=0.333)
    inner_name_label=tk.Label(inner_name_frame,text='Pokemon Name',font='Helvetica 8')
    inner_name_label.place(relx=0.5,rely=0.1,anchor='n')
    set_frame=tk.Frame(name_frame,background='red')
    set_frame.place(relx=0.333,rely=0,relheight=0.5,relwidth=0.333)
    rarity_frame=tk.Frame(name_frame)
    rarity_frame.place(relx=0.333,rely=0.5,relheight=0.5,relwidth=0.333)
    rarity_descriptive_label=tk.Label(rarity_frame,text='Rarity:',font='Helvetica 10')
    rarity_descriptive_label.place(relx=0.1,rely=0.5,anchor='w')
    set_descriptive_label=tk.Label(set_frame,text='Set:',font='Helvetica 10')
    set_descriptive_label.place(relx=0.1,rely=0.5,anchor='w')
    pv_frame=tk.Frame(name_frame)
    pv_frame.place(relx=0.666,rely=0,relheight=0.5,relwidth=0.333)
    pv_label=tk.Label(pv_frame,text='PV:',font='Helvetica 10')
    pv_label.place(relx=0.1,rely=0.5,anchor="w")
    type_frame=tk.Frame(name_frame)
    type_frame.place(relx=0.666,rely=0.5,relheight=0.5,relwidth=0.333)
    type_label=tk.Label(type_frame,text='Type:',font='Helvetica 10')
    type_label.place(relx=0.1,rely=0.5,anchor="w")

    #Description frame:
    description_frame = tk.LabelFrame(card_depiction_frame, border=1)
    description_frame.place(relx=0.35, rely=0.3, relheight=0.65,relwidth=0.65, anchor="nw")
    #structure of the description frame
    # Structure of the ability frame
    ability_frame = tk.Frame(description_frame)
    ability_frame.place(relx=0,rely=0,relheight=0.25,relwidth=1,anchor='nw')
    ability_name_frame=tk.Frame(ability_frame)
    ability_name_frame.place(relx=0,rely=0,relwidth=0.3,relheight=1)
    ability_effect_frame=tk.Frame(ability_frame)
    ability_effect_frame.place(relx=0.3,rely=0,relwidth=0.7,relheight=1)
    # Structure of the move1 frame
    move1_frame = tk.Frame(description_frame)
    move1_frame.place(relx=0,rely=0.25,relheight=0.25,relwidth=1,anchor='nw')
    move1_name_frame=tk.Frame(move1_frame)
    move1_name_frame.place(relx=0,rely=0,relheight=1,relwidth=0.3)
    move1_cost_frame=tk.Frame(move1_frame)
    move1_cost_frame.place(relx=0.3,rely=0,relheight=1,relwidth=0.1)
    move1_effect_frame=tk.Frame(move1_frame)
    move1_effect_frame.place(relx=0.4,rely=0,relheight=1,relwidth=0.5)
    move1_damage_frame=tk.Frame(move1_frame)
    move1_damage_frame.place(relx=0.9,rely=0,relheight=1,relwidth=0.1)
    # Structure of the move2 frame
    move2_frame = tk.Frame(description_frame)
    move2_frame.place(relx=0,rely=0.5,relheight=0.25,relwidth=1,anchor='nw')
    move2_name_frame=tk.Frame(move2_frame)
    move2_name_frame.place(relx=0,rely=0,relheight=1,relwidth=0.3)
    move2_cost_frame=tk.Frame(move2_frame)
    move2_cost_frame.place(relx=0.3,rely=0,relheight=1,relwidth=0.1)
    move2_effect_frame=tk.Frame(move2_frame)
    move2_effect_frame.place(relx=0.4,rely=0,relheight=1,relwidth=0.5)
    move2_damage_frame=tk.Frame(move2_frame)
    move2_damage_frame.place(relx=0.9,rely=0,relheight=1,relwidth=0.1)
    #Structure of the lower frame
    lower_frame = tk.Frame(description_frame)
    lower_frame.place(relx=0,rely=0.75,relheight=0.25,relwidth=1,anchor='nw')
    #Wekness frame
    weakness_frame=tk.Frame(lower_frame)
    weakness_frame.place(relx=0,rely=0,relheight=1,relwidth=0.333)
    weakness_label=tk.Label(weakness_frame,text='Weakness',font='Helvetica 10')
    weakness_label.place(relx=0.5,rely=0.25,anchor='center')
    #Resistance frame
    resistance_frame=tk.Frame(lower_frame)
    resistance_frame.place(relx=0.333,rely=0,relheight=1,relwidth=0.333)
    resistance_label=tk.Label(resistance_frame,text='Resistance',font='Helvetica 10')
    resistance_label.place(relx=0.5,rely=0.25,anchor='center')
    #Retreat frame
    retreat_frame=tk.Frame(lower_frame)
    retreat_frame.place(relx=0.666,rely=0,relheight=1,relwidth=0.333)
    retreat_label=tk.Label(retreat_frame,text='Retreat cost',font='Helvetica 10')
    retreat_label.place(relx=0.5,rely=0.25,anchor='center')

    # Start the application's main loop
    root.mainloop()