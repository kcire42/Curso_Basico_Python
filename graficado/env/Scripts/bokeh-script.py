#!d:\documentos\python\curso_python_basico_platzi\ejercicios\graficado\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==2.2.3','console_scripts','bokeh'
__requires__ = 'bokeh==2.2.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==2.2.3', 'console_scripts', 'bokeh')()
    )
