<div id="top"></div>

# Police-Cross-District-Enforcement-System

<!-- TABLE OF CONTENTS -->
## Table of Contents
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
        <li><a href="#installation">Installation</a></li>
      </ul>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<p align="justify">This project is created for the Integrated Design Project (IDP 2021) for Mechatronic Courses. The title choose is based on the Covid-19 themes which it believed that can help most of the people during Covid-19 pandemic. This project will uses raspberry pi which 2 webcamera and 1 pi camera. The system itself is divided into two types of accounts which is officer and citizen account. Citizen account allow the citizen to apply cross-district permission through webbased system. It will needed an approval from the police which will be approved by the officer and the office. At the roadblock, the officer can uses either manual scan or Optical Character Recognition (OCR) to allow the system read the car plate at the roadblock which reduce the process of inspection at the police roadblock during movement control order (MCO).</p>

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This project uses several frameworks and libraries to ensure the system works!

* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Django](https://djangoprojects.com)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

The system will be running through Django which it required Django. Therefore, python and Django need to be installed first. 


### Prerequisites

Several required libraries need to install in the requirements files.
* requirments.txt files
  ```sh
  pip install -r requirements.txt (Python 2)
  ```
  or 
  ```sh
  pip install -r pip3 install -r requirements.txt (Python 3)
  ```

### Installation

_For the installation, it required the user to install all the required files including django. Then, the user need to configure the system._

1. Create new project at the Django by enter the command 
   ```js
   django-admin startproject police
   ```    
2. Copy the repo files in the newproject files

3. Create migrations files before running migration
   ```js
   ./manage.py makemiggrations
   ```
4. Migration
   ```js
   ./manage.py migrate
   ```
   
4. Run the server
   ```sh
   ./manage.py runserver 0:8000
   ```
<p align="right">(<a href="#top">back to top</a>)</p>
