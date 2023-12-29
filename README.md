Bépolar
================================================================================


## TL;DR

Dérivé de BÉPO, Bépolar est une disposition clavier s’appuyant sur des mécanismes modernes afin d’améliorer le confort de frappe. Les mécanismes utilisés en font un candidat plus confortable que BÉPO en Français, et meilleur que BÉPO pour l’anglais et la programmation avec sa couche AltGr dédiée au développement.


## Pourquoi une nouvelle disposition ?

### Rationale
BÉPO se base sur la méthode Dvorak. Cela veut dire plusieurs choses :

1. La disposition a été développée pour écrire principalement en **Français**. Aujourd’hui, l’anglais s’est énormément développé et est de plus en plus utilisé, que ce soit pour des Anglicismes, ou tout simplement pour écrire à l’international. Écrire en BÉPO est fastidieux, notamment à cause de la position du `W` qui est très excentré. De même certains symboles de programmation ont des caractères très excentrés comme le `$`, ce qui est fastidieux pour coder dans certains langages.

2. Pour écrire du Français correct, nous avons besoin de bien des diacritiques sur des lettres `é è ù û à â ô ç` pour ne citer que les plus courants en français. Sur des machines à écrire, il n’y a pas le choix, il faut impérativement utiliser plus de touches pour permettre une bonne typographie (majuscules accentuées, espace insécable, guillemets à la française, _etc_.). Le fait d’avoir plus de touches rend nécessairement les touches les plus éloignées mois accessible. Dvorak proposait d’excentrer les touches les moins utilisée. Le problème de cette approche, c’est que les touches les moins utilisée sont mise sur les positions les plus difficiles. Ainsi il est bien plus fréquent de faire des fautes de frappe sur ces touches et l’apprentissage de la dactylographie est plus long.

Il faut donc changer d’approche ! Ne plus aller chercher les touches loin avec les doigts, mais plutôt les amener sous les doigts —passer d’un paradigme _finger-to-caps_ à _caps-to-finger_.

Avec ce nouveau paradigme, on ouvre beaucoup de possibilités, mais **apprendre une nouvelle disposition, c’est long et fastidieux**. C’est pourquoi j’ai conçu Bépolar, une disposition clavier le plus proche possible de BÉPO mais qui évites les soucis mentionnés en agençant toutes les lettres dans la zone confortable, le pavé de 30 touches (3 colonnes × 5 touches × 2 mains).

