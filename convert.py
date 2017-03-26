from PyQt4.QtGui import*
from PyQt4.QtCore import*
import sys


class window(QMainWindow):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        
        self.resize(801, 600)
        self.setWindowIcon(QIcon('convert.png'))
        self.setWindowTitle('Convert')
        self.setStyleSheet("background-color:rgb(84, 84, 253)")
        
        self.button_open = QPushButton('Open',self)
        self.button_open.setGeometry(50, 20, 101, 23)
        self.button_open.clicked.connect(self.open)
        self.button=QPushButton('Convert',self)
        self.button.setGeometry(380,20,101,23)
        self.button.clicked.connect(self.convert)
        self.button=QPushButton('Quit',self)
        self.button.setGeometry(490,20,101,23)
        self.button.clicked.connect(self.closing)
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(280, 20, 69, 22))
        self.comboBox.addItems(sorted(['avi','mp4','flv','wmv','3gp','mov','mpeg','vob','mkv','dv','webm']))
        self.comboBox.setStyleSheet('font-family: "Book Antiqua", Palatino,"Palatino \
                                     Linotype", "Palatino LT STD", Georgia, serif;'
                                     'font-size: 14px;'
                                     'background-color:#400080;'
                                     'color:white;'
                                     'width:20' )
        
        self.label = QLabel('Choose format',self)
        self.label.setGeometry(QRect(175, 22, 81, 21))
        self.labelp=QLabel(self)
        photo=QPixmap('show.png')
        self.labelp.setPixmap(photo)
        self.labelp.setGeometry(380,200,500,400)
        self.frame_2 = QFrame(self)
        self.frame_2.setGeometry(QRect(50, 110, 690, 80))
        self.frame_2.setStyleSheet("background-color:rgb(56, 56, 170)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label=QLabel(self.frame_2)
        self.label.setText('Autor : Rashad Garayev')
        self.label.move(20,5)
        self.label1=QLabel(self.frame_2)
        self.label1.setText('Version : 0.1')
        self.label1.move(20,20)
        self.label2=QLabel(self.frame_2)
        self.label2.setText('used background ffmpeg')
        self.label2.move(20,35)
      	self.list=QListWidget(self)
      	self.list.setGeometry(50,200,300,300)
      	
        self.show()
    def closing(self):
    	self.close()
    def open(self):
    	try:
    		self.path=QFileDialog.getOpenFileName(self,'','','Files (*.mp4 *.wmv *.mpeg *.avi *.3gp *.mov *.mkv *.vob *.flv)' ,'All files (*.*)')
    		self.statusBar().showMessage('File directory : '+self.path)
    		self.list.addItem('File : %s'%str(self.path))
    	except:
            message=QMessageBox()
            message.setWindowTitle('QMessageBox')
            message=QMessageBox.critical(self,'Message','Please choose file',QMessageBox.Ok)
 			

    def convert(self):
    	try:

	    	import os
	    	if self.comboBox.currentText()=='3gp':
	    		os.system('nircmd.exe exec show ffmpeg -i "{}" -f 3gp -vcodec h263 -acodec amr_nb {}.3gp'.format(str(self.path),self.path))
	    		
	    	elif self.comboBox.currentText()=='mp4':
	    		os.system('nircmd.exe exec show ffmpeg -i "{}" -c:a aac -b:a 128k -c:v libx264 -crf 23 {}.mp4'.format(str(self.path),self.path))
	    		
        	elif self.comboBox.currentText()=='vob':
        		os.system('nircmd.exe exec show ffmpeg -i "{}" -target ntsc-dvd -preset ultrafast {}.vob'.format(str(self.path),self.path))
        		
        	elif self.comboBox.currentText()=='avi':
        		os.system('nircmd.exe exec show ffmpeg -i "{}" -acodec copy -vcodec copy {}.avi'.format(str(self.path),self.path))
        		
        	elif self.comboBox.currentText()=='flv':
        		os.system('nircmd.exe exec show ffmpeg -i "{}" -vcodec flv -b:v 512k -s 480x360 -r 30 -acodec libmp3lame -ar 44100 -f flv {}.flv'.format(str(self.path),self.path))
        		
        	elif self.comboBox.currentText()=='dv':
        		os.system('nircmd.exe exec show ffmpeg -i "{}" -s pal -r pal -aspect 4:3 -ar 48000 -ac 2 {}.dv'.format(str(self.path),self.path))
        		
       		elif self.comboBox.currentText()=='mkv':
       			os.system('nircmd.exe exec show ffmpeg -i "{}" -f matroska -vcodec libx264 -acodec libvorbis {}.mkv'.format(str(self.path),self.path))
       			
       		elif self.comboBox.currentText()=='mpeg':
       			os.system('nircmd.exe exec show ffmpeg -i "{}" -target ntsc-dvd {}.mpeg'.format(str(self.path),str(self.path)))	
       			
       		elif self.comboBox.currentText()=='mov':
       			os.system('nircmd.exe exec show ffmpeg -i "{}" -acodec libmp3lame -ab 192 {}.mov'.format(str(self.path),self.path))
       		elif self.comboBox.currentText()=='wmv':
       			os.system('nircmd.exe exec show ffmpeg -i "{}" -b:v 2M -vcodec msmpeg4 -acodec wmav2 {}.wmv'.format(str(self.path),str(self.path)))
       			
       		elif self.comboBox.currentText()=='webm':
       			os.system('nircmd.exe exec show ffmpeg -i "{}" -cpu-used 4 -threads 8 {}.webm'.format(str(self.path),str(self.path)))


       		else:
       			self.list.addItem('File does not support type')
       				
       		
        	
        	
        	
        except:
            message=QMessageBox()
            message.setWindowTitle('QMessageBox')
            message=QMessageBox.critical(self,'Message','Not file',QMessageBox.Ok)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = window()
    app.exec_()

