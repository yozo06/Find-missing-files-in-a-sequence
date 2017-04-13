import re
from os import listdir
from os.path import isfile, join

mypath = raw_input("Enter the path of the directory:")
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print files;
j= len(files);
i=0;
count=0;
count1=0;
print "##Missing file numbers:" ,
while(i!=j-1):
	str3=re.findall('\d',files[i]);
	str3=str3[0]+str3[1]+str3[2];
	#print str3;
	count=count+1;
	if(count!=int(str3)):
		print count ,
		i=i-1;
		count1=count1+1;
	i=i+1;
print "";
print "##Total files missing :",count1;




