# Travis rPI Notifier

## Synopsis

rPI project to retrieve the build status for a given project and displays the build status on an array of LEDs. The board is composed of 3 LEDs colored Red, Green and Blue. 

The monitored repository is configured in `config.yml` along with the GPIO numbers connected to each LED. The LEDs will blink / go on or off depending on the status of the monitored travis build for a given repository.

## Electronic Build

![Build GIF](https://github.com/mena-devs/travis-rpi-notifier/blob/repo-screenshots/electronics/images/travis-ci-notifier.gif)

![Electrical Diagram](https://raw.githubusercontent.com/mena-devs/travis-rpi-notifier/repo-screenshots/electronics/images/tn_rpi2B_sketch_schem.png)
![Breadboard Diagram](https://raw.githubusercontent.com/mena-devs/travis-rpi-notifier/repo-screenshots/electronics/images/tn_rpi2B_sketch_bb.png)

### Screenshots

![Top View #1](https://raw.githubusercontent.com/mena-devs/travis-rpi-notifier/repo-screenshots/electronics/images/trn_top_view.JPG)
![Top View #2](https://raw.githubusercontent.com/mena-devs/travis-rpi-notifier/repo-screenshots/electronics/images/trn_top_view-2.JPG)
![Side View](https://raw.githubusercontent.com/mena-devs/travis-rpi-notifier/repo-screenshots/electronics/images/trn_side_view.JPG)

## Installation and Configuration

Ubuntu Mate setup:

http://ubuntu-mate.org/raspberry-pi/

travispy Docs:

http://travispy.readthedocs.io/en/latest/entities/#travispy.entities.Repo

## Changelog