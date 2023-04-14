---
Topic: "packages_not_in_requirements.txt Creator"
Author: "구FS"
---
<link href="./src/KFS/md_style.css" rel="stylesheet"></link>
<body>

# <p style="text-align: center">`packages_not_in_requirements.txt` Creator</p>
<br>
<br>

- [1. General](#1-general)

## 1. General

The name pretty much sums up what this program does. It creates a current requirements list with `pip freeze > requirements_current.temp`, subtracts all the (desired) requirements from `requirements.txt`, and saves the result in `packages_not_in_requirements.txt`. The unnecessary requirements can now be easily removed with `pip uninstall -y -r packages_not_in_requirements.txt` without reinstalling everything.


<div class="img_centre_30">
    <a href="https://www.paypal.com/paypalme/KooFelixSangmo">
        <img alt="Error: Could not load image source."
        src="https://i.pinimg.com/originals/60/fd/e8/60fde811b6be57094e0abc69d9c2622a.jpg"/>
    </a>
    <p class=img_caption>Click to buy me a beer!</p>
</div>
</body>