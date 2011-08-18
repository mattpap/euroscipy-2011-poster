INPUT=poster
OUTPUT=output

all:
	mkdir -p $(OUTPUT)
	pdflatex -shell-escape -output-directory=$(OUTPUT) $(INPUT).tex

.PHONY: view clean

view:
	evince output/$(INPUT).pdf

clean:
	rm -rf $(OUTPUT)/*
