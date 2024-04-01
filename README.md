# US-Visa-Approval-Prediction

conda create -n visa python=3,8 -y
condo activate visa 

git add .
git commit -m "added folders"
git push origin main 

git config --global user.name "John Doe"
git config --global user.email johndoe@example.com

git cofig --list 

pip install -r requirements.txt

to configur conda to git hub 
Open Git Bash.
Run the following command to add the Conda shell script to your .bashrc file:
Code
echo 'source ~/anaconda3/etc/profile.d/conda.sh' >> ~/.bashrc
Close and reopen Git Bash.
Activate your Conda environment by running the following command:
Code
conda activate <environment_name>

workflow 

1.constants 
2.config_entity 
3.artifact entity 
4.component  data engestion 
5.Pipeline 
6.app.py 

export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>