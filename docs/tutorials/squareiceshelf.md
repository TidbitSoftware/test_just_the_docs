---
layout: default
title: 
parent: Tutorials
NOTE: This file was generated automatically by running bin/latex2jtd.py. To make changes, edit the corresponding <FILE>.tex file and commit the changes to the repository.
---
This is an example of velocity computation in steady state for a square ice shelf. First, launch MATLAB. In the left sidebar, select `ISSM_DIR` (the directory in which ISSM is stored) as your Current Directory. Then, navigate to `examples/SquareIceshelf`, which you can also do via the left sidebar or by running the following in the MATLAB Command Window:


````
>> cd examples/SquareIceShelf
````

You can create an empty model structure by running:


````
>> md=model;
````

Create a mesh of the domain outline with a resolution of 50,000 meters:


````
>> md=triangle(md,'DomainOutline.exp',50000);
````

Define the glacier system as an ice shelf (no island):


````
>> md=setmask(md,'all','');
````

Parameterize the model with the file `Square.par` (which you can see exists in the current directory by inspecting the left sidebar):


````
>> md=parameterize(md,'Square.par');
````

Define all elements as SSA:


````
>> md=setflowequation(md,'SSA','all');
````

Compute the velocity field of the ice shelf:


````
>> md=solve(md,'Stressbalance');
````

Finally, generate a plot of the velocity:


````
>> plotmodel(md,'data',md.results.StressbalanceSolution.Vel);
````


<div style="display:flow-root"><img style="float:left;width:100.00%" src="../../../images/issm/documentation/tutorials/squareiceshelf/squarevel.png" alt="Figure 1: squarevel"></div>