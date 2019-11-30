import os
import xlsxwriter as xl
import common_functions as cf

"""
   Function    : hitech_excel_create 
   Parameters  : save_path - It contain the path(location) 
                             where the file(excel) will be save.
   Description : function is used creating the waring xlxs sheet
                 and filling it the data:
   ____________________________________________________________________
   |S No | File Path |File Name|Line Number | Column Number | Warning |
   |_____|___________|_________|____________|_______________|_________|
   |     |           |         |            |               |         |
   |     |           |         |            |               |         |
   |_____|___________|_________|____________|_______________|_________|
"""
def hitech_excel_create(save_path):
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
   worksheet.write('E1', 'Column Number', nav_cell_format_)
   worksheet.write('F1', 'Warning', nav_cell_format_)
   worksheet.write('G1', 'Warning Type', nav_cell_format_)
   worksheet.autofilter('A1:F1')
   worksheet.set_column(1, 1, 80)
   worksheet.set_column(5, 5, 50)
   
   cell_format_row = warning_book.add_format({'text_wrap' : True, 'align' : 'left'})

   for i in range(len(cf.file_path_list)):
      worksheet.write(row+i, column+1, cf.file_path_list[i], cell_format_row)
      worksheet.write(row+i, column+2, cf.file_name_list[i], cell_format_row)
   for i in range(len(cf.col_number_list)):
      worksheet.write(row+i, column+3, cf.line_number_list[i])
      worksheet.write(row+i, column+4, cf.col_number_list[i])
   for i in range(len(cf.warning_list)):
      worksheet.write(row+i,0, i+1, cell_format_row)
      worksheet.write(row+i, column+5, cf.warning_list[i], cell_format_row)
      worksheet.write(row+i, column+6, cf.warning_type_list[i], cell_format_row)  
   warning_book.close()

"""
   Function name : list_update()
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
def hitech_list_update(save_path):
   path = str(save_path+'\\output.txt')
   word = ["warning"]
   file_path_list_temp = []
   digit = ""
   with open(path, "r") as f1:
      for l in f1:
         s1 = str(l)
         cf.warning_list_temp.append(s1[s1.index(word[0]) + len(word[0]):])
         file_path_list_temp.append(s1[:s1.index(word[0])])
   f1.close
   os.remove(path)

   # print(*file_path_list_temp, sep='\n')  """TEST CODE"""
   
   for count in  range(len(file_path_list_temp)):
      temp = file_path_list_temp[count]
      for i in range(len(temp)):
         if ':' == temp[i]:
            if temp[i+1].isdigit() == True:
               j=i+1
               while temp[j] != ':':
                  digit += temp[j]
                  j+=1
               cf.line_col_number_list.append(digit)
               j=0
               digit =""

   for i in range(len(cf.line_col_number_list)):
      if i%2 == 0:
         cf.line_number_list.append(cf.line_col_number_list[i])
      else:
         cf.col_number_list.append(cf.line_col_number_list[i])
   for count in range(len(file_path_list_temp)):
      temp_file_path = file_path_list_temp[count]
      temp_warning_path = cf.warning_list_temp[count]
      temp_file_path = temp_file_path.replace(':','')
      temp_file_path = temp_file_path[:1] + ':' + temp_file_path[1:]
      temp_digit = ""
      x = len(temp_file_path)-1
      while (temp_file_path[x].isalpha() != True):
         temp_digit += temp_file_path[x]
         x-=1
      temp_name = ""
      while (temp_file_path[x] != '/'):
         temp_name += temp_file_path[x]
         x-=1
         
      temp_file_path = temp_file_path.replace(temp_digit[::-1],'')
      cf.file_path_list.append(temp_file_path)
      cf.file_name_list.append(temp_name[::-1])
      
      temp_string = ""
      x = len(temp_warning_path)-1
      while(temp_warning_path[x] != "["):
         temp_string += temp_warning_path[x]
         x-=1
      cf.warning_type_list.append(('['+temp_string[::-1]))
      temp_warning_path = temp_warning_path.replace(('['+temp_string[::-1]),'')
      cf.warning_list.append(temp_warning_path.replace(":",''))
   
   """TEST CODE"""
   # print(*file_name_list, sep='\n')
   # print(len(file_name_list))
   # print(*warning_list, sep='\n')
   # print(*file_path_list, sep='\n')
   # print(*warning_type_list, sep='\n')
   # print(len(warning_list))
   # print(len(warning_type_list))
   # print(len(file_path_list))
   # print(len(file_path_list_temp))
   # print(len(warning_list_temp))
   # print(len(col_number_list))