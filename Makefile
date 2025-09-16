
FILE := OneVine-Gothic-Regular.ttf

all:
	python makefont.py

install:
	install -m 644 $(FILE) ~/.fonts/
	fc-cache -f

scan:
	fc-scan $(FILE)

download:
	-mkdir original
	curl -L https://github.com/intel/intel-one-mono/releases/download/V1.4.0/ttf.zip -o original/intelone.zip
	cd original ; unzip -o intelone.zip
	cp original/ttf/IntelOneMono-Regular.ttf original/
	curl -L https://github.com/daisukesuzuki/VLGothic/raw/main/VL-Gothic-Regular.ttf -o original/VL-Gothic-Regular.ttf

clean:
	rm -f HackVine-Gothic-Regular.ttf
	rm -fr original
