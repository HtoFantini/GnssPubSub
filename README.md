# GPS

> Biblioteca genérica para utilizar GPS nos diversos projetos. Ele deve concentrar os diversos dispositivos GPSs de forma a padronizar o acesso a seus dados e disponibilização deles

## 📝 Notas de atualização do produto

* (19/02/2025) &#8594; Biblioteca inicial com device Neo6m

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Compatível com `<python 3.11.9>`
- Compatível com máquina `<Windows / Linux>`.

## ⚙️ Configurando e compilando <GPS>

Para instalar o <GPS>, siga estas etapas:

Linux e Windows (poetry):

```shell
poetry add git+https://github.com/HarpiaHarpyja/GpsPublisher.git@v0.1.0
```

Linux e Windows (pip):

```shell
pip install git+https://github.com/HarpiaHarpyja/GpsPublisher.git@v0.1.0
```

## ☕ Executando <GPS>

Para usar <GPS>, siga estas etapas:

```python
from typing import Dict, Any
from gpspublisher.application.application import Gps

# Seleciona o Device GPS e qual é a frequência de leitura em segundos
gps = Gps({"device": "Neo6M", "read_time": 1})

# Inicial o Device para leitura contínua
gps.start_gps_thread()

# Consulta o dado recente do gps
dict_gps: Dict[str, Any] = gps.get_gps()

# Finaliza o Device de leitura do gps
gps.stop_gps_thread()

```

Adicione comandos de execução e exemplos que você acha que os usuários acharão úteis. Forneça uma referência de opções para pontos de bônus!
