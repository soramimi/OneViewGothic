
FILE := HackVine-Gothic-Regular.ttf

all:
	python makefont.py

install:
	install -m 644 $(FILE) ~/.fonts/
	fc-cache -f

scan:
	fc-scan $(FILE)

download:
	-mkdir original
	curl -L https://github.com/source-foundry/Hack/releases/download/v3.003/Hack-v3.003-ttf.tar.gz -o original/Hack.tar.gz
	cd original ; tar zxvf Hack.tar.gz
	cp original/ttf/Hack-Regular.ttf original/
	curl -L https://github.com/daisukesuzuki/VLGothic/raw/main/VL-Gothic-Regular.ttf -o original/VL-Gothic-Regular.ttf

clean:
	rm -f HackVine-Gothic-Regular.ttf
	rm -fr original
