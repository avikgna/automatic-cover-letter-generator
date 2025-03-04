from bs4 import BeautifulSoup
import tkinter as tk
import requests
import csv

def send_url_GUI():
    url = entry.get()
    web_scraping(url)
# Sending url for webscraping (command for GUI button)

def web_scraping(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            content = BeautifulSoup(response.text,'html.parser')

            job_name = content.find_all('h1', class_= '_4603vi0 _9l8a1v4y _1wqtj1z0 _1wqtj1zl _1rhqcq74 _1wqtj1zs _1wqtj1z21')

            company_name = content.find_all('span',
                                            class_ = '_4603vi0 _9l8a1v4y _1wqtj1z0 _1wqtj1z1 _1wqtj1z21 _1rhqcq74 _1wqtj1za')

            location_name = content.find_all('span', class_ = '_4603vi0 _9l8a1v4y _1wqtj1z0 _1wqtj1z1 _1wqtj1z21 _1rhqcq74 _1wqtj1z7')


            csv_file = 'job_scope.csv'
            with open(csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Posistion Name', 'Company Name', 'Company Address'])

                for job, company, location in zip(job_name, company_name, location_name):
                    row = [job.text.strip(), company.text.strip(), location.text.strip()]
                    writer.writerow(row)
        else:
            print(f'Error Loading Webpage. Status code: {response.status_code}')

    except requests.RequestException as e:
        print(f'An error has occured: {e}')



window = tk.Tk()

window.title('Seek Webscraper')

header = tk.Label(window, text='Input URL :)',
                  font=('Times New Roman', 24),
                    )
entry = tk.Entry(width=60)
send_button = tk.Button(text='Send',
                        fg='white',
                        bg='green',
                        font=('Times New Roman', 14),
                        width=10,
                        command=send_url_GUI
                        )

header.pack(pady=50)
entry.pack()
send_button.pack(pady=30)
window.geometry('500x250')
window.mainloop()