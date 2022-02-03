from email import message
from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generar():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    E_password.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def guardar():
    
    site=E_site.get()
    email=E_email.get()
    password=E_password.get()
    new_data={
        site:{
            "email":email,
            "password":password,
        }
        
        }
    
    if site == "" or email=="" or password=="" or email==ejemplo_mail:
        messagebox.showwarning(title="Error", message="Falta algún campo por rellenar")
    else:
            try:
                with open("data.json", "r") as data_file:
                  
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:              
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
               E_site.delete(0, END)
               E_password.delete(0, END)

# ---------------------------- BUSCAR ------------------------------- #
def Buscar():
    site = E_site.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No hay un archivo con datos")
    else:
        if site in data:
            email = data[site]["email"]
            password = data[site]["password"]
            messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Sin detalles si {site} existe. ")
        


# ---------------------------- UI SETUP ------------------------------- #

ventana = Tk()
ventana.title("Gestor de Contraseñas")
ventana.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1, columnspan=2)

#Etiquetas

L_site=Label(text="Website:")
L_site.grid(row=1,column=0,)
L_email=Label(text="Email/Usuario:")
L_email.grid(row=2,column=0)
L_password=Label(text="Password:")
L_password.grid(row=3,column=0)

#Entradas
E_site=Entry(width=35)
E_site.grid(row=1,column=1,columnspan=2)
E_email=Entry(width=35)
E_email.grid(row=2,column=1,columnspan=2)
ejemplo_mail="ejemplodeemail@outlook.com"
E_email.insert(0,ejemplo_mail)
E_password=Entry(width=21)
E_password.grid(row=3,column=1)

#Botones
B_genera_password=Button(text="Autogenerar", command=generar)
B_genera_password.grid(row=3,column=2)

B_anyade=Button(text="Añadir", command=guardar)
B_anyade.grid(row=4,column=1,columnspan=2)

B_Buscar=Button(text="Buscar",command=Buscar)
B_Buscar.grid(row=1,column=3)


ventana.mainloop()