# Random Forest Tutorial with astronomical data 

This tutorial contains two jupyter notebooks in the `notebooks` directory:
- `random-forest-classification`
- `random-forest-regression`

Both of them demonstrate a simple application of the random forest
algorithm to relevant problems in astronomy, using the 
[scikit-learn](https://scikit-learn.org/stable/) machine learning
package for python.
<br>

The `DATA` directory contains a single text file with 6 entries 
for each of the $\sim 200\, 000$ central galaxies observed by
the Sloan Digital Sky Survey (SDSS). The structure of the file is explained in detail in the classification notebook.

<br>

The compiled data uses the following publically available
catalogues:
- star formation rate (SFR) and stellar mass ($M_\ast$) estimates from the [MPA-JHU release of spectrum measurements](https://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/)
- dark matter halo mass estimates from the [Yang Catalogue](https://gax.sjtu.edu.cn/data/Group.html)
- stellar velocity dispersions ($\sigma_{\rm disp}$) from the [NYU Value-Added Galaxy Catalogue](http://sdss.physics.nyu.edu/vagc/)
- the supermassive black hole masses ($M_{\rm BH}$) are estimated using the $M_{\rm BH}-\sigma_{\rm disp}$ relation in [Saglia et al. 2016](https://arxiv.org/abs/1601.00974)


<br>

I hope you enjoy the content of these two notebooks and, hopefully,
find them useful. If you have any questions, comments or requests,
please feel free to reach out to me directly!