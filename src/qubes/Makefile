PYTHON = /usr/bin/python2
PYTHON_SITEARCH = $(shell python2 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_lib(1))')
ALL = imggen.py imggen.pyc imggen.pyo

all:
	$(PYTHON) -m compileall .
	$(PYTHON) -O -m compileall .
.PHONY: all

clean:
	$(RM) *.py[co]
.PHONY: clean

install:
	mkdir -p $(DESTDIR)/$(PYTHON_SITEARCH)/qubes/
	cp $(ALL) $(DESTDIR)/$(PYTHON_SITEARCH)/qubes/
.PHONY: install
