print ("File stated")

import random 
import string


def check_strenght(password):
   score =0
   if len(password) >= 8 :
      score += 1
   if any (c.isdigit () for c in password):
      score += 1
   if any (c.isupper() for c in password ):
      score += 1
   if any (c in string.punctuation for c in password ):
      score += 1
   
   if score <=1 :
      return "WEAK 😩️"
   elif score ==2 :
      return "MEDIUM 🙂‍↔️️"
   else :
      return "STRONG 💪️"
      
def gen_pas (length=12):
   all_chars = string.ascii_letters +string.digits +string.punctuation
   password ="".join(random.choice(all_chars) for _ in range(length))
   return password

def Password_report(password):
   report = {}
   report["length"] = len(password) >= 8
   report["has_digit"] = any(c.isdigit() for c in password)
   report["has_upper"] = any(c.isupper() for c in password)
   report["has_sympol"] = any(c in string.punctuation for c in password)
   return report
   #print a formatted password strength report
def print_report(report):
   checks_order = ["length","has_digit", "has_upper" , "has_symbol"]
   messeges = {"length": "Minimum length(8 characters)","has_digit": "contains a digit", "has_upper":"contains uppercase letter", "has_symbol":"contains symbol"}
   print ("\nPassword report")
   print ("-"*20)
   for key in checks_order:
      if report.get(key):  
         print(f"✅️ {messeges[key]}")
      else :
         print(f"❌️ {messeges[key]}")
   
   
def main () :
   print ("Welcome to Password tool 🔐️")
   while True : 
      print ("\n Choose an option :")
      print (" 1- Check password strength ")
      print ("2- Generate strong password ")
      print  ("3- EXIT")
      
      choice = input("Your choice :   ")
      if choice == "1" :
         pwd = input ("Enter your password ")
         result = check_strenght(pwd)     
         print (f"Password strength : {result}")
         rep_op = input("If you want password's report press * or press any key: ")
         if rep_op == "*" :
            test = Password_report(pwd)
            print (test)
            print_report(test)
      elif choice == "2" :
         length =input ("Password length (default 12): ")
         if length.isdigit():
            length = int (length)
         else :
            length =12 
         pwd = gen_pas (length)
         print (f"Generated Password : {pwd}")
      elif choice == "3"or choice == "exit":
         print ("BYE BYE ")
         break
      else :
         print ("INVALID CHOICE , Try again ")
if __name__ == "__main__":
  main()
   
