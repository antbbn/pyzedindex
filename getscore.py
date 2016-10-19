import json
import sys
import numpy as np

from zooplazedindex import getZooplaZedIndex,ZooplaError, OutcodeNotFoundError


def get_outcode_score(outcode, api_key, codes_filename = 'codes.json'):
  with open(codes_filename) as codes_file:
    codes = json.load(codes_file)
  
  
  # First we grab the zed_index for the area of interest
  # it's ok for this to raise an error
  zed_index = getZooplaZedIndex(outcode,api_key)
  
  # Then the zed index for all the neighboring areas
  for area,neighboroods in codes.items():
    if outcode in neighboroods:
      indices = np.array([])
      for neighbor in neighboroods:
        try:
          indices = np.append(indices,getZooplaZedIndex(neighbor,api_key))
        except (ZooplaError, OutcodeNotFoundError):
          pass # we ignore errors here because if some neighborood is missing it's still ok
      break
  
  # Then we average the ratios of the neighboring areas to the area of interest
  # higher than one means lowe prices in the outcode of interest
  # lower than one means higer prices in the outcode of interest
  score = np.mean(indices/zed_index)
  
  return score

if __name__ == "__main__":
  outcode = 'NW10'
  api_key=FIXME
  try:
   score = get_outcode_score(outcode,api_key)
   print(score)
  except (ZooplaError, OutcodeNotFoundError) as e:
   print(e)
   sys.exit(1)
 
