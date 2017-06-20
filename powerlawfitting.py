import bip_degrees as bk
import plfit

'''This module contains the power-law distributions fitted to the music and video game data. plfit can be found at: http://tuvalu.santafe.edu/~aaronc/powerlaws/
'''

#--------------------------------------------------------------------------
# Music data, cumulative

#pl_m9800 = [plfit.plfit(bk.m00_kU.values()), plfit.plfit(bk.m00_kO.values())]
pl_m9800 = [[2.78, 2, -3683.9248650772533], [2.16, 6, -3216.0023338559513]]

#pl_m9803 = [plfit.plfit(bk.m03_kU.values()), plfit.plfit(bk.m03_kO.values())]
pl_m9803 = [[2.62, 2, -12921.788125887044], [2.21, 21, -3440.50732401333]]

#pl_m9806 = [plfit.plfit(bk.m06_kU.values()), plfit.plfit(bk.m06_kO.values())]
pl_m9806 = [[2.55, 2, -24975.374459847328], [2.34, 47, -3254.6804231527362]]

#pl_m9809 = [plfit.plfit(bk.m09_kU.values()), plfit.plfit(bk.m09_kO.values())]
pl_m9809 = [[2.53, 3, -20548.985439634303], [2.27, 37, -5503.491837336332]]

#pl_m9812 = [plfit.plfit(bk.m12_kU.values()), plfit.plfit(bk.m12_kO.values())]
pl_m9812 = [[2.67, 3, -37915.7913950638], [1.91, 3, -46184.87367810719]]

#pl_m9814 = [plfit.plfit(bk.m14_kU.values()), plfit.plfit(bk.m14_kO.values())]
pl_m9814 = [[2.56, 1, -420474.54408050433], [2.1, 4, -86624.02922341874]]

#--------------------------------------------------------------------------
# Video game data, cumulative

#pl_vg9700 = [plfit.plfit(bk.vg00_kU.values()), plfit.plfit(bk.vg00_kO.values())]
pl_vg9700 = [[3.05, 1, -4198.909305060134], [2.44, 8, -901.2543351066217]]

#pl_vg9703 = [plfit.plfit(bk.vg03_kU.values()), plfit.plfit(bk.vg03_kO.values())]
pl_vg9703 = [[2.6, 2, -14305.860978397805], [2.04, 8, -7439.587748479391]]

#pl_vg9706 = [plfit.plfit(bk.vg06_kU.values()), plfit.plfit(bk.vg06_kO.values())]
pl_vg9706 = [[2.56, 2, -26721.508396533092], [2.91, 88, -1143.7289108026641]]

#pl_vg9709 = [plfit.plfit(bk.vg09_kU.values()), plfit.plfit(bk.vg09_kO.values())]
pl_vg9709 = [[2.69, 2, -52804.93437028017], [2.9, 122, -1579.2556302569715]]

#pl_vg9712 = [plfit.plfit(bk.vg12_kU.values()), plfit.plfit(bk.vg12_kO.values())]
pl_vg9712 = [[2.74, 1, -284422.02634586947], [2.71, 139, -3394.025798820938]]

#pl_vg9714 = [plfit.plfit(bk.vg14_kU.values()), plfit.plfit(bk.vg14_kO.values())]
pl_vg9714 = [[2.96, 8, -22537.716892050834], [2.83, 348, -2317.5839814877613]]
