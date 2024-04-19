"""
-----------------------------------------------------------------------------------------
py-echo
-----------------------------------------------------------------------------------------
A Python package to provide tools for an easy handling echo images in DICOM format built 
on top of pydicom, NumPy, MatPlotLib and Open-CV.

#### Version: 0.0.3

### Author:
Alejandro Alcaine, Ph.D\\
CoMBA research group\\
MESC Working Group on e-Cardiology\\
MESC European Association of Cardiovascular Imaging (EACVI)\\
lalcaine@usj.es

Faculty of Health Sciences\\
University San Jorge\\
Villanueva de Gállego (Zaragoza)\\
Spain

### Acknowledgments:
This package was possible partially thanks to the Departamento de Ciencia, Universidad y 
Sociedad del Conocimiento, from the Gobierno de Aragón (Spain) (Research Group T71\_23D). 
Also thanks to Project PID2022-139143OA-I00 funded by MICIU/AEI/10.13039/501100011033 and 
by ERDF/EU. 

### Citation:
If you use this package in your research, please cite as:

D. Chaparro-Victoria et. al. "Automatic Segmentation of the Inferior Vena Cava from M-mode 
Ultrasound Images". Proceedings of Computing in Cardiology 2024.

"""

__version__ = "0.0.3"

from pyecho.echo_io import read_echo