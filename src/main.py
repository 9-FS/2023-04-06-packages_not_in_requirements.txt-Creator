#Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
import KFS.log  #timeit
import logging  #standard logging
import os


@KFS.log.timeit
def main() -> None:
    packages_too_many:  list[str]=[]    #{requirements_current} \ {requirements}, the requirements that should be uninstalled
    PACKAGES_TOO_MANY_FILENAME: str="packages_not_in_requirements.txt"
    REQUIREMENTS_CURRENT_FILENAME: str="requirements_current.temp"
    requirements_current: list[str]     #requirements that the project actually has at the moment
    requirements_desired: list[str]     #requirements that the project should have


    logging.info("Generating current requirements...")
    os.system(f"pip freeze > {REQUIREMENTS_CURRENT_FILENAME}")                                                                      #write requirements current
    logging.info(f"\rGenerated current requirements, saved in \"{REQUIREMENTS_CURRENT_FILENAME}\".")
    logging.info(f"Loading current requirements from \"{REQUIREMENTS_CURRENT_FILENAME}\"...")
    with open(REQUIREMENTS_CURRENT_FILENAME, "rt") as requirements_current_file:                                                    #load requirements current
        requirements_current=[requirement.strip("\n") for requirement in requirements_current_file.readlines() if requirement!=""]  #filter out empty lines
    logging.info(f"\rLoaded current requirements from \"{REQUIREMENTS_CURRENT_FILENAME}\".")
    logging.debug(requirements_current)
    logging.info(f"Removing \"{REQUIREMENTS_CURRENT_FILENAME}\"...")
    os.remove(REQUIREMENTS_CURRENT_FILENAME)                                                                                        #removing now unncessary temp file
    logging.info(f"\rRemoved \"{REQUIREMENTS_CURRENT_FILENAME}\".")

    logging.info(f"Loading desired requirements from \"requirements.txt\"...")
    with open("requirements.txt", "rt", encoding="utf-16-le") as requirements_desired_file: #generated requirements.txt has sussy encoding                                                         #load requirements desired
        requirements_desired=[requirement.strip("\n") for requirement in requirements_desired_file.readlines() if requirement!=""]  #filter out empty lines
    if 1<=len(requirements_desired):
        requirements_desired[0]=requirements_desired[0][1:] #cut off BOM
    logging.info(f"\rLoaded desired requirements from \"requirements.txt\".")
    logging.debug(requirements_desired)


    for requirement in requirements_current:            #go through all current requirements
        if requirement not in requirements_desired:     #if requirement not in the desired requirements:
            packages_too_many.append(requirement)       #append to list to uninstall
    logging.info("Installed packages, that are not in \"requirements.txt\":")
    logging.info(packages_too_many)
    

    logging.info(f"Saving packages not in \"requirements.txt\" in \"{PACKAGES_TOO_MANY_FILENAME}\"...")
    with open(PACKAGES_TOO_MANY_FILENAME, "wt") as requirements_too_many_file:
        requirements_too_many_file.write("\n".join(packages_too_many))
    logging.info(f"\rSaved packages not in \"requirements.txt\" in \"{PACKAGES_TOO_MANY_FILENAME}\".")

    return