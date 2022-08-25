import numpy as np
import cdx_toolkit
import os
import multiprocessing

print("HI")

cdx = cdx_toolkit.CDXFetcher(source='ia')
url = 'https://www.linkedin.com/in/*'

for year in np.arange(2006, 2017, 1):
    lim = 10
    objs = list(cdx.iter(url, from_ts=f'{year}01', to=f'{year+1}01', limit = lim, filter='status:200'))
    
    print(f"Year:{year}, Total Extracted:{len(objs)}, Total Unique: {len(set([objs[i]['urlkey'] for i in range(len(objs))]))}")
    
for year in np.arange(2006, 2017, 1):
    """try:
        os.mkdir("cc/"+str(year))
    except:
        pass"""
    lim = 10
    objs = list(cdx.iter(url, from_ts=f'{year}01', to=f'{year+1}01', limit = lim, filter='status:200'))
    print(f"Obtained {year}")
    storlist = []
    j = 0
    def outputPersonIA(objs):
        global j
        global storlist
        if objs['urlkey'] not in storlist:
            # Creating an HTML file
            Func = open(f"cc/{year}/Person{j+1}.html","w")
            # Adding input data to the HTML file
            try:
                Func.write(objs.content.decode("utf-8"))
                j+=1
            except:
                pass
                #print(f"Failed saving {objs[i]['urlkey']}")
            Func.close()
            storlist.append(objs['urlkey'])

    pool = multiprocessing.Pool(15)
    pool.map(outputPersonIA, objs)
    
    print(storlist)
    print(f"Finished {year}, Total saved: {len(os.listdir('ia/test'))}")