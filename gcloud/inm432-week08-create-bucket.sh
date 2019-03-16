# week 08

# set project - change project id as applicable
gcloud config set project inm432

# make bucket
gsutil mb -c regional -l europe-west1 -p inm432 gs://inm432-week08

# download data
wget http://files.grouplens.org/datasets/movielens/ml-20m.zip

# decompress
unzip ml-20m.zip

# store in bucket - charges apply
gsutil cp -r ml-20m gs://inm432-week08/
