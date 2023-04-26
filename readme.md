---
Topic: "packages_not_in_requirements.txt Creator"
Author: "구FS"
---
<link href="./doc_templates/md_style.css" rel="stylesheet"></link>
<body>

# <p style="text-align: center">`packages_not_in_requirements.txt` Creator</p>
<br>
<br>

- [1. General](#1-general)

## 1. General

The name pretty much sums up what this program does. It creates a list of currently installed packages that are not listed in `requirements.txt` and saves the result in `packages_not_in_requirements.txt`. The unnecessary requirements can now be easily removed with `pip uninstall -y -r packages_not_in_requirements.txt`, otherwise you'd need to bruteforce this functionality by uninstalling everything and then reinstalling all desired packages from `requirements.txt`.

</body>