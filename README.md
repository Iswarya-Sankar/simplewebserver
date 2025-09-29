# EX01 Developing a Simple Webserver
## Date: 29.09.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```

from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>

            My Webpage
        </title>
    </head>
    <body bgcolor="66CCCC">
            <h1>Web Development</h1>
         <hr>
         <h2>Device Specification</h2>
         <table border="2" cellpadding="5" cellspacing="10">
            <tr bgcolor="996633">
                <th>S.no</td>
                <th>Device Specification</td>
                <th>type</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Device name</td>
                <td>DEVICE-4BY46V</td>
            </tr>
            <tr>
                <td>2</td>
                <td>RAM</td>
                <td>16.0GB</td>
            </tr>
            <tr>
            <td>2</td>
            <td>Product ID</td>
            <td>524851</td>
            </tr>
            <tr>
            <td>3</td>
            <td>Processor</td>
            <td>Intel-i5</td>
            <tr>
            <td>3</td>
            <td>Windows version</td>
            <td>Windows 11</td>
            </tr>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

```

## OUTPUT:
![alt text](<Screenshot (22).png>)
![alt text](<Screenshot (23).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
