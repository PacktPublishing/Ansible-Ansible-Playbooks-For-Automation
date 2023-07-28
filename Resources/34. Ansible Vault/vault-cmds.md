To Encrypt any Yaml File: 
    ansible-vault encrypt provisionEC2_Instance.yml
To run encrypted Playbooks:
    ansible-playbook provisionEC2_Instance.yml --ask-vault-password
Encrypt:
 ansible-vault encrypt aws_keys.yml
View:
    ansible-vault view aws_keys.yml
Edit:
    ansible-vault edit aws_keys.yml
rekey:
    ansible-vault rekey aws_keys.yml
decrypt:
    ansible-vault decrypt aws_keys.yml

