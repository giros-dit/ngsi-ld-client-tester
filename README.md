# NGSI-LD client tester

Tester for the [`Python-based NGSI-LD API client`](https://github.com/giros-dit/python-ngsi-ld-client/tree/1.6.1) compliant with the [NGSI-LD API OpenAPI specification](https://forge.etsi.org/rep/cim/NGSI-LD/-/tree/1.6.1).

To deploy a docker-compose scenario with the [`Orion-LD`](https://github.com/FIWARE/context.Orion-LD) context broker (a reference implementation of NGSI-LD context broker compliant with the  NGSI-LD API specification by [ETSI GS CIM 009 V1.6.1](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.06.01_60/gs_CIM009v010601p.pdf)), execute the following command:
```bash
$ docker-compose up
```

In case you are interested in running the scenario in background, use the following command:
```bash
$ docker-compose up -d
```

Tear the scenario down as follows:
```bash
$ docker-compose down
```

> **Note:**
>
> In the `.env` file, environment variables are defined and parameterized (i.e., the context broker endpoint and the NGSI-LD context URL).

To validate the [`create_entity`](https://github.com/giros-dit/python-ngsi-ld-client/blob/1.6.1/docs/ContextInformationProvisionApi.md#create_entity) and [`retrieve_entity`](https://github.com/giros-dit/python-ngsi-ld-client/blob/1.6.1/docs/ContextInformationConsumptionApi.md#retrieve_entity) operations for a simple NGSI-LD Entity (e.g., NGSI-LD Entity of type Sensor available [here](sensor-tester/example/example-normalized.json)) follow these steps:
1. Download and install `poetry` by following the [official documentacion](https://python-poetry.org/docs/master/#installing-with-the-official-installer).
2. Make sure you have the right Python version for this project (Python>3.9 in this case):
     ```bash
    $ sudo apt-get install python3.9
    ```
3. Install `distutils` package for your specific Python release:
    ```bash
    $ sudo apt-get install python3-distutils
    ```
4. Install `python-is-python3` package (symlinks /usr/bin/python to Python3 as specified in [link 1](https://askubuntu.com/questions/1296790/python-is-python3-package-in-ubuntu-20-04-what-is-it-and-what-does-it-actually) and [link 2](https://stackoverflow.com/questions/61921940/running-poetry-fails-with-usr-bin-env-python-no-such-file-or-directory)):
    ```bash
    $ sudo apt-get install python-is-python3
    ```
5. Move to [`/sensor-tester`](sensor-tester/) folder:
    ```bash
    $ cd sensor-tester
    ```
6. Enable virtual environment for your specific Python release:
    ```bash
    $ poetry env use 3.9
    ```
7. Setup the virtual environment with poetry:
    ```bash
    $ poetry shell
    $ poetry install
    ```
    The virtual environment is now prepared and activated to be used.
8. To create a sample NGSI-LD Entity, run the [sensor-tester/create-sensor-entity.py](sensor-tester/create-sensor-entity.py) Python script as follow:
    ```bash
    $ python create-sensor-entity.py
    ```
9. To retrieve the previously NGSI-LD Entity, run the [sensor-tester/retrieve-sensor-entity.py](sensor-tester/retrieve-sensor-entity.py) Python script  as follow:
    ```bash
    $ python retrieve-sensor-entity.py
    ```

In addition, for validating example JSON-LD payloads (e.g., [`Sensor`](sensor-tester/example/example-normalized.json) example) against the autogenerated Python class bindings (e.g., `Sensor` Pydantic class available [here](https://github.com/giros-dit/python-ngsi-ld-client/blob/1.6.1/ngsi_ld_client/models/sensor.py)), run the [sensor-tester/tests/test_sensor.py](sensor-tester/tests/test_sensor.py) Python unit test from the `sensor-tester` folder as follows:
```bash
$ cd sensor-tester
$ python tests/test_sensor.py
```
