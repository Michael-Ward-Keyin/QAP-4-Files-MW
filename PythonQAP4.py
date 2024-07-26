# One Stop Insurance Company
# Michael Ward
# July 21st

# Define required libraries
import datetime
import FormatValues as FV
import time
import sys


# functions
def constants_file(file_path): # Opens the file and sets the constants 
    
    f = open(file_path, "r")
    for ConstantsFile in f:
        Constants = ConstantsFile.split(",")
        PolNum = Constants[0].strip()
        PolNum = int(PolNum)
        BasePrem = Constants[1].strip()
        BasePrem = float(BasePrem)
        AddCarDisc = Constants[2].strip()
        AddCarDisc = float(AddCarDisc)
        ExtLiab = Constants[3].strip()
        ExtLiab = float(ExtLiab)
        GlassCost = Constants[4].strip()
        GlassCost = float(GlassCost)
        LoanerCost = Constants[5].strip()
        LoanerCost = float(LoanerCost)
        HstRate = Constants[6].strip()
        HstRate = float(HstRate)
        ProcessFee = Constants[7].strip()
        ProcessFee = float (ProcessFee)   
    f.close()

    return PolNum, ExtLiab, GlassCost, LoanerCost, HstRate, ProcessFee, BasePrem, AddCarDisc

def calculate_extracost(NumCarIns, ExtLiab, ExtLiabVal, GlassCost, GlassCostVal, LoanerCost, LoanCarVal):

    ExtraCostTotal = (ExtLiab * ExtLiabVal + GlassCost * GlassCostVal + # Calculates the extra cost
                      LoanerCost * LoanCarVal) * NumCarIns

    return ExtraCostTotal

def calculate_premium(NumCarIns, BasePrem, AddCarDisc): # Calculates the premium cost
    PremiumCost = BasePrem + (NumCarIns - 1) * (BasePrem * (1 - AddCarDisc))

    return PremiumCost

def calculate_total_cost(HstRate, PremiumCost, ExtraCostTotal): #Calculates total and HST cost
    TotalPremium = ExtraCostTotal + PremiumCost
    HstCost = TotalPremium * HstRate
    TotalCost = HstCost + TotalPremium
    return HstCost, TotalCost

def calculate_monthly_total_downpay(ProcessFee, TotalCost, DownPayAmt): # Calculates a monthly total using a down payment
    MonthlyPay = (TotalCost + ProcessFee - DownPayAmt) / 8

    return MonthlyPay
def calculate_monthly_total(ProcessFee, TotalCost): # Calculates a monthly total with no down payment present
    MonthlyPay = (TotalCost + ProcessFee) / 8

    return MonthlyPay

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr

def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr

def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'): # Generates a progress bar
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    



# constants
CURDATE = datetime.datetime.now()



# Main program starts here
while True:
    
   
    EndInput = input("Enter END to end program or enter anything else to continue: ").upper()
    if EndInput == "END":
        break
    else:
        PolNum, ExtLiab, GlassCost, LoanerCost, HstRate, ProcessFee,  BasePrem, AddCarDisc = constants_file("const.dat")
        ExtLiabVal = 0
        GlassCostVal = 0
        LoanCarVal = 0
