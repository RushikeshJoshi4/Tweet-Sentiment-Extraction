# Tweet-Sentiment-Extraction
273P project

## Data:
Download from kaggle website and paste the csv files into the tweet-sentiment-extraction folder.

## To make the bert notebook work:
Go to https://huggingface.co/roberta-base
Download these the files (using curl or something equivalent) and paste them into input folder - 
  
config.json
merges.txt
pytorch_model.bin
vocab.json
  
If using curl:  
curl -o pytorch_model.bin https://cdn-lfs.huggingface.co/roberta-base/278b7a95739c4392fae9b818bb5343dde20be1b89318f37a6d939e1e1b9e461b   
curl -o merges.txt https://huggingface.co/roberta-base/resolve/main/merges.txt  
curl -o config.json https://huggingface.co/roberta-base/resolve/main/config.json  
curl -o vocab.json https://huggingface.co/roberta-base/resolve/main/vocab.json  
  
Make sure their names are of the form - config.json and not roberta-config.json or something like that. Just rename if so.

