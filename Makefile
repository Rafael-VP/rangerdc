CONFIGPATH = ${HOME}/.config/rangerdc/
CONFIGFILE = ${CONFIGPATH}config.ini
TARGET = ${HOME}/.local/bin/rangerdc

.PHONY:
all: ${CONFIGPATH}config.ini
	$(info ********** built **********)

clean:
	-rm ${TARGET}
	-rm -rf ${CONFIGPATH}

install: all config
	cp rangerdc.py ${TARGET}
	chmod +x ${TARGET}

config:
	mkdir -p ${CONFIGPATH}
	cp config.ini ${CONFIGFILE}
	cp filepicker ${CONFIGPATH}filepicker
