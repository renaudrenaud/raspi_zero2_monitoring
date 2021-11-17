# raspi_zero2_monitoring

A project to show how to manage computer monitoring with the little Raspberry Pi Zero 2.

## Tools

For this funny project we want to use:
* python3
* Postgresql
* Grafana


## Postgres Install & Config

Installation is done with the following command:

```sudo apt install postgresql```

When done, it's possible to start PG using:

```sudo pg_ctlcluster 11 main start```

And stop with:

```sudo pg_ctlcluster 11 main stop```

To be able to access the database accross the lan at home, you have to modify 2 files:

* pg_hba.conf
* postgresql.conf

### pg_hba.conf

```sudo nano /etc/postgresql/11/main/pg_hba.conf```

At the end of the file, add the followinf line:

```hostnossl    all          all            0.0.0.0/0  trust```

### postgresql.conf

Add the line:

```listen_addresses = '*'```




