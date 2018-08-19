#!/usr/bin/env bash

# Quick script for backing up all Route53 records in all zones with optional copying to an S3 bucket.
# The aws cli needs to be configured to use an API key with read access to Route53 and the ability to write to S3 (optional)
# Be sure to update the AWS_CLI_PROFILE, BACKUP_DIR AND BACKUP_BUCKET variables accordingly
# Script also assumes you already have aws cli and jq installed

# Restoring the zone files take a little editing of each file - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html


set -e

# Dump route 53 zones to a text file and upload to S3.
AWS_CLI_PROFILE=eureka-terraform
BACKUP_DIR=/Users/kevinmcgarry/dns-backup
BACKUP_BUCKET=eureka-aws-billing

# Use full paths for cron
CLIPATH="/usr/local/bin"

# Function to dump all zones to individual files and upload to s3
function backup_all_zones () {
  local zones
  # Enumerate all zones
  # will update to use native cli filters/jmespath 
  zones=$($CLIPATH/aws route53 list-hosted-zones --profile $AWS_CLI_PROFILE | jq -r '.HostedZones[].Id' | sed "s/\/hostedzone\///")
  for zone in $zones; do
  echo "Backing up zone $zone"
  $CLIPATH/aws route53 list-resource-record-sets --hosted-zone-id $zone > $BACKUP_DIR/$zone.json
  done

  # Upload backups to s3
  # $CLIPATH/aws s3 cp $BACKUP_DIR s3://$BACKUP_BUCKET --recursive --sse
}

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Backup up everything and output the amount of time it took to complete
time backup_all_zones