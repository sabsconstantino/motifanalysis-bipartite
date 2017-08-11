import bip_degrees as bk
import plfit

'''This module contains the power-law distributions fitted to the music and video game data. plfit can be found at: http://tuvalu.santafe.edu/~aaronc/powerlaws/
'''
#--------------------------------------------------------------------------
# File for printing
mfile = open("powerlawfitting_music.csv","w")
mfile.write("years,users_alpha,users_xmin,users_L,objects_alpha,objects_xmin,objects_L\n") # header

vgfile = open("powerlawfitting_videogames.csv","w")
vgfile.write("years,users_alpha,users_xmin,users_L,objects_alpha,objects_xmin,objects_L\n") # header

#--------------------------------------------------------------------------
# Music data, cumulative

pl_m9800 = [plfit.plfit(bk.m00_kU.values()), plfit.plfit(bk.m00_kO.values())]
s = str(pl_m9800)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
mfile.write('1998-2000,' + s + '\n')

pl_m9803 = [plfit.plfit(bk.m03_kU.values()), plfit.plfit(bk.m03_kO.values())]
s = str(pl_m9803)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
mfile.write('1998-2003,' + s + '\n')

pl_m9806 = [plfit.plfit(bk.m06_kU.values()), plfit.plfit(bk.m06_kO.values())]
s = str(pl_m9806)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
mfile.write('1998-2006,' + s + '\n')

pl_m9809 = [plfit.plfit(bk.m09_kU.values()), plfit.plfit(bk.m09_kO.values())]
s = str(pl_m9809)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
mfile.write('1998-2009,' + s + '\n')

pl_m9812 = [plfit.plfit(bk.m12_kU.values()), plfit.plfit(bk.m12_kO.values())]
s = str(pl_m9812)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
mfile.write('1998-2012,' + s + '\n')

pl_m9814 = [plfit.plfit(bk.m14_kU.values()), plfit.plfit(bk.m14_kO.values())]
s = str(pl_m9814)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
mfile.write('1998-2014,' + s + '\n')

#--------------------------------------------------------------------------
# Video game data, cumulative

pl_vg9700 = [plfit.plfit(bk.vg00_kU.values()), plfit.plfit(bk.vg00_kO.values())]
s = str(pl_vg9700)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
vgfile.write('1997-2000,' + s + '\n')

pl_vg9703 = [plfit.plfit(bk.vg03_kU.values()), plfit.plfit(bk.vg03_kO.values())]
s = str(pl_vg9703)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
vgfile.write('1997-2003,' + s + '\n')

pl_vg9706 = [plfit.plfit(bk.vg06_kU.values()), plfit.plfit(bk.vg06_kO.values())]
s = str(pl_vg9706)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
vgfile.write('1997-2006,' + s + '\n')

pl_vg9709 = [plfit.plfit(bk.vg09_kU.values()), plfit.plfit(bk.vg09_kO.values())]
s = str(pl_vg9709)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
vgfile.write('1997-2009,' + s + '\n')

pl_vg9712 = [plfit.plfit(bk.vg12_kU.values()), plfit.plfit(bk.vg12_kO.values())]
s = str(pl_vg9712)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
vgfile.write('1997-2012,' + s + '\n')

pl_vg9714 = [plfit.plfit(bk.vg14_kU.values()), plfit.plfit(bk.vg14_kO.values())]
s = str(pl_vg9714)
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(' ','')
vgfile.write('1997-2014,' + s + '\n')