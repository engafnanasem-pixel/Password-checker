"""password strenght checker
      Checks if the user password is strong based on :  
       -Length   - Uppercas e letter   -Lowercase letter    -number    -symbols
"""
def main() :
   #Get user password
   while True :
      user_pass= input ("Enter the password you want to check or (type exit to quit) :")
      if user_pass.lower() == "exit":
         print ("GOODBYE👋️")
         break
      else:
#check password length
         length = len(user_pass)
#check uppercase
         up_pass = any (char.isupper() for char in user_pass)
#check lowercase
         low_pass = any (char.islower() for char in user_pass)
#check number
         digi_pass = any (char.isdigit() for char in user_pass)
         symbols = "!@#$%^&*-_+="
#check symbol
         symbol_pass = any (char in symbols for char in user_pass)
  
   
         checks = {
        "At least 8 character 📏️": length >= 8,
        "Uppercase letter 🔠️": up_pass,
        "Lowercase letter 🔡️": low_pass,
        "Number🔢️": digi_pass,
        "symbols🔐️":symbol_pass }
#******password shorter than 8 *************

         failed = False
         for rule, passed in checks.items():
            if not passed:
              print(f"❌️{rule}")
              failed = True
         if not failed:
           print ("🤩️ Strong Password !Great job")
         else:
           print("🙂‍↔️️Nope , fix the above issues    ")
   
main()

