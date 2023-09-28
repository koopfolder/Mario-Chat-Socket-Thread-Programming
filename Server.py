#Panyakup Chanwiset
#6310742728

from socket import * #Library สำหรับใช้งาน Socket
from threading import * #Module สำหรับการสร้างและทำงานของ Thread

#สร้าง socket object ไว้สำหรับเรียกใช้งาน API ของ socket
hostSocket = socket(AF_INET, SOCK_STREAM) #สร้าง object ในการเชื่อมต่อกับ socket
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1) #ฟังก์ชั่นให้สามารถใช้ port เดิมได้

hostIp = "127.0.0.1" #กำหนดค่า IP ที่เชื่อมต่อ
portNumber = 2728 #port ที่จะใช้ในการติดต่อ ต้องเหมือนกันกับ client
addr = (hostIp,portNumber) #รวม hostIP กับ portNumber เข้าเป็น tuple เดียวกัน
hostSocket.bind((addr)) #ผูก Object เพื่อเชื่อมต่อ
hostSocket.listen() #กำหนดจำนวน Client ของการเชื่อมต่อที่เราจะอนุญาตต่อครั้ง
print ("รอการเชื่อมต่อจาก Client...") #แสดงว่ารอการเชื่อมต่อจาก Client

clients = set() #ตัวแปรที่สามารถเพิ่มลบค่า เอาไว้เก็บผู้เชื่อมต่อ

def clientThread(clientSocket, clientAddress):
    while True:
        message = clientSocket.recv(1024).decode("utf-8") #รับข้อมูลที่ได้จากclientเป็น stringกำหนดเป็นหน่วยbytes
        print(clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message) #แสดงผลข้อความที่ได้รับจาก client
        for client in clients:
            if client is not clientSocket:
                client.send((clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message).encode("utf-8")) #ส่งกลับข้อมูล

        if not message: #เมื่อจบการเชื่อมต่อ
            clients.remove(clientSocket) #ตัดการเชื่อมต่อ
            print(clientAddress[0] + ":" + str(clientAddress[1]) +" has been disconnected") #แสดงผลว่าตัดการเชื่อมต่อ
            break

    clientSocket.close()

while True: 
    clientSocket, clientAddress = hostSocket.accept() #ยืนยันว่ามีการเชื่อมต่อกับ Server แล้วจะเก็บลงใน Address เป็นการเชื่อมต่อข้อมูลขาเข้า
    clients.add(clientSocket) #เพิ่ม(clientSocket)เข้ามาเชื่อมต่อภายในตัวแปรclients=set()
    print ("Connection from : ", clientAddress[0] + " : " + str(clientAddress[1])) #แสดงว่าเชื่อมต่อมาจาก hostIP : portNumber
    thread = Thread(target=clientThread, args=(clientSocket, clientAddress, )) #สร้างThreadมาเก็บในตัวแปรthreadในคอนสตรัคเตอร์นั้นเราสามารถส่งอาร์กิวเมนต์targetและargs
    thread.start() #เป็นการบอกให้ Thread เริ่มการทำงาน 