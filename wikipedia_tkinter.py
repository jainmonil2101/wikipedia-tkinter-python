from tkinter import *
import wikipedia

root = Tk()
root.title("Wikipedia")
root.geometry("800x450")
root.iconbitmap("wikipedia.ico")
root.config(bg="white")
root.resizable(False, False)

img = PhotoImage(file="wikipedia.png")

img_label = Label(root, image=img, bg="white")
img_label.place(relx=0.5, rely=0.15, anchor=CENTER)


search_box = Entry(root, font=("Helvetica", 18), width=38, bd=2)
search_box.place(relx=0.5, rely=0.36, anchor=CENTER)

new_frame = ""
label_frame = ""

def gb():
    new_frame.destroy()

def showResult():
    global new_frame, label_frame
    

    new_frame = Frame(root, height=450, width=800, bg="white")
    new_frame.pack()
    monil = search_box.get()


    go_back = Button(new_frame, text="Go Back", relief=FLAT, font=("Helvetica", 13), width=12, command=gb)
    go_back.place(relx=0.8, rely=0.1)

    answer = Text(new_frame, width=64, height=13, bd=2, font=("Helvetica", 16), fg="blue")
    answer.place(relx=0.015, rely=0.28)

    try:
        query = wikipedia.page(monil)
        answer.insert(END, f"{query.summary}")
    except Exception:
        answer.insert(END, f"No results found for {monil.capitalize()}")
        search_box.delete(0, "end")

    label_1 = Label(new_frame, text=f"Search results for {query.title}", fg="white",font=("Helvetica", 23), bg="gray")
    label_1.place(relx=0.04, rely=0.09)
    

    search_box.delete(0, "end")


search_btn = Button(root, text="Search Wikipedia", font=(
    "Helvetica", 14), relief=FLAT, command=showResult)
search_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
