# Random Forest Tutorial with astronomical data 

This tutorial contains two jupyter notebooks in the `notebooks` directory:
- [`random-forest-classification`](https://nbviewer.jupyter.org/github/Dzoenapi/random-forest-in-SDSS/blob/main/notebooks/random-forest-classification.ipynb)
- [`random-forest-regression`](https://nbviewer.jupyter.org/github/Dzoenapi/random-forest-in-SDSS/blob/main/notebooks/random-forest-regression.ipynb)

Both of them demonstrate a simple application of the random forest
algorithm to relevant problems in astronomy, using the 
[scikit-learn](https://scikit-learn.org/stable/) machine learning
package for python. The classification notebook describes all steps in more detail and contains links to appropriate scikit-learn manuals.

<br>

The `DATA` directory contains a single text file with 6 entries 
for each of the  ~200 000 central galaxies observed by
the Sloan Digital Sky Survey (SDSS). The structure of the file is explained in detail in the classification notebook. <br>

The compiled data uses the following publically available
catalogues:
- star formation rate (SFR) and stellar mass (M<sub>*</sub>) estimates from the [MPA-JHU release of spectrum measurements](https://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/)
- dark matter halo mass estimates from the [Yang Catalogue](https://gax.sjtu.edu.cn/data/Group.html)
- stellar velocity dispersions (σ<sub>disp</sub>) from the [NYU Value-Added Galaxy Catalogue](http://sdss.physics.nyu.edu/vagc/)
- the supermassive black hole masses (M<sub>BH</sub>) are estimated using the M<sub>BH</sub>-σ<sub>disp</sub> relation in [Saglia et al. 2016](https://arxiv.org/abs/1601.00974)


<br>

Finally, the `scripts` directory contains a single script
`support_tools`, where my favourite `configure_plots` function
is defined.

<br>

I hope you enjoy the content of these two notebooks and, hopefully,
find them useful. If you have any questions, comments or requests,
please feel free to reach out to me directly!

<br>
*I would like to thank my supervisor* [*Asa Bluck*](https://www.kicc.cam.ac.uk/directory/dr-asa-bluck) *for introducing me to the joy of machine learning and inspiring this tutorial*
