# This scripts assumes:
# 1. There is a google cloud project called inm432 (change as required)
# 2. Storage billing has been enabled
# 3. Clusters API is enabled

# set project
gcloud config set project inm432

# set environment variable
export PROJECT_ID=inm432

# make sure it stuck
echo ${PROJECT_ID}

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