# User Inputs
        CusFirst = input("Enter customer first name: ").title()
        CusLast = input("Enter customer last name: ").title()
        StreetAdd = input("Enter customer street address: ")
        CusCity = input("Enter customer city: ").title()
        PostalCode = input("Enter customer postal code: ")
        CusPhoneNum = input("Enter customer phone number: ")

        ValidProv = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", ]
        while True:
            CusProv = input("Enter customer province in abbreviated form (example: NL): ").upper()
            if CusProv in ValidProv:
                break
            else:
                print("Province entry is invalid")

        NumCarIns = input("Enter number of cars insured: ")
        NumCarIns = int(NumCarIns)
        while True:
            ExtLiabInput = input("Extra liability? (Y for yes or N for no): ").upper()
            ExtLiabVal = 0
            if ExtLiabInput == "Y":
                ExtLiabVal += 1
                ExtLiabPrint = "Yes"
                break
            else:
                ExtLiabPrint = "No"
                break

        while True:
            GlassCov = input("Extra Glass Coverage? (Y for yes or N for no): ").upper()
            GlassCostVal = 0
            if GlassCov == "Y":
                GlassCostVal += 1
                GlassCovPrint = "Yes"
                break
            else:
                GlassCovPrint = "No"
                break
        while True:
            LoanCar = input("Does customer need loaner?(Y for yes or N for no): ").upper()
            LoanCarVal = 0
            if LoanCar == "Y":
                LoanCarVal += 1
                LoanCarPrint = "Yes"
                break
            else:
                LoanCarPrint = "No"
                break
        

        ValidPay = ["F", "M", "D",]
        while True:
            PayMethod = input("For payment option enter (F for Full, M for Monthly, or D for Down-pay): ").upper()
            if PayMethod in ValidPay:
                break
            else:
                print("Payment option invalid")
        DownPayAmt = 0
        if PayMethod == "D":
            PayMethodPrint = "Down-pay"
            DownPayAmt = input("Enter downpayment amount: ")
            DownPayAmt = float(DownPayAmt)
        if PayMethod == "F":
            PayMethodPrint = "Full"
        if PayMethod == "M":
            PayMethodPrint = "Monthly"
        

        AllClaims = []

        while True:
            ClaimNum = input("Enter claim number (Type END to Finish): ")
            if ClaimNum.upper() == "END":
                break
            ClaimAmt = input("Enter customer claim amount: ")
            ClaimAmt = float(ClaimAmt)
            ClaimAmtStr =FDollar2(ClaimAmt)
            while True:
               
                try:
                    ClaimDate = input("Enter claim date (YYYY-MM-DD): ")
                    ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
                    ClaimDateStr = FDateS(ClaimDate)
                except:
                    print("invalid claim date.")
                else:
                    break
            AllClaims.append(ClaimNum)
            AllClaims.append(ClaimDateStr)
            AllClaims.append(ClaimAmtStr)


