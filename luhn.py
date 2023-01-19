class Luhn:

    def pass_luhn(self, acct):
        sum=0
        is_number=True
        for x in range(1, len(acct)+1):
            if(acct[-x]=="0" or acct[-x]=="1" or acct[-x]=="2" or acct[-x]=="3" or acct[-x]=="4" or acct[-x]=="5" or acct[-x]=="6" or acct[-x]=="7" or acct[-x]=="8" or acct[-x]=="9"):
                num=(int)(acct[-x])

                if (x%2==0):
                    num=num*2
                    if (num > 9):
                        str_num=str(num)
                        num=int(str_num[0])+int(str_num[1])
                
                #print(num)
                sum+=num
            else:
                is_number=False
        if is_number:   
            #print(sum)
            if sum % 10 == 0:
                #print("Is divisble by 10")
                return True
            else:
                #print('Is not divisble by 10')
                return False
        else:
            #print("Is not all numbers")
            return False
    
    def is_amex(self, acct):
        is_luhn=self.pass_luhn(acct)
        if is_luhn==False:
            return is_luhn
        else:
            length=len(acct)
            if (length == 15):
                first_Two=(int)(acct[0:2])
                if(first_Two==34 or first_Two==37):
                    return True
                else:
                    return False
            else:
                return False

    def is_visa(self, acct):
        is_Luhn=self.pass_luhn(acct)
        if is_Luhn==False:
            return is_Luhn
        else:
            length=len(acct)
            if (length == 13 or length == 16):
                return True
            else:
                return False

    def is_mastercard(self, acct):
        is_Luhn=self.pass_luhn(acct)
        if (is_Luhn==False):
            return is_Luhn
        else:
            length=len(acct)
            if (length == 16):
                first_Two=(int)(acct[0:2])
                if(first_Two>=51 and first_Two<=55):
                    return True
                else:
                    return False
            else:
                return False

    def is_discover(self, acct):
        is_luhn=self.pass_luhn(acct)
        if is_luhn==False:
            return is_luhn
        else:
            length=len(acct)
            if length == 16:
                first_four=(int)(acct[0:4])
                if(first_four==6011):
                    return True
                else:
                    return False
            else:
                return False

    def is_valid_cc(self, acct):
        is_visa=self.is_visa(acct)
        is_master=self.is_mastercard(acct)
        is_amex=self.is_amex(acct)
        is_discover=self.is_discover(acct)
        if is_visa or is_master or is_amex or is_discover:
            return True
        else:
            return False