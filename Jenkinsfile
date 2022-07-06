pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',url: 'https://github.com/CT2-DEVOPS-Team2/myinsurancescripts.git' 
                
	        }
        }        
        stage('Compile') {
            steps {
                echo 'Building...'
                }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Package') {
            steps {
                echo 'Packaging...'                
            }
        }
        stage('Acceptance test') {
            steps {
                echo 'Acceptance...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
