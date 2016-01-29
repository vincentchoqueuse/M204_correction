from pylab import *     #importation de pylab pour les graphiques
from numpy import *
from scipy import signal

m=0.5
m_vect=[0.5,0.7,1,1.3,1.6]
wn=10
K=1


for m in m_vect:

    tf=signal.lti([K],[(1/(wn**2)),2*m/wn,1])
    t,y=signal.step(tf)


    #affichage de la RI
    plot(t,y,label="m=%f" %m)

    #calcul de la valeur finale
    vf=y[-1]
    vect_tr=where((y>1.05*vf)|(y<0.95*vf))[0] #Identification des éléments pour lesquelles la réponse indicielle est
    index_tr=vect_tr[-1]                        #Récupération du dernier élément du vecteur
    tr=t[index_tr]

    #calcul du dépassement relatif
    Dr=100*(max(y)-vf)/vf

    print("---------m=%f--------" % m)
    print("Valeur finale:\t %f" % vf)
    print("Temps de réponse: %f" % tr)
    print("Depassement relatif: %f (pourcent)" %Dr)

#affichage des courbes
legend()
show()