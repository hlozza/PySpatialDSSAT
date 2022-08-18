import os
import glob
import shutil
import subprocess
import configparser

def CSM(config, ucIx, ucName, ucCode):

    # Clean tmp dir
    tmpDir = os.path.abspath(config.get("PROC", "tmp_dir"))
    tmpFiles = glob.glob(os.path.join(tmpDir, '*OUT'))
    for f in tmpFiles:
        os.remove(f)

    # Remove experimental file in order to start with a clean one
    csmDir = os.path.abspath(config.get("PROC", "csm_dir"))
    xFile = os.path.join(csmDir, config.get("PROC", "x_file"))
    xtmpFile = os.path.join(tmpDir, config.get("PROC", "x_file"))
    os.remove(xtmpFile)
    shutil.copy(xFile, tmpDir)
        
    # Edit experiment file
    #read input file
    fin = open(xtmpFile, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace('SOIL__CODE', ucCode)
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(xtmpFile, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()

    # Execute DSSAT CSM
    currentDir = os.path.abspath(os.getcwd())
    os.chdir(tmpDir)
    execArg1 = config.get("PROC", "exec_arg_1")
    execArg2 = config.get("PROC", "exec_arg_2")
    execArg3 = config.get("PROC", "exec_arg_3")

    process = subprocess.Popen([execArg1, execArg2, execArg3], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()

    
    os.chdir(currentDir)

    print ("Output ", output)
    print ("Error ", error)
    if output is not None and b'STOP' in output:
        print ("Simulation ERROR")
        return 0
    elif error is not None and b'STOP' in error:
        print ("Simulation ERROR")
        return 0
    else:
        print ("OK")

    # COPY SUMMARY
    # create a new dir to store summaries from each UC 
    summaryDir = os.path.abspath(config.get("PROC", "summary_dir"))
    nameDir = os.path.join(summaryDir, str(ucIx))
    os.mkdir(nameDir)
    # Copy Summary.OUT to the new directory for each UC
    summaryFile = os.path.join(tmpDir, 'Summary.OUT')
    shutil.copy(summaryFile, nameDir)

    # Get value from summary file
    fin = open(summaryFile, "rt")
    #for each line in the input file
    nLine = 0
    hwSummary = []
    for line in fin:
        nLine = nLine + 1
        if nLine > 4:
            # For GNU/Linux users
            # hwSummary.append(line[213:220])
            # For Windows users
            hwSummary.append(line[158:164])
    #close input files
    fin.close()

    return hwSummary

