#!/bin/bash

OKTA_DOMAIN="vinetidev.okta.com"
API_TOKEN="007ImE9lyiIlUNnoz3DLG6GUy6WSL3tywbCkO7nDEB"

APPID=$(curl --silent GET \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: SSWS $API_TOKEN" \
"https://$OKTA_DOMAIN/api/v1/apps?q=barb-ui-cicd-pr1178" | jq -r '.[] | .id')

#echo $APPID

if [ -z "$APPID" ]; then
    echo "empty string"
else
    echo "https://vinetidev.okta.com/api/v1/apps/${APPID}/lifecycle/deactivate"
    echo "https://vinetidev.okta.com/api/v1/apps/${APPID}"
fi