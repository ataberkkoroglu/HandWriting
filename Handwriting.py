from PyQt5.QtWidgets import QWidget,QMainWindow,QPushButton,QTextEdit,QLabel,QVBoxLayout,QHBoxLayout,QApplication,QLineEdit,QErrorMessage,QMessageBox
from PyQt5.QtGui import QIcon,QKeySequence,QPixmap,QFont
import pywhatkit as p
import sys,os

class HandWriting(QMainWindow):
  def __init__(self):
     super().__init__()
     self.program()
          
  
  def program(self):
    
    self.windows=QWidget()
    self.windows.setWindowTitle("HandWriting Applications")
    self.windows.setStyleSheet("background : black")
    self.windows.setWindowIcon(QIcon("handwriting.jpg"))

    self.text_field=QTextEdit(self)
    self.text_field.setStyleSheet("color : white")
    self.text_field.setFont(QFont('Arial',20,3))

    self.label=QLabel("Write or Paste Your Text : ")
    self.label.setStyleSheet("color : white")
    self.label.setFont(QFont('Arial',20,3))

    self.color_label=QLabel("Enter Values Of RGB With Integer[0-255] : ")
    self.color_label.setStyleSheet("color : white")
    self.color_label.setFont(QFont("Arial",20,3))

    self.color_R=QLineEdit()
    self.color_R.setStyleSheet("color : white")
    self.color_R.setFont(QFont("Arial",16,2))

    self.color_R_label=QLabel("Value of R : ")
    self.color_R_label.setStyleSheet("color : white")
    self.color_R_label.setFont(QFont("Arial",16,2))

    self.color_B=QLineEdit()
    self.color_B.setStyleSheet("color : white")
    self.color_B.setFont(QFont("Arial",16,2))

    self.color_B_label=QLabel("Value of B : ")
    self.color_B_label.setStyleSheet("color : white")
    self.color_B_label.setFont(QFont("Arial",16,2))

    self.color_G=QLineEdit()
    self.color_G.setStyleSheet("color : white")
    self.color_G.setFont(QFont("Arial",16,2))

    self.color_G_label=QLabel("Value Of G : ")
    self.color_G_label.setStyleSheet("color : white")
    self.color_G_label.setFont(QFont("Arial",16,2))

    self.transform=QPushButton("Transform")
    self.transform.setFont(QFont("Arial",14,2))
    self.transform.setStyleSheet("background : green")
    self.transform.setShortcut(QKeySequence('Ctrl+return'))
    self.transform.setMinimumWidth(300)

    self.delete=QPushButton("Delete")
    self.delete.setFont(QFont("Arial",14,2))
    self.delete.setStyleSheet("background : red")
    self.delete.setShortcut('Ctrl+Delete')
    self.delete.setMinimumWidth(300)

    v_box=QVBoxLayout()
    v_box.addWidget(self.label)
    v_box.addSpacing(10)
    v_box.addWidget(self.text_field)
    v_box.addSpacing(30)
    v_box.addWidget(self.color_label)

    h_box=QHBoxLayout()
    h_box.addWidget(self.color_R_label)
    h_box.addSpacing(30)

    h_box.addWidget(self.color_R)
    h_box.addSpacing(30)
    h_box.addWidget(self.color_B_label)
    h_box.addSpacing(30)
    h_box.addWidget(self.color_B)
    h_box.addSpacing(30)
    h_box.addWidget(self.color_G_label)
    h_box.addSpacing(30)
    h_box.addWidget(self.color_G)

    h_box2=QHBoxLayout()
    h_box2.addWidget(self.transform)
    h_box2.addSpacing(30)
    h_box2.addWidget(self.delete)
    
    v_box.addLayout(h_box)
    v_box.addSpacing(30)
    v_box.addLayout(h_box2)
    v_box.addSpacing(30)

    self.windows.setLayout(v_box)
    self.windows.show()
    self.transform.clicked.connect(self.process)
    self.delete.clicked.connect(self.process)
  
  def process(self):
    
    sender=self.sender()

    if sender.text()=="Delete":
      self.text_field.clear()
      self.color_B.clear()
      self.color_G.clear()
      self.color_R.clear()

    elif sender.text()=="Transform":
    
     if self.text_field.toPlainText()!="" and self.color_R.text()!="" and self.color_B.text()!="" and self.color_G.text()!="":

      try:  
       r=int(self.color_R.text())
       r=255 if r>255 else abs(r)

       b=int(self.color_B.text())
       b=255 if b>255 else abs(b)

       g=int(self.color_G.text())
       g=255 if g>255 else abs(g)
       
       p.text_to_handwriting(self.text_field.toPlainText(),save_to="Text.png",rgb=(r,g,b))
      
       self.windows=QWidget()
       self.windows.setWindowIcon(QIcon("handwriting.jpg"))
       self.windows.setStyleSheet("background: black;")

       self.img=QLabel()
       self.img.setPixmap(QPixmap(f"{os.getcwd()}/Text.png"))

       self.name=QLineEdit()
       self.name.setFont(QFont("Arial",16,3))
       self.name.setStyleSheet("color : white")

       self.name_label=QLabel("Filename With Directory : ")
       self.name_label.setStyleSheet("color : white")
       self.name_label.setFont(QFont("Arial",16,3))
     
       self.status=QLabel()
       self.transform=QPushButton("Save")
       self.transform.setStyleSheet("background : green")
       self.transform.setFont(QFont("Arial",20,3))

       self.delete=QPushButton("Delete")
       self.delete.setStyleSheet("background : red")
       self.delete.setFont(QFont("Arial",20,3))

       v_box=QVBoxLayout()
       v_box.addWidget(self.img)
       v_box.addSpacing(30)

       h_box=QHBoxLayout()
       h_box.addWidget(self.name_label)
       h_box.addSpacing(30)
       h_box.addWidget(self.name)
      
       h_box2=QHBoxLayout()
       h_box2.addWidget(self.transform)
       h_box2.addSpacing(30)
       h_box2.addWidget(self.delete)

       v_box.addLayout(h_box)
       v_box.addSpacing(30)
       v_box.addLayout(h_box2)
       v_box.addSpacing(30)
       v_box.addWidget(self.status)
       self.windows.setLayout(v_box)

       self.windows.setWindowTitle("HandWriting Applications")
       self.windows.show()

       self.transform.clicked.connect(self.process2)
       self.delete.clicked.connect(self.process2)

      except:
        self.error=QErrorMessage()
        self.error.setWindowIcon(QIcon(QPixmap("Error.jpg")))
        self.error.setWindowTitle("Error Message")
        self.error.setStyleSheet("color : red")
        self.error.setFont(QFont("Arial",20,6))                             
        self.error.showMessage("Text Couldn't Be Transform To HandWriting Successfully!!")
     else:
        self.error=QErrorMessage()
        self.error.setWindowIcon(QIcon(QPixmap("Error.jpg")))
        self.error.setWindowTitle("Error Message")
        self.error.setStyleSheet("color : red")
        self.error.setFont(QFont("Arial",20,6))                             
        self.error.showMessage("Text Field Mustn't Be Empty Please Write Something!!")
        
  
  def process2(self):
    
    sender=self.sender()

    if sender.text()=="Save":

      os.rename("Text.png",self.name.text())
      status=os.access(self.name.text(),mode=os.X_OK)
      
      self.status.setFont(QFont("Arial",20,3))

      if status==True:
         self.status.setStyleSheet("color : green")
         self.status.setText("This File Could Be Saved Successfully!!")

      else:
        self.status.setStyleSheet("color : red")
        self.status.setText("This File Couldn't Be Saved Successfully!!")
        
    
    else:
     if self.name.text()=="":
      os.remove(f"{os.getcwd()}\\Text.png")
      status=os.access(self.name.text(),os.X_OK)

      if status==True:
       self.message=QMessageBox(text="This File Couldn't Be Delete Successfully!!")
       self.message.setStyleSheet("color : red")
       self.message.setWindowIcon(QIcon(QPixmap("Error.jpg")))
       self.name.clear()
      
      else:
       self.message=QMessageBox(text="This File Could Be Delete Successfully!!")
       self.message.setStyleSheet("color : green")
       self.message.setWindowIcon(QIcon(QPixmap("message.jpg")))
       
      

     else:
      try:
       os.remove(self.name.text())
       status=os.access(self.name.text(),os.X_OK)

       if status==True:
        self.message=QMessageBox(text="This File Couldn't Be Delete Successfully!!")
        self.message.setStyleSheet("color : red")
        self.message.setWindowIcon(QIcon(QPixmap("Error.jpg")))
      
       else:
        self.message=QMessageBox(text="This File Could Be Delete Successfully!!")
        self.message.setStyleSheet("color : green")
        self.message.setWindowIcon(QIcon(QPixmap("message.jpg")))

       self.message.setWindowTitle("Message") 
       self.message.show()
       self.windows.close()
       self.program()

      except:
        self.error=QErrorMessage()
        self.error.setWindowIcon(QIcon(QPixmap("Error.jpg")))
        self.error.setWindowTitle("Error Message")
        self.error.setStyleSheet("color : red")
        self.error.setFont(QFont("Arial",20,6))                                
        self.error.showMessage(f"Not Found {self.name.text()}!")
        self.name.clear()
       
     
     
app=QApplication(sys.argv)
main=HandWriting()
sys.exit(app.exec())
    