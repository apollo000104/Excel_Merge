import glob
import pandas as pd

path="F:\Learn\Python\panda_learn\excel_merge"
file_list=glob.glob(path+"/*.xlsx")
print(file_list)
excl_list=[]
for file in file_list:
    excl_list.append(pd.read_excel(file))
    pass
excl_merged=pd.DataFrame()
for excl_file in excl_list:
    excl_merged=excl_merged._append(
        excl_file, ignore_index=True
    )
    pass
excl_merged.to_excel('total.xlsx', index= False)
