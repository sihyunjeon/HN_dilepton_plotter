import os

filenames=['SR_rebins.txt', 'SR_xaxis.txt', 'SR_yaxis.txt'] 
#filenames=['CR_rebins.txt', 'CR_xaxis.txt', 'CR_yaxis.txt'] 

From = "_DiElectron_2jets_OffZ_SS"
To = "_DiElectron_Preselection_SS"

for filename in filenames:

  tempfile = open('test_'+filename,'w')

  lines = open(filename).readlines()

  savethem=[]

  for line in lines:
    if From in line:
      savethem.append(line)
    tempfile.write(line)

  for line in savethem:
    line = line.replace(From,To)
    tempfile.write(line)

  tempfile.close()
  os.system('mv test_'+filename+' '+filename)
  
