---
layout: default
title: Installation
NOTE: This file was generated automatically by running bin/latex2jtd.py. To make changes, edit the corresponding <FILE>.tex file and commit the changes to the repository.
---
# Installation

## Binaries
The easiest way to install ISSM is to download the
<a href="https://issm.jpl.nasa.gov/download/binaries/" target="_blank">pre-compiled binaries</a>. No need to compile the
code, just open the compressed file.

## Citations
Inversions where first introduced to glaciology by [<a href="#references">*MacAyeal1993a*</a>] for an SSA model, and extended since to 3D models for other model parameters.

Now, let's run our transient with historical mass balance! Use Jason Box's surface mass balance (SMB) time series as forcing [<a href="#references">*Box2013a,Box2013b,Box2013c*</a>].<sup>1</sup>

<sup>1</sup> <small>The year 1840-2012 Greenland near surface air temperature (T) and land ice SMB reconstruction after Box [2013] is calibrated to RACMO2 output [<a href="#references">*Meijgaard2008,Ettema2009,Broeke2009,Angelen2011*</a>]. The calibration for T and SMB components is based on the 53 year overlap period 1960-2012. The calibration for snow accumulation rate is shorter because ice core data availability drops after 1999. Calibration is made using linear regression coefficients for 5 km grid cells that match the average of the reconstruction to RACMO2. The RACMO2 data are resampled and reprojected from the native 0.1 deg (<img src="https://latex.codecogs.com/gif.latex?\sim" alt="Equation 1">10 km) grid to a 5 km grid better resolving areas where sharp gradients occur, especially near the ice margin where mass fluxes are largest. Several refinements are made to the Box [2013] temperature (T) and SMB reconstruction. Multiple station records now contribute to the near surface air temperature for each given year, month and grid cell in the domain while in Box [2013], data from the single highest correlating station yielded the reconstructed value. The estimation of values is made for a domain that includes land, sea, and ice. Box [2013] reconstructed T over only ice. A physically-based meltwater retention scheme [<a href="#references">*Pfeffer1990,Pfeffer1991*</a>] replaces the simpler approach used by Box [2013]. The RACMO2 data have a higher native resolution of 11 km as compared to the 24 km Polar MM5 data used by Box [2013] for air temperatures. The revised surface mass balance data end two years later in year 2012. The annual accumulation rates from ice cores are dispersed into a monthly temporal resolution by weighting the monthly fraction of the annual total for each grid cell in the domain evaluated using a 1960-2012 RACMO2 data.</small>

### Fonts
<small>Small text</small> x<sup>2</sup> H<sub>2</sub>O em dash&#8212; Line break<br>Some **bold** text Some *italic* text

### Equations


<div align="center"><img src="https://latex.codecogs.com/gif.latex?
S(\theta,\phi,t) = \frac{R}{M} \left[ \mathcal{G}(\alpha) \otimes L(\theta',\phi',t) \right] +\frac{1}{g} \sum_{m=0}^{2} \sum_{i=1}^{2} \Lambda_{2mi} (t) \mathcal{Y}_{2mi} (\theta,\phi) +\mathcal{E}(t)" alt="Equation 2"></div>
<div align="center"><img src="https://latex.codecogs.com/gif.latex?L(\theta,\phi,t) = \rho_I H(\theta,\phi,t) \mathcal{I}(\theta,\phi) + \rho_O S(\theta,\phi,t)
\mathcal{O}(\theta,\phi)" alt="Equation 3"></div>
<div align="center"><img src="https://latex.codecogs.com/gif.latex?
S(\theta,\phi,t) = \frac{R}{M} \left[ \mathcal{G}(\alpha) \otimes L(\theta',\phi',t) \right] +\frac{1}{g} \sum_{m=0}^{2} \sum_{i=1}^{2} \Lambda_{2mi} (t) \mathcal{Y}_{2mi} (\theta,\phi) +\mathcal{E}(t)" alt="Equation 4"></div>
<div align="center"><img src="https://latex.codecogs.com/gif.latex?S(\theta,\phi,t) = \frac{R}{M} \left[ \mathcal{G}(\alpha) \otimes L(\theta',\phi',t) \right] + \frac{1}{g} \sum_{m=0}^{2} \sum_{i=1}^{2} \Lambda_{2mi} (t) \mathcal{Y}_{2mi} (\theta,\phi) + \mathcal{E}(t)" alt="Equation 5"></div>

