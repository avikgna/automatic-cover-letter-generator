import info_gui
import SEEK_webscraper
from docxtpl import DocxTemplate
import csv
from datetime import datetime

today_date = datetime.now().strftime('%d-%m-%Y')


with open('CL_info.csv', 'r') as f1:
    csv_reader1 = csv.DictReader(f1)
    for gui_data in csv_reader1:
        Name = gui_data['Name']
        HP = gui_data['Phone Number']
        email = gui_data['Email Address']
        PJP = gui_data['Previous Job Posistion']
        TS1 = gui_data['Technical Skill (1)']
        TS2 = gui_data['Technical Skill (2)']
        SS = gui_data['Soft Skill']
        PJRD = gui_data['Past Job Role Description']
        PCN = gui_data['Previous Company Name']


with open('job_scope.csv', 'r') as f2:
    csv_reader2 = csv.DictReader(f2)
    for job_data in csv_reader2:
        PN = job_data['Posistion Name']
        CN = job_data['Company Name']
        CA = job_data['Company Address']

context = {
    'name' : Name, 'phone_number' : HP, 'email_address' : email, 'previous_job_posistion' : PJP,
    'technical_skill1' : TS1, 'technical_skill2' : TS2, 'soft_skill' : SS, 'past_job_role_description' : PJRD,
    'posistion_name' : PN, 'company_name'  : CN, 'company_address' : CA, 'curr_date' : today_date,
    'previous_company_name' : PCN
}

template_doc = DocxTemplate('CL_Template.docx')
template_doc.render(context)
template_doc.save('CL_Template'+ '_' + CN + '_'+ PN +'.docx')

