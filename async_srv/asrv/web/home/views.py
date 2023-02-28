headers = (
    "HTTP/1.1 200 OK"
    "Server: nginx/1.2.1"
    "Date: Sat, 08 Mar 2014 22:53:46 GMT"
    "Content-Type: application/octet-stream"
    "Content-Length: 7"
    "Last-Modified: Sat, 08 Mar 2014 22:53:30 GMT"
    "Connection: keep-alive"
    "Accept-Ranges: bytes"

)

body = (
    "<html>"
    "<head><title>302 Found</title></head>"
    "<body bgcolor='white'>"
    "<center><h1>302 Found</h1></center>"
    "<hr><center>nginx</center>"
    "</body>"
    "</html>"

)


async def home_page(request):
    return (headers.format(len(body))+body).encode("utf-8")