### 📑 Cahier des Charges
Pour ce faire, voici les contraintes que je me suis données.
* Le moins de changement possible par rapport à BÉPO
* Toutes les lettres sont situées sur le pavé des 30 (3x5x2) touches principales du clavier
* Les accents et autres diacritiques les plus communs via une touche morte de type [Lafayette](https://qwerty-lafayette.org/). On y mettera aussi quelques symboles typographiques utilisé en français.
* Les chiffres accessibles en direct
* Une couche Alt dédiée à la programmation

Cette disposition se veut le meilleur compromis pour ceux qui ont déjà appris le BÉPO et ne veulent pas investir dans une nouvelle disposition. Elle permet de rester proche du BÉPO tout en s’éloignant des contraintes Dvorak issue des machines à écrires.

Pour ceux ne connaissant pas BÉPO, je conseille plutôt de passer sur une disposition telle que [Ergo-L](https://ergol.org/) plus optimisée que Bépolar, mais requérant un apprentissage long.

Pour ceux qui ne peuvent vivre sans VIM, et qui ne souhaitent pas programmer leur clavier, [QWERTY-Lafayette](https://qwerty-lafayette.org/) est un bon compromis. Un autre projet est en cours afin de pouvoir utiliser Bépolar et vim confortablement (accès aux flèches directionnelles sur `[HJKL]`) : [Girondin](https://github.com/Ced-C/Girondin)



## ⌨ Disposition
### Classique — Niveau 1
La disposition Bépolar est présentée ci-dessous :

![disposition bepolar](img/bepolar_Default.svg)
Légende:
- En noir la touche frappé
- En rouge les touches « mortes », il faut les frapper puis enchainer avec un autre caratères pour voir leur effet
- En vert le résultat de la touche morte lafayette combiné avec le caractère sur la touche courante. 

### Touche morte — Niveau 3
La touche morte `*` (en rouge sur le layout) donne accès au charactères en vert :
- Tous les accents communs en français (aigüe, grave, circonflexe)
- Certaine diacritique usuelle en langue européenne `ç ñ`
- Les ligatures les plus courantes `œ, æ, ß`
- D’autres symboles typographiques usuels tels que l’apostrophe typographique, les espaces insécables (fine ou non), les guillemets anglo-saxons, les points de suspension, le point médian, *etc.*
- Des symboles mathématiques tels que `≠ ≃ ± × ₀₋₉⁰⁻⁹` *etc.*
L’ensemble des symboles accessibles sont ici présentés :

![disposition bepolar touche morte](img/bepolar_DeadKey.svg)

⚠ Ce n’est pas très visible, mais touche morte suivi d’espace permet de faire l’appostrophe (typographique)


#### Principe
- La touche morte `*` suivie d’une voyelle (colonne du milieu ou *home row*) donne généralement cette dernière avec un accent grave (*i.e.* `à`, `ù`, `è`)
- La touche morte `*` suivie de la touche au-dessus de cette voyelle (colonne haute) donne un accent circonflexe (*i.e.* `â`, `û`, `î`, `ô`). ⚠ Exception pour le `ê` qui est à la droite du `è`
- La touche morte `*` suivie de `i` donne `é`
- Deux appuis successifs sur la touche morte `**` donne une touche morte trémas `*¨`. Pour faire un `ï` par exemple, il suffit de faire l’enchainement `**i` (soit trois touches, mais les mots à trémas sont rares).

L’utilisation de la touche morte pour les accents n’est peut-être pas intuitive de prime abord, mais permet de placer l’ensemble des lettres sur les 30 touches, tout en favorisant l’apprentissage de la mémoire musculaire.


*In fine*, grâce aux touches classiques, (niveau 1), la touche shift/maj (niveau 2), et la touche morte `*` (niveau 3), l’ensemble des symboles nécessaires à taper un Français correct sont accessibles.
Il est en outre possible d’écrire correctement et confortablement Français et en anglais. Dans une moindre ergonomie, l’espagnol, l’allemand et l’espéranto sont égallement accéssible.

### Alt Gr. — Niveau 5
La couche Alt. Gr est utilisé pour faciliter la programmation informatique en rendant accessible l’ensemble des symboles utilisé pour coder.

![disposition bepolar AltGr](img/bepolar_AltGr.svg)

⚠ Cette couche n’est pas aussi mature que les autres et peut être amenée à évoluer davantage que la couche principale.

### La touche espace
La touche espace est utilisée pour les symboles suivants :
- L’espace classique : ` `
- L’espace insécable fine (shift+espace) : ` `
- L’apostrophe typographique (touche_morte+espace) : `’`
- L’underscore (AltGr+espace) : `_`
- L’espace insécable (AltGr+shift+espace) : ` `

## 🧩 Installation
Les pilotes pour Linux, Mac et Windows sont disponibles dans le dossier `dist`.
Les pilotes sont générés via le script [Kalamine](https://github.com/fabi1cazenave/kalamine). Je mets à disposition la dispo pour tous les systèmes d’exploitation, mais **seule la version linux est testée** de mon côté.

### Sous Linux

#### Méthode simple | Wayland / X11
La façon la plus simple d’installer Bépolar est de faire
```bash
wget https://github.com/Ced-C/Bepolar/blob/master/dist/bepolar.xkb_custom
sudo cp bepolar.xkb_custom /usr/share/X11/xkb/symbols/custom
```

Il faut ensuite se déconnecter et se **reconecter à sa session** pour que le système voit la nouvelle disposition dans les paramètres clavier. Elle ne sera pas dans Français, mais dans custom et sera nommée `custom / A user-defined custom layout`.

Pour avoir la disposition d’installée sous son vrai nom, il faut passer par la méthode avancée.  

#### Méthode avancée — compilation depuis les sources
Installer Kalamine  :
```bash
pip3 install kalamine --break-system-packages
```

Pour générer les pilotes, télécharger le fichier `Bepolar.yml` du répertoire et faites un :
```bash
kalamine Bépolar.yml
```

Pour installer la disposition qui appraraitra dans la catégorie Fr/Bépolar en user-space
```bash
xkalamine install Bepolar.yml # insalle la dispo
```
Pour installer la disposition qui appraraitra dans la catégorie Fr/Bépolar sur tout le systeme (root). Il faut alors installer kalamine via pyVenv puis
```bash
sudo xkalamine install Bepolar.yml # insalle la dispo
```

Il faut ensuite se déconnecter et se **reconecter à sa session**.

#### Bug sous Ubuntu/Gnome (section obsolète ?)
Parfois, la couche AltGr ne fonctionne pas. Si cela vous arrive :
1. télécharger `GNOME Tweaks`
2. Dans la partie Keyboard & Mouse cliquer sur `Additional Layout Option`
3. Trouver l’option `key to choose 5th level`
4. Selectioner l’option `Right Alt Chooses 5th Level


## 💡 Faites votre propre disposition
Si vous souhaitez modifier la disposition pour l’adapter à vos besoins, le fichier `Bepolar.yml` est lisible facilement et peut être modifié à la main avant d’utiliser kalamine pour générer vos propres pilotes.

## 🙏 Mention
Un _grand_ merci à `Kazé` pour ses nombreux softs utiles dont :
- kalamine pour générer les pilotes
- X-keyboard pour générer les images de layout

Et son implication dans de nombreux projet (BÉPO, QWERTY-lafayette)

De même, merci à :
- `Nuclear Squid` pour ses explications, et son [serveur discord](https://discord.gg/RH34GjQEgC) qui m’ont permis de me lancer dans le sujet
- `Lobre` pour ses retours éclairants
- `Aeshar` & `Brab` et leur version custom `BMP` de laquelle `Bépolar` est issue.