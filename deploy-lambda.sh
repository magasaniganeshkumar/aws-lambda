# Change the directory
cd $CODEBUILD_SRC_DIR

# Loop all the first level folders
for dir in */; do
    echo "---------------------------------------"
    
    # zip the files
    zip_file_name="$(basename $dir)"
    zip_file_full_path=/tmp/$zip_file_name.zip
    echo "Step 1 --> Processing $zip_file_name"
    zip -r $zip_file_full_path $dir*
    
    # find the SHA
    new_sha=$(cat /tmp/$zip_file_name.zip |sha256sum |cut -d' ' -f1 |xxd -r -p |base64)
    echo "Step 2 --> New SHA --> $new_sha"
    
    # get lambda details
    lambda_name=$LAMDBA_NAME_PREFIX$zip_file_name
    lambda_details=$(aws lambda get-function --function-name $lambda_name)
    ret=$?


    # if lambda exists
    if [ $ret -eq 0 ]; then
        # get SHA
        existing_sha=$(echo $lambda_details | jq -r '.Configuration.CodeSha256')
        
        echo "Step 3 --> Existing SHA - $existing_sha"
    
        # compare SHA
        if [ "$new_sha" = "$existing_sha" ]; then
            echo "Step 4 --> Lambda is not updated as there is no change"
        else
            # deploy if the SHA is different
            echo "Step 4 --> Lambda is getting updated as SHA is changed"
            aws lambda update-function-code --function-name $lambda_name --zip-file fileb://$zip_file_full_path
        fi
    
    else
        echo "Error lambda not found --> $lambda_name"
    fi
    
    echo "---------------------------------------"
done