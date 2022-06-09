# Election Application
## made for Vidhya Niketan Public School

#### Packages Required
- `firebase-admin`
- `pyqt5`
- `pyqt5-tools`
- `pillow` (use `pip install PIL`)

Kindly use `pip` for installing the above modules

### Prerequisites
Apart from installing the modules, kindly ensure that the following files are inside the project.

Inside `offlineApplication`, there will be 8 folders for all eight posts. Apart from that, lookout for the following files too:

- `data.json` (used to store all voting data)
- `FontsFree-Net-SFProDisplay-Heavy-1.ttf` (Font family for the application)
- `README.md` (The one you are reading right now)
- `results.py` (used to view and save results)
- `setup.py` (used to create candidate spaces inside `data.json`)

Also, inside the folders, look out for the following files and folders:

- `Logo_VNPS.png` (Our school logo)
- `main.py` (the main program)
- `\maleCandidate` and `\femaleCandidate` folders (exception for SwachBarathCoord, which only has `\personCandidate`)
- `picturesetup.py` (inside both the folders)

### Setting Up

Kindly follow the below steps for setting up the Election Environment

- Use `setup.py` to enter number of candidates for each post and their names respectively. This will create a voting container for every candidate in `data.json` 
- A voting container looks like `"maleASPL": {"candidate1": {"name": "candidatename1", "votes": 0}}`
- Open the post folders. Use `maleCandidate/picturesetup.py` to assign images. This program will once again ask the number of candidates, and photos MUST BE selected in the same order as earlier at `setup.py`. 
- This program will fetch the image, resize it to a square of dimensions `369x369` and also curves the edges.
- Now that setup process is over, you can run `main.py` inside post folders to start voting.

### Things to remember

- While using `setup.py`, kindly be cautious. Modifying of data would result in entering the whole candidate data again
- In `picturesetup.py`, kindly select photos in the same order as entered in `setup.py`
- Suggest the candidate to prodive a square photograph, inorder to avoid distortion at `picturesetup.py`
- Install `FontsFree-Net-SFProDisplay-Heavy-1.ttf` font (not mandatory)

### Contact 

Email: akashthelezend@gmail.com

Phone: +91 9943803882