### Inline Equations

where <img src="https://latex.codecogs.com/gif.latex?y" alt="Equation 14"> is a generic variable, <img src="https://latex.codecogs.com/gif.latex?t" alt="Equation 13"> indicates the model time step, <img src="https://latex.codecogs.com/gif.latex?\overline{y}_{t}" alt="Equation 12"> is the deterministic component of <img src="https://latex.codecogs.com/gif.latex?y_{t}" alt="Equation 11">, and <img src="https://latex.codecogs.com/gif.latex?\epsilon_{y,t}" alt="Equation 10"> is the stochastic perturbation applied at <img src="https://latex.codecogs.com/gif.latex?t" alt="Equation 9"> to <img src="https://latex.codecogs.com/gif.latex?y" alt="Equation 8">. The distribution of <img src="https://latex.codecogs.com/gif.latex?\epsilon_{y}" alt="Equation 7"> at any time step is Normal with a variance <img src="https://latex.codecogs.com/gif.latex?\sigma^{2}_{y}" alt="Equation 6">.


<div align="center"><img src="https://latex.codecogs.com/gif.latex? \label{eq2}
\boldsymbol{\epsilon}_{t} \sim N(\boldsymbol{0},\Sigma)" alt="Equation 15"></div>
where <img src="https://latex.codecogs.com/gif.latex?\Sigma" alt="Equation 19"> is the covariance matrix, and the bold font denotes vectors. If only the diagonal terms of <img src="https://latex.codecogs.com/gif.latex?\Sigma" alt="Equation 18"> are non-zero, all the individual entries of <img src="https://latex.codecogs.com/gif.latex?\boldsymbol{\epsilon}_{t}" alt="Equation 17"> are independent of each other. Covariance between the entries can be applied by adjusting the off-diagonal terms of <img src="https://latex.codecogs.com/gif.latex?\Sigma" alt="Equation 16">.

### vspace

Some text followed by vspace
<div style="height:3cm"></div>
Some text following vspace


### Code folds

Some text followed by a opening code fold 
some text in the middle
closing code fold


### Figures

Standard figure

<div style="display:flow-root"><img style="float:left;width:100.00%" src="../../../images/issm/documentation/tutorials/uncertaintyquantification/SamplingResults.png" alt="Figure 1: SamplingResults"></div>
Figure containing two figures

<div style="display:flow-root"><img style="float:left;width:50.00%" src="../../../images/issm/documentation/tutorials/uncertaintyquantification/PlotSensitivities.png" alt="Figure 2: PlotSensitivities"><img style="float:left;width:50.00%" src="../../../images/issm/documentation/tutorials/uncertaintyquantification/ImportanceFactors.png" alt="Figure 2: ImportanceFactors"></div>
Figure with caption

<div style="display:flow-root"><img style="float:left;width:100.00%" src="../../../images/issm/documentation/picop/picop.png" alt="Figure 3: picop"></div><span style="display:block;width:100%;text-align:center"><small>Melt calculation in PICOP, adapted from [<a href="#references">*Pelle2019*</a>].</small></span>
Another figure with a different caption

<div style="display:flow-root"><img style="float:left;width:100.00%" src="../../../images/issm/documentation/picop/picop.png" alt="Figure 4: picop"></div><span style="display:block;width:100%;text-align:center"><small>A great new caption</small></span>

### Test nested substitutions
Some text with `%nested substitutions` but here we have a literal percent 

