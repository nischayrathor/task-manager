## task-manager

#### Running Application
'''
pip3 install -r requirements.txt
python3 main.py
'''

#### Building container images
'''
docker-compose --env-file .env build
docker-compose --env-file .env up app --force-recreate
'''
