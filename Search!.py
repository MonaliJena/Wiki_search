import wikipedia
import pyttsx3 as p #as alias in python i.e duplicate name
print("hello... welcome to trust page :)")
user=str(input("so..what you want to search!!"))
result=wikipedia.summary(user,sentences=3)
a=str(input("do want to see the result \n press 1 for yes and 0 for no:-"))
if(a=='1'):
              print(result)
              b=str(input("do you want us to read it out \n press 1 for yes and 0 for no:-"))
              if(b=='1'):
                            p.speak(result)
              elif(b=='0'):
                            pass
              else:
                            print("Enter valid output!")
elif(a=='0'):
              print("Bye..")
else:
              print("Enter valid input!")

#DONE----Problem Solved :)
