import qrcode
# input 
inp = str(input("Enter The Text or URL to be converted into QR code: "))

# output file name 
output_name = str(input("Enter the name of the output file (without extension): "))

# qrcode generation
qr = qrcode.make(inp)

qr.save(output_name + ".png")

print("QR code generated and saved as " + output_name + ".png")