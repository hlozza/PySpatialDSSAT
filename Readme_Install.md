# Instalación de PySpatialDSSAT

Pasos para ejecutar el script PySpatialDSSAT en Python3.

## Windows 10

### Instalar Python3

Descargar Python3 desde

[python.org](https://www.python.org/downloads/windows/)

Por ejemplo, se puede optar por la opción "Latest Python 3 Release" o "Python 3.9". Luego, cliquear sobre "Windows installer". Elegir la opción 32bit o 64bit según corresponda al OS instalado en la computadora. 

### Instalar Miniconda3

Descargar Miniconda3 desde 

[Miniconda3](https://docs.conda.io/en/latest/miniconda.html#windows-installers)

Por ejemplo, se puede optar por la opción "Windows installers" y elegir la versión de Python 3.9. Luego, cliquear sobre "Miniconda3 Windows". Elegir la opción 32bit o 64bit según corresponda al OS instalado en la computadora.

Miniconda 3 incluye el gestor de paquetes y un Python. Posiblemente, podría salterase el primer paso...

### Crear ambiente

Luego de instalar Miniconda3 se crea un ambiente en el que se instalan todos los paquetes necesarios y en sus versiones específicas de manera que no tengan conflictos con otras versiones instaladas.

Escribir Miniconda3 en la barra para buscar aplicaciones de Windows. Elegir la opción para lanzar la aplicación dentro de una terminal. Ejecutar

`conda create -n pygdal39 python=3.9`

 para crear el ambiente `pygdal39` para python 3.9. Luego, se debe activar el ambiente
 
`conda activate pygdal39`
 
 y se puede comenzar a instalar paquetes requerdios. Por ejemplo,
 
`conda install -c conda-forge gdal`
 
 Para más información, ver

[How To Install GDAL for Python with Anaconda](https://opensourceoptions.com/blog/how-to-install-gdal-with-anaconda/)
 
### Para finalizar

Para finalizar, hay que desactivar el ambiente ejecutando

`conda deactivate`

## PySpatialDSSAT

El archivo PySpatialDSSAT contiene un script para Python3. Luego de descomprimirlo en la ubicación deseada, se debe copiar el ejecutable de DSSAT. Típicamente,

`copy C:\DSSAT47\DSCSM047.EXE path_to\PySpatialDSSAT\CSM`

o con una herramienta gráfica como el "Explorador de Windows".

Para más información, ver

[DSSAT.net](https://dssat.net/) y [dssat-csm-os](https://github.com/DSSAT/dssat-csm-os).


### Ejecución

Para ejecutar el script PySpatialDSSAT debemos hacerlo desde el ambiente creado previamente. Es decir, debemos estar desde una terminal de Miniconda3 y tener el ambiente pygdal39 activado como vimos en las secciones anteriores. Típicamente, deberemos cambiar al directorio correspondiente

`cd C:\path_to\PySpatialDSSAT\CSM`

y ya podemos ejecutar

`python main.py`

Para correr nuevamente el script se debe vaciar previamente la carpeta `path_to\PySpatialDSSAT\Output\Summary`.

### Ejecución aislada de DSSAT

Es posible correr el ejecutable de DSSAT dentro de la carpeta tmp para ejecutar pruebas aisaldas

```
cd C:\path_to\PySpatialDSSAT\tmp
DSCSM047.EXE B DSSBatch.v47
```

La carpeta CSM no es un lugar adecuado para correr DSSAT dado que tiene los archivos de referencia y necesita ediciones adicionales. Por ejemplo, el archivo exerimental tiene un suelo indefinido *SOIL_CODE*. 
 

 ## GNU/Linux

Aqui el comando `python` hace referencia a `python3`. Primero creo el ambiente virtual. Lo activo, actualizo los paquetes e instalo otros requerimientos como GDAL.

*.Creo el venv

    mkdir SD-venv
    python -m venv SD-venv/
    cd SD-venv/

*.Activo el ambiente y actualizo versiones

    source bin/activate
    python -m pip install --upgrade pip
    python -m pip install --upgrade wheel
    python -m pip install --upgrade setuptools

*.Instalo requerimientos. Chequeo versión de GDAL para instalar un paquete compatible con los headers

    gdalinfo --version
    python -m pip install configparser
    python -m pip install numpy
    python3 -m pip install gdal==3.4 --no-cache-dir

*.Copio el script y lo ejecuto

    cd SD-venv/
    cp -ir ../PySpatialDSSAT/ ./
    cd PySpatialDSSAT/
    python main.py

*.Fianlizo

    deactivate


### Ejecución

Una vez creado el ambiente virtual, para ejecutar el script sólo hay que realizar

    cd SD-venv/
    source bin/activate
    cd PySpatialDSSAT/
    python main.py
    deactivate

