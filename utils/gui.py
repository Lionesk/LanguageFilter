from tkinter import *
from features import filter
from utils import lines


root = Tk()

filter_output = StringVar()


def display_filtered():
    global text_entry
    filter_output.set(filter.filtertext(filter.linesToList(lines.stringToLines(text_entry.get()))))

top_label = Label(root, text="Language Filter")

text_entry = Entry(root)

button1 = Button(text="Test", bg="red", command=display_filtered)

message = Message(root, textvariable=filter_output)

top_label.pack()
text_entry.pack()
button1.pack()
message.pack()

root.mainloop()
