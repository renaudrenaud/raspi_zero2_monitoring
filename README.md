# raspi_zero2_monitoring

A project to show how to manage computer monitoring with the little Raspberry Pi Zero 2.

## Tools

For this funny project we want to use:
* python3
* Postgresql
* Grafana

The OS for the Pi is the following, this is before the new version from November 2021.
It is still a 32 bit version.

```
pi@raspberrypi:~/temperature $ uname -a
Linux raspberrypi 5.10.63-v7+ #1459 SMP Wed Oct 6 16:41:10 BST 2021 armv7l GNU/Linux
```



## Postgres Install & Config

Installation is done with the following command:

```sudo apt install postgresql```

When done, it's possible to start /stop PG using:

```
sudo pg_ctlcluster 11 main start
sudo pg_ctlcluster 11 main stop
```

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



## Grafana

From my point of view the most difficult task is to find where to get the package.

This is here https://grafana.com/grafana/download?platform=arm

Please do not select the arm64 version if your system is not arm64! It should be something like that (depending on the last Grafana version, replace 8.2.4 by the correct version number):

```
sudo apt-get install -y adduser libfontconfig1
wget https://dl.grafana.com/enterprise/release/grafana-enterprise_8.2.4_armhf.deb
sudo dpkg -i grafana-enterprise_8.2.4_armhf.deb
```

And you're done. Grafana is visible on port 3000.
