# ScuffedBCPY
A crappy replacement for Burp Collaborator

Leverage pythons HTTPServer module to have a very limited implementation of a pingback server for SSRF testing. Listens for any requests and outputs information about the source and requested path to the specified output file. In order to identify inidividual requests, use formatting such as this:

```
X-Forwarded-For: [serverip]:6996/name-of-endpoint/x-forwarded-for
```
This way, in the output file (if you use conistent formatting, you can infer where teh pingback came from


# Useage

```
python3 ScuffedBCPY.py output.txt
```
