import mysql.connector as mq
from datetime import datetime
MQL=mq.connect(host='localhost',user='root',password='a3glolop',database='MyHotel')
mcursor=MQL.cursor()




#.............................................................................................................................................
def RoomMenu():
	while True:
		print("...........................................................")
		print ("PRESS 1 TO ADD INFORMATION INTO ROOM TABLE          :-   .")
		print ("PRESS 2 TO MODIFY THE INFORMATION INTO ROOM         :-   .")
		print ("PRESS 3 TO DELETE THE INFORMATION INTO ROOM TABLE   :-   .")
		print ("PRESS 4 TO RETURN INTO MAIN MENU                    :-   .")
		print("...........................................................")
		Var=int(input("ENTER YOUR CHOCIE :- "))
		
#.............................................................................................................................................
		if Var==1:
			print("............................................................")
			roomNo=int(input(       "ENTER ROOM NUMBER       .                "))
			roomType=input  (       "ENTER ROOM TYPE         .                " )
			RoomFac=input   (       "ENTER ROOM FACILITIES   .                " )
			RoomCost=float  ( input("ENTER ROOOM COST        .                "))
			avail=int       (input("ENTER AVAIBILITY(y/1,n/0).                "))
		
			print(".........................................................................................................................")
			mcursor.execute(f"insert into Room values({roomNo},'{roomType}','{RoomFac}',{RoomCost},{avail})")
			MQL.commit()

#.............................................................................................................................................
		elif Var==2:
			print("............................................................")
			print ("PRESS 1 TO UPDATE ROOM NUMBER          :-   .")
			print ("PRESS 2 TO UPDATE ROOM TYPE            :-   .")
			print ("PRESS 3 TO UPDATE ROOM FACILITIES      :-   .")
			print ("PRESS 4 TO  UPDATE ROOM COST           :-   .")
			print ("PRESS 5 TO UPDATE ROOM Avaibility      :-   .")
			print("...........................................................")
			UPDATE=int(input("ENTER YOUR CHOICE :- "))

			if UPDATE==1:
				rono=int(input("ENTER OLD ROOM NUMBER :- "))
				ronew=int(input("ENTER NEW ROOM NUMBER:- "))
				mcursor.execute(f"UPDATE Room set roomNo={ronew} where roomNo={rono}")
				MQL.commit()

			if UPDATE==2:
				roty=(input("ENTER OLD ROOM TYPE :- "))
				rotew=(input("ENTER NEW ROOM TYPE:- "))
				mcursor.execute(f"UPDATE Room set roomType={rotew} where roomType={roty}")
				MQL.commit()

			elif UPDATE==3:
				rofc=(input("ENTER OLD ROOM FACILITES :- "))
				rfnew=(input("ENTER NEW ROOM FACILITES:- "))
				mcursor.execute(f"UPDATE Room set RoomFac={rfnew} where RoomFac={rofc}")
				MQL.commit()

			elif UPDATE==4:
				roco=int(input("ENTER OLD ROOM COST :- "))
				rcnew=int(input("ENTER NEW ROOM NEW:- "))
				mcursor.execute(f"UPDATE Room set roomNo={rcnew} where roomNo={roco}")
				MQL.commit()
			elif UPDATE==5:
				roco=int(input("ENTER OLD Avaibility :- "))
				rcnew=int(input("ENTER NEW Avaibility:- "))
				mcursor.execute(f"UPDATE Room set Avaibility={rcnew} where roomNo={roco}")
				MQL.commit()
#.............................................................................................................................................
		elif Var==3:
				ron=int(input("ENTER ROOM NUMBER TO DELETE THE COLUMN :- "))
				mcursor.execute(f"DELETE from Room  where roomNo={ron}")
				MQL.commit()
    

#.............................................................................................................................................
		elif Var==4:
			break


#.............................................................................................................................................
#.............................................................................................................................................
#...............................................................END OF ROOM TABEL.............................................................
#.............................................................................................................................................




		else:
			print("WRONG CHOICE ")
#.............................................................................................................................................			
def CustMenu():
	while True:
		print("...............................................................")
		print ("PRESS 1 TO ADD INFORMATION INTO CUSTOMER TABLE          :-   .")
		print ("PRESS 2 TO MODIFY THE INFORMATION INTO CUSTOMER         :-   .")
		print ("PRESS 3 TO DELETE THE INFORMATION INTO CUSTOMER TABLE   :-   .")
		print ("PRESS 4 TO RETURN INTO MAIN MENU                        :-   .")
		print("...............................................................")
		VAr=int(input("ENTER YOUR CHOCIE :- "))
