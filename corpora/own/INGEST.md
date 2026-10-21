# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 260 (the final check needs at least 200)
- Words: 298,259
- Estimated tokens (words times 1.4): 417,562 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `actinolite` | 267 | - | - | - |
| `adakite` | 488 | - | - | - |
| `aegirine` | 367 | - | - | - |
| `agate` | 2,899 | - | - | - |
| `albite` | 386 | - | - | - |
| `alkali_feldspar_granite` | 240 | - | - | - |
| `amethyst` | 1,712 | - | - | - |
| `ametrine` | 358 | - | - | - |
| `amphibole` | 1,127 | - | - | - |
| `amphibolite` | 952 | - | - | - |
| `analcime` | 794 | - | - | - |
| `andesine` | 273 | - | - | - |
| `andesite` | 1,566 | - | - | - |
| `anhydrite` | 651 | - | - | - |
| `ankerite` | 284 | - | - | - |
| `anorthite` | 284 | - | - | - |
| `anorthoclase` | 226 | - | - | - |
| `anorthosite` | 2,147 | - | - | - |
| `anthophyllite` | 506 | - | - | - |
| `anthracite` | 2,955 | - | - | - |
| `apatite` | 1,416 | - | - | - |
| `aphanite` | 148 | - | - | - |
| `aplite` | 296 | - | - | - |
| `appinite` | 3,125 | - | - | - |
| `aragonite` | 807 | - | - | - |
| `arfvedsonite` | 115 | - | - | - |
| `argillite` | 341 | - | - | - |
| `arkose` | 267 | - | - | - |
| `augite` | 328 | - | - | - |
| `banded_iron_formation` | 4,451 | - | - | - |
| `basalt` | 4,172 | - | - | - |
| `basaltic_andesite` | 400 | - | - | - |
| `basanite` | 451 | - | - | - |
| `bauxite` | 1,917 | - | - | - |
| `benmoreite` | 129 | - | - | - |
| `beryl` | 1,724 | - | - | - |
| `biotite` | 1,010 | - | - | - |
| `blairmorite` | 106 | - | - | - |
| `blueschist` | 764 | - | - | - |
| `boninite` | 533 | - | - | - |
| `borolanite` | 317 | - | - | - |
| `breccia` | 1,406 | - | - | - |
| `bronzite` | 431 | - | - | - |
| `bytownite` | 264 | - | - | - |
| `calcarenite` | 132 | - | - | - |
| `calcite` | 2,775 | - | - | - |
| `carbonatite` | 1,358 | - | - | - |
| `carnelian` | 614 | - | - | - |
| `cataclasite` | 544 | - | - | - |
| `chalcedony` | 1,154 | - | - | - |
| `chalcopyrite` | 1,601 | - | - | - |
| `chalk` | 1,493 | - | - | - |
| `charnockite` | 766 | - | - | - |
| `chert` | 2,798 | - | - | - |
| `chlorite_group` | 824 | - | - | - |
| `chromite` | 2,068 | - | - | - |
| `chrysoprase` | 308 | - | - | - |
| `citrine` | 836 | - | - | - |
| `coal` | 6,834 | - | - | - |
| `coesite` | 510 | - | - | - |
| `comendite` | 100 | - | - | - |
| `conglomerate_-geology` | 1,425 | - | - | - |
| `coquina` | 1,931 | - | - | - |
| `cordierite` | 555 | - | - | - |
| `corundum` | 1,135 | - | - | - |
| `cristobalite` | 797 | - | - | - |
| `cummingtonite` | 355 | - | - | - |
| `dacite` | 1,092 | - | - | - |
| `diabase` | 947 | - | - | - |
| `diamictite` | 247 | - | - | - |
| `diamond` | 9,566 | - | - | - |
| `diatomaceous_earth` | 2,676 | - | - | - |
| `diopside` | 647 | - | - | - |
| `diorite` | 1,004 | - | - | - |
| `dolomite_-mineral` | 960 | - | - | - |
| `dolomite_-rock` | 2,528 | - | - | - |
| `dunite` | 595 | - | - | - |
| `eclogite` | 752 | - | - | - |
| `enstatite` | 634 | - | - | - |
| `epidote` | 614 | - | - | - |
| `essexite` | 301 | - | - | - |
| `evaporite` | 1,345 | - | - | - |
| `feldspar` | 1,435 | - | - | - |
| `feldspathoid` | 201 | - | - | - |
| `felsite` | 181 | - | - | - |
| `flint` | 1,743 | - | - | - |
| `fluorite` | 2,703 | - | - | - |
| `forsterite` | 885 | - | - | - |
| `gabbro` | 1,637 | - | - | - |
| `ganister` | 429 | - | - | - |
| `garnet` | 2,939 | - | - | - |
| `gneiss` | 1,313 | - | - | - |
| `goethite` | 813 | - | - | - |
| `gossan` | 234 | - | - | - |
| `granite` | 4,668 | - | - | - |
| `granodiorite` | 620 | - | - | - |
| `granophyre` | 222 | - | - | - |
| `granulite` | 1,376 | - | - | - |
| `graphite` | 6,284 | - | - | - |
| `greenschist` | 830 | - | - | - |
| `greywacke` | 829 | - | - | - |
| `gritstone` | 178 | - | - | - |
| `gypsum` | 2,044 | - | - | - |
| `harzburgite` | 472 | - | - | - |
| `hauyne` | 939 | - | - | - |
| `hawaiite` | 365 | - | - | - |
| `heliotrope_-bloodstone` | 457 | - | - | - |
| `hematite` | 1,471 | - | - | - |
| `hornblende` | 523 | - | - | - |
| `hornfels` | 1,776 | - | - | - |
| `hyaloclastite` | 269 | - | - | - |
| `hypersthene` | 314 | - | - | - |
| `icelandite` | 154 | - | - | - |
| `ignimbrite` | 2,559 | - | - | - |
| `ijolite` | 195 | - | - | - |
| `illite` | 329 | - | - | - |
| `ilmenite` | 1,919 | - | - | - |
| `ironstone` | 359 | - | - | - |
| `itacolumite` | 397 | - | - | - |
| `jadeitite` | 124 | - | - | - |
| `jasper` | 1,075 | - | - | - |
| `jasperoid` | 455 | - | - | - |
| `kaolinite` | 3,216 | - | - | - |
| `kimberlite` | 2,460 | - | - | - |
| `komatiite` | 2,275 | - | - | - |
| `kyanite` | 1,002 | - | - | - |
| `labradorite` | 672 | - | - | - |
| `lamproite` | 783 | - | - | - |
| `lamprophyre` | 1,594 | - | - | - |
| `lapis_lazuli` | 1,604 | - | - | - |
| `larvikite` | 289 | - | - | - |
| `laterite` | 2,734 | - | - | - |
| `latite` | 143 | - | - | - |
| `leucite` | 303 | - | - | - |
| `leucitite` | 1,321 | - | - | - |
| `lherzolite` | 658 | - | - | - |
| `lignite` | 1,874 | - | - | - |
| `limestone` | 5,704 | - | - | - |
| `listwanite` | 397 | - | - | - |
| `litchfieldite` | 913 | - | - | - |
| `llanite` | 216 | - | - | - |
| `magnesite` | 1,446 | - | - | - |
| `magnetite` | 2,412 | - | - | - |
| `malachite` | 1,350 | - | - | - |
| `marble` | 1,881 | - | - | - |
| `marl` | 1,142 | - | - | - |
| `melilite` | 547 | - | - | - |
| `metaconglomerate` | 138 | - | - | - |
| `mica` | 3,855 | - | - | - |
| `microcline` | 329 | - | - | - |
| `migmatite` | 2,233 | - | - | - |
| `minette_-ore` | 457 | - | - | - |
| `moganite` | 330 | - | - | - |
| `monazite` | 1,513 | - | - | - |
| `monzogranite` | 390 | - | - | - |
| `monzonite` | 452 | - | - | - |
| `mudrock` | 2,965 | - | - | - |
| `mudstone` | 600 | - | - | - |
| `mugearite` | 176 | - | - | - |
| `muscovite` | 885 | - | - | - |
| `mylonite` | 757 | - | - | - |
| `napoleonite` | 585 | - | - | - |
| `nepheline` | 649 | - | - | - |
| `nepheline_syenite` | 1,741 | - | - | - |
| `nephelinite` | 468 | - | - | - |
| `norite` | 211 | - | - | - |
| `novaculite` | 372 | - | - | - |
| `obsidian` | 2,155 | - | - | - |
| `oil_shale` | 3,535 | - | - | - |
| `oligoclase` | 410 | - | - | - |
| `olivine` | 1,628 | - | - | - |
| `onyx` | 745 | - | - | - |
| `oolite` | 709 | - | - | - |
| `opal` | 2,635 | - | - | - |
| `orthoclase` | 446 | - | - | - |
| `pantellerite` | 148 | - | - | - |
| `pargasite` | 111 | - | - | - |
| `pegmatite` | 2,323 | - | - | - |
| `pelite` | 196 | - | - | - |
| `peridotite` | 3,182 | - | - | - |
| `phlogopite` | 481 | - | - | - |
| `phonolite` | 781 | - | - | - |
| `phosphorite` | 2,018 | - | - | - |
| `phyllite` | 295 | - | - | - |
| `picrite_basalt` | 442 | - | - | - |
| `pietersite` | 145 | - | - | - |
| `pigeonite` | 229 | - | - | - |
| `plagioclase` | 2,247 | - | - | - |
| `porphyry_-geology` | 1,872 | - | - | - |
| `pseudotachylyte` | 995 | - | - | - |
| `pumice` | 3,537 | - | - | - |
| `pyrite` | 2,579 | - | - | - |
| `pyrolite` | 641 | - | - | - |
| `pyrope` | 516 | - | - | - |
| `pyroxene` | 1,112 | - | - | - |
| `pyroxenite` | 781 | - | - | - |
| `quartz` | 2,269 | - | - | - |
| `quartz_monzonite` | 329 | - | - | - |
| `quartzite` | 1,404 | - | - | - |
| `quartzolite` | 252 | - | - | - |
| `rapakivi_granite` | 641 | - | - | - |
| `rhyodacite` | 284 | - | - | - |
| `rhyolite` | 1,246 | - | - | - |
| `riebeckite` | 391 | - | - | - |
| `rodingite` | 112 | - | - | - |
| `rutile` | 1,078 | - | - | - |
| `sandstone` | 2,666 | - | - | - |
| `sanidine` | 531 | - | - | - |
| `scapolite` | 1,375 | - | - | - |
| `schist` | 1,024 | - | - | - |
| `scoria` | 858 | - | - | - |
| `serpentinite` | 1,466 | - | - | - |
| `shale` | 1,640 | - | - | - |
| `shonkinite` | 271 | - | - | - |
| `shoshonite` | 373 | - | - | - |
| `siderite` | 792 | - | - | - |
| `sillimanite` | 230 | - | - | - |
| `siltstone` | 437 | - | - | - |
| `skarn` | 1,294 | - | - | - |
| `slate` | 1,900 | - | - | - |
| `smoky_quartz` | 301 | - | - | - |
| `soapstone` | 1,880 | - | - | - |
| `sodalite` | 1,207 | - | - | - |
| `spinel` | 701 | - | - | - |
| `stishovite` | 329 | - | - | - |
| `suevite` | 224 | - | - | - |
| `syenite` | 856 | - | - | - |
| `tachylite` | 1,170 | - | - | - |
| `taconite` | 1,029 | - | - | - |
| `talc` | 2,952 | - | - | - |
| `talc_carbonate` | 548 | - | - | - |
| `tectonite` | 254 | - | - | - |
| `teschenite` | 342 | - | - | - |
| `theralite` | 323 | - | - | - |
| `tiger-s_eye` | 477 | - | - | - |
| `till` | 1,672 | - | - | - |
| `titanite` | 526 | - | - | - |
| `tonalite` | 220 | - | - | - |
| `topaz` | 1,959 | - | - | - |
| `tourmaline` | 2,360 | - | - | - |
| `trachyandesite` | 423 | - | - | - |
| `trachybasalt` | 221 | - | - | - |
| `trachyte` | 1,373 | - | - | - |
| `travertine` | 2,455 | - | - | - |
| `tremolite` | 239 | - | - | - |
| `tridymite` | 553 | - | - | - |
| `troctolite` | 148 | - | - | - |
| `trondhjemite` | 195 | - | - | - |
| `tufa` | 835 | - | - | - |
| `tuff` | 2,790 | - | - | - |
| `turbidite` | 1,110 | - | - | - |
| `unakite` | 677 | - | - | - |
| `variolite` | 610 | - | - | - |
| `wackestone` | 198 | - | - | - |
| `wehrlite` | 183 | - | - | - |
| `whiteschist` | 384 | - | - | - |
| `wollastonite` | 1,180 | - | - | - |
| `zeolite` | 3,487 | - | - | - |
| `zircon` | 1,617 | - | - | - |
| `zoisite` | 255 | - | - | - |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
