# Simple-webserver-using-Docker-on-Ubuntu
This repository contains a minimalistic setup for running a simple web server using Docker on an Ubuntu environment. This is part of my DevOps mini projects. It is designed to demonstrate how to containerize a basic web server, making it easy to deploy and run on any machine with Docker. 

Deploy a simple web server using Docker on Ubuntu

Deploying a simple web server using Docker on Ubuntu involves a few steps. For this example, let's use Nginx as the web server since it is lightweight and straightforward.
Prerequisites
Ubuntu System: Make sure you have Ubuntu installed.
Docker: Ensure Docker is installed on your Ubuntu system. 
You can install Docker by following these steps:

![image](https://github.com/user-attachments/assets/b180864d-7792-4e10-ad03-6db370bd40ef)

Steps to Deploy a Simple Web Server
Create a Directory for Your Project

![image](https://github.com/user-attachments/assets/ca77a82f-80a6-4288-81c3-1d8564642688)

2. Create a Simple HTML File
Create an index.html file in this directory to serve as your web page.

![image](https://github.com/user-attachments/assets/9c301963-4886-4670-8b1a-a6c0734cab22)

3. Create a Dockerfile
A Dockerfile is a text document that contains all the commands to assemble an image. For Nginx, you don't need to build a custom image from scratch; you can use the official Nginx image directly. However, creating a Dockerfile can be useful for customization.
Create a file named Dockerfile:

![image](https://github.com/user-attachments/assets/38fc7a8f-7e95-4c37-8846-91a835e4a501)

4. Build the Docker Image
Build the Docker image using the Dockerfile:


![image](https://github.com/user-attachments/assets/c065a92a-ec22-40fd-8598-3fa4ca20be33)

5. Run the Docker Container
Now run a container from the image you just built. This will map port 80 on the host to port 80 on the container.

![image](https://github.com/user-attachments/assets/40dd3456-d3c9-420a-9ec7-858f03595d9b)

-d: Run in detached mode.
-p 8080:80: Map port 8080 on the host to port 80 on the container.

Access Your Web Server
Open your web browser and navigate to http://localhost:8080. You should see the message "Hello, Docker World!" displayed on the web page.



Check out my full blogpost on Medium https://mukherjeechandril.medium.com/devops-mini-projects-p-1-6b96e7a04357
