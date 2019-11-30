import os
import xlsxwriter as xl
import common_functions as cf

"""
   Function    : daib_excel_create 
   Parameters  : save_path - It contain the path(location) 
                             where the file(excel) will be save.
   Description : function is used creating the waring xlxs sheet
                 and filling it the data:
   ____________________________________________________________________
   |S No | File Path |File Name|Line Number |Warning Number | Warning |
   |_____|___________|_________|____________|_______________|_________|
   |     |           |         |            |               |         |
   |     |           |         |            |               |         |
   |_____|___________|_________|____________|_______________|_________|
"""
def daib_excel_create(save_path):
   row    = 1 
   column = 0
   path = save_path+'\\warning.xlsx'
   if cf.file_check(path) == True:
      os.remove(path)
   else:
      pass
   
   warning_book = xl.Workbook(save_path+'\\warning.xlsx')
   nav_cell_format_ = warning_book.add_format({'bold': True, 'bg_color': '#fca044', 'center_across': True,'text_wrap' : True})
   worksheet = warning_book.add_worksheet()  
   worksheet.write('A1', 'S No.', nav_cell_format_)
   worksheet.write('B1', 'File Path', nav_cell_format_)
   worksheet.write('C1', 'File Name', nav_cell_format_)
   worksheet.write('D1', 'Line Number', nav_cell_format_)
   worksheet.write('E1', 'Warning Number', nav_cell_format_)
   worksheet.write('F1', 'Warning ', nav_cell_format_)
   worksheet.autofilter('A1:F1')
   worksheet.set_column(1, 1, 80)
   worksheet.set_column(4, 4, 10)
   worksheet.set_column(5, 5, 50)
   
   cell_format_row = warning_book.add_format({'text_wrap' : True, 'align' : 'left'})

   for i in range(len(cf.file_path_list)):
      worksheet.write(row+i, column+1, cf.file_path_list[i], cell_format_row)
      worksheet.write(row+i, column+2, cf.file_name_list[i], cell_format_row)
      worksheet.write(row+i, column+3, cf.line_number_list[i])
      worksheet.write(row+i, column+4, cf.warning_number[i])
      worksheet.write(row+i, 0, i+1, cell_format_row)
      worksheet.write(row+i, column+5, cf.warning_list[i], cell_format_row)
   warning_book.close()

"""
   Function name : diab_list_update()
   Parameters    : save_path - It contain the path(location) 
                               where the file will be save.
   Description   : The function is reponsible for updating lists(software buffers)
                   mainly:
                   file_path_list   : Contains the list of the file path
                   warning_list     : Contains the warning
                   line_number_list : Contains the line numbers
                   col_number_list  : Contains the column numbers
                   This list filled the data extract from final.txt file, which removed
                   after data is extrated.
"""
def diab_list_update(save_path):
   path = str(save_path+'\\output.txt')
   warning_list = []
   file_path  = ""
   file_name  = ""
   line_no    = ""
   warning_no = ""
   warning    = ""

   with open(path, "r") as f1:
      for l in f1:
         warning_list.append(str(l))
   f1.close
   os.remove(path)

   for j in range(len(warning_list)):
      s = warning_list[j]
      s = s.replace("\"","")
      temp = s
      for i in range(len(s)):
         while temp[i] != ",":
            file_path += temp[i]
            i+=1
         while temp[i].isdigit() != True:
            i+=1
         while temp[i].isdigit() != False:
            line_no += temp[i]
            i+=1
         while temp[i] != "(":
            i+=1
         while temp[i] != " ":
            if temp[i] == ":":
               if temp[i+1] == " ":
                  break
               else:
                  warning_no += temp[i]
            else:
               warning_no += temp[i]
            i+=1
         while temp[i].isalpha() != True:
            i+=1
         while temp[i] != s[-1]:
            warning += temp[i]
            i+=1
         warning+=temp[i]
         temp_file_path = file_path
         k=-1
         while temp_file_path[k] != "/":
            file_name += temp_file_path[k]
            k-=1
         break
      
      warning_no = warning_no.replace("(","")
      warning_no = warning_no.replace(")","")
      warning_no = warning_no.replace("etoa","")
      warning_no = warning_no.replace(":","")
      cf.file_path_list.append(file_path)
      cf.file_name_list.append(file_name[::-1])
      cf.line_number_list.append(line_no)
      cf.warning_number.append(warning_no)
      cf.warning_list.append(warning)
      file_path  = ""
      file_name  = ""
      line_no    = ""
      warning_no = ""
      warning    = ""

   """
      Test for checking the lists are from here
   """
   # print(cf.file_name_list[1])
   # print(len(cf.file_path_list))
   # print(len(cf.file_name_list))
   # print(len(cf.line_number_list))
   # print(len(cf.warning_number))
   # print(len(cf.warning_list))


"""
   Test Code Form Here
"""

if __name__ == "__main__":
   file_path = "D:\\My_Work\\Warning_Isolator\\log_file\\HD_23REL.build.log"
   save_path = "D:\\My_Work\\Warning_Isolator\\Warning_isolator_V2.xx\\Output"
   cf.warning_creator(file_path, save_path)
   diab_list_update(save_path)
   daib_excel_create(save_path)