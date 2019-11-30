import sys
import time
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.uic import loadUi
import warning_isolator_gui
import common_functions as cf
import hitech as ht
import diab as db

complier_list = ["Select an option",
                 "Hitech",
                 "Diab", 
                 "Tasking"]

class mainPage(QtWidgets.QMainWindow):
   def __init__(self):
      super(mainPage, self).__init__()
      loadUi('warning_isolator.ui', self)
 
      for i in complier_list:
         self.complierselect_comboBox.addItem(i)

      self.gen_pushButton.clicked.connect(self.generate)
      self.open_pushButton.clicked.connect(self.open_file)

   def open_file(self):
      path = self.get_save_path() + "\\warning.xlsx"
      if cf.file_check(path) == True:
         try:
            cf.open_excel_sheet(self.get_save_path())
         except IOError:
            self.update_status("Error:Please Close the excel sheet",1)
      else:
         self.update_status("Error: Excel File not Found",1)
         

   def update_status(self,s, chk_type,width=40):
      if chk_type == 1:
         self.update_textEdit.append(s)
      else:
         self.update_textEdit.append(cf.banner(s,width))

   def get_log_file_path(self):
      return self.log_textEdit.toPlainText()
      
   def get_save_path(self):
      return self.save_textEdit.toPlainText()

   def does_file_exist(self):
      if cf.file_check(self.get_log_file_path()) == True:
         return True
      else:
         return False
      
   def functional_check(self):
      if self.get_log_file_path() == "":
         self.update_status("Error: Please Enter the LOG Path",1)
         return False
      elif self.get_save_path() == "":
         self.update_status("Error: Please Enter the Save Location",1)
         return False
      elif self.complierselect_comboBox.currentText() == "Select an option":
         self.update_status("Select a Complier",1)
         return False
      else:
         return True

   def create_hitech_warning(self):
      start = time.time()
      cf.clear_list()
      self.initial_text("HiTech")
      cf.warning_creator(self.get_log_file_path(), self.get_save_path())
      self.update_status('''Copying: Done
                            Error  : None ''', 1)
      ht.hitech_list_update(self.get_save_path())
      self.update_status("Creating the Excel Sheet", 0)
      ht.hitech_excel_create(self.get_save_path())
      self.update_status('''Excel Sheet Created
                           Total Warning: '''+ str(len(cf.warning_list)), 1)
      end = time.time()
      time_taken = ("Time Taken: " + str(round((end - start), 2))+'s')
      self.update_status(time_taken, 1)
      self.update_status("Done",1)
      cf.clear_list()
      
   def create_diab_warning(self):
      start = time.time()
      cf.clear_list()
      self.initial_text("Diab")
      cf.warning_creator(self.get_log_file_path(), self.get_save_path())
      self.update_status('''Copying: Done
                            Error  : None ''', 1)
      db.diab_list_update(self.get_save_path())
      self.update_status("Creating the Excel Sheet", 0)
      db.daib_excel_create(self.get_save_path())
      self.update_status('''Excel Sheet Created
                           Total Warning: '''+ str(len(cf.warning_list)), 1)
      end = time.time()
      time_taken = ("Time Taken: " + str(round((end - start), 2))+'s')
      self.update_status(time_taken, 1)
      self.update_status("Done",1)
      cf.clear_list()
   
   def initial_text(self,option):
      self.update_status("Initiating Warning Process",0)
      self.update_status(option + " Complier Selected", 1)
      self.update_status("Copying form Log",0)

   def generate(self):
      option = self.complierselect_comboBox.currentText()
      self.update_textEdit.clear()
      if self.does_file_exist() == True:
         if self.functional_check() == True:
            if option == 'Hitech':
               try:
                  self.create_hitech_warning()
               except IOError:
                  self.update_status("Error:Please Close the excel sheet",1)
            elif option == 'Diab':
               try:
                  self.create_diab_warning()
               except IOError:
                  self.update_status("Error:Please Close the excel sheet",1)
            elif option == 'Tasking':
               """Add Code Here"""
               pass
            else:
               """DO NOTHING"""
               pass
         else: pass
      else:
         self.update_textEdit.setText("File Not Found")

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   main = mainPage()
   main.show()
   sys.exit(app.exec_())