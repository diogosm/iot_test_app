
# Como Executar

## Premissas

Esse código assume que há um broker rodando em um determinado IP ou DNS e que ele roda numa máquina com conexão pouco intermitente. Não necessariamente precisa ser a mesma máquina do broker.

## Authors

- [@diogosm](https://www.github.com/diogosm)


## Executando

Rodando em background o código

```bash
  nohup python brokerListen2sendToFb.py &
```

Se precisar encerrar o código. Consulte ele funcionando com ```ps -aux```.

```bash
  kill $(pgrep -f 'brokerListen2sendToFb.py')
```

## Estrutura da base

Uma ideia seria seguir essa linha de estrutura

```
FirebaseRoot
| — — EndNode 1
      | — — Record 1 (TimestampColeta, pH, Temperatura, etc…)
      | — — Record 2 (TimestampColeta, pH, Temperatura, etc…)
      | — — …..
      | — — Record N (TimestampColeta, pH, Temperatura, etc…)
| — — EndNode 2
...
| — — EndNode N
```

## Código

O que precisa ter atenção e modificar nesse código é citado abaixo.

```python
broker = "127.0.0.1"  ## IP do broker ou DNS
port = 1883
```

```python
## Verificar o tópico e a estrutura do tópico no broker
client.subscribe("SENSOR_DATA/PH_VALUE") 
```

```python
## Alterar a URL do firebase e a estrutura
def send_to_firebase_server(msg):
    firebaseApp = firebase.FirebaseApplication('$URL_DO_FIREBASE', None)

    data = {'ph_value': msg.payload,
            'time_created': datetime.datetime.now()}
    result = firebaseApp.post('/SENSOR_DATA', data)
    print("Firebase post result: \n\t")
    print result
```
