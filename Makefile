INPUT=poster
OUTPUT=output
VIEWER=evince

all: build view

.PHONY: build view clean

build:
	mkdir -p $(OUTPUT)
	pdflatex -shell-escape -output-directory=$(OUTPUT) $(INPUT).tex

view:
	$(VIEWER) output/$(INPUT).pdf

clean:
	rm -rf $(OUTPUT)/*
