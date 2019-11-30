# s1 = "C:\\Work_18\\Allison_Gen6\\WA_NextGen_MCAL\\main\\Appl\\Test/MCAMOS\\mcamos_can.c18413"
# x = len(s1)-1
# temp =""
# while (s1[x] != "["):
#    temp += s1[x]
#    # print(s1[x])
#    x-=1
# print('['+temp[::-1])
# print(s1[:x].replace(':',''))
# s = s.replace(temp[::-1],'')
# print(s)

s = "\"C:/Projects/HD_23REL/Main/HAL/DeviceDrivers/ProjectCompiler/reuse.h\", line 772: warning (etoa:5387): explicit conversion of a 64-bit integral type to a smaller integral type (potential portability problem)"
print(s)
file_path = ""
file_name = ""
line_no   = ""
warning_no = ""
warning = ""

temp = s
for i in range(len(s)):
   while temp[i] != " ":
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
   break
   
print(file_path)
print(line_no)
print(warning_no)
print(warning)