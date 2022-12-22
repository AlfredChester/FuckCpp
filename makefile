default:
	pyinstaller .\entry.spec --noconfirm
	mkdir dist\fuckCpp\js
	xcopy js dist\fuckCpp\js /e /y
	mkdir dist\fuckCpp\lib
	xcopy lib dist\fuckCpp\lib /e /y
