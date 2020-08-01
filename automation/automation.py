import re
import shutil

# f = open('potential-contacts.txt', 'r')
# message = f.read()
# print(message)

class PhoneInfo:
  def __init__(self):
    self.input = ''
    self.output = ''
    self.phone_numbers = []
    self.emails = []
    
  
  def open(self, file_path):
    with open(file_path, 'r') as file:
      self.input = file.read()
    return self.input

  def get_phone_numbers(self):
    self.phone_numbers = []
  
    pattern = r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}'
    phone_numbers = re.findall(pattern, self.input)
  
    for number in phone_numbers:
        formatted_number = [c for c in number if c.isnumber()]
        formatted_number.insert(3, '-')
        formatted_number.insert(7, '-')
        self.phone_numbers.append(''.join(formatted_number))
      
    return self.phone_numbers
    print(self.phone_numbers) 