#USING NORMAL WAY
#o_string = "hello"
#r_string = o_string[::-1]
#print(r_string)
#------------------------------------------------------------#
#USING FOR LOOP
o_string = "hello"
r_string = " "
for char in o_string:
    r_string = char + r_string
    print(r_string)