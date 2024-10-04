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

        stage('Run Pytest') {
            steps {
                script {
                    try {
                        echo 'Running unit tests...'
                        bat '"C:\\Users\\Manvendra Nema\\anaconda3\\envs\\vercil\\python.exe" test_all.py'
                    } catch (Exception e) {
                        echo "Tests failed: ${e.message}"
                        error "Stopping the pipeline due to test failures."
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        echo "Building Docker image ${DOCKER_IMAGE}:${DOCKER_TAG}..."
                        def dockerImage = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                    } catch (Exception e) {
                        echo "Docker image build failed: ${e.message}"
                        error "Stopping the pipeline due to build failures."
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    try {
                        echo "Pushing Docker image ${DOCKER_IMAGE}:${DOCKER_TAG} to Docker Hub..."
                        withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                            docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                                docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                            }
                        }
                    } catch (Exception e) {
                        echo "Failed to push Docker image: ${e.message}"
                        error "Stopping the pipeline due to push failures."
                    }
                }
            }
        }

        // stage('Deploy to Kubernetes') {
        //     steps {
        //         script {
        //             try {
        //                 echo "Deploying to Kubernetes using Minikube..."
        //                 kubernetesDeploy(
        //                     configs: 'streamlit-deployment.yaml',  
        //                     kubeconfigId: 'minikube-kubeconfig',    
        //                     enableConfigSubstitution: true
        //                 )
                        
        //                 kubernetesDeploy(
        //                     configs: 'streamlit-service.yaml',  
        //                     kubeconfigId: 'minikube-kubeconfig',
        //                     enableConfigSubstitution: true
        //                 )
        //             } catch (Exception e) {
        //                 echo "Kubernetes deployment failed: ${e.message}"
        //                 error "Stopping the pipeline due to deployment failures."
        //             }
        //         }
        //     }
        // }
    }
}
