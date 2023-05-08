This is the code for my final project of PHYS 5070 at CU Boulder

To run the code you first modify the parameters.json and sim_box.json files. 
Parameters contains information about the initial wavefunction, type of potential
and values for the potentials, and propagation scheme. Sim_box controls the size 
of the simulation box as well as the number of time steps. 

After that you run the Main.py which runs the simulation and saves the wavefunction
as an Nt X Nx array. From here you can either run ShowPsi.py to plot the wavefunction
at a particular time during the simulation, or to create plots in general. You can also
run AnimateWave.py to make a video of the entire simulation. The frames paramter controls
how many time slices Nt to animate in the simulation. 

There are also a multitude of helper files to make the Main.py file not crowded. 
For example Gird, Plot, Propagator, Psi etc. The archive file contains the original 
Crank Nicholson 3-pont and 5-point propagators before I consolidated them into Propagator.py.
There is also the images file which is where plots of the wavefunction made by ShowPsi.py are sent.
Finally there is the psi_files folder which is where the wavefunction is saved after the simulation
is complete.

This project uses the Second Order in time Crank-Nicholson scheme to propagate the 
wavefunction forward in time, and uses a 5-point Fourth Order finite difference 
stencil to discretize the Hamiltonian. 

The full discretized Crank-Nicholson Equation can be found in the appendices of my slides,
as well as additional info on where the Crank-Nicholson Equation comes from. 
