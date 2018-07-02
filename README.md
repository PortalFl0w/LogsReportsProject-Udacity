# Logs Analysis - Udacity

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You will need to install/download the following prior to running this software:

* Python2
* Virtual Box
* Vagrant
* Logs Database

### Installing

Download the database here:
[LogsDatabase](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Then extract the database into the root folder of this project (this is wherever you saved this project on your local machine).

Run your vagrant machine using the Vagrantfile provided with the project. This process can take a while.

```
vagrant up
```

Inside of the virtual machine navigate to

```
cd /vagrant
```

Once there, run the following command to add the SQL database to your virtual machine:

```
psql -d news -f newsdata.sql
```

Once the database is installed, run the folloing command to produce a report:

```
python report.py
```

That's it! Once the program appears to be finished, check the log.txt file.

## Built With

* [Python2](http://www.dropwizard.io/1.0.2/docs/) - Programming Language Used
* [PostgreSQL](https://maven.apache.org/) - Database Language

## Authors

* **Mateusz Lipski** - *Initial work* - [PortalFl0w](https://github.com/PortalFl0w)
