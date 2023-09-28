import binascii

def hex_code_convert(value):
    hex_string = ''
    if isinstance(value, int):
        hex_string = hex(value)[2:]
        print(f"The hex code of {value} is: {hex_string}")
    elif isinstance(value, str):
        byte_data = value.encode('utf-8')
        hex_string = binascii.hexlify(byte_data).decode('utf-8')
        print(f"The hex code of '{value}' is: {hex_string}")
    return hex_string  # Return both hex_string 

def len_str(hex_string):
    length = len(hex_string)  # Calculate the length of hex_string
    return length

####

# Data for different entries
Seller_name = 'ABC Electronics'
Seller_VAT_name = 'VAT123456789'
Date_and_Time = '2023-09-15 10:30 AM'
Invoice_Total = 500  # Assuming the invoice total is $500
VAT_Total = 75  # Assuming the VAT total is $75

# Calculate hex codes and lengths for each entry
sn_hex = hex_code_convert(Seller_name)
sn_len = len_str(sn_hex)  # Pass sn_hex, which is a string

svn_hex = hex_code_convert(Seller_VAT_name)
svn_len = len_str(svn_hex)  # Pass svn_hex, which is a string

dat_hex = hex_code_convert(Date_and_Time)
dat_len = len_str(dat_hex)  # Pass dat_hex, which is a string

it_hex = hex_code_convert(Invoice_Total)
it_len = len_str(str(Invoice_Total))  # Typecast to str and calculate length

vt_hex = hex_code_convert((VAT_Total))
vt_len = len_str(str(VAT_Total))  # Typecast to str and calculate length

# Modify TLV strings to add original length divided by 2
tlv_sn = '01' + f"{sn_len // 2:02}" + sn_hex
tlv_svn = '02' + f"{svn_len // 2:02}" + svn_hex
tlv_dat = '03' + f"{dat_len // 2:02}" + dat_hex
tlv_it = '04' + f"{it_len // 2:02}" + it_hex
tlv_vt = '05' + f"{vt_len // 2:02}" + vt_hex
tlv_total = tlv_sn + tlv_svn + tlv_dat + tlv_it + tlv_vt
print(tlv_total)
###################################################
###################################################
###################################################
import base64
# Input string
input_string = "011541424320456c656374726f6e69637302125641543132333435363738390319323032332d30392d31352031303a333020414d04011f405014b"
# Convert the string to bytes
input_bytes = input_string.encode('utf-8')
# Encode the bytes in Base64
base64_string = base64.b64encode(input_bytes).decode('utf-8')
print("Base64 String:", base64_string)

import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1, box_size=10, error_correction = qrcode.constants.ERROR_CORRECT_H, border= 4,)
# qr.add_data(input("Enter the data to be Encoded: "))
qr.add_data(base64_string)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color= 'White')
img.save("code.png")







'''
# Print TLV strings and original lengths of hex codes
print("\nThe Seller Name info:")
print(Seller_name)
print(f'The TLV string for Seller name is: {tlv_sn}')
print(f'The original length of Seller name hex code is: {sn_len}')

print("\nThe Seller Vat Name info:")
print(Seller_VAT_name)
print(f'The TLV string for Seller VAT name is: {tlv_svn}')
print(f'The original length of Seller VAT name hex code is: {svn_len}')

print("\nThe Date and Time info:")
print(Date_and_Time)
print(f'The TLV string for Date and Time is: {tlv_dat}')
print(f'The original length of Date and Time hex code is: {dat_len}')

print("\nThe Invoice Info info:")
print(Invoice_Total)
print(f'The TLV string for Invoice Total is: {tlv_it}')
print(f'The original length of Invoice Total hex code is: {it_len}')

print("\nThe VAT Total info:")
print(VAT_Total)
print(f'The TLV string for VAT Total is: {tlv_vt}')
print(f'The original length of VAT Total hex code is: {vt_len}')
'''