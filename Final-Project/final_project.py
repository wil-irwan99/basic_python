#import module Yagmail
import yagmail

#definisi variabel (subject, isi, dan attachment file pada email)
subject = 'Final Project Basic Python'
content = 'Berikut adalah file yang memuat tugas akhir dari course Basic Python'
berkas = r'C:\Users\ASUS\Testing\berkas\Copy of Final Project - Basic Python.pdf'

#input pengirim email
user_email = str(input('Masukkan email Anda : '))
user_password = str(input('Masukkan password email Anda : '))

#ambil email tujuan dari list
with open("receiver_list.txt", "r") as filex:
    list_email = filex.read().splitlines()

try:
    #initializing the server connection
    yag = yagmail.SMTP(user=user_email, password=user_password)
    #sending the email
    yag.send(to= list_email,  subject=subject, contents=content, attachments= berkas)
    print("Email sent successfully")
except:
    print("Error, email was not sent")
