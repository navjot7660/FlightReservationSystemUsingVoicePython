import mysql.connector as mc
import random as rss
import cursor 
import speech_recognition as sr 
print(""" WELCOME TO AIRLINE RESERVATION
 \n""")
con=mc.connect(host="localhost",user="root",database="phone",passwd="system")
if con.is_connected():
      print("succefully\n")
cr=con.cursor()
r = sr.Recognizer()
print("""MENU
     1. REGISTER USER DETAIL
     2.BOOK TICKETS
     3.DISPLAY YOUR DETAILS
      \n  """)
with sr.Microphone() as s:
     r.adjust_for_ambient_noise(s,duration=1)
     print("Speak:  ")                                                                                   
     aab = r.listen(s,timeout=5)
     print( r.recognize_google(aab))
choice=(r.recognize_google(aab))
if (choice==1) or (choice=="register user details") or (choice=='register'):
     cr.execute("create table if not exists register(name varchar(20),Lname varchar(20),dob char(25),email varchar(50),password char(12),Rpassword char (12),gender char(10),rsno char(10));")
     cr.execute("create table if not exists booking(rsno char(100),desplace char(100),boadplace char(100),Ddate char(12),Bdate char(12),nopas char(20),Tcurr char(100));")
     print("PLEASE ENTER YOUR DETAILS FOR REGISTRATION")
     print("ENTER YOUR DETAILS IN CAPTAIL LETTER")
     print("ENTER YOUR NAME:")                                                                                  
     with sr.Microphone() as s:
          r.adjust_for_ambient_noise(s,duration=1)
          print("Speak:  ") 
          aab1 = r.listen(s,timeout=5)
          print(r.recognize_google(aab1))
     a=r.recognize_google(aab1)
     print("\nENTER YOUR LAST NAME:")
     with sr.Microphone() as s:
          r.adjust_for_ambient_noise(s,duration=1)
          print("Speak:  ") 
          aab2 = r.listen(s,timeout=5)
          print(r.recognize_google(aab2))
     b=r.recognize_google(aab2)
     print("\nENTER YOUR DATE OF BIRTH:")
     with sr.Microphone() as s:
          r.adjust_for_ambient_noise(s,duration=1)
          print("Speak:  ") 
          aab3 = r.listen(s,timeout=5)
          print(r.recognize_google(aab3))
     c=r.recognize_google(aab3)
     print("\nENTER YOUR EMAIL ID:")
     with sr.Microphone() as s:
          r.adjust_for_ambient_noise(s,duration=1)
          print("Speak:  ") 
          aab4 = r.listen(s,timeout=5)
          print(r.recognize_google(aab4))
     d=r.recognize_google(aab4)
     print("\nCREATE YOUR PASSWORD:")
     with sr.Microphone() as s:
          r.adjust_for_ambient_noise(s,duration=1)
          print("Speak:  ") 
          aab5 = r.listen(s,timeout=5)
          print(r.recognize_google(aab5))
     e=r.recognize_google(aab5)
     print("\nRE-ENTER YOUR PASSWORD:")
     with sr.Microphone() as s:
          r.adjust_for_ambient_noise(s,duration=1)
          print("Speak:  ") 
          aab6 = r.listen(s,timeout=5)
          print(r.recognize_google(aab6))
     f=r.recognize_google(aab6)
     if e==f:
          print("\nPASSWORD IS CORRECT")
     else:
          print("PASSWORD IS INCORRECT")
     print("ENTER YOUR GENDER:")
     with sr.Microphone() as s:
          r.adjust_for_ambient_noise(s,duration=1)                                                                                   
          aab7 = r.listen(s,timeout=5)
          print(r.recognize_google(aab7))
     g=r.recognize_google(aab6)
     h=rss.randint(1,10000)
     IN="insert into register(name,Lname,dob,email,password,Rpassword,gender,rsno) values('{}','{}','{}','{}','{}','{}','{}',{})".format(a,b,c,d,e,f,g,h);
     cr.execute(IN)
     cr.execute("select * from register;")
     mcc=cr.fetchall()
     for i in mcc:
        print(i)
     print("YOUR REGISTRATION NUMBER IS:  ",h)
     print("\nYOUR REGISTRATION IS SUCCESSFULL")
     print("\n YOU CAN PROCCED FOR BOOKING TICKET")
