#at first pip install thefuzz 
from thefuzz import fuzz
dfs = []
match_count=0
#yip will be the primary dataset with more data
new_yip=yip #making a copy 

#sametham here will be the secodary dataset with less data
new_sametham=sametham #making a copy

name='matched_data'
counter=0 #just to keep track of iterations
threshold = 101 #setting the threshold to 101 so that it will be 100 when it enter into the loop

print("loading>>>>>>>>>")
print(f'sametham at:{new_sametham.shape[0]}')
print(f'yip at:{new_yip.shape[0]}')

while new_yip.shape[0] > 0:
    columns = list(yip.columns.astype(str)) + list(sametham.columns.astype(str))+ ['Threshold'] #dynamic column allocation for the mapped dataset
    matched_data = pd.DataFrame(columns=columns)
    counter+=1
    print(f'counter at {counter}')
    threshold=threshold-1
    print(f'threshold at {threshold}')


    # Iterate through yip dataset and find matches in sametham
    for index1, row1 in new_yip.iterrows():
        name1 = row1['Derived ID_yip']
        matches = new_sametham[new_sametham['Derived Id_sametham'].apply(lambda name2: fuzz.WRatio(name1, name2) > threshold)] #takes value of Derived Id of one row from yip and iterates all Derived Id of sametham and returns all matches above threshold
        matches = matches.assign(Threshold=threshold)
        # If there are matches, combine the details
        if not matches.empty:
            combined_data = pd.concat([row1, matches.iloc[0]])  # Assuming you want to combine the first match
            matched_data = pd.concat([matched_data, combined_data.to_frame().T], ignore_index=True)
    dfs.append(matched_data)  # Append a list containing matched_data to dfs
    mapped_data=pd.concat(dfs, ignore_index=True)
    match_count=match_count+matched_data.shape[0]
    if(matched_data.shape[0]>0):
        print(f'currently matched {matched_data.shape[0]}')
    else:
        print(f'no match at threshold:{threshold}')

    print(f'matched total :{match_count}')
    new_yip=new_yip[~new_yip['Sl No'].isin(matched_data['Sl No'].unique())] #SL No is the unique identity of primary dataset.This is used to remove matched row from dataset
  
    print(f'remaining yip:{new_yip.shape[0]} , remaining sametham:{new_sametham.shape[0]}')
    print("-------------------------------------------")

    if new_yip.shape[0] <= 0 :
        break