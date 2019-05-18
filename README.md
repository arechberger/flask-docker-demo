# flask-docker-demo
A Small flask app to test out CI / CD workflow with CircleCI and Docker / Kubernetes.

## PYDAYS WORKSHOP 19
Started at the [Pydays 19  Workshop - Deploying Python with Docker, CircleCI, and Kubernetes](https://cfp.linuxwochen.at/de/LWW19/public/events/883)
- [Instructions from the workshop](https://docs.google.com/document/d/165PC4KFmLELeqVk7U2pxFcepcfKndXK2xjsEfqRTqio/edit#)
- all is done on local machine

Dockerhub repos generated:
- [rechberger/flask-docker-demo-small](https://hub.docker.com/r/arechberger/flask-docker-demo-small)
- [arechberger/flask-docker-demo](https://hub.docker.com/r/arechberger/flask-docker-demo)

## Deployment

Notes from testing out the deployment on Digital Ocean.
### Docker container only.
#### Droplet generation
- Create a Droplet: [Docker One-Click Droplet](https://cloud.digitalocean.com/marketplace/5ba19751fc53b8179c7a0071?i=1d65fb&referrer=droplets%2Fnew). 
- Choose the cheapest option available.
#### Droplet setup.
- ssh into the droplet
 ```bash
ssh root@<DROPLET_IP>
 ```

- generate ssh keypair. Will be used to allow access from circle-ci. We choose to create a new ssh keypair, instead of using an existing one (such as the one used to login to the droplet from our local machine).

From: https://circleci.com/docs/2.0/add-ssh-key/
>Note: Since CircleCI cannot decrypt SSH keys, every new key must have an empty passphrase. CircleCI also will not accept OpenSSH’s default file format - use ssh-keygen -m pem if you are using OpenSSH to generate your key.
```bash
ssh-keygen -b 4096 -t rsa -f ~/.ssh/id_rsa_deployment -C "deployment@circleci"
cat ~/.ssh/id_rsa_deployment.pub >> ~/.ssh/authorized_keys
```

add the `deploy_app.sh` script to the droplet and make it executable.
```bash
wget https://raw.githubusercontent.com/arechberger/flask-docker-demo/master/deploy_app.sh -O ~/deploy_app.sh
chmod +x ~/deploy_app.sh
```
#### Configure CircleCi
- add previously generated ssh key to circleci: https://circleci.com/docs/2.0/add-ssh-key/

