import re
import shutil


content = ''

def out_string():
  with open('potential-contacts.txt', 'r') as f:
    return f.read()
  
phone = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'

email = r'\S+@\S+'

os = out_string()

ph = re.findall(phone, os)

em = re.findall(email, os)

# print(phone numbers)
# print(email)

def duplicate_phone():
  new_list = []
  for i in ph: 
    if i not in new_list: 
      new_list.append(i)
      
  print(new_list)
  print(len(new_list))
      
  return new_list 
  
  

def duplicate_email():
  new_list = []
  for i in em: 
    if i not in new_list: 
      new_list.append(i)
  

  print(new_list)
  print(len(new_list))
  
  return new_list 
      
      
if __name__ == "__main__":
  
  duplicate_phone()
  duplicate_email()
  
  