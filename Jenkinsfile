pipeline {
    agent any
    
     environment {
     username = 'admin'
     password = 'Pa55w.rd'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',url: 'https://github.com/CT2-DEVOPS-Team2/myinsurancescripts.git' 
                bat 'rd /s /q "dist"'
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
                bat 'c:/Users/Administrator/AppData/Local/Programs/Python/Python39/python.exe -m build'
                bat 'dir'
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
                echo "u${username} -p${password}"
                bat "twine upload  --repository-url http://localhost:8081/repository/hosted-python/ dist/* -u${username} -p${password}"
                // withCredentials([usernamePassword(credentialsId: 'nexus2_credentials', usernameVariable: 'USER', passwordVariable: 'USERPASS')]) {
                //     echo "$USER $USERPASS"
                //     bat "twine upload  --repository-url http://localhost:8081/repository/hosted-python/ dist/* -u${USER} -p${USERPASS}"
                }
        }
    }
}
