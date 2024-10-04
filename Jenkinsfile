pipeline {
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')  
        DOCKER_IMAGE = "maven0/my-streamlit-app"
        DOCKER_TAG = "new"
        REPO_URL = "https://github.com/manvendra-nema/Project-EXL-Segementation.git"
        MINIKUBE_PATH = "C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe"
        PATH = "C:\\Windows\\System32;C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
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
                        echo 'Running unittests...'
                        bat '"C:\\Users\\Manvendra Nema\\anaconda3\\envs\\vercil\\python.exe" test_all.py'
                    } catch (Exception e) {
                        echo "Tests failed: ${e.message}"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
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
                        configs: 'streamlit-deployment.yaml',  
                        kubeconfigId: 'minikube-kubeconfig',    
                        enableConfigSubstitution: true
                    )
                    
                    kubernetesDeploy(
                        configs: 'streamlit-service.yaml',  
                        kubeconfigId: 'minikube-kubeconfig',
                        enableConfigSubstitution: true
                    )
                }
            }
        }
    }
}
