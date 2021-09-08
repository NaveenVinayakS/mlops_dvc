create env
''' bash
conda create -n mlops_wineq python=3.7 -y
'''

activate enviorment

'''bash
conda activate mlops_wineq
'''

create a req file

install the requirement
'''bash
pip install -r requirements.txt
'''

Download data from

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

git init

dvc init

data add data_given/winewuality.csv

git add .

git commit -m "first commit"

