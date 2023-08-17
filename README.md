Bépolar
================================================================================

Dérivé de BÉPO, Bépolar est une disposition clavier s’appuyant sur des mécanismes moderne afin d’améliorer le confort de frappe. 

## Cahier des Charges

* Le moins de changement possible par rapport à BÉPO
* Toutes les lettres sont situées sur le pavé des 30 (3x5x2) touches principales du clavier
* Les accents et autres diacritiques les plus communs via une touche morte de type [lafayette](#lien)
* Les chiffres accessible en direct
* Une couche Alt dédié à la programmation

Cette disposition ce veut le meilleur compromis pour ceux qui ont déjà appris le BÉPO et ne veulent pas investir dans une nouvelle disposition. Elle permet de rester proche du BÉPO tout en s’éloignant des contraintes Dvorak issue des machines à écrires (alternance des mains, éparpillement des lettres accentuées au delà des 30 touches, *etc.*).

Pour ceux ne connaîssant pas BÉPO, je conseil plutôt de passer sur une disposition telle que [Ergo-L](ergol.org), plus optimisée que Bépolar, mais requierant un apprentissage long. 

Pour ceux qui ne peuvent vivre sans VIM, [QWERTY-lafayette](#lien) est un bon compromis.



## Disposition
### Classique — Couche 0
La disposition Bépolar est présenté ci-dessous :

![disposition bepolar](img/bepolar.png)
### Touche morte — Couche 3
La touche morte `*` donne accès à :
- Tous les accents communs en français (aigüe, grave, circonflexe)
- Certains diacritique usuel en langue européennes (ç, ñ)
- D’autres symboles typographique usuels tel que l’apostrophe typographique, les espaces incécables (fine ou non), les guillement anglo-saxons, les points de suspentions, le point médiant, *etc.*
- Des symboles mathématiques tel que supérieur, inférieur, différent, multiplier, plus-ou-moins, pourmille, *etc.*
L’ensemble des symboles accessibles sont ici présenté :

![disposition bepolar touche morte](img/bepolar_dk.png)
#### Principe
- La touche morte `*` suivie d’une voyelle (colonne du milieu ou home row) donne généralement cette dernière avec un accent grave (*i.e.* `à`, `ù`, `è`)
- La touche morte `*` suivie de la touche au dessus de cette voyelle (colonne haute) donne un accent circonflexe (*i.e.* `â`, `û`, `î`, `ô`). ⚠ Exeption pour le `ê` qui est à la droite du `è`
- La touche morte `*` suivie de `i` donne `é`

L’utilisation de la touche morte pour les accents n’est peut-être pas intuitive de prime abord, mais permet de placer l’ensemble des lettres sur les 30 touches, tout en favorisant l’apprentissage de la mémoire musculaire.


*In fine*, grace aux touches classique, (niveau 0), la touche shift/maj (niveau 1), et la touche morte `*` (niveau 3), l’ensemble des symboles nécessaires à taper un français correcte sont accessibles. 
Il est en outre possible d’écrire correctement en aglais, espagñol, Allemand et espéranto.

### Alt Gr. — Couche 2 et 4
La couche Alt. Gr est utilisée pour faciliter la programation informatique en rendant accessible l’ensemble des symboles utilisé pour coder.

![disposition bepolar AltGr](img/bepolar_alt.png)

⚠ Cette couche n’est pas aussi mature que les autre et peut être amennée à évoluer davantage que la couche principale.

### La touche espace
La touche espace est uliliser pour les symboles suivants :
- L’espace classique : ` `
- L’espace insécable fine (shif+espace) : ` `
- L’appostrophe typographique (touche_morte+espace) : `’`
- L’underscore (AltGr+espace) : `_`
- L’espace insécable (AltGr+shift+espace) : ` `

## Installation
Les pilotes pour Linux, Mac et Windows sont disponible dans le dossier `dist`.
La dernière version de [Kalamine](https://github.com/fabi1cazenave/kalamine) est nécessaire pour générer la version actuelle ou une variante de Bépolar. 

Pour installer Kalamine :
```bash
sudo pip install kalamine # Yes, you *do* need root privileges
```

Pour générer les pilotes, télécharger le fichier `Bépolar.yml` du répertoire et faites un :
```bash
kalamine Bépolar.yml
```
Il est ensuite possible d’utiliser les fichier générer pour installer les pilotes dans votre système.
### Spcécificité Linux :
Sous Linux Kalamine est capable d’installer et de supprimer des dispositions :
#### Sous X11
```bash
sudo xkalamine install Bépolar.yml # insalle la dispo
xkalamine apply Bépolar.yml # teste la dispo en locale
```

#### Sous Wayland
Il y a actuellement un bug connu sous kalamine qui l’empêche de bien fonctionner sous wayland. Pour y remédier :
```bash
xkbpath=/usr/share/X11/xkb
# sauvegarde de la config actuelle
sudo cp $xkbpath/rules/evdev.xml $xkbpath/rules/evdev.xml.bk
sudo cp $xkbpath/rules/base.xml $xkbpath/rules/base.xml.bk
sudo cp $xkbpath/symbols/fr $xkbpath/symbols/fr.bk

sudo xkalamine install Bépolar.yml
# supprime les varibles qui posent problèmes pour wayland
sudo python3 ./script/kalamine_clean.py
# kalamine n’est plus capable de supprimer la disposition, mais, `sudo ./set_org_xkb.sh` permet de revenir comme avant si les étapes précédantes ont bien été suivies.
```


## Faites votre propre disposition
Si vous souhaitez modifier la disposition pour l’adapter à vos besoins, le fichier `Bépolar.yml` est lisible facilement et peut être modifier à la main avant d’utiliser kalamine pour générer vos propres pilotes. 

