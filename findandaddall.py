

import re

string = "96h11k4959q615948s50922o38h1453ij38w73413d5577lzrqw3780b389750vf100zd29z73j5wh73l6965n85vm77cw10awrjr29265289222238n10013uk10062f9449acbhfgcm35j78q80"

#print(re.findall(r'\d+', string))

total = 0
#list = []

#list = (re.findall(r'\d', string))

#print(list)

for num in (re.findall(r'\d', string)):
    print(f">> num is:  {num}")
    total += int(num)

print (total)
