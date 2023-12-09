FILENAME=$1

aws s3 mv $FILENAME s3://gac-financial/data-provider/files/historical-series/pending/$FILENAME > ./.logs/$FILENAME.txt