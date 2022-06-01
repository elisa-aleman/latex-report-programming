# XeLaTeX programming report template

I made a template (don't really read the document) to be able to write programming reports with code snippets in grey backgrounds and colored keywords in Japanese.

A lot of it was hard work so I left this template here to start faster next time.

- lststyle-css.sty
- lststyle-html.sty

Were created with the help of this code in Stack Exchange:

https://tex.stackexchange.com/questions/99500/listings-code-style-for-html5-css-html-javascript

For the details on:

- latexcompile.sh
- my_latexdiff.sh
- recursive_clean_latex_secondary_files.sh
- argparse.bash

Refer to:

https://github.com/elisa-aleman/latex_helpers

The python code to make a color palette was useful and might use in future reports, since seaborn.palplot does not connect to an existing ax, as seen here:

https://stackoverflow.com/questions/50516094/add-seaborn-palplot-axes-to-existing-figure-for-visualisation-of-different-color