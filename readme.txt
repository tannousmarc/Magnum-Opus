The platform requires a number of localhost servers to run.
1. In a terminal window, navigate to ./client/ and, after installing all the npm dependencies, use the command "npm run serve" to start the client UI.
2. In another terminal window, navigate to ./nlpengine/ and, after installing all the python dependencies, use the command "python server.py" to start the server.
3. In another terminal window, navigate to ./mappingengine/ and use the command "./d2r-server mapping.ttl" to run the server.
Now, assuming that you have CORS requests errors disabled (due to servers being run on local host), navigate to localhost:8080 (or wherever the client is running) to use the platform.

! Google search scraping is banned on some wi-fis, such as eduroam. The Cloud works, and my home wi-fi works. I assume this is on Google's side.
! To disable CORS requests either start chrome in a lower security mode or install the chrome addon.