# Calculations      
        ExtraCostTotal = calculate_extracost(NumCarIns, ExtLiab, ExtLiabVal, GlassCost, GlassCostVal, LoanerCost, LoanCarVal) # Brings in the functions to calculate the costs

        PremiumCost = calculate_premium(NumCarIns, BasePrem, AddCarDisc)

        HstCost, TotalCost = calculate_total_cost(HstRate, PremiumCost, ExtraCostTotal)

        while True: # Determines if the payment method is monthly or down payment and uses the appropriate function
            if PayMethod == "D":    
                MonthlyPay = calculate_monthly_total_downpay(ProcessFee, TotalCost, DownPayAmt)
                break
            elif PayMethod == "M":
                MonthlyPay = calculate_monthly_total(ProcessFee, TotalCost)
                break
            else:
                break

        if CURDATE.month == 12:
            NextMonth = 1
            NextYear = CURDATE.year + 1
            
        else:
            NextMonth = CURDATE.month + 1
            NextYear = CURDATE.year 
            
        
        FirstPayDate = datetime.datetime(year=NextYear,month=NextMonth,day=1)
        FirstPayDateStr = FDateS(FirstPayDate)
        CurrentDateStr = FDateS(CURDATE)
        

        
        
        
        
        
        print()
        print(" ---------------------------------")
        print(f"One Stop Insurance Company Policy Receipt")
        print(" ---------------------------------")
        print()
        print(f"Policy Number: {PolNum}")
        print(f"Customer: {CusFirst} {CusLast}")
        print(f"Street Address: {StreetAdd}")
        print(f"City:  {CusCity}")
        print(f"Province: {CusProv}")
        print(f"Postal Code: {PostalCode}")
        print(f"Phone: {CusPhoneNum}")
        print(f"Number of cars: {NumCarIns}")
        print(f"Extra liability coverage: {ExtLiabPrint}")
        print(f"Glass coverage: {GlassCovPrint}")
        print(f"Loaner car coverage: {LoanCarPrint}")
        print(f"Payment method: {PayMethodPrint}")
        while True:
            if PayMethod == "D":
                DownPayAmtStr=FDollar2(DownPayAmt)
                print(f"Down payment: {DownPayAmtStr}")
                break
            else:
                print("Down payment: N/A")
                break
        print(" ---------------------------------")
        print(f"Premium breakdown:")
        print(" ---------------------------------")
        ExtraCostTotalStr =FDollar2(ExtraCostTotal)
        print(f"Total extra costs: {ExtraCostTotalStr}")
        PremiumCostStr=FDollar2(PremiumCost)
        print(f"Total premium (before tax): {PremiumCostStr}")
        HstCostStr=FDollar2(HstCost)
        print(f"HST (15%): {HstCostStr}")
        TotalCostStr=FDollar2(TotalCost)
        print(f"Total cost (after tax): {TotalCostStr}")
        if PayMethod == "M" or PayMethod == "D":
            MonthlyPayStr=FDollar2(MonthlyPay)
            print(f"Monthly payment: {MonthlyPayStr}")
        
        print(f"Invoice date: {CurrentDateStr:<10s}")
        print(f"First pay date: {FirstPayDateStr:<10s}")
        print(" ---------------------------------")
        print("Previous Claims:")
        print()
        print("Claim #   Claim Date   Amount")
        print(" ---------------------------------")

        MaxLength = (len(AllClaims) + 2) // 3  # Sets up every third piece of the list to print for each associated piece of the claim 
        for i in range(MaxLength):
            ClaimNumPrint = AllClaims[i*3] if i * 3 < len(AllClaims) else ""
            ClaimDatePrint = AllClaims[i*3 + 1] if i * 3 + 1 < len(AllClaims) else ""
            ClaimAmtPrint = AllClaims[i*3 + 2] if i * 3 + 2 < len(AllClaims) else ""

            print(f"{ClaimNumPrint:<10s}{ClaimDatePrint:<10s}   {ClaimAmtPrint:10s}")
        
        print()
 
        TotalIterations = 30
        Message = "Saving Policy Data"
    
        for i in range(TotalIterations + 1):
             
            ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
            time.sleep(0.1)

        print()
        print("Policy information has been successfully saved to policy.dat ...") 
        print()
        print()
        Policy = open("policy.dat", "a") # Opens and prints to the policy file to save customer info
        Policy.write(f"{PolNum},")
        Policy.write(f"{CusFirst},")
        Policy.write(f"{CusLast},")
        Policy.write(f"{StreetAdd},")
        Policy.write(f"{CusCity},")
        Policy.write(f"{CusProv},")
        Policy.write(f"{PostalCode},")
        Policy.write(f"{CusPhoneNum},")
        Policy.write(f"{NumCarIns},")
        Policy.write(f"{ExtLiabPrint},")
        Policy.write(f"{GlassCovPrint},")
        Policy.write(f"{LoanCarPrint},")
        Policy.write(f"{PayMethodPrint},")
        Policy.write("\n")
        Policy.close()

        PolNum += 1

        f= open("const.dat", "w") # Opens the constants file to increase the policy number for the next entry
        f.write(f"{PolNum},")
        f.write(f"{BasePrem},")
        f.write(f"{AddCarDisc},")
        f.write(f"{ExtLiab},")
        f.write(f"{GlassCost},")
        f.write(f"{LoanerCost},")
        f.write(f"{HstRate},")
        f.write(f"{ProcessFee},")
        f.close()
    
        print()


            




                
        


           

        
        
        



  


        

