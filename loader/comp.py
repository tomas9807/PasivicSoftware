import re 
import traceback
 # quick comparisons







    #RETURNS ARE 0 FOR OK,1 FOR ERROR
    #Everything should be returned in a tuple like this (value,error) #example (pedro,2)

        
          #contains the positions where the id,name,etc reside in the sheet  #if there were any errors then it will display a GUI to select the rows by hand
def is_name(var):
    try:            
        if len(str(var))<2: return (None,False)

        pattern_wrong = re.compile(r'([^A-Za-z\.,Ññ ]+)')
    
        match_wrong = pattern_wrong.findall(str(var))
        #MATCH_WRONG AND MATCH_OK RETURNS ONLY ONE GROUP ('ALAMO A.LORENZO A.')

        if len(match_wrong)>0: 
            
            return (var,False)
        else:
            pattern_ok = re.compile(r'([A-Za-z\.,Ññ ]+)')
            match_ok = pattern_ok.findall(str(var))
            
            return (match_ok[0],True)
    except IndexError:
        print(traceback.format_exc())

        return (var,False)





    
def is_id(var):
    is_ok = True
    tmp = str(var)
    if tmp.isalnum(): 
        return (var,not is_ok)
    else:
        split = re.split(r'[-]?',tmp)
        
        if not len(split)==2: return (var,not is_ok)
        else:
            split_one = str(split[0]).upper().strip()
            split_two = str(split[1]).strip()
            if not split_one=='E' and not split_one=='V': 
                return (var,not is_ok)
            elif  not split_two.isdigit(): 
                return (var,not is_ok)
            else:
                return ((split_one, split_two),is_ok)


def is_account(var): 
    is_ok = True 
    try:
        if var=='': return (None,not is_ok)    

        tmp = str(var) 
        pattern_wrong = re.compile(r'([^0-9-]+)')
        matches_wrong = pattern_wrong .findall(tmp)
        if len(matches_wrong)>0: return (var,False)
        
        pattern_ok = re.compile(r'([0-9])+-?([0-9])+')
        matches_ok = pattern_ok.findall(tmp)
        #REMEMBER ADDING OPTION TO SWITCH BETWEEN ONE AND TWO COLUMNS
        print(matches_ok)
        if len(matches_ok)>1 and len(matches_ok[0])==4 and len(matches_ok[1])==4:   #it means the account is longer thats supposed 
                                #so most likely that complete account is enterily in one cell
            return (var,is_ok)
        else:  #error ocurred
            return (var,not is_ok)
    except IndexError:

        return (var,not is_ok)    

def is_account2(var):
    is_ok = True  
    try:
        if var=='':
            return (None,not is_ok)
        pattern = re.compile(r'([0-9]+)')
        tmp = int(var) if isinstance(var,float) else var
        matches = pattern.findall(str(tmp))
        if len(matches)==1: 
            return (matches[0],is_ok)
        else:  #error ocurred
            return (matches[0],not is_ok)
    except:

        return (var,not is_ok) 






        