#.............................................................................................................................................
		if VAr==1:
			print("............................................................")
			roomno=input(     "ENTER ROOM NUMBER                     .                    ")
			Cname=input (     "ENTER YOUR FULL NAME                  .                    ")
			noCost=input(     "ENTER NUMBER OF CUSTOMER IN ROOM      .                   " )
			adharNo=int(input("ENTER ADHAR NUMBER FOR ID PROOF       .                   "))
			print("..........................................................................")
			mcursor.execute(f"insert into customer values({roomno},'{Cname}',{noCost},{adharNo})")
			MQL.commit()
			
#.............................................................................................................................................

		elif VAr==2:
			print("............................................................")
			print ("PRESS 1 TO UPDATE NUMBER OF CUSTOMER                 :-   .")
			print ("PRESS 2 TO UPDATE ROOM NUMBER                        :-   .")
			print ("PRESS 3 TO UPDATE ADHAR NUMBER                       :-   .")
			print ("PRESS 4 TO UPDATE CHECK-INT DATE                     :-   .")
			print ("PRESS 5 TO UPDATE CHECK-OUT DATE                     :-   .")
			print ("PRESS 6 TO UPDATE CUSTOMER NAME 					 :-	  .") 
			print("............................................................")
			update=int(input("ENTER YOUR CHOICE :- "))

			if update==1:
				CCL=int(input("ENTER OLD NUMBER CUSTOMER NUMBER :- "))
				CCN=int(input("ENTER NEW NUMBER CUSTOMER NUMBER:- "))
				mcursor.execute(f"UPDATE customer set noCost={CCN} where noCost={CCL}")
				MQL.commit()

			if update==2:
				RNUML=(input("ENTER OLD ROOM NUMBER :- "))
				RNUMN=(input("ENTER NEW ROOM NUMBER :- "))
				mcursor.execute(f"UPDATE customer set roomno={RNUMN} where roomno={RNUML}")
				MQL.commit()

			elif update==3:
				ro=int(input ("ENTER OLD ADHAR NUMBER :- "))
				rn=int(input("ENTER NEW ADHAR NUMBER :-  "))
				mcursor.execute(f"UPDATE customer set adharNO={rn} where adharNo={ro}")
				MQL.commit()

			elif update==4:
				od=int(input("ENTER OLD CHECK-IN DATE    :- "))
				ND=int(input("ENTER NEW CHECK-IN DATE    :- "))
				mcursor.execute(f"UPDATE Room set roomNo={ND} where roomNo={od}")
				MQL.commit()

			elif update==5:
				do=int(input("ENTER OLD CHECK-OUT DATE    :- "))
				dn=int(input("ENTER NEW CHECK-OUT DATE    :- "))
				mcursor.execute(f"UPDATE Room set roomNo={dn} where roomNo={do}")
				MQL.commit()

			elif update==6:
				co=int(input("ENTER OLD CUSTOMER NAME    :- "))
				cn=int(input("ENTER NEW CUSTOMER NAME    :- "))
				mcursor.execute(f"UPDATE Room set roomNo={cn} where roomNo={co}")
				MQL.commit()
			
			else:
				print ("WRONG CHOICE PLEASE TRY AGINA")
#.............................................................................................................................................
		elif VAr==3:
			ron1=int(input("ENTER ROOM NUMBER TO DELETE THE COLUMN :- "))
			mcursor.execute(f"DELETE from customer  where roomNo={ron1}")
			MQL.commit()

#.............................................................................................................................................
		elif VAr==4:
			break
#.............................................................................................................................................
def Bill():
	pass
    	


#.............................................................................................................................................
while True:
	print (".............................................")
	print ("PRESS 1 TO ENTER INTO ROOM          .       .")
	print ("PRESS 2 TO ENTER INTO CUSTOMER      .       .")
	print ("PRESS 3 FOR BILL                    .       .")
	print ("PRESS 4 TO EXIT                     .       .")
	print (".............................................")
	          
	VAR=int(input("ENTER YOUR CHOCIE PLEASE :- "))
	
	if VAR==1:
		RoomMenu()	
			
	elif VAR==2:
		CustMenu()
		
	elif VAR==3:
		Bill()
		
	elif VAR==4:
		exit()
#............................................................................END.............................................................
	
			




		
		
