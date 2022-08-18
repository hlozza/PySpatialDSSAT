import sys
import os
import glob
import shutil
import configparser
from osgeo import gdal
from osgeo import osr
from osgeo import ogr
from csm import CSM

def SpatialDSSAT(config):


    # UC SHAPEFILE
    # Read shp and get geom features
    resourcesDir = os.path.abspath(config.get("PROC", "resources_dir"))
    ucShapefile = os.path.join(resourcesDir, config.get("PROC", "uc_shapefile"))

    shpDriver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = shpDriver.Open(ucShapefile, 0) # 0 means read-only. 1 means writeable.

    # Check to see if shapefile is found.
    if dataSource is None:
        print ('Could not open %s' % (ucShapefile))
        exit

    print ('Opened %s' % (ucShapefile))
    layer = dataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print ("Number of features in %s: %d" % (os.path.basename(ucShapefile),featureCount))

    # MEMORY VECTOR    
    # Reference System
    srs = osr.SpatialReference()
    srs.SetWellKnownGeogCS("EPSG:4326")

    # CREATE in memory VECTOR
    memDriver = ogr.GetDriverByName('MEMORY')
    memSource = memDriver.CreateDataSource('memData')
    memLyr = memSource.CreateLayer( 'uc', srs=srs, geom_type=ogr.wkbPolygon)

    # ADD a set of yield FIELD
    yieldField = ogr.FieldDefn("yield_1", ogr.OFTReal)
    memLyr.CreateField(yieldField)


    # ADD an identification FIELD
    ixField = ogr.FieldDefn("ix", ogr.OFTInteger)
    memLyr.CreateField(ixField)

    # Copy Name and Codigo field
    nameField = ogr.FieldDefn("Name", ogr.OFTString)
    nameField.SetWidth(254)
    memLyr.CreateField(nameField)
    codigoField = ogr.FieldDefn("Codigo", ogr.OFTString)
    nameField.SetWidth(10)
    memLyr.CreateField(codigoField)

    # Prepare tmp dir
    csmDir = os.path.abspath(config.get("PROC", "csm_dir"))
    csmFiles = glob.glob(os.path.join(csmDir, '*'))
    tmpDir = os.path.abspath(config.get("PROC", "tmp_dir"))
    for f in csmFiles:
        shutil.copy(f, tmpDir)

    # for feature in layer:
    for ftIx in range(0, layer.GetFeatureCount()):
    # Get the input Feature
        feature = layer.GetFeature(ftIx)
        geom = feature.GetGeometryRef()
        ftName = feature.GetFieldAsString("Name")
        print ("Name : %s" %(ftName))
        ftCodigo = feature.GetFieldAsString("Codigo")

        if not ftCodigo:
            continue

        csmValue = CSM(config, ftIx, ftName, ftCodigo)

        feat = ogr.Feature( memLyr.GetLayerDefn() )
        feat.SetGeometryDirectly( ogr.CreateGeometryFromWkt(geom.ExportToWkt()) )
        feat.SetField("yield_1", float(csmValue[0]))
        feat.SetField("ix", ftIx)
        feat.SetField("Name", ftName)
        feat.SetField("Codigo", ftCodigo)
        memLyr.CreateFeature( feat )
        feat = None

    # layer.ResetReading()

    #create an output datasource in shapefile
    outputDir = os.path.abspath(config.get("PROC", "output_dir"))
    outShapefile = os.path.join(outputDir, config.get("PROC", "out_shapefile"))
    outDriver = ogr.GetDriverByName('ESRI Shapefile')
    outSource = outDriver.CreateDataSource(outShapefile)
    #copy a layer to output
    outSource.CopyLayer(memLyr, 'uc')
    outSource = None
    outDriver = None
    
    memLyr = None
    memSource = None

    layer = None
    dataSource = None



