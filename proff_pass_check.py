print ("File stated")

import random 
import string

# Function: Check individual password rules
def password_tips(password):
    score = 1
    tips = []
    if len(password) < 8:
        tips.append("Make it at least 8 characters")
    else :
        score +=1    
    if not any(char.isupper() for char in password):
        tips.append("Add at least one uppercase letter")
    else :
        score +=1   
    if not any(char.isdigit() for char in password):
        tips.append("Add at least one number")
    else :
        score +=1   
    if not any(char in "!@#$%^&*()" for char in password):
        tips.append("Add at least one special character (!@#$%^&*())")
    else :
        score +=1   
    return tips , score

def print_strength_bar(password):
    _ , score = password_tips(password)
    total = 5
    bar = '🟩️'* score + '⬜️' * (total-score)
    print (f"STRENGTH: [{bar}] {score*20}%")

# Function: Evaluate password strength
def check_strenght(password):
    tips , _ = password_tips(password)
    if tips:
        print("Your password is weak. Tips to improve:")
        for tip in tips:
            print("-", tip)
        return "Weak"
    else:
        print("Your password is strong!")
        return "Strong"

def gen_pas (length=12):
   all_chars = string.ascii_letters +string.digits +string.punctuation
   password ="".join(random.choice(all_chars) for _ in range(12))
   return password

def Password_report(password):
   report = {}
   report["length"] = len(password) >= 8
   report["has_digit"] = any(c.isdigit() for c in password)
   report["has_upper"] = any(c.isupper() for c in password)
   report["has_lower"] = any(c.islower() for c in password)
   report["has_symbol"] = any(c in string.punctuation for c in password)
   report["strength"] = check_strenght(password)
   return report
   #print a formatted password strength report
   
def print_report(report):
   checks_order = ["length","has_digit", "has_upper" , "has_symbol"]
   messeges = {"length": "Minimum length(8 characters)","has_digit": "contains a digit", "has_upper":"contains uppercase letter", "has_symbol":"contains symbol"}
   print ("\nPassword report🔐️")
   print ("-"*20)
   """for key in checks_order:
      if report.get(key):  
         print(f"✅️ {messeges[key]}")
      else :
         print(f"❌️ {messeges[key]}")"""
   print (f"Strength : {report['strength']}")
   print ("\n Details :")
   print (f"{'✅️ ' if report['length']>= 8 else '❌️'} length      : {len(report)} characters")
   print (f"{'✅️ ' if report['has_upper'] else '❌️'} Uppercase letter")
   print (f"{'✅️ ' if report['has_lower'] else '❌️'} Lowercase letter")
   print (f"{'✅️ ' if report['has_digit'] else '❌️'} Numbers")
   print (f"{'✅️ ' if report['has_symbol']else '❌️'} Special Symbols")

def get_suggest(report):
   suggestion =[]
   if not report.get("length"):
      suggestion.append("*Use at least 8 characters")
   if not report.get("has_digit"):
      suggestion.append("*Add at least one number")
   if not report.get("has_upper"):
      suggestion.append("*Add at least one UPPERCASE letter")
   if not report.get("has_symbol"):
      suggestion.append("*Add at least one symbol like @ # $ % & ")
   return suggestion
   
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
         strength = check_strenght(pwd) 
         '''if strength == "Weak":
           print("Suggested strong password:", gen_pas())  '''
         print_strength_bar(pwd)
         #print (f"Password strength : {strength}")
         rep_op = input("If you want password's report press * or press any key: ")
         if rep_op == "*" :
            report = Password_report(pwd)
            #print (test)
            print_report(report)
            
            if report.get("strength") != "STRONG" :
               suggestion= get_suggest (report)
               print ("\n Suggestion to improve your password :")
               for s in suggestion :
                  print (s)
                  
      elif choice == "2" :
         length =input ("Password length (default 12): ")
         if length.isdigit():
            length = int (length)
         else :
            length =12 
         pwd = gen_pas (length)
         print (f"Generated Password : {pwd}")
      elif choice == "3"or choice.lower() == "exit":
         print ("BYE BYE ")
         break
      else :
         print ("INVALID CHOICE , Try again ")
if __name__ == "__main__":
  main()
   
