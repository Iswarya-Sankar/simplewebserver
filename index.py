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
         <h2>Device Specification</h2><h4>(Iswarya-S 25016326)</h4>
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