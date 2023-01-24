DISTROUTE=dist\fuckCpp

default:
	make windows

windows:
	pyinstaller .\entry.spec --noconfirm
	mkdir ${DISTROUTE}\js
	xcopy js ${DISTROUTE}\js /e /y
	mkdir ${DISTROUTE}\lib
	xcopy lib ${DISTROUTE}\lib /e /y

linux:
	pyinstaller entry.spec --noconfirm
	cp -r js ${DISTROUTE}
	cp -r lib ${DISTROUTE}