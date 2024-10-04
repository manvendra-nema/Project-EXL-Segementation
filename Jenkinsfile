pipeline {
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')  // Docker Hub credentials stored in Jenkins
        DOCKER_IMAGE = "maven0/my-streamlit-app"
        DOCKER_TAG = "latest"
        REPO_URL = "https://github.com/manvendra-nema/Project-EXL-Segementation.git"
        MINIKUBE_PATH ="\"C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe\""  // Use the absolute path of Minikube
        PATH = "C:\\Windows\\System32;${env.PATH}"  // Ensure cmd.exe is in PATH

    }

    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        
        stage('Pytest') {
    steps {
        script {
            try {
                 echo 'running unittest'
                bat '"C:\\Users\\Manvendra Nema\\anaconda3\\envs\\vercil\\python.exe" test_all.py'
            } catch (Exception e) {
                echo "Tests failed: ${e.message}"
                // Optionally: Mark the build as unstable or perform other actions
            }
        }
    }
}


        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using Docker plugin
                    def dockerImage = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Use credentials for Docker Hub login
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                            // Push the Docker image to Docker Hub
                            docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                        }
                    }
                }
            }
        }

        stage('Deploy to Kubernetes via Minikube') {
            steps {
                script {
                    kubernetesDeploy(
                        configs: 'streamlit-deployment.yaml',  // Deployment YAML file for Kubernetes
                        kubeconfigId: 'minikube-kubeconfig',    // Jenkins kubeconfig ID for accessing Minikube
                        enableConfigSubstitution: true
                    )
                    
                    kubernetesDeploy(
                        configs: 'streamlit-service.yaml',  // Service YAML file for Kubernetes
                        kubeconfigId: 'minikube-kubeconfig',
                        enableConfigSubstitution: true
                    )
                }
            }
        }
          // stage('Get Minikube Service URL') {
          //   steps {
          //       script {
          //           // Capture and print the service URL
          //           def minikubeServiceUrl = bat(script: "${env.MINIKUBE_PATH} service streamlit-service --url", returnStdout: true).trim()
          //           echo "Minikube Service URL: ${serviceUrl}"
          //       }
          //   }
          // }
    }
}
