---
Topic: "packages_not_in_requirements.txt Creator"
Author: "구FS"
---
<link href="md_style.css" rel="stylesheet"></link>
<div id="global">

# <p style="text-align: center">`packages_not_in_requirements.txt` Creator</p>
<br>
<br>

The name pretty much sums up what this program does. It creates a current requirements list with `pip freeze > requirements_current.temp`, subtracts all the (desired) requirements from `requirements.txt`, and saves the result in `packages_not_in_requirements.txt`. The unnecessary requirements can now be easily removed with `pip uninstall -y -r packages_not_in_requirements.txt` without reinstalling everything.
</div>