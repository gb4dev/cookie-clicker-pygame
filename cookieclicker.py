import pygame
from pygame.locals import *
from objets import *

pygame.init()
fenetre=pygame.display.set_mode((640,480))

#fonctions
def calc_cps():
    cps=0.0
    for objet in liste_objets:
        cps+=objet.cps_total()
    return cps

def achat_boss(prix):
    return round(prix*1.62)

def total_cpc(nombre_boss) :
    if nombre_boss==1 :
        return 2
    else : 
        return 2**nombre_boss


#chargement des images des up
image_curseur=pygame.image.load("bcurseur.png").convert()
image_cuisinier=pygame.image.load("bcuisinier.png").convert()
image_banque=pygame.image.load("bbanque.png").convert()
image_usine=pygame.image.load("busine.png").convert()
image_ferme=pygame.image.load("bferme.png").convert()
image_mine=pygame.image.load("bmine.png").convert()
boss_ultime=pygame.image.load("illuminati.png").convert_alpha()

#chargement des images
fond_shop=pygame.image.load("menushop.png").convert_alpha()
fond=pygame.image.load("fond.jpg").convert()
image_gcookie=pygame.image.load("gcookie.png").convert_alpha()
image_pcookie=pygame.image.load("pcookie.png").convert_alpha()
image_gshop=pygame.image.load("gcharioshop.png").convert_alpha()
image_pshop=pygame.image.load("pcharioshop.png").convert_alpha()
#texte et police
cfont=pygame.font.SysFont("comicsansms",25)
afont=pygame.font.SysFont("comicsansms",15)
texte_cookie=cfont.render("Cookies : {}",0,(255,255,255))
texte_cps=cfont.render("Cps : {}",0,(255,255,255))
texte_cpc=cfont.render("Cpc : {}",0,(255,255,255))
texte_pboss=afont.render("prix : {}",0,(255,255,255))
texte_nboss=afont.render("boss : {}",0,(255,255,255))


pygame.display.set_caption("Cookie clicker")
pygame.display.set_icon(image_gcookie)

pos_boss=(540,0)
pos_menushop=fond_shop.get_rect(centerx=fenetre.get_width()/2)
pos_fond=(0,0)
pos_cookie=image_gcookie.get_rect(center=(320,240))
pos_shop=(20,316)
pos_tcookie=texte_cookie.get_rect(centerx=fenetre.get_width()/2)
pos_cps=texte_cps.get_rect(centerx=fenetre.get_width()/2,centery=50)
pos_cpc=texte_cpc.get_rect(centerx=fenetre.get_width()/2,centery=85)
pos_nboss=(pos_boss[0],pos_boss[1]+100)
pos_pboss=(pos_nboss[0],pos_nboss[1]+20)

img_cookie=image_gcookie
img_shop=image_gshop

Curseur=objet("Curseur",image_curseur,(160,90),10,0.2)
Cuisinier=objet("Cuisinier",image_cuisinier,(160,155),100,1.3)
Banque=objet("Banque",image_banque,(160,220),1000,10)
Usine=objet("Usine",image_usine,(160,285),10000,50)
Ferme=objet("Ferme",image_ferme,(160,350),100000,300)
Mine=objet("Mine",image_mine,(160,415),1000000,1500)
liste_objets=[Curseur,Cuisinier,Banque,Usine,Ferme,Mine]
prix_boss=1234
cpc=1
nombre_boss=0
cookies=0
cps=0

continuer=1
jeu=1
menu=0

while continuer :
    pygame.time.Clock().tick(30)
    #evenements
    for event in pygame.event.get():
        if event.type == QUIT :
            continuer=0
        if menu==1 and jeu==0 :
            if event.type==MOUSEBUTTONDOWN:
                posx=event.pos[0]
                if posx>480 or posx<160 :
                    jeu=1
                    menu=0
                for objet in liste_objets :
                    if event.pos[0]>objet.position[0] and event.pos[0]<objet.position[0]+320 and event.pos[1]>objet.position[1] and event.pos[1]<objet.position[1]+60:
                        if cookies >= objet.prix() :
                            cookies-=objet.prix()
                            objet.achat()
                            
                

            
        if jeu==1 and menu==0 :
            if event.type==MOUSEBUTTONDOWN:
                if event.pos[0]>20 and event.pos[0]<179 and event.pos[1]>316 and event.pos[1]<460 :
                    jeu=0
                    menu=1
                    img_shop=image_pshop
                if event.pos[0]>200 and event.pos[0]<440 and event.pos[1]>120 and event.pos[1]<360 :
                    cookies+=cpc
                    img_cookie=image_pcookie
                if event.pos[0]>540 and event.pos[1]<96 :
                    if cookies>=prix_boss :
                        cookies-=prix_boss
                        prix_boss=achat_boss(prix_boss)
                        nombre_boss+=1
                        cpc=total_cpc(nombre_boss)
                    
            if event.type ==MOUSEBUTTONUP :
                img_cookie=image_gcookie
                img_shop=image_gshop
        
    #logique du jeu
    cps=calc_cps()
    cookies+=cps/30
    texte_cookie=cfont.render("Cookies : {}".format(round(cookies,1)),0,(255,255,255))
    texte_cps=cfont.render("Cps : {}".format(round(cps,1)),0,(255,255,255))
    texte_cpc=cfont.render("Cpc : {}".format(cpc),0,(255,255,255))
    texte_nboss=afont.render("boss : {}".format(nombre_boss),0,(255,255,255))
    texte_pboss=afont.render("prix : {}".format(prix_boss),0,(255,255,255))
    
            
    #affichage
    
        
    if jeu==1 and menu==0:
        fenetre.blit(fond,pos_fond)
        fenetre.blit(img_cookie,pos_cookie)
        fenetre.blit(img_shop,pos_shop)
        fenetre.blit(texte_cookie,pos_tcookie)
        fenetre.blit(texte_cps,pos_cps)
        fenetre.blit(texte_cpc,pos_cpc)
        fenetre.blit(boss_ultime,pos_boss)
        fenetre.blit(texte_nboss,pos_nboss)
        fenetre.blit(texte_pboss,pos_pboss)
        pygame.display.flip()

    if menu==1 and jeu==0 :
        fenetre.blit(fond,pos_fond)
        fenetre.blit(img_shop,pos_shop)
        fenetre.blit(fond_shop,pos_menushop)
        fenetre.blit(texte_cookie,pos_tcookie)
        fenetre.blit(texte_cps,pos_cps)
        for objets in liste_objets :
            objets.dessiner(fenetre)
        pygame.display.flip()
pygame.quit()
    
            
    

