#Panyakup Chanwiset
#6310742728

from socket import * #Library สำหรับใช้งาน socket
from threading import * #Module สำหรับการสร้างและทำงานของ Thread
from tkinter import * #Library สำหรับตกแต่ง Gui

#สร้าง socket object ไว้สำหรับเรียกใช้งาน API ของ socket
clientSocket = socket(AF_INET, SOCK_STREAM) #สร้าง object ในการเชื่อมต่อกับ socket
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #ฟังก์ชั่นให้สามารถใช้ port เดิมได้

hostIp = "127.0.0.1" #กำหนดเป็น IP ของ server ที่ใช้เชื่อมต่อ
portNumber = 2728 #port ที่จะใช้ในการติดต่อ
addr = (hostIp,portNumber) #รวม hostIP กับ portNumber เข้าเป็น tuple เดียวกัน
clientSocket.connect((addr)) #เชื่อมต่อกับ IP และ port

window = Tk() #สร้างหน้าต่างขึ้นมา
window.title("Welcome To : Mario Chat") #ตั้งชื่อของหน้าต่าง
window.geometry("480x550") #กำหนดขนาดหน้าจอ

#กำหนดรูปภาพเป็นภาพพื้นหลัง
mario = PhotoImage(file="mariott_background.png") #แนบไฟล์รูปภาพ
my_label = Label(window, image=mario) #การใส่รูปภาพ
my_label.place(x=0, y=0, relwidth=1, relheight=1) #ปรับขนาดของรูปภาพพื้นหลัง
#window.configure(background='#CCFFFF')>>กรณีต้องการเปลี่ยนภาพพื้นหลังเป็นแค่สี

#txtMessages = Text(window, width=65, bg="#aec8ef") #กำหนดขนาดของกล่องข้อความและสีพื้นหลัง(1)
txtMessages = Text(window, width=65, bg="#a9dfbf") #กำหนดขนาดของกล่องข้อความและสีพื้นหลัง(2)
txtMessages.grid(row=0, column=0, padx=0, pady=0) #กำหนดตำแหน่งของกล่องข้อความ

typeYourMessage = Entry(window, width=50) #กำหนดขนาดของกล่องพิมพ์ข้อความ(Entry คือการใช้ฟังก์ชั่นกรอกข้อความ)
typeYourMessage.insert(0,"Type your message here...") #กำหนดคำที่อยู่ในกล่องพิมพ์ข้อความ
typeYourMessage.grid(row=1, column=0, padx=10, pady=10) #กำหนดตำแหน่งของกล่องพิมพ์ข้อความ

#กำหนดคำสั่งเมื่อคลิกส่งข้อความ
def sendMessage():
    clientMessage = typeYourMessage.get() #ดึงข้อความมาแสดงผล
    txtMessages.insert(END, "\n" + "You: "+ clientMessage) #กำหนดความเรียบร้อยของข้อความให้มีการแสดงผู้ส่งและขึ้นบรรทัดใหม่
    clientSocket.send(clientMessage.encode("utf-8")) #ส่งข้อมูลโดยก่อนส่งได้เข้ารหัสตัวอักษรเป็น utf-8

btnSendMessage = Button(window, text="Send", fg="Blue", font=10 ,width=5, command=sendMessage) #กำหนดปุ่มส่งข้อความ
btnSendMessage.grid(row=2, column=0, padx=10, pady=10) #กำหนดตำแหน่งของปุ่มส่งข้อความ

def recvMessage():
    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8") #ดึงผลลัพธ์การรับข้อมูลที่เข้ามาเป็น string
        print(serverMessage) #แสดงผลข้อความ
        txtMessages.insert(END, "\n"+serverMessage) #กำหนดให้มีการขึ้นบรรทัดใหม่

recvThread = Thread(target=recvMessage) #สร้างThreadมาเก็บในตัวแปรrecvThreadในคอนสตรัคเตอร์นั้นเราสามารถส่งอาร์กิวเมนต์target=recvMessage
recvThread.daemon = True #โดยหาก Thread หลักจบการทำงาน recvThread.daemon ก็จะจบการทำงานไปด้วย
recvThread.start() #เป็นการบอกให้ Thread เริ่มการทำงาน

window.mainloop() #ลูปทำการรันวนเรื่อยๆเมื่อทำการสั่งรันโปรแกรมเพื่อดูการทำงานในหน้าต่าง