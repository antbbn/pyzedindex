import requests

class ZooplaError(Exception):
  """Specific exception for placeilive.com API error"""
  pass

class OutcodeNotFoundError(Exception):
  """Specific exception for placeilive.com API error"""
  pass

def getZooplaZedIndex(outcode, api_key, base_url = "http://api.zoopla.co.uk/api/v1/zed_index.js"):
    """ This function performs an API request. 
    The api is quite simple and the only input it requires is
    an outcode and an api_key.  It returns a JSON response.
    The third argument is there just in case something changes
    with the API (e.g. version).
  
    Returns a Zed-index
    """
  
    res = requests.get(base_url, 
                       params = {'area': outcode, 
                                 'output_type': 'outcode',
                                 'api_key': api_key},
                       headers = {"Accept":"application/json"})

    if res.status_code != requests.codes.ok :
      if res.status_code == 400:
        raise OutcodeNotFoundError("Outcode Not Found")
      else:
        raise ZooplaError("Error code {}".format(res.status_code))
  
    # A good request will return a JSON array of dictionaries.
    try:
      result = res.json()
      return  int(result['zed_index'])
    except (ValueError, KeyError):
      raise ZooplaError("Invalid response content")



if __name__ == "__main__":
  
  api_key=FIXME
  res = getZooplaZedIndex("N5",api_key)
  print(res)

  res = getZooplaZedIndex("BH",api_key)
  print(res)
  res = getZooplaZedIndex("BH14",api_key)
  print(res)
