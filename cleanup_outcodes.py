import pandas as pd
import json

outcodes_df = pd.read_csv('outcodes.csv', header=None, names=["fake","area","outcode"])

def mysum(arr):
  string = ''
  for val in arr:
    string += " " + val.strip() + " "
  return string.replace(',',' ').replace('\n','')

grouped = outcodes_df[["area","outcode"]].groupby("area")
res = grouped.agg(mysum)
#res = grouped.agg(" ".join)

out = {}
for area,row in res.itertuples():
  out[area] = []
  for code in row.split():
    out[area].append(code.strip())

print(json.dumps(out , sort_keys=True,
                 indent=4, separators=(',', ': '))
                 )

#with open('codes.dat','wb') as codes:
#	pickle.dump(out,codes)
  
#print(out)
