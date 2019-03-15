# This scripts assumes:
# 1. There is a google cloud project id inm432 NB This is the id, not name - (change as required)
# 2. Storage billing has been enabled
# 3. Clusters API is enabled
# 4. This script runs from Google Cloud terminal

# set environment variable
export PROJECT_ID=inm432

# make sure it stuck
echo ${PROJECT_ID}

# set project
gcloud config set project inm432

# create bucket
gsutil mb -c regional -l europe-west1 -p ${PROJECT_ID} gs://${PROJECT_ID}

# clone project
git clone https://github.com/tweyde/Data-Science-City.git

# copy data to bucket
gsutil cp Data-Science-City/* gs://${PROJECT_ID}/

# create cluster
gcloud dataproc clusters create ${PROJECT_ID} --project=${PROJECT_ID} --worker-machine-type='n1-standard-2' --zone='europe-west1-b'

# create job
gcloud dataproc jobs submit pyspark gs://${PROJECT_ID}/sparkSubmitDemo.py --cluster=${PROJECT_ID} -- gs://${PROJECT_ID}/hamlet.txt

# delete cluster 
gcloud dataproc clusters delete ${PROJECT_ID} --quiet

# remove bucket contents
gsutil rm -r gs://${PROJECT_ID}/*

# remove bucket
gsutil rb gs://${PROJECT_ID}

# remove local data
rm -rf Data-Science-City

# week 08
# make bucket 
gsutil mb -c regional -l europe-west1 -p inm432 gs://inm432-week08

# download data
wget http://files.grouplens.org/datasets/movielens/ml-20m.zip

# decompress
unzip ml-20m.zip

# store in bucket - charges apply
gsutil cp -r ml-20m gs://inm432-week08/
