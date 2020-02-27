==========
energy-cli
==========

**energy-cli** is commad-line-interface to set and tune beamline `2bm <https://docs2bm.readthedocs.io>`_ mode changes between mono, pink and white beam

Installation
============

::

    $ git clone https://github.com/xray-imaging/2bm-ops.git
    $ cd 2bm-ops
    $ python setup.py install

in a prepared virtualenv or as root for system-wide installation.

.. warning:: If your python installation is in a location different from #!/usr/bin/env python please edit the first line of the bin/tomopy file to match yours.


Usage
=====

Set energy
----------

To set the beamline energy to 20 keV::

    $ energy set --energy-value 20 

to list of all available options::

    $ energy -h
      usage: energy [-h] [--config FILE] [--version]  ...

      optional arguments:
        -h, --help     show this help message and exit
        --config FILE  File name of configuration file
        --version      show program's version number and exit

    Commands:
  
      init         Create configuration file
      set          Set energy
      save         Associate the current beamline positions to an energy value
                   and save in a config file
      status       Show status



Configuration File
------------------

The beamline status is stored in **ops2bm.conf**. You can create a template with::

    $ energy init

**osp2bm.conf** is constantly updated to keep track of the last stored parameters, as initalized by **init** or modified by setting a new option value. For example to set the beamline to the last energy configuration ::

    $ energy set

to list of all **energy save** options::

    $ energy save -h
    
If the beamline has been manually optimized after setting a preset energy configuration, you can save the current beamline status in a custom config file with::  

    $ energy save --energy-value 27

The config file name is named **ops2bm_mono_27.0.conf**. You can restore the beamline positions for the optimized energy configuration with::

    $ energy set --config ops2bm_mono_27.0.conf


Testing mode
------------

In testing mode, the motor positions are printed but not actual motor motion occurs. To enable testing mode set:: 

    TESTING = True 

in `epics_move <https://github.com/xray-imaging/2bm-ops/blob/master/energy2bm/epics_move.py>`_ file, then re-install with::

    $ cd 2bm-ops
    $ python setup.py install

