release:
	rm  dist/*
	kalamine make Bépolar.yml
	cp Bépolar.yml dist/
	mv dist/bepolar.svg img/
	cp img/bepolar.svg img/bepolar_AltGr.svg
	cp img/bepolar.svg img/bepolar_DeadKey.svg
	cp img/bepolar.svg img/bepolar_Default.svg
	sed -i 's/iso intlBackslash/ergo ol40/g' img/bepolar.svg
	sed -i 's/iso intlBackslash/iso intlBackslash dk/g' img/bepolar_DeadKey.svg
	sed -i 's/iso intlBackslash/iso intlBackslash altgr/g' img/bepolar_AltGr.svg
	sed -i 's/iso intlBackslash/iso intlBackslash base/g' img/bepolar_Default.svg