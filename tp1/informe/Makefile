NOMBRE=informe
.PHONY: all clean

all: 
	pdflatex -interaction nonstopmode $(NOMBRE).tex
	pdflatex -interaction nonstopmode $(NOMBRE).tex
	pdflatex -interaction nonstopmode $(NOMBRE).tex

view:
	zathura -l error $(NOMBRE).pdf

open:
	make && make view

clean:
	rm -f $(NOMBRE).pdf *.aux *.log *.toc *.out *.bbl *.blg
