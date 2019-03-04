import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu



# Extracting charge data from .out files
aln = []
sin = []
alnstdev = []
sinstdev = []



strtype = ['m40p', 'm40n', 'm5m10m5', 'm10m10m10m10', 'm10m20m10', 'm20m20'] 
chargeratio = ['0', '0', '1', '1', '1', '1']

#strtype = ['m40ncen', 'm40pcen'] 
#chargeratio = ['0', '0']
#strtype = ['m30m10', 'm5m30m5','m15m10m15']

pathstring  = []

ph = []
linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

for i in range(len(strtype)):
    pathstring.append('alsi/polymer/quenchedpoly/{:s}'.format(str(chargeratio[i])) + '/{:s}/'.format(str(strtype[i])))

for j in range(len(pathstring)):
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.out')):
        print(p) 
  
        # mu.getAvgPartCharge() returns three values: average charge fraction, precision and fluctuation
        # Input arguments are: mu.getAvgPartCharge( [path to file in], [particle type] )
        # Note that the particle type must be given as a string
        charge_1 = mu.getAvgPartCharge(p, 'alumina')
        charge_2 = mu.getAvgPartCharge(p, 'silica')
    
        aln[j].append( charge_1[0] )
        sin[j].append( charge_2[0] )
    
        alnstdev[j].append( charge_1[2] )
        sinstdev[j].append( charge_2[2] )
        ph[j].append( int(p.parts[-2][2]) )
        
        titlestring = '{:s}'.format(p.parts[-4]) 
        labelstring = 'ph = {:d}'.format(int(p.parts[-2][2]))  

    plt.figure(j+1)    
    plt.errorbar(ph[j], aln[j], alnstdev[j], label = labelstring, color = 'royalblue', marker ='o', linestyle = ':', ) 
    plt.errorbar(ph[j], sin[j], sinstdev[j], label = labelstring, color = 'darkorange', marker ='o', linestyle = ':')  
  
    plt.errorbar(ph, alp, alpstdev, label = labelstring, color = 'royalblue', marker ='*', linestyle = '--') 
    plt.errorbar(ph, sip, sipstdev, label = labelstring, color = 'darkorange', marker ='*', linestyle = '--')

        plt.figure(3)
        #plt.subplot(313)        
        plt.errorbar(f[:,0], f[:,1], f[:,2], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        plt.title('{:s}'.format(titlestring)+'\nProbability of outer tube surface')
       
    #for k in range(len(pathstring)):   
    plt.figure(1)
    plt.ylim(0.00, 1.00)
    plt.ylabel(r'$Prob(d<7.1\AA)$')
    plt.xlabel(r'$Monomer\ index$')
    plt.legend()
    py.savefig('{:s}'.format(titlestring) + '_prob' + '_io')

'''
alp = []
sip = []
alpstdev = []
sipstdev = []
ph = []


for p in sorted(Path('alsi/polymer/quenchedpoly/m40p/zero/').glob('ph*/cylinder_shell.out')):
    print(p)  
    # mu.getAvgPartCharge() returns three values: average charge fraction, precision and fluctuation
    # Input arguments are: mu.getAvgPartCharge( [path to file in], [particle type] )
    # Note that the particle type must be given as a string
    charge_1 = mu.getAvgPartCharge(p, 'alumina')
    charge_2 = mu.getAvgPartCharge(p, 'silica')

    alp.append( charge_1[0] )
    sip.append( charge_2[0] )

    alpstdev.append( charge_1[2] )
    sipstdev.append( charge_2[2] )
    ph.append( int(p.parts[-2][2]) )
    
 
plt.figure(2)    
plt.errorbar(ph, aln, alnstdev, label = 'Alumina, m40n', color = 'royalblue', marker ='o', linestyle = ':', ) 
plt.errorbar(ph, sin, sinstdev, label = 'Silica, m40n', color = 'darkorange', marker ='o', linestyle = ':')  
plt.errorbar(ph, alp, alpstdev, label = 'Alumina, m40p', color = 'royalblue', marker ='*', linestyle = '--') 
plt.errorbar(ph, sip, sipstdev, label = 'Silica, m40p', color = 'darkorange', marker ='*', linestyle = '--')


plt.fill_between(ph, aln - alnstdev, aln + alnstdev)     
plt.fill_between(ph, sin - sinstdev, sin + alnstdev)     
plt.fill_between(ph, alp - alpstdev, alp + alpstdev)     
plt.fill_between(ph, sip - sinstdev, sip + alnstdev)        

plt.legend()
plt.ylim(-0.10, 1.1)
plt.ylabel(r'$fractional\ charge$') 
plt.xlabel(r'$pH$')

plt.show()
py.savefig('{:s}'.format(titlestring) + '_prob' + '_o')   


plt.ylim(0.00, 1.00)
plt.ylabel(r'$Prob(d<7.1\AA)$')
plt.xlabel(r'$Monomer\ index$')
plt.legend()
py.savefig('{:s}'.format(titlestring) + '_prob' + '_o')        
'''  