default:
	pyinstaller .\entry.spec --noconfirm
	mkdir dist\fuckCpp\js
	xcopy js dist\fuckCpp\js /e /y