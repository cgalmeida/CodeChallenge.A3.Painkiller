# Painkiller Software Engineer Challenge
<!--ts-->
   * [Part 1: Backend](#backend)
      * [About](#about)
      * [Archtecture](#archtecture)
      * [API Documentation](#API-Documentation)
      * [How to run?](#how-to-run)
      * [Further steps](#further-steps)
   * [Part 2: Unit Testing](#unit-testing)
      * [About](#implementation)
      * [How to run?](#test-run)
   * [Part 3: Machine Learning](#unit-testing)
      * [Architecture Discussion (not implemented)](#implementation)
<!--te-->
## Backend
### About
 Painkiller is REST FastAPI with the following endpoints:
* ```POST /api/v1/patient```: Receive a new patient's data (name, age, medical conditions, etc.) in JSON format, store it in a database, and return the patient object with an assigned ID.

* `GET /api/v1/patient/<patient_id>`: Returns the data of the patient corresponding to the `patient_id`.

* `POST /api/v1/patient/<patient_id>/measurements`: Receives and stores health measurements (e.g., temperature, blood pressure) for the patient corresponding to the patient_id.

The API also provides the following endpoints for CRUD operations: 

* Patients:
* `POST /api/v1/patient/list`: Return list with data of all patient
* `POST /api/v1/patient/delete/<patient_id>`: Deletes the data of the patient corresponding to the patient_id.

* Measurements:
* `POST /api/v1/measurements/list`: Return list with data of all measures
* `POST /api/v1/measurements/delete/<patient_id>`: Deletes the data of the measures corresponding to the measures_id.

```
🚩For more details and payload examples, please check the api doc at:

    /api/v1/patient/docs
    /api/v1/measurements/docs
```
### Archtecture 
![alt text](./doc/Diagrama%20sem%20nome.drawio.png?raw=true)
#### Decisões de projeto e arquitetura TODO
* Arquitetura baseada em microsserviços
* Para manter a performance de escala horizontal as seguintes decisões foram feitas:
  * Para que o processo de escala possa ser configurado a nível de microsserviço, os processos estão conteinerizados (com docker)
  * Todos os microsserviços trabalham de forma stateless
* DB e PAC:
  * consistencia eventual
* Resiliencia e self-healing:
consistencia eventual
* Autenticação: OpenID
* NginX: proxy reverse

## How to run
 - Make sure you have installed `docker` and `docker-compose`
 - Run `docker-compose up -d`
 <!-- - Head over to http://localhost:8080/api/v1/movies/docs for movie service docs 
   and http://localhost:8080/api/v1/casts/docs for cast service docs -->

```bash
docker-compose run --user 1000 app sh -c 'alembic upgrade head'
docker-compose run --user 1000 measurement_service sh -c 'alembic upgrade head'

docker-compose run app sh -c "pytest -W ignore::DeprecationWarning"

```
# Unit Testing
## Implementation
1. **Unit Testing:** The unit tests for this application were built using the tdd methodology, using `pytest`. An postgressql service was configured as db test instance for test isolation.

## Test Run
Tests for each service can be run with the following command:

```
docker-compose run <container_service_name> sh -c "pytest -W ignore::DeprecationWarning"

```

Example for measurement_service:

```
docker-compose run measurement_service sh -c "pytest -W ignore::DeprecationWarning"

```

<!--
2. **Microservices:** Divide the application into at least two microservices: one for managing patients and another for managing measurements.
-->

<!--

## Evaluation

You will be evaluated on:

- Code quality: Easy to understand, clean, and well-structured.
- Adherence to requirements: All requirements must be met.
- Documentation: Clear documentation of how to install, configure, and run the application.
- Testing: The application should have adequate test coverage, including unit tests.
- Solution architecture: How the different parts of the application work together.


Please include in the repository:

- All source code.
- A README.md file with detailed instructions on how to install, configure, and run the application.
- Any other documentation you find necessary.
-->

# Part 3: Machine Learning (Optional) - (Bonus)

## Architecture Discussion (not implemented)

1. **Machine Learning Model:** <!-- -Implement a simple Machine Learning model in the application that utilizes the measurement data to predict whether a patient has a high risk of some health problem (for example, based on fluctuations in blood pressure). Use OpenAI's API and its models for this task.-->

2. **Model Implementation:**  <!-- -Demonstrate how you would implement and maintain this model in a production environment.-->

3. **Model Monitoring:** <!-- - Show how you would monitor and optimize this Machine Learning model to ensure its performance and scalability.-->

![alt text](./doc/Diagrama%20sem%20nome.drawio.png?raw=true)