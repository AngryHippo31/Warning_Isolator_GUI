s = "C:/Work_18/Allison_Gen6/WA_NextGen_MCAL/main/Appl/HAL/HWIO/QSPI_MCAL_SPI_Port/10.DeviceDriver/TC3xx/dd_qspi_spi_port.c:329:28: warning: unused parameter 'in_interface' [-Wunused-parameter]"
print(s)
file_path  = ""
file_name  = ""
line_no    = ""
col_no = ""
warning    = ""

temp = s

for i in range(len(s)):
   while temp[i] != '.':
      file_path += temp[i]
      i+=1
   if (temp[i+1]=="c") or (temp[i+1]=="h"):
      i+=1
      file_path += temp[i]
   else:
      i+=1
      while temp[i] != ':':
         file_path += temp[i]
         i+=1

   i+=1
   while temp[i].isdigit() != False:
      line_no += temp[i]
      i+=1
   
   i+=1
   while temp[i].isdigit() != False:
      col_no += temp[i]
      i+=1
   
   while temp[i] != " ":
      i+=1

   while temp[i] != s[-1]:
      warning += temp[i]
      i+=1

   warning += temp[i]

   break

print(file_path)
print(line_no)
print(col_no)
print(warning)