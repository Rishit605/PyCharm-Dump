import customtkinter
# import tkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1270x720")

# # Creating the frame
# frame = customtkinter.CTkFrame(master = app)
# frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
#
#
# def btn_fn():
#     img = Image.open('0002.png')
#     img = img.resize((1270, 720))
#     img = ImageTk.PhotoImage(img)
#     label = customtkinter.CTkLabel(master=frame, image=img, text="JK LOL!", text_color="red")
#     label.pack()
#     print("button pressed")
#
# # # Use CTkButton for displaying the image
# button = customtkinter.CTkButton(master=frame, text="Display Image", command=btn_fn())
# button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
# button.pack()

import tkinter as tk

# create the main window
root = tk.Tk()

# create a button
# button = tk.Button(root, text="Click me!")
button = tk.Button(root, text="Click me!", font=("Arial", 12), bg="red", fg="white", command=my_function)


# pack the button into the window
button.pack()

# start the main event loop
root.mainloop()


# app.mainloop()

