import pygame
class objet() :
    def __init__(self,nom,image,position,prix_base,cps_base):
        self.image=image
        self.prix_base=prix_base
        self.cps_base=cps_base
        self.nombre=0
        self.nom=nom
        self.position=position

    def dessiner(self,fenetre) : #fontion qui affiche l'up
        #creation du texte
        afont=pygame.font.SysFont("comicsansms",15)
        position=self.position
        nom_objet=self.nom
        prix=self.prix()
        texte_nombre=afont.render("{} : {}".format(nom_objet,self.nombre),0,(0,0,0))
        texte_prix=afont.render("Prix : {}".format(round(prix,1)),0,(0,0,0))
        pos_nombre=(position[0]+170,position[1]+5)
        pos_prix=(pos_nombre[0],pos_nombre[1]+20)
        #affichage
        fenetre.blit(self.image,self.position)
        fenetre.blit(texte_nombre,pos_nombre)
        fenetre.blit(texte_prix,pos_prix)
        

    def cps_total(self) : #retourne les cps total de l'up
        return self.cps_base*self.nombre

    def prix(self): #retourne le prix du l'up
        return self.prix_base*1.1**self.nombre

    def achat(self):
        self.nombre+=1

    def colision(self,positon_click):
        position=self.position
        if position_click[0]>position[0] and position_click[1]<position[1]+60 and position_click[0]<positon[0]+320 and position_click[1]>position[1]:
                return True
        else:
                return False
