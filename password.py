from tkinter import *
import pyperclip, random


f = ("poppins", 20, "bold")
t = ("poppins", 10, "bold")
b = "#FFFFFF"
a = "#000000"


window = Tk()
window.geometry("600x400")
window.config(bg=b)
pass_str = StringVar()
pass_length = IntVar()
pass_length.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    
    password = ""
    
    for x in range(pass_length.get()):
        password += random.choice(pass1)
    
    pass_str.set(password)
    
def copy():
    random_password = pass_str.get()
    pyperclip.copy(random_password)
    
   
    
Label(window, text="Random Password Generator", font=f, bg=b, fg=a).pack(pady=30)

Label(window, text="Enter Password Length", font=t, bg=b, fg=a).pack(pady=5)
Entry(window, textvariable=pass_length).pack(pady=10)

Button(window, text="Generate Password", command=generate, activebackground=b, activeforeground=a).pack(pady=7)

Entry(window, textvariable=pass_str).pack(pady=10)

Button(window, text="Copy to Clipboard", command=copy, activebackground=b, activeforeground=a).pack(pady=7) 


window.mainloop()
    

