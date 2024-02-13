# FastAPI Car Park
<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#running">Running</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The aim of this project is to fulfill author task. The task is about to create a simple API to manage car park system.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
This project built with these tools.
* [![Python][Python]][Python-url]
* [![Docker][Docker]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is how to run our program. Before we start our program we need to ensure we have done all of prerequisites.

### Prerequisites

* Docker (Docker version 24.0.2)

### Running

_After all prerequisites done, we need to look for the repository on author GitHub._

1. Here is link to [FastAPI Car Park](https://github.com/hahiho14/fastapi-car-park)
2. Clone the repo
   ```sh
   git clone https://github.com/hahiho14/fastapi-car-park.git
   ```
3. Ensure we have `.env` file under `fastapi-car-park` folder. Which look like this. It will exporting env variable to our container. 
   ```sh
   PARK_CAPACITY=5
   ACCESS_TOKEN_EXPIRE_MINUTES=5
   ```
4. After that, we need to run our `docker-compose.yaml` by running this command.
   ```docker
   docker compose up --build
   ```
5. Wait until the application running on our docker, and we can go to:
   ```
   http://0.0.0.0:8080
   ```
6. To see high level documentation, we can open swagger built in app by go to:
   ```
   http://localhost:8080/docs
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Authored by : Haris Prasetya Dharma Syahputra S

Phone/ WA   : 089523464687

[![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/hahiho14/fastapi-car-park](https://github.com/hahiho14/fastapi-car-park)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/haris-situmeang-290b26133/
[Python]: <img-link>
[Python-url]: https://docs.python.org/3/
[Docker]: <img-link>
[Docker-url]: https://docs.docker.com/