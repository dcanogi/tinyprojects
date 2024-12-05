# Dockerized Web App Deployment to Kubernetes with GitHub Actions

This project demonstrates how to set up a CI/CD pipeline using **GitHub Actions** for a **Dockerized web application** deployed on **Kubernetes**. The goal is to automate the process of building, testing, and deploying a simple web application into a Kubernetes cluster.

## Project Overview

This project consists of the following components:

1. **Web Application**: A simple web application developed in Node.js or Python.
2. **Dockerfile**: A configuration file used to create the Docker image for the web application.
3. **GitHub Actions CI/CD Workflow**: A configuration file (`.github/workflows/ci-cd.yml`) that automates the build, test, and deployment process.
4. **Kubernetes Deployment**: A `deployment.yaml` file for deploying the application on a Kubernetes cluster.

## Technologies Used

- **Docker**: For containerizing the web application.
- **GitHub Actions**: For automating the CI/CD pipeline.
- **Kubernetes**: For deploying and managing the application in a containerized environment.
- **Node.js / Python**: For the web application development.

## Prerequisites

Before starting, ensure you have the following:

- A GitHub account.
- A Kubernetes cluster (either local or hosted on a cloud provider like GKE, EKS, or AKS).
- A Docker registry account (e.g., Docker Hub) for storing your images.

## Project Structure

The repository contains the following structure:

- **/app**: The source code of the web application.
- **/Dockerfile**: The Dockerfile used to build the Docker image.
- **/.github/workflows/ci-cd.yml**: The GitHub Actions workflow configuration.
- **/k8s/deployment.yaml**: The Kubernetes deployment configuration for the application.

## How to Use

1. **Clone the repository**:

   ```bash
   git clone https://github.com/dcanogi/tinyprojects.git
   cd tinyprojects/Dockerized-web-deploy-kubernetes-with-github-actions
