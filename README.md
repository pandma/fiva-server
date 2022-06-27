
<h1 align="center">Fiva Server Side</h1>
 

<h2 align="center">Description</h2>

Fiva is an Electricity optimization software that we are currently developing.
This software takes all the registers a maximeter makes in a year and return the optimal power you should hire for hecah period from p1 to p6,
also saving the most amount of electricity and money.


 
 
<h2 align="center"> API Endpoints</h2>

 
<div align="center">
 
| METHOD  |             URL              |       DESCRIPTION                   |
| ------  | :--------------------------: | ----------------:                   |
| POST    |api/register                  | register new users                  |
| POST    |api/login                     | login users                         |
| GET     |api/user                      | gets user info by JWT               |
| POST    |api/logout                    | Log out users                       |
| GET     |api/companies                 | gets elcetric companies             |
| POST    |api/companies                 | adds elcetric companies             |
| PUT     |api/companies                 | updates elcetric companies          |
| GET     |api/les50                     | gets meximeters lower than 50KW     |
| POST    |api/les50                     | adds meximeters lower than 50KW     |
| PUT     |api/les50                     | updates meximeters lower than 50KW  |
| GET     |api/max50                     | gets meximeters lower than 150KW    |
| POST    |api/max50                     | adds meximeters lower than 150KW    |
| PUT     |api/max50                     | updates meximeters lower than 150KW |


</div>


## How to satart


Run env\Scripts\Activate in the command line to start the virtual environment, it should look something like:
<br/>
(env) PS C:\Users\pablo\documents\work\fiva>
<br/>
then pip install if you don't have pip installed also pip install django and finally
<br/>
python manage.py migrate and python manage.py runserver.


## Models

### 3.0 Model


{
    <br/>
    owner = models.CharField(max_length=100)
    <br/>
    direction = models.CharField(max_length=100)
    <br/>
    postalcode = models.CharField(max_length=100)
    <br/>
    cups = models.CharField(max_length=100)
    <br/>
    nif = models.CharField(max_length=100)
    <br/>
    anualConsumption = models.CharField(max_length=100, blank=True)
    <br/>
    annualSavings = models.CharField(max_length=100, blank=True)
    <br/>
    recomendedPower = models.CharField(max_length=100, blank=True)
    <br/>
}


## Body payload

### Post api/3.0/ 

{
    "owner":"pablo",
    "direction":"calle la barca",
    "postalcode":"19005",
    "cups":"3434",
    "nif":"234503F"

}

### Put api/3.0/:id


{
    "anualConsumption":"",
    "annualSavings":"",
    "recomendedPower":""
}


### Post api/companies/


{
    "name":"iberdrola",
    "p1":"23",
    "p2":"23",
    "p3":"2",
    "p4":"23",
    "p5":"12",
    "p6":"23"
}