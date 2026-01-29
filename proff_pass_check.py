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
      return "WEAK 😩️ \n Try adding symbols or numbers👀️"
   elif score ==2 :
      return "MEDIUM 🙂‍↔️️ \n GOOD but can be stronger🙃️"
   else :
      return "STRONG 💪️\n GREATE password 💪️"
      
def gen_pas (length=12):
   all_chars = string.ascii_letters +string.digits +string.punctuation
   password ="".join(random.choice(all_chars) for _ in range(length))
   return password

def Password_report(password):
   report = {}
   report["length"] = len(password) >= 8
   report["has_digit"] = any(c.isdigit() for c in password)
   report["has_upper"] = any(c.isupper() for c in password)
   report["has_symbol"] = any(c in string.punctuation for c in password)
   return report
   
def print_report(report):
   print ("\n Password report:")
   messages = {"length":"Minimum length (8 char)",
               "has_digit": "contains a digit" ,
               "has_upper": "contains uppercase letter",
               "has_symbol":"Contains symbol" }
   for key , text in messages.items():
      if report[key]:
         print (f"💯️{text}")
      else :
         print (f"❌️{text}")  
   
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
            report = Password_report(pwd)
            print_report(report)
      elif choice == "2" :
         length =input ("Password length (default 12): ")
         if length.isdigit():
            length = int (length)
         else :
            length =12 
         pwd = gen_pas (length)
         print (f"Generated Password : {pwd}")
      elif choice == "3" :
         print ("BYE BYE ")
         break
      else :
         print ("INVALID CHOICE , Try again ")
if __name__ == "__main__":
  main()
   
