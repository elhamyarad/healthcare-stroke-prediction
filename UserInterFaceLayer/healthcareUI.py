from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
from BusinessLogicLayer import BuildNBModule
from babel import dates
from babel import numbers


def entryformload():
    entryForm = Tk()
    entryForm.title("اطلاعات بیمار")
    entryForm.configure(background='light yellow')
    entryForm.geometry('650x600')
    entryForm.resizable(0, 0)
    entryForm.iconbitmap('images/entry.ico')
    right = int(entryForm.winfo_screenwidth() / 2 - 650 / 2)
    down = int(entryForm.winfo_screenheight() / 2 - 600 / 2)
    entryForm.geometry('+{}+{}'.format(right, down))

    def predictStroke():
        intWorkType = 0
        intSmoke = 0

        if txtWorkType.get() == 'Private':
            intWorkType = 1
        elif txtWorkType.get() == 'Self-employed':
            intWorkType = 2
        elif txtWorkType.get() == 'children':
            intWorkType = 3
        elif txtWorkType.get() == 'Govt_job':
            intWorkType = 4
        elif txtWorkType.get() == 'Never_worked':
            intWorkType = 5

        if txtSmoke.get() == 'never smoked':
            intSmoke = 1
        elif txtSmoke.get() == 'Unknown':
            intSmoke = 2
        elif txtSmoke.get() == 'formerly smoked':
            intSmoke = 3
        elif txtSmoke.get() == 'smokes':
            intSmoke = 4

        result = [intSex.get(), int(txtAge.get()), intHypertension.get(), intHeartDisease.get(), intMarried.get(),
                  intWorkType, intResidenceType.get(), int(txtAvgGlucoseLevel.get()), int(txtBMI.get()), intSmoke]

        predict = BuildNBModule.healthcarePredection(result)
        if predict[0][0] == 0:
            "My name is {}, I'm {}".format("John", 36)
            msg.showinfo('Predict of Stroke', "Predict is: {} with {} percent".format('No', int((predict[1][0][0])
                                                                                                * 100)))
        else:
            msg.showinfo('Predict of Stroke',
                         "Predict is: {} with {} percent".format('Yes', int((predict[1][0][1]) * 100)))

    def resetForm():
        for widget in entryForm.winfo_children():
            if type(widget) == ttk.Entry:
                widget.delete(0, END)
            if type(widget) == ttk.Combobox:
                cmbWorkType.current(0)
            if type(widget) == ttk.Radiobutton:
                intSex.set(0)
                intHypertension.set(0)
                intHeartDisease.set(0)
                intMarried.set(0)
                intResidenceType.set(0)

    lblGender = Label(entryForm, text='Gender : ', font=('Arial', 14))
    lblGender.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    intSex = IntVar()
    entSexMale = ttk.Radiobutton(entryForm, width=15, text='Female', value=1, variable=intSex)
    entSexMale.grid(row=0, column=1, padx=10, pady=0, sticky='w')

    entSexFemale = ttk.Radiobutton(entryForm, width=15, text='Male', value=2, variable=intSex)
    entSexFemale.grid(row=0, column=2, padx=10, pady=0, sticky='w')

    entSexOther = ttk.Radiobutton(entryForm, width=15, text='Other', value=3, variable=intSex)
    entSexOther.grid(row=0, column=3, padx=10, pady=0, sticky='w')

    lblAge = Label(entryForm, text='Age : ', font=('Arial', 14))
    lblAge.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    txtAge = StringVar()
    entAge = ttk.Entry(entryForm, width=15, textvariable=txtAge)
    entAge.grid(row=1, column=1, padx=10, pady=0, sticky='w')

    lblHypertension = Label(entryForm, text='Hypertension ? ', font=('Arial', 14))
    lblHypertension.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    intHypertension = IntVar()
    entHypertensionY = ttk.Radiobutton(entryForm, width=15, text='Yes', value=1, variable=intHypertension)
    entHypertensionY.grid(row=2, column=1, padx=10, pady=0, sticky='w')

    entHypertensionN = ttk.Radiobutton(entryForm, width=15, text='No', value=0, variable=intHypertension)
    entHypertensionN.grid(row=2, column=2, padx=10, pady=0, sticky='w')

    lblHeartDisease = Label(entryForm, text='HeartDisease ? ', font=('Arial', 14))
    lblHeartDisease.grid(row=3, column=0, padx=10, pady=10, sticky='w')

    intHeartDisease = IntVar()
    entHeartDiseaseY = ttk.Radiobutton(entryForm, width=15, text='Yes', value=1, variable=intHeartDisease)
    entHeartDiseaseY.grid(row=3, column=1, padx=10, pady=0, sticky='w')

    entHeartDiseaseN = ttk.Radiobutton(entryForm, width=15, text='No', value=0, variable=intHeartDisease)
    entHeartDiseaseN.grid(row=3, column=2, padx=10, pady=0, sticky='w')

    lblMarried = Label(entryForm, text='Ever married ? ', font=('Arial', 14))
    lblMarried.grid(row=4, column=0, padx=10, pady=10, sticky='w')

    intMarried = IntVar()
    entMarriedY = ttk.Radiobutton(entryForm, width=15, text='Yes', value=1, variable=intMarried)
    entMarriedY.grid(row=4, column=1, padx=10, pady=10, sticky='w')

    entMarriedN = ttk.Radiobutton(entryForm, width=15, text='No', value=0, variable=intMarried)
    entMarriedN.grid(row=4, column=2, padx=10, pady=10, sticky='w')

    WorkType = ['Private', 'Self-employed', 'children', 'Govt_job', 'Never_worked']
    lblWorkType = ttk.Label(entryForm, text='Work type: ', font=('Arial', 14))
    lblWorkType.grid(row=5, column=0, padx=10, pady=10, sticky='w')

    txtWorkType = StringVar()
    cmbWorkType = ttk.Combobox(entryForm, width=15, textvariable=txtWorkType, values=WorkType, state='readonly')
    cmbWorkType.current(0)
    cmbWorkType.grid(row=5, column=1, padx=10, pady=10)

    lblResidenceType = Label(entryForm, text='Residence Type ? ', font=('Arial', 14))
    lblResidenceType.grid(row=6, column=0, padx=10, pady=10, sticky='w')

    intResidenceType = IntVar()
    entResidenceTypeY = ttk.Radiobutton(entryForm, width=15, text='Urban', value=1, variable=intResidenceType)
    entResidenceTypeY.grid(row=6, column=1, padx=10, pady=0, sticky='w')

    entResidenceTypeN = ttk.Radiobutton(entryForm, width=15, text='Rural', value=2, variable=intResidenceType)
    entResidenceTypeN.grid(row=6, column=2, padx=10, pady=0, sticky='w')

    lblAvgGlucoseLevel = Label(entryForm, text='Average Glucose Level : ', font=('Arial', 14))
    lblAvgGlucoseLevel.grid(row=7, column=0, padx=10, pady=10, sticky='w')

    txtAvgGlucoseLevel = StringVar()
    entAvgGlucoseLevel = ttk.Entry(entryForm, width=15, textvariable=txtAvgGlucoseLevel)
    entAvgGlucoseLevel.grid(row=7, column=1, padx=10, pady=0, sticky='w')

    lblBMI = Label(entryForm, text='BMI : ', font=('Arial', 14))
    lblBMI.grid(row=8, column=0, padx=10, pady=10, sticky='w')

    txtBMI = StringVar()
    entBMI = ttk.Entry(entryForm, width=15, textvariable=txtBMI)
    entBMI.grid(row=8, column=1, padx=10, pady=0, sticky='w')

    smoking = ['never smoked', 'Unknown', 'formerly smoked', 'smokes']
    lblSmoke = ttk.Label(entryForm, text='Smoker type? ', font=('Arial', 14))
    lblSmoke.grid(row=9, column=0, padx=10, pady=10, sticky='w')

    txtSmoke = StringVar()
    cmbSmoke = ttk.Combobox(entryForm, width=15, textvariable=txtSmoke, values=smoking, state='readonly', )
    cmbSmoke.current(0)
    cmbSmoke.grid(row=9, column=1, padx=10, pady=10)

    btnReset = ttk.Button(entryForm, text='Reset Form', width=16, command=resetForm)
    btnReset.grid(row=10, column=2, padx=0, pady=10, sticky='w')

    btnPredict = ttk.Button(entryForm, text='Predict Stroke', width=20, command=predictStroke)
    btnPredict.grid(row=10, column=3, padx=0, pady=10, sticky='w')

    entryForm.mainloop()
