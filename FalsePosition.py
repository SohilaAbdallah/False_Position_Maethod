import math

Xr_old = 0
Error = 100

Xl = float(input("Enter the Lower limit:"))
Xu = float(input("Enter the Upper limit:"))

while Error < 0.001:
    Xr_new = (Xl+Xu)/2

    F_Xl = math.pow((math.pow(Xl, 2)+1), 2)-25
    F_Xu =  math.pow((math.pow(Xu, 2)+1), 2)-25
    F_Xr =  math.pow((math.pow(Xr_new, 2)+1), 2)-25

    Xr_new = ((Xu*F_Xl) - (Xl*F_Xu)) / (F_Xl - F_Xu)

    r3 = F_Xl*F_Xr

    if r3==0:
        break
    if r3>0:
        Xl=Xr_new
    else:
        Xu=Xr_new
    
    if Xr_old != 0:
        Error = ((Xr_new - Xr_old)/Xr_new) *100

        if(Error < 0):
            Error = Error * -1
        else:
            Error = Error

    Xr_old = Xr_new

print("The Root = ",Xr_new,"The Error = ",Error)


