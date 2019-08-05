# Android MZX Data Logger 4.0 Wireless Specification

This document describes an implementation for a wireless connection between the Android MZX Data Logger 4.0 and the MZX panel.

## Components

To provide a wireless link between Android application and panel, three components are required:  

1. A wireless option on Android app, to switch between wired and wireless connection.
2. A cloud service to broker request and service queues between Android app and panel
3. A wifi enabled embedded device attached to MZX panel to service requests

## Top level architectures

Required components should incorporate the following features:  

1. Android app
* The app shall incorporate dual connectivity via wired or wireless with the use of a button to switch between the two.
* The app shall poll the cloud service with requests for panel point information, we expect the app to wait for a response from the panel before we send the next packet but in the event no such thing returns then a timeout of 10 seconds should be implemented before moving on the the next point (applicable to poll loop functionality).

* All other features as per wired version.

2. Cloud service

* A public static ip address, through which the service is available.
* Open http ports on firewall
* A web service able to service http requests
* A broker service available to the Android app, capable of adding Android requests to a request queue, reading serviced requests queue back to Android app, reading request queue to panel embedded device, and writing serviced requests, fulfilled by panel embedded device, to serviced requests queue. The broker service shall be able to manage both request and service queues, by adding and removing entries
* A file saving service able to store human readable panel point log entries, supplied by Android app, to a web server log, for future reference may the need arise to inspect such logs or convert to csv for processing (currently stored as txt logs)
http://3.8.97.201/<panelid>_Data.html

3. Wifi enabled device attached to panel

* A background service process to monitor requests from cloud service, relay point information requests to panel and send back serviced requests to cloud service. The frequency of requests shall be such that for any given Android app request, the response (serviced request) shall have a latency of no more than 1.5 seconds. During periods when no requests are being made, the service shall wind down, with a longer latency between requests, and as soon as requests are being made, the frequency shall increase to observe required operational latency.
* An adequate library capable of querying the panel via RS232 com port 2
* A configuration option to connect directly, bypassing cloud service, to the embedded device acting as a hot spot.
* The embedded device shall be capable of connecting concurrently to RS232 com 1 port to collect print outs supplied by panel and make such information available as required, to Android app, desktop app or web server.

## Flow chart

```
                 Send point info request                              Get request
+-------------+ +-----------------------> +----------------------+  <-------------+
| Android App |                           | Cloud service broker |                |
+-------------+ <-----------------------+ +----------------------+  <---------+   |
                  Get serviced request                                        |   |
                                                              Return serviced |   |
                 Relay point info request                      request        |   |
 +-----------+ <------------------------+ +----------------------+  +---------+   |
 | MZX Panel |                            | Embedded application |                |
 +-----------+ +------------------------> +----------------------+  +-------------+
               Return point info response
```
## Future developments

* Multiple client architecture such that 1 * x embedded devices can communicate to 1 * x android phones through the use of single broker server. This would be the ideal next step after the milestone demo.

* The same architecture may be used to supply data to mobile, desktop and web panel gui apps, with all the functionality currently provided by desktop apps.

* Shorten cables - at the moment they are cluttering panel.

* Packet building on embedded device.

* Schedulling.

* Embedded device state broadcast - idle, polling, scheduled, etc.

* Embedded device logging - need to log every action, specially with respect to scripts running and wifi availability.

As always open to suggestion.
