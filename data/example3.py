import boto3

client = boto3.client('route53')

response = client.create_hosted_zone(
    Name='hirocom.com',
    CallerReference='0416'
)

response = client.change_resource_record_sets(
    HostedZoneId = response['HostedZone']['Id'],
     ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'www.hirocom.com',
                    'Type': 'A',
                    'TTL':300,
                    'ResourceRecords': [
                        {
                            'Value': '198.51.100.234'
                        },
                    ],

                    }
            },
        ]
    }
)
