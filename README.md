Bépolar
================================================================================


## TL;DR

Dérivé de BÉPO, Bépolar est une disposition clavier s’appuyant sur des mécanismes modernes afin d’améliorer le confort de frappe.
La disposition est plus confortable que BÉPO en Français, et meilleur que BÉPO pour l’anglais et la programmation avec sa couche AltGr dédiée au développement.

C’est un bon moyen, pour un bépoète, de tester l’approche 1DFH qui est l’essence d’[Ergo-L](https://ergol.org/) avec un temps d’apprentissage record.

👉 [Apprendre / tester](https://ergol.org/lafayette/#b%C3%A9polar)


## Pourquoi une nouvelle disposition ?
BÉPO m’a permis de découvrir le monde de l’ergonomie clavier et je l’en remercie. Depuis sa sortie, d’autres disposition (bien) plus optimisées ont vu le jour. 

Mais

**Apprendre une nouvelle disposition, c’est long et fastidieux**. Bépolar se veut le plus proche possible de BÉPO tout en évitant son principal problème : les caractères `M Z Ç W` sont ~~très~~ trop excentrés, ce qui est la principale cause de TMS documenté.

Quelques défaut de BÉPO corrigés par Bépolar :

1. L’anglais — La disposition BÉPO a été développée pour écrire principalement en **Français**. Aujourd’hui, l’anglais s’est énormément développé et est de plus en plus utilisé, que ce soit pour des Anglicismes, ou tout simplement pour écrire à l’international. Écrire en anglais en BÉPO est extrêmement fastidieux, notamment à cause de la position du `W`. 
2. La précision — Pour écrire du Français correct, nous avons besoin de bien des diacritiques sur des lettres `é è ù û à â ô ç` pour ne citer que les plus courants en français. Sur des machines à écrire, il n’y a pas le choix, il faut impérativement utiliser plus de touches pour permettre une bonne typographie (majuscules accentuées, espace insécable, guillemets à la Française, _etc_.). Le fait d’avoir plus de touches rend nécessairement les touches les plus éloignées moins confortable (et moins précises). Dvorak proposait d’excentrer les touches les moins utilisée. Le problème de cette approche, c’est que les touches les moins utilisées sont misent sur les positions les plus difficiles. Ainsi il est bien plus fréquent de faire des fautes de frappe sur ces touches et l’apprentissage de la dactylographie est plus long.
3. L’auriculaire droit — `M` est une lettre fréquemment doublée, la mettre en extension sur un doigt faible n’est pas judicieux. 
4. La programmation — Certains symboles de programmation ont des caractères très excentrés comme le `$`, ce qui est fastidieux pour coder dans certains langages.

Tous les problèmes mentionnés ont la même origine, l’utilisation de touches excentrées. Il faut donc changer d’approche ; Ne plus aller chercher les touches loin avec les doigts, mais plutôt les amener sous les doigts —passer d’un paradigme _finger-to-caps_ à _caps-to-finger_!

Pour cela, Bépolar agence toutes les lettres dans la zone la plus confortable du clavier : le pavé de 30 touches (3 colonnes × 5 touches × 2 mains).

La disposition étant très proche de BÉPO, elle s’apprend _très_ rapidement ; moins d’une petite semaine pour retrouver ma vitesse dans mon cas.

Pour ceux ne pratiquant pas BÉPO, je conseillerais plutôt de passer sur une disposition telle que [Ergo-L](https://ergol.org/) plus optimisée que Bépolar, mais requérant un apprentissage long.

Pour ceux qui ne peuvent vivre sans VIM, *et* qui ne souhaitent pas programmer leur clavier (via QMK ou un logiciel comme [Kanata](https://github.com/jtroo/kanata)) [QWERTY-Lafayette](https://qwerty-lafayette.org/) est un bon compromis.


### 📑 Cahier des Charges
Pour ce faire, voici les contraintes que je me suis données.
* Le moins de changement possible par rapport à BÉPO, seule quatre (ou cinq sur un clavier iso) touches doivent changer `É È À ^!` (`Ê`)
* Toutes les lettres sont situées sur le pavé des 30 (3x5x2) touches principales du clavier
* Les accents et autres diacritiques les plus communs via une touche morte de type [Lafayette](https://qwerty-lafayette.org/). On y mettera aussi quelques symboles typographiques utilisé en français.
* Les chiffres accessibles en direct
* Une couche Alt dédiée à la programmation
* Garder une disposition intuitive


## ⌨ Disposition
### Classique — Niveau 1 — Couche Alpha
La disposition Bépolar est présentée ci-dessous :

![disposition bepolar](img/bepolar_Default.svg)
Légende:
- En noir la touche frappé
- En rouge les touches « mortes », il faut les frapper puis enchaîner avec un autre caractères pour voir leur effet (comme le `^` en AZERTY.
- En vert le résultat de la touche typographique (en forme d’étoile) combiné avec le caractère sur la touche courante. 

### Touche Typographique — Niveau 5 — Techiquement un *iso_level_5_latch*, un cousin d’AltGr
La touche Typographique `★` (en rouge sur le layout) donne accès aux caractères en vert :
- Tous les accents communs en français (aigüe, grave, circonflexe)
- Certaine diacritique usuelle en langue européenne `ç ñ`
- Les ligatures les plus courantes `œ, æ, ß`
- D’autres symboles typographiques usuels tels que l’apostrophe typographique, les espaces insécables (fine ou non), les guillemets anglo-saxons, les points de suspension, le point médian (·), *etc.*
- Des symboles mathématiques tels que `≠ ≃ ± × ₀₋₉⁰⁻⁹` *etc.*
L’ensemble des symboles accessibles sont ici présentés :

![disposition bépolar touche morte](img/bepolar_DeadKey.svg)

> ⚠ Ce n’est pas très visible, mais touche morte suivi d’espace permet de faire l’apostrophe (typographique)

#### Principe
- La touche Typographique `★` suivie d’une voyelle (colonne du milieu ou *home row*) donne généralement cette dernière avec un accent grave (*i.e.* `à`, `ù`, `è`)
- La touche Typographique `★` suivie de la touche au-dessus de cette voyelle (colonne haute) donne un accent circonflexe (*i.e.* `â`, `û`, `î`, `ô`). ⚠ Exception pour le `ê` qui est à la droite du `è`
- La touche Typographique `★` suivie de `i` donne `é` ce qui facilite l’enchainement `ée`
- Deux appuis successifs sur la touche morte `★★` donne une touche morte trémas `*¨`. Pour faire un `ï` par exemple, il suffit de faire l’enchainement `★★i` (soit trois touches, mais les mots à trémas sont rares).
- La touche Typographique `★` suivie d’un symbole / lettre ayant une variate courante donne cette variante : `★c` → `ç`, `★n` → `ñ`, `★s` → `ß`, `★=` → `≠`, _etc_.

L’utilisation de la touche Typographique pour les accents n’est peut-être pas intuitive de prime abord. En effet, quand on tape à deux doigts comme le commun des mortels, toutes les touches se valent et il est préférable d’avoir une touche excentrée que de taper deux touches.
En revanche, quand on tape en position dactylo, toutes les touches excentrées sont pénibles et sujet à erreurs. Placer l’ensemble des lettres sur les 30 touches confortable du clavier, est donc plus efficace, tout en favorisant l’apprentissage de la mémoire musculaire.

*In fine*, grâce aux touches classiques, (niveau 1), la touche shift/maj (niveau 2), et la touche Typographique `★` (niveau 5), l’ensemble des symboles nécessaires à taper un Français correct sont accessibles.
Il est en outre possible d’écrire correctement et confortablement Français et en anglais ; et, dans une moindre mesure, l’allemand, l’espagnol et l’espéranto.

### Alt Gr. — Niveau 3 — ISO level 3
La couche Alt. Gr est facultative. Elle permet de faciliter la programmation informatique en rendant accessible l’ensemble des symboles utilisé pour coder sur la zonne confortable du clavier.

Cette couche est partagée entre les projets Bépolar, [Ergo-L](https://ergol.org/) et [QWERTY-Lafayette](https://qwerty-lafayette.org/). Elle a été pensée pour les développeurs en mettant les symboles les plus courants aux endroits les plus accessibles. 

![disposition bepolar AltGr](img/bepolar_AltGr.svg)

### La touche espace
La touche espace est utilisée pour les symboles suivants :
- L’espace classique : ` `
- L’espace insécable fine (shift+espace) : ` `
- L’espace insécable (AltGr+shift+espace) : ` `
- L’apostrophe typographique (★+espace) : `’`

> **NB :** Contrairement à bépo, l’underscore `_` n’est pas en AltGr+space, mais en ★+x (ou AltGr-.). Cela permet d’enchaîner espaces et symboles de programmation en couche AltGr, et de permettre d’enchaîner du texte facilement en snake_case. 

## 🧩 Installation
Les pilotes pour [Linux](#sous-linux), [Mac](#sous-mac) et [Windows](#sous-windows) sont disponibles dans le dossier `dist`.
Les pilotes sont générés via le script [Kalamine](https://github.com/fabi1cazenave/kalamine). Je mets à disposition la disposition pour tous les systèmes d’exploitation, mais **la version linux est la plus testée**.

### Sous Linux

#### Méthode simple | Wayland / X11
La façon la plus simple d’installer Bépolar est de faire
```bash
wget https://github.com/Ced-C/Bepolar/blob/master/dist/bepolar.xkb_custom
sudo cp bepolar.xkb_custom /usr/share/X11/xkb/symbols/custom
```

En fonction de votre environnement de bureau, il faut ensuite se déconnecter et se **reconnecter à sa session** pour que le système voit la nouvelle disposition dans les paramètres clavier. Elle ne sera pas dans Français, mais dans custom et sera nommée `custom / A user-defined custom layout`.

Pour avoir la disposition d’installée sous son vrai nom, il faut passer par la méthode avancée.  

#### Méthode avancée — compilation depuis les sources

Récupérer le layout de Bépolar :
```bash
wget https://github.com/Ced-C/Bepolar/blob/master/Bépolar.yml
```

Installer Kalamine  :
```bash
pip3 install pipx # si nécéssaire, pipx est une amélioration de pip
pipx install kalamine
```

```bash
# Pour générer les pilotes, télécharger le fichier `Bépolar.yml` du répertoire et faites un :
kalamine Bépolar.yml

# Pour installer la disposition qui appraraitra dans la catégorie Fr/Bépolar en user-space
xkalamine install Bépolar.yml

```

Pour installer la disposition qui appraraitra dans la catégorie Fr/Bépolar sur tout le système (root). Il faut alors installer kalamine via pyVenv puis
```bash
sudo xkalamine install Bépolar.yml
```

Il peut être nécessaire de se déconnecter et se **reconnecter à sa session**.

### Sous Mac
Il suffit de copier le fichier [bepolar.keylayout](dist/bepolar.keylayout) dans le dossier `/Library/Keyboard Layouts` et **relancer la session**. La disposition de clavier est disponible dans les préférences « Langue et Texte », onglet « Méthodes de saisie ».
On peut aussi l’enregistrer dans `~/Library/Keyboard Layouts` (pour le seul utilisateur courant), mais la disposition ne sera pas active et disponible au login.
Il est possible (et recommandé) d’utiliser Karabiner pour inverser les touches ⌘ Command et ⌥ Option à droite, afin d’accéder plus facilement à la couche de symboles.

### Sous Windows
Si vous avez les droits d’administration sur votre poste Windows, utiliser l’installeur (`setup.exe`) disponible dans [Bépolar.zip](dist/bepolar-0.6.0-win.zip)
Exécuter l’installeur et relancer la session. La disposition de clavier apparaît dans la barre de langues (indicateur de la barre des tâches).

Si vous n’avez pas les droits d’administrations, une version portable est disponible : [Bépolar.ahk](dist/bepolar.ahk)
Après lancement, un indicateur apparaît dans la barre des tâches. Le pilote peut être activé / désactivé avec le raccourci Alt‑AltGr.

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