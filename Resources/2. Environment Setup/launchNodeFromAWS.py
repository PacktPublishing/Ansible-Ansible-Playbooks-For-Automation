import boto3
import os


awsRegion='us-east-2'
awsAccessKey='AKIAQD4EUQEZ2RJWDLPF'
awsSecretKey='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'

keyName='automation' #Dont give .pem as extention
pathForPem=r'C:\Users\VRTec\Documents'

ansibleNodes={
    'ansibleController': 
        { 'osName' : 'rhel', 'ami' : '' }, 
    'managerNode_1':
        { 'osName': 'rhel', 'ami' : '' },
    'managerNode_2': 
        { 'osName' : 'ubuntu' , 'ami': '' }
}




ec2Client = boto3.client('ec2',
            aws_access_key_id=awsAccessKey,
            aws_secret_access_key=awsSecretKey,
            region_name=awsRegion)

print('==============================')
print("Validting a key pair:")
pemFile=os.path.join(pathForPem,keyName)+'.pem'
try:
    ec2Client.describe_key_pairs( KeyNames=[ keyName ])
    if not os.path.exists(pemFile) :
        print('You already Created the Key Pair but dont find the pem file in {}'.format(pathForPem))
        print('Select new name for Key Pair or copy the {} to the location {} and retry'.format(keyName+'.pem',pathForPem))
        exit(1)
        print('=======================================================================================================')
    
except Exception as e: 
    print('Creating Key Pair for {}'.format(keyName))
    keypair = ec2Client.create_key_pair(KeyName=keyName)
    pf=open(pemFile,'w')
    pf.write(keypair['KeyMaterial'])
print("Your pem File to Connect with aws servers is: {}".format(pemFile))

    