### .bashrc

- Open `/c/msys64/home/<user>/.bashrc` for editing and add the following at the bottom of the file, 


````
## MATLAB
#
MATLAB_VER="<MATLAB_VER>" # Allows for easy resetting of MATLAB version added to path
export MATLAB_PATH=$(cygpath -u $(cygpath -ms "/c/Program Files/MATLAB/${MATLAB_VER}"))
export PATH="${MATLAB_PATH}/bin:${PATH}"

## ISSM
#
export ISSM_DIR=<ISSM_DIR>
export ISSM_DIR_WIN=$(cygpath -ms "${ISSM_DIR}") # Needed by MATLAB
````
where `<MATLAB_VER>` is the version of MATLAB that you have installed (for example, "R2023b")
and `<ISSM_DIR>` is the path to your local copy of the ISSM source code repository (for example, `/c/Users/<USER>/ISSM`, where &#60;USER&#62; is your username)
- Another item
  - Nested list item
  - Another nested list item


````
Another code block that follows a nested list
with different content but following text contains a new line
````
this is the following text preceded and followed by a new line
## Microsoft MPI

- Navigate to <a href="https://docs.microsoft.com/en-us/message-passing-interface/microsoft-mpi-release-notes" target="_blank">https://docs.microsoft.com/en-us/message-passing-interface/microsoft-mpi-release-notes</a>
- Click the link for 'Microsoft Download Center' that corresponds with the latest release (take note of the version number that you download for the next step; it can also be found by going to 'Settings' / 'Apps & Features')
- Click the 'Download' button
  1. Redistributions of source code must retain the above copyright notice,
		this list of conditions and the following disclaimer.
  1. Redistributions in binary form must reproduce the above copyright
			notice, this list of conditions and the following disclaimer in the
			documentation and/or other materials provided with the distribution.
    - Ordered list item 1
    - Ordered list item 2
    - Ordered list item 3
  1. Neither the name of the California Institute of Technology (Caltech),
			its operating division the Jet Propulsion Laboratory (JPL), the National
			Aeronautics and Space Administration (NASA), nor the names of its
			contributors may be used to endorse or promote products derived from
			this software without specific prior written permission.
- Make sure both boxes are checked, then click the 'Next' button
- Click the 'Save File' button for each file
- When the download completes, run each installer
- Follow the prompts, using the default installation directories
## Source Code
If you would like to install ISSM from source, you will need to download the source code first. The
source code of ISSM is available on <a href="https://github.com/ISSMteam/ISSM" target="_blank">GitHub</a>. It can be
downloaded via https with,


````
git clone https://github.com/ISSMteam/ISSM.git
````
or `ssh` with,


````
git clone git@github.com:ISSMteam/ISSM.git
````
This will download the latest version of ISSM from the repository into the current local directory (or to the location of your choosing by passing a path as an optional argument to the command). 

If you downloaded the source code, you need to compile and install ISSM. Compilation of the ISSM
source code is theoretically possible on any platform. It has been successfully carried out on
Linux, macOS, and Windows. Here are some instructions to compile and install ISSM from the source
code:

<!--DATASETS LIST START-->


- A list item without any other markup
- <a href="https://issm.jpl.nasa.gov/download/unix" target="_blank">Linux/Mac</a>
- <a href="https://issm.jpl.nasa.gov/download/windows" target="_blank">Windows</a> (under development)
- A list item without any other markup
- <a href="https://issm.jpl.nasa.gov/download/autodiff" target="_blank">Installation with AD capability</a> (under development)
- <a href="https://issm.jpl.nasa.gov/download/se" target="_blank">Installation with Solid Earth capability</a> (under development)
- A list item without any other markup

<!--DATASETS LIST END-->

Compilation is a more involved process, which is not recommended for beginners or casual users.

## License
ISSM is released under a <a href="https://opensource.org/license/bsd-3-clause" target="_blank">BSD Three Clause License</a>.

Copyright (c) 2008-2024, California Institute of Technology.
All rights reserved. Based on Government Sponsored Research under contracts NAS7-1407 and/or NAS7-03001.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:


1. Redistributions of source code must retain the above copyright notice,
		this list of conditions and the following disclaimer.
1. Redistributions in binary form must reproduce the above copyright
		notice, this list of conditions and the following disclaimer in the
		documentation and/or other materials provided with the distribution.
1. Neither the name of the California Institute of Technology (Caltech),
		its operating division the Jet Propulsion Laboratory (JPL), the National
		Aeronautics and Space Administration (NASA), nor the names of its
		contributors may be used to endorse or promote products derived from
		this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE CALIFORNIA INSTITUTE OF TECHNOLOGY BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## References
- J. E. Box, N. Cressie, D. H. Bromwich, J.-H. Jung, M. van den Broeke, J. H. van
   Angelen, R. R. Forster, C. Miege, E. Mosley-Thompson, B. Vinther, and J. R.
   McConnell.
 Greenland Ice Sheet Mass Balance Reconstruction. Part
   I: Net Snow Accumulation (1600-2009).
 J. Clim., 26(11):3919-3934, JUN 2013.

- Jason E. Box.
 Greenland Ice Sheet Mass Balance Reconstruction. Part
   II: Surface Mass Balance (1840-2010).
 J. Clim., 26(18):6974-6989, SEP 2013.

- Jason E. Box and William Colgan.
 Greenland Ice Sheet Mass Balance Reconstruction. Part
   III: Marine Ice Loss and Total Mass Balance (1840-2010).
 J. Clim., 26(18):6990-7002, SEP 2013.

- J. Ettema, M. R. van den Broeke, E. van Meijgaard, W. J. van de Berg, J. L.
   Bamber, J. E. Box, and R. C. Bales.
 Higher surface mass balance of the Greenland Ice Sheet revealed
   by high-resolution climate modeling.
 Geophys. Res. Lett., 36:1-5, JUN 16 2009.

- D. R. MacAyeal.
 A tutorial on the use of control methods in ice-sheet modeling.
 J. Glaciol., 39(131):91-98, 1993.

- T. Pelle, M. Morlighem, and J. H. Bondzio.
 Brief communication: PICOP, a new ocean melt parameterization under
   ice shelves combining PICO and a plume model.
 Cryosphere, 13(3):1043-1049, 2019.

- W. T. Pfeffer, T. H. Illangasekare, and M. F. Meier.
 Analysis and modeling of melt-water refreezing in dry snow.
 J. Glaciol., 36(123):238-246, 1990.

- W. T. Pfeffer, M. F. Meier, and T. H. Illangasekare.
 Retention of Greenland Runoff by Refreezing: Implications
   for Projected Future Sea-Level Rise.
 J. Geophys. Res. - Oceans, 96(C12):22117-22124, DEC 15 1991.

- J. H. van Angelen, M. R. van den Broeke, and W. J. van de Berg.
 Momentum budget of the atmospheric boundary layer over the
   Greenland ice sheet and its surrounding seas.
 J. Geophys. Res. - Atmospheres, 116:1-14, MAY 18 2011.

- Michiel van den Broeke, Jonathan Bamber, Janneke Ettema, Eric Rignot, Ernst
   Schrama, Willem Jan van de Berg, Erik van Meijgaard, Isabella Velicogna, and
   Bert Wouters.
 Partitioning Recent Greenland Mass Loss.
 Science, 326(5955):984-986, NOV 13 2009.

- E. van Meijgaard, L. H. van Ulft, W. J. Van de Berg, F. C. Bosvelt, B. J. J. M.
   Van den Hurk, G. Lenderink, and A. P. Siebesma.
 The KNMI regional atmospheric model RACMO version 2.1, Technical
   Report 302.
 Technical report, KNMI, De Bilt, The Netherlands, 2008.

