# Painkiller Software Engineer Challenge

## About

### Decisões de projeto e arquitetura
* Arquitetura baseada em microsserviços
* Para manter a performance de escala horizontal as seguintes decisões foram feitas:
  * Para que o processo de escala possa ser configurado a nível de microsserviço, os processos estão conteinerizados (com docker)
  * Todos os microsserviços trabalham de forma stateless
* DB e PAC:
  * consistencia eventual
* Resiliencia e self-healing:
consistencia eventual

```bash
docker-compose run --user 1000 app sh -c 'alembic upgrade head'

docker-compose run app sh -c "pytest -W ignore::DeprecationWarning"

```

<!-- This test is designed to assess the technical skills of the candidate for the Senior Software Engineer role in areas such as backend development, DevOps, and Machine Learning. -->

## Melhorias 

<!-- For this test, we would like you to create a system that could be used in a hospital to monitor patient conditions. We have provided a sample CSV file (`patients.csv`) containing patient data that you can use to test your application. -->

### Part 1: Backend

<!-- 1. **API:** Develop a REST API using FastAPI with the following endpoints: 
    - `POST /api/v1/patient`: Should receive a new patient's data (name, age, medical conditions, etc.) in JSON format, store it in a database, and return the patient object with an assigned ID.
    - `GET /api/v1/patient/<patient_id>`: Should return the data of the patient corresponding to the `patient_id`.
    - `POST /api/v1/patient/<patient_id>/measurements`: Should receive and store health measurements (e.g., temperature, blood pressure) for the patient corresponding to the `patient_id`.

2. **Microservices:** Divide the application into at least two microservices: one for managing patients and another for managing measurements.

3. **Database:** Implement CRUD operations in a database of your choice to manage the data of the patients and their measurements.

### Part 2: Unit Testing

1. **Unit Testing:** Write unit tests for your application to validate its functionality and robustness.

### Part 3: Machine Learning (Optional) - (Bonus)

1. **Machine Learning Model:** Implement a simple Machine Learning model in the application that utilizes the measurement data to predict whether a patient has a high risk of some health problem (for example, based on fluctuations in blood pressure). Use OpenAI's API and its models for this task.

2. **Model Implementation:** Demonstrate how you would implement and maintain this model in a production environment.

3. **Model Monitoring:** Show how you would monitor and optimize this Machine Learning model to ensure its performance and scalability.

## Evaluation

You will be evaluated on:

- Code quality: Easy to understand, clean, and well-structured.
- Adherence to requirements: All requirements must be met.
- Documentation: Clear documentation of how to install, configure, and run the application.
- Testing: The application should have adequate test coverage, including unit tests.
- Solution architecture: How the different parts of the application work together.

## Delivery

Deliver on Gupy.

Please include in the repository:

- All source code.
- A README.md file with detailed instructions on how to install, configure, and run the application.
- Any other documentation you find necessary.

Good luck!

---

# Sample CSV File

The `patients.csv` file contains patient data that can be used to test your application. It has the following format:

```
patient_id,first_name,last_name,age,condition
1,John,Doe,55,Healthy
2,Jane,Smith,30,Healthy
3,James,Brown,50,High blood pressure
...
```

Each line represents a patient, with the following fields:

- `patient_id`: Patient ID (unique)
- `first_name`: Patient's first name
- `last_name`: Patient's last name
- `age`: Patient's age
- `condition`: Patient's health condition -->

## How to run??
 - Make sure you have installed `docker` and `docker-compose`
 - Run `docker-compose up -d`
 <!-- - Head over to http://localhost:8080/api/v1/movies/docs for movie service docs 
   and http://localhost:8080/api/v1/casts/docs for cast service docs -->

