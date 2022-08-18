import sys
import configparser
from spatialdssat import SpatialDSSAT

configFileName = "spatialdssat.config"

def main(argc, argv):
    if (argc > 1):
        print ("Use {0} ".format(sys.argv[0]))
        return 128

    # Configuarations
    config = configparser.ConfigParser()
    if len(config.read(configFileName)) == 0:
        print("Could not open configuration file: " + configFileName)
        return 128

    # Compute for each UC (Unidad Cartografica)
    SpatialDSSAT(config)

        
    return 0


if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
