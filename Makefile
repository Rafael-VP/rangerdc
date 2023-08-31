CONFIGPATH = ${HOME}/.config/rangerdc/
CONFIGFILE = ${CONFIGPATH}/config.ini
TARGET = /usr/bin/rangerdc

.PHONY:
all: ${CONFIGPATH}/config.ini
	$(info ********** built **********)

install: all
	cp rangerdc.py ${TARGET}

${CONFIGFILE}:
	mkdir -p ${CONFIGPATH}
	test -s ${CONFIGFILE} || cp config.ini ${CONFIGFILE}
	cp filepicker ${CONFIGPATH}filepicker