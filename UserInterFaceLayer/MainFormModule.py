from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import UserInterFaceLayer.healthcareUI


def patienFormLoad(firstName, lastName):
    mainForm = Tk()
    mainForm.title('PatientForm')
    mainForm.geometry('400x400')
    mainForm.resizable(0, 0)
    mainForm.iconbitmap('images/Doctor.ico')
    right = int(mainForm.winfo_screenwidth() / 2 - 400 / 2)
    down = int(mainForm.winfo_screenheight() / 2 - 400 / 2)

    def entryformfunction():
        mainForm.destroy()
        UserInterFaceLayer.healthcareUI.entryformload()

    mainForm.geometry('+{}+{}'.format(right, down))
    lblWelcomeMessage = ttk.Label(mainForm, text='Welcome ' + firstName + ' ' + lastName + '!')
    lblWelcomeMessage.grid(row=0, column=0, padx=20, pady=20, sticky='n')

    patientPhoto = PhotoImage(file='images/Patient.png')
    btnPatient = Button(mainForm, text='Patient', image=patientPhoto, compound=TOP, pady=10,
                        width=100, height=100, command=entryformfunction)

    btnPatient.grid(row=1, column=0, padx=20, pady=20, sticky='w')

    mainForm.mainloop()
