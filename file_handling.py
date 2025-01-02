file = None
try:



 file = open("hello.txt", "r")
 print(file.read())

except FileNotFoundError as e:
 print("file not found",e)




except:
 print("something went wrong!!!!")

finally:
 if file:
  file.close()