import os

"""
Global Varaibles
"""
file_path_list       = []
warning_list         = []
warning_type_list    = []
line_number_list     = []
col_number_list      = []
line_col_number_list = []
warning_list_temp    = []
file_name_list       = []
warning_number       = []

file_not_found = "Fill Not Found"
file_found     = "File Found"

def banner(s, width=69):
       equals = '=' * width
       pad = (width + len(s)) // 2
       return '{0}\n{1:>{2}}\n{0}'.format(equals, s, pad)

def file_check(file_path):
   if os.path.exists(file_path):
      return True
   else:
      return False

def close_file(save_path):
   path = str(save_path+'\\warning.xlsx')
   os.close(path)
   pass

def open_excel_sheet(excel_sheet_path):
   path = excel_sheet_path +'\\warning.xlsx'
   os.system("start EXCEL.EXE "+path)

"""
   Clear all the software buffers
   NOTE: Don't call this function anywhere in this file.
"""

def clear_list():
   warning_list.clear()
   file_path_list.clear()
   col_number_list.clear()
   line_number_list.clear()
   warning_type_list.clear()
   warning_list_temp.clear()
   line_col_number_list.clear()
   file_name_list.clear()
   warning_number.clear()

"""
   Function      : warning_creator()
   Parameters    : file_path - It contain the path(location) 
                               of the log path
                   save_path - It contain the path(location) 
                               where the file will be save.
   Description   : The function take of collecting the warning from the log
                   to tempprary text file(output), which is removed later on.
"""
def warning_creator(file_path, save_path):
   path = str(save_path+'\\output.txt')
   words = [".mak", "pragma", "warnings","dld"]
   with open(file_path, "r") as f:
      with open(path, "w") as f1:
         for line in f:
            if "warning" in line:
               if any(x in line for x in words):
                  pass
               else:
                  f1.write(line)

"""
   Code from here is for testing the function
   
"""
def main():
   file_path = 'D:\\My_Work\\Warning_Isolator\\log_file\\HD_23REL.build.log'
   save_path = 'D:\\My_Work\\Warning_Isolator\\Warning_isolator_V2.xx\\Output'
   
   warning_creator(file_path, save_path)
   # list_update(save_path)
   # final_iso(save_path)
   
# if __name__ == '__main__':
#    main()