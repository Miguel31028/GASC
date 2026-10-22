# Geração do relatório de análise

Scripts que geram `Docs/Relatorio_Analise_Sistema_GASC.docx` a partir do modelo `Docs/Modelo_Relatorio_Estagio_Doc.docx`.

Pré-requisitos: Python 3 com `python-docx` e `Pillow`, LibreOffice (`soffice`) e Poppler (`pdftotext`, `pdfinfo`).

```bash
# 1. (opcional) regenerar os diagramas PlantUML
cd Docs/diagramas && java -jar plantuml.jar -tpng *.puml

# 2. (opcional) regenerar os mockups
cd Docs/mockups && npm install && node gerar.mjs

# 3. gerar o relatório (duas passagens: a segunda preenche os números de página dos índices)
python3 Docs/fonte_relatorio/build.py Docs/Modelo_Relatorio_Estagio_Doc.docx \
    Docs/diagramas Docs/mockups Docs/Relatorio_Analise_Sistema_GASC.docx
```

| Ficheiro | Conteúdo |
|---|---|
| `lib.py` | Motor de construção sobre o modelo (secções, títulos, legendas, tabelas, índices). |
| `front.py` | Capa, resumo, abstract, glossário e siglas. |
| `cap1_2.py` … `cap6_9.py`, `cap_mockups.py` | Conteúdo de cada capítulo, bibliografia e anexos. |
