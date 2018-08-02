import pandas as pd

from pprint import pprint
ID = 0
ACC = 1   #quick comparions
NAME = 2



def evaluate_row_pattern(row,patterns):  #returns the patternsition of names,id numbers,accounts numbers,etc
    
    
    # for idx_cell,value in enumerate(row):
    #     if not patterns.get(ID):
    #         if utils.is_id(value):
    #             patterns[ID] = idx_cell
    #     if not patterns.get(ACC):
    #         if utils.is_account(value):
    #             patterns[ACC] = [idx_cell,idx_cell+1]
    #     if not patterns.get(NAME):
    #         if utils.is_name(value):
    #             patterns[NAME] = idx_cell

    # return True if len(patterns.keys())==3 else False
    return True



def start_database_test(df,patterns):
    TEST = []
    for index,row in  df.iterrows():
        row_list = row.tolist()
        # TEST.append({'NAME':row_list[patterns[NAME]],'ID':row_list[patterns[ID]]}) 
        TEST.append({'NAME':row_list[0],'ID':row_list[2]})
    pprint(TEST)



def read_file(path):
    patterns = {}   
    df = pd.read_excel(path) #reading excel file
    for index,row in  df.iterrows():
        if (evaluate_row_pattern(row.tolist(),patterns)):
            #then it find a pattern in the row and 
            #it will start substractting the data form the file into the database
            start_database_test(df,patterns)

            break

    
        #here no pattern was found 
    

          
            
if __name__=='__main__':
    read_file(r'C:\Users\PC\Desktop\PASIVIC 2016\SOCIOS 2017 NUEVO.xls')