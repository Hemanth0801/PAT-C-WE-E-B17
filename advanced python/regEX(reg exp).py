# A RegEx or Regular Expression is a sequence or character that forms a search pattern.
# Import the re module to start using regex expressions.


import re

# print(re.search('m','hemu'))

#validate pancard
# def valid_pan(pan_no):
#     pattern = r"^[A-Z]{5}[1-9]{4}[A-Z]{1}$"
#     if re.match(pattern, pan_no):
#         return True
#     else:
#         return False
# print(valid_pan("CIAPN6185R"))


#validate email
def val_email(email):
    pattern = r"^[a,z0-9_,]"