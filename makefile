default:
	make windows

windows:
	pyinstaller .\entry.spec --noconfirm
	mkdir dist\fuckCpp\js
	xcopy js dist\fuckCpp\js /e /y
	mkdir dist\fuckCpp\lib
	xcopy lib dist\fuckCpp\lib /e /y

linux:
	pyinstaller entry.spec --noconfirm
	cp -r js dist/fuckCpp
	cp -r lib dist/fuckCpp