elif (choice==2) or (choice=="book") or (choice=="book tickets"):
       cr.execute("create table if not exists flights(flightno char(12),flightname varchar(15),fromd varchar(20),toa varchar(20),time char(12),date char(12),day char(12),price char(12));")
       cr.execute("insert into flights values('1001','GO AIR','AGRA','MUMBAI','12:30','12-10-2019','SUNDAY','$2000');")
       cr.execute("insert into flights values('1002','INDIGO','AGRA','BANGLORE','11:30','1-10-2019','MONDAY','$4000');")
       cr.execute("insert into flights values('1003','GO AIR','JAIPUR','MUMBAI','12:30','11-10-2019','WEDNESDAY','$2500');")
       cr.execute("insert into flights values('1004','AIR INDIA','CHENNAI','BANGLORE','1:30','12-9-2019','TUESDAY','$4000');")
       cr.execute("insert into flights values('1005','AIR INDIA','AGRA','CHENNAI','8:30','12-1-2020','THURSDAY','$9000');")
       cr.execute("insert into flights values('1006','GO AIR','AGRA','SULUR','2:30','12-2-2019','SUNDAY','$3500');")
       cr.execute("insert into flights values('1007','INDIGO','AGRA','MUMBAI','3:30','12-12-2019','SUNDAY','$1900');")
       cr.execute("insert into flights values('1008','GO AIR','AGRA','BANGLORE','18:30','26-2-2019','MONDAY','$2400');")
       cr.execute("insert into flights values('1009','INDIGO','JAIPUR','MUMBAI','22:30','18-3-2019','SUNDAY','$3333');")
       cr.execute("insert into flights values('1010','GO AIR','MUMBAI','BANGLORE','21:30','12-9-2019','WENESDAY','$1343');")
       cr.execute("insert into flights values('1011','AIR INDIA','AGRA','MUMBAI','19:30','19-2-2020','MONDAY','$1442');")
       print('''MENU
                1.SEE ALL FLIGHTS
                2.SEARCH FLIGHT''')
       print("\nENTER YOUR CHOICE:")
       with sr.Microphone() as s:
          r.adjust_for_ambient_noise(s,duration=1)
          print("Speak:  ") 
          aab7 = r.listen(s,timeout=5)
          print(r.recognize_google(aab7))
       a=r.recognize_google(aab7)
       if (a=="all flights") or (a=="see all fights") or (a==1) or("see all fight"):
           cr.execute('select * from flights')
           my=cr.fetchall()
           for i in my:
               print(i)
       elif (a==2) or (a=="search") or (a=="search flight"):
           print("\nFROM:")
           with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab8= r.listen(s,timeout=5)
                 print(r.recognize_google(aab8))
           f=r.recognize_google(aab8)
           print("\nTO:")
           with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab9= r.listen(s,timeout=5)
                 print(r.recognize_google(aab9))
           g=r.recognize_google(aab9)
           kl=(f,g)
           cr.execute("select * from flights where fromd=%s and toa=%s;",kl)
           my=cr.fetchall()
           for i in my:
               print(i)
            
           print("\nWANT TO BOOK TICKETS (y/n):")
           with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab10= r.listen(s,timeout=5)
                 print(r.recognize_google(aab10))
           g1=r.recognize_google(aab10)
           print("\nENTER FLIGHT NUMBER:")
           with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab11= r.listen(s,timeout=5)
                 print(r.recognize_google(aab11))
           g=r.recognize_google(aab11)
           print("\nENTER DATE OF TRAVELLING")
           with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab12= r.listen(s,timeout=5)
                 print(r.recognize_google(aab12))
           d=r.recognize_google(aab12)
           z=(g,d)
           cr.execute("select * from flights where flightno=%s and date=%s;",z)
           mk=cr.fetchall()
           for i in mk:
               print(i)
           qw=input('\nWANT TO BOOK(Y/N)')
       else:
           print('wrong choice')
           
       print("\nENTER YOUR BOOKING DETAILS FOR FLIGHT BOOKING")
       print("ENTER YOUR REGISTER NUMBER:")
       with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab13= r.listen(s,timeout=5)
                 print(r.recognize_google(aab13))
       x=r.recognize_google(aab13)
       print("\nENTER YOUR DESTINATION PLACE:")
       with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab14= r.listen(s,timeout=5)
                 print(r.recognize_google(aab14))
       i=r.recognize_google(aab14)
       print("\nENTER YOUR BOARDING PLACE:")
       with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab15= r.listen(s,timeout=5)
                 print(r.recognize_google(aab15))
       j=r.recognize_google(aab15)
       print("\nENTER DATE OF DEPARTURE:")
       with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab16= r.listen(s,timeout=5)
                 print(r.recognize_google(aab16))
       k=r.recognize_google(aab16)
       print("\nENTER RETURN DATE OF JOURNEY:")
       with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab17= r.listen(s,timeout=5)
                 print(r.recognize_google(aab17))
       l=r.recognize_google(aab17)
       
       print("\nENTER NO OF PASSENGER:")
       with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab18= r.listen(s,timeout=5)
                 print(r.recognize_google(aab18))
       m=int(r.recognize_google(aab18))
       print("\nENTER PAY IN CURRENCY:")
       with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab19= r.listen(s,timeout=5)
                 print(r.recognize_google(aab19))
       n=r.recognize_google(aab19)
       IN1="insert into booking(rsno,desplace,boadplace,Ddate,Bdate,nopas,Tcurr) values('{}','{}','{}','{}','{}','{}','{}')".format(x,i,j,k,l,m,n);
       cr.execute(IN1)
       cr.execute("select * from booking;")
       kkl=cr.fetchall()
       for i in kkl:
           print(i)
       print("\nDETAILS OF PASSENGERS")
       cr.execute("create table if not exists passenger(name varchar(20),age char(12),gender char(12),addhar char(20));")
       for i in range(1,m+1):
             print("\nPASSENGER",i)
             print("\nNAME")
             with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab20= r.listen(s,timeout=5)
                 print(r.recognize_google(aab20))
             abc=r.recognize_google(aab20)
             print("\nAGE")
             with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab20= r.listen(s,timeout=5)
                 print(r.recognize_google(aab20))
             bcd=r.recognize_google(aab20)

             print("\nGENGER")
             with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab21= r.listen(s,timeout=5)
                 print(r.recognize_google(aab21))
             cde=r.recognize_google(aab21)
             print("\nAADHAAR NUMBER")
             with sr.Microphone() as s:
                 r.adjust_for_ambient_noise(s,duration=1)
                 print("Speak:  ") 
                 aab22= r.listen(s,timeout=5)
                 print(r.recognize_google(aab22))
             add=r.recognize_google(aab22)
             
             cr.execute("insert into passenger(name,age,gender,addhar) values('{}','{}','{}','{}')".format(abc,bcd,cde,add))
       cr.execute("select * from passenger;")     
       mkk=cr.fetchall()
       for i in mkk:
            print(i)
            
       print("""
             YOUR BOOKING HAS BEEN CONFORMED
                                            """)
       
elif (choice==3) or (choice=="display")or (choice=="display your details"):
       print("your details are:")
       print("""
                REGISTERATIN DETAILS
                                   """)
       cr.execute("select * from register;")
       nmo=cr.fetchall()
       for i in nmo:
            print(i)
       print("""
              BOOKING DETAILS
                             """)
       cr.execute("select * from booking;")
       mnp=cr.fetchall()
       for i in mnp:
           print(i)
       print("""
                PASSENGERS DETAILS
                                  """)
       cr.execute("select * from passenger;")
       mpl=cr.fetchall()
       for i in mpl:
           print(i)
