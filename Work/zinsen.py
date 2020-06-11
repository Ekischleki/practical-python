ischulden = float(input("wie viele schulden hast du bei yaraak? " ))
tag = 0
schulden = 0
zinssatz =  float(input("zinssatz bidde "))
laufzeit = float(input("wie lange ist die Laufzeit? "))
zurückgezahlt =float(input("wie fiel hast du zurückgezahlt"))
while tag < laufzeit:
    tag = tag +1
    schulden = ischulden / 100 * zinssatz - zurückgezahlt 
    ischulden = schulden + ischulden 

    print("die schulden von tag: " ,tag, " betragen:" ,ischulden )



