# How to compile

```bash
jupyter nbconvert --to latex --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_input_tags="hide_input" "question on utility.ipynb"
pdflatex "question on utility.tex"
```