import sys
import subprocess
import pkg_resources

install_requires = {'numpy', 'pandas', 'datasets'}
existing_packages = {pkg.key for pkg in pkg_resources.working_set}
missing_packages = install_requires - existing_packages

if missing_packages:
    print("The following packages are missing and will be installed:\n{packs}".format(packs = missing_packages))
    try:    
        subprocess.check_call([sys.executable, '-m', 'pip'+sys.version_info[0], 'install', *missing_packages], stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("subprocess.CalledProcessError: installation went wrong.") 
    except OSError:
        print("OSError: command not found.") 
    else:
        print("Installation was successful")