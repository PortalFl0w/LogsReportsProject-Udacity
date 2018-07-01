# Logs Analysis - Udacity

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You will need to install the following prior to running this software:

* Python2
* Virtual Box
* Vagrant

### Installing

Run your vagrant machine using the Vagrantfile provided with the project.

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

That's it!

## Built With

* [Python2](http://www.dropwizard.io/1.0.2/docs/) - Programming Language Used
* [PostgreSQL](https://maven.apache.org/) - Database Language

## Authors

* **Mateusz Lipski** - *Initial work* - [PortalFl0w](https://github.com/PortalFl0w)
