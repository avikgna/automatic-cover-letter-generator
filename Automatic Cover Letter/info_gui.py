import tkinter as tk
import csv

window = tk.Tk()

window.title('Personal Job Details')
header = tk.Label(window, text='Input Your Details Below', font=('Times New Roman', 23))
header.pack(pady=20)


def create_personal_label_entry(parent, label_text):
    label = tk.Label(parent, text=label_text, font=('Times New Roman',12))
    entry = tk.Entry(parent, bg='#FFFDD0', width=40)
    label.pack()
    entry.pack(pady=10)
    return label, entry

personal_widgets=[ create_personal_label_entry(window, 'Name'),
        create_personal_label_entry(window, 'Phone Number'),
        create_personal_label_entry(window, 'Email address'),
                  ]

def create_job_label_entry(parent, label_text):
    label = tk.Label(parent, text=label_text, font=('Times New Roman', 12))
    entry = tk.Entry(parent, bg='#FFFDD0', width=40)
    label.pack()
    entry.pack(pady=10)
    return label, entry

job_widgets =  [ create_job_label_entry(window, 'Previous job posistion'),
                 create_job_label_entry(window, 'First Technical Skill from previous job'),
                 create_job_label_entry(window, 'Second Technical Skill'),
                 create_job_label_entry(window, 'A Soft Skill you developed'),
                 create_job_label_entry(window, 'Name of your previous company')
                  ]


def create_label_textbox(parent, text_box):
    label = tk.Label(parent, text=text_box, font=('Times New Roman',12))
    box = tk.Text(parent, bg='#FFFDD0', width=35, height=6)
    label.pack(pady=10)
    box.pack()
    return label, box

text_boxes = [create_label_textbox(window, 'Briefly describe your previous role'),]

def retrieve_info():
    job_info = [entry.get() for _, entry in job_widgets]
    personal_info = [entry.get() for _, entry in personal_widgets]
    text_info = [box.get('1.0', tk.END) for _, box in text_boxes]

    all_info = personal_info + job_info + text_info

    csv_file = 'CL_info.csv'
    with open(csv_file, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Name', 'Phone Number', 'Email Address', 'Previous Job Posistion', 'Technical Skill (1)',
                             'Technical Skill (2)', 'Soft Skill','Previous Company Name', 'Past Job Role Description'])
        csv_writer.writerow(all_info)

send_button = tk.Button(text='Send', font=('Times New Roman bold', 12), width=10, bg='#7C4700', fg='white',
                        command=retrieve_info)



send_button.pack(pady=18)
header.pack()
window.geometry('600x800')
window.mainloop()
