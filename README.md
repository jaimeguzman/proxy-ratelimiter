# Proxy Flask + Prometheus + Grafana + Rate Limiter


## Running Dockers 

```shell
docker-compose build

docker-compose up
```


## Experiment with Proxy Rate Limit 
```shell
cd proxy-ratelimit

#Start 
virtualenv venv
#For activate virtual enviroment
source venv/bin/activate

#install dependencies
pip install -r requeriment.txt

#for deactivate
deactivate

```

## Further documentation

Must Read docs folder with more examples



## Cleaning up

Para limpiar todo

```shell
docker-compose down -v --rmi all
```
