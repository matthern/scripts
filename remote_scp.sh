#!/bin/bash

#===========================================================================#
#   Script Name: remote_scp.sh												#
#        Author: m2m														#
#       Created: 30/03/2023													#
#       Purpose: This script uploads files to remote server.				#
#               															# 
#===========================================================================#

function upload {
     cd $FILEDIR
     su $LOCAL_USER -c "scp -v $FILENAME $REMOTE_USER@$REMOTE_SERVER:$REMOTEDIR" >> $LOGFILE 2>&1
     
     RET=$?
     if [ "$RET" = 0 ]; then
         echo "$FILEDIR/$FILENAME has been transferred to ANZ $REMOTE_SERVER:$REMOTEDIR" | tee -a $LOGFILE 2>&1
         echo "Moving $FILEDIR/$FILENAME to xlam archive directory" | tee -a $LOGFILE 2>&1
         mv $FILENAME $ARCHIVEDIR
     else
         echo "Transfer of $FILEDIR/$FILENAME FAILED on `date` $LOGFILE"
     fi
}


#---------------------------------------------------------------------------#
# MAIN section																#
#---------------------------------------------------------------------------#

FILEDIR=
FILENAME= 
LOGDATE=`date +%Y%m%d`
LOGFILE=/tmp/scp_$FILENAME.log.$LOGDATE
LOCAL_USER=
REMOTE_USER=
REMOTE_SERVER=
REMOTEDIR=
ARCHIVEDIR=
echo "Uploading $FILEDIR/$FILENAME to ANZ Live sftp server $REMOTE_SERVER..." | tee -a $LOGFILE 2>&1
upload
      
