#Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
import KFS.log  #timeit
import logging  #standard logging
import os


@KFS.log.timeit
def main() -> None:
    packages_current: list[str]         #packages that the project actually has installed at the moment
    PACKAGES_CURRENT_FILENAME: str="packages_current.temp"
    packages_desired: list[str]         #packages that the project should have
    packages_too_many:  list[str]=[]    #{packages_current} \ {packages_desired}, the requirements that should be uninstalled
    PACKAGES_TOO_MANY_FILENAME: str="packages_not_in_requirements.txt"


    logging.info("Generating list of currently installed packages...")
    os.system(f"pip freeze > {PACKAGES_CURRENT_FILENAME}")                                                          #write packages current
    logging.info(f"\rGenerated list of currently installed packages, saved in \"{PACKAGES_CURRENT_FILENAME}\".")
    logging.info(f"Loading list of currently installed packages from \"{PACKAGES_CURRENT_FILENAME}\"...")
    with open(PACKAGES_CURRENT_FILENAME, "rt") as packages_current_file:                                            #load packages current
        packages_current=[package.strip("\n") for package in packages_current_file.readlines() if package!=""]      #filter out empty lines
    logging.info(f"\rLoaded list of currently installed packages from \"{PACKAGES_CURRENT_FILENAME}\".")
    logging.info(packages_current)
    logging.info(f"Deleting \"{PACKAGES_CURRENT_FILENAME}\"...")
    os.remove(PACKAGES_CURRENT_FILENAME)                                                                            #delete now unncessary temp file
    logging.info(f"\rDeleted \"{PACKAGES_CURRENT_FILENAME}\".")

    logging.info(f"Loading desired packages from \"requirements.txt\"...")
    with open("requirements.txt", "rt") as packages_desired_file:                                               #load packages desired
        packages_desired=[package.strip("\n") for package in packages_desired_file.readlines() if package!=""]  #filter out empty lines
    logging.info(f"\rLoaded desired packages from \"requirements.txt\".")
    logging.info(packages_desired)


    for package in packages_current:            #go through all currently installed packages
        if package not in packages_desired:     #if package not in the desired packages:
            packages_too_many.append(package)   #append to list to uninstall
    logging.info("Installed packages that are not in \"requirements.txt\":")
    logging.info(packages_too_many)
    

    logging.info(f"Saving packages that are not in \"requirements.txt\" in \"{PACKAGES_TOO_MANY_FILENAME}\"...")
    with open(PACKAGES_TOO_MANY_FILENAME, "wt") as packages_too_many_file:
        packages_too_many_file.write("\n".join(packages_too_many))
    logging.info(f"\rSaved packages that are not in \"requirements.txt\" in \"{PACKAGES_TOO_MANY_FILENAME}\".")

    return