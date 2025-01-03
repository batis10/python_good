try:


    a = int(input("enter a number"))
    print(22 / a)
except ZeroDivisionError:
  print("cannot divide by zero")

except TypeError:
   print("please enter int or float")

except ValueError:
   print("you cant eneter string please enter a number")   

except:
   print("something went wrong")   

else:
   print("code run without any exception")  

finally:
   print("program execution completed no matter what")    
    
