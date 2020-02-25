# Pre-Workshop Directions

### Point your browser to `https://bit.ly/2TiJexR`

To participate in the hands-on lessons one will need:

- An account on Adroit, Perseus, Della or Tiger. If you do not have an account then complete [this form](https://forms.rc.princeton.edu/registration/?q=adroit) to get an account on Adroit.
- A laptop with sufficient battery power and the ability to connect to the eduroam wireless network.
- The ability to Duo authenticate.

## Using Applications with GUIs on the HPC Clusters

In addition to Jupyter and RStudio, this workshop will show participants how to use the PyCharm debugger and DDT. Run the test below to see if your laptop is available to use GUIs on the cluster. If the directions below fail for you then you can still use the command-line tools and watch the demos. You could also try using TurboVNC as discussed at the bottom of this page.

### Linux

Linux comes with a built-in X server. Try running these commands:

```bash
$ ssh -Y <YourNetID>@adroit.princeton.edu
$ module load ddt/20.0.1
$ ddt
# if the DDT GUI appears then you can do the hands-on GUI exercises
```

### Mac

Install [XQuartz](https://www.xquartz.org/) on your laptop. If you already have it installed then make sure that you have the latest version by opening XQuartz and choosing "XQuartz" in the menu then "Check for X11 Updates ...".

With XQuartz running, run the following commands in a terminal (`/Applications/Utilities/Terminal`):

```bash
$ ssh -Y <YourNetID>@adroit.princeton.edu
$ module load ddt/20.0.1
$ ddt
# if the DDT GUI appears then you can do the hands-on GUI exercises
```

### Windows

Try using [MobaXterm](https://mobaxterm.mobatek.net/) (Home Edition). Visit the [OIT Tech Store](https://princeton.service-now.com/snap?id=kb_article&sys_id=ea2a27064f9ca20018ddd48e5210c771) for resolving issues with installing and configuring this software.

## TurboVNC

If the directions above fail and you have an acount on Tiger, Della or Perseus, then consider installing [TurboVNC](https://researchcomputing.princeton.edu/faq/how-do-i-use-vnc-on-tigre). In this case your goal is to use graphical applications on tigressdata. Visit the [OIT Tech Store](https://princeton.service-now.com/snap?id=kb_article&sys_id=ea2a27064f9ca20018ddd48e5210c771) for resolving issues with installing and configuring this software.

```bash
$ ssh -Y <YourNetID>@tigressdata.princeton.edu
# start a terminal by clicking on the small black square icon in the menu
$ eog
# if a window appears then you can do the hands-on GUI exercises
```

## Clone the Repo on Adroit

For Linux and Mac users:

```bash
$ ssh -X adroit
$ cd /scratch/network/<YourNetID>    # or /scratch/gpfs on Perseus, Della, Tiger
$ git clone https://github.com/PrincetonUniversity/intro_debugging
$ module load anaconda3
```

Windows users should connect using MobaXterm (Home Edition) or WSL.
