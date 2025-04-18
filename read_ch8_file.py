file_name = "flightrunner.ch8"
with open(file_name,"rb") as file:
    data = file.read()

out_hex = ['{:02X}'.format(b) for b in data]


print("".join(out_hex))
