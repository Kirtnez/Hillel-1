#_ => True
#__ => False
#___ => False
#x => True
#get_value => True
#get value => False
#get!value => False
#some_super_puper_value => True
#Get_value => False
#get_Value => False
#getValue => False
#3m => False
#m3 => True
#assert => False
#assert_exception => True
import keyword
import string

user = input("Type name: ")
nw = string.punctuation.replace ("_", "")
if user [0].isdigit() :
    print (False)
elif not user.lower() == user :
    print(False)
elif user in keyword.kwlist :
    print (False)
elif "__" in user :
    print (False)
elif " " in user :
    print (False)
elif user:
    for element in user :
        if element in string.punctuation :
            print (False)
            break
    else:
     print (True)
