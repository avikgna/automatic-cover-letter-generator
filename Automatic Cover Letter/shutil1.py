import shutil
import os


source_path = r'C:\Users\Avikgna Linganathan\Downloads\CL_Template.docx'

destination_directory = 'Project-4'
project_directory = r'C:\Users\Avikgna Linganathan\PycharmProjects\Project-0'
destination_filename = 'CL_Template.docx'
destination_path = os.path.join(project_directory, destination_directory, destination_filename)

shutil.move(source_path, destination_path)