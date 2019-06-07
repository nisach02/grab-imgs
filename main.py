import urllib


#THIS CODE GRABS THE IMAGES FROM THE LIST OF URLS FROM A FITS FILE AND SAVES IT TO YOUR WANTED SPECIFIC FOLDER
#OR TO THE DEFAULT FOLDER RUNNING THE FILE ON


from astropy.io import fits
from astropy.table import Table



hdu_list1 = fits.open("fits-file.fits", memmap=True)
file_data1 = Table(hdu_list1[1].data)

url = file_data1['img-url']
filename = file_data1['name']

#mypath = any list of folder names you can create, or already exists.

#fullfilename = os.path.join(myPath, filename) #to join in case we want to put downloads in specific folders
#WE HAVEN'T USED THIS HERE YET, CAUSE WE WANT TO SAVE IN THE SAME PROGRAM FOLDER ANYWAY

for url in range(len(urls)):
        
    fullfilename = str(filenames[url]) + str('.png')
    
    urllib.request.urlretrieve(urls[url], fullfilename)
