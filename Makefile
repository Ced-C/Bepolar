release:
	rm  dist/*
	kalamine build Bépolar.toml
	cp Bépolar.toml dist/
	cp dist/bepolar.svg img/
	cp img/bepolar.svg img/bepolar_AltGr.svg
	cp img/bepolar.svg img/bepolar_DeadKey.svg
	cp img/bepolar.svg img/bepolar_Default.svg
	sed -i 's/iso intlBackslash mixed/ergo ol40/g' img/bepolar.svg
	sed -i 's/iso intlBackslash mixed/iso intlBackslash odk/g' img/bepolar_DeadKey.svg
	sed -i 's/iso intlBackslash mixed/iso intlBackslash altgr/g' img/bepolar_AltGr.svg
	sed -i 's/iso intlBackslash mixed/iso intlBackslash base/g' img/bepolar_Default.svg
