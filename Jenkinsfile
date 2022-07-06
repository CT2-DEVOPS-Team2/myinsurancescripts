pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',url: 'https://github.com/CT2-DEVOPS-Team2/myinsurancescripts.git' 
                
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
                bat 'twine upload --repository-url http:///83.56.41.119:8085/localhost:8081/repository/hosted-python/ dist/* -uadmin -pPa55w.rd'
            }
        }
    